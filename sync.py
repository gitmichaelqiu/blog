import os
import hashlib
import json
import shutil
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# --- CONFIGURATION ---
SOURCES = [
    (Path("~/Files/Obsidian/ALevel").expanduser(), "alevel"),
    (Path("~/Files/Obsidian/AP").expanduser(), "ap"),
    (Path("~/Academics/01_HFLSSenior/25_Q4_G11_Sem1/04_Chemistry/04_Chem_Mindmap").expanduser(), "chem_mindmap"),
]

DEST_DIR = Path("./content").expanduser() 
STATE_FILE = Path("./sync-state.json").expanduser()

# Theme Colors
COLOR_NEW = "#2e7d32"      # Green
COLOR_MODIFIED = "#1565c0" # Blue
COLOR_DELETED = "#c62828"  # Red
COLOR_FOLDER = "#37474f"   # Dark Grey
COLOR_BG = "#ffffff"
COLOR_STRIPE = "#f5f5f5"

def get_file_hash(filepath):
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        if not filepath.is_file():
            return None
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def load_state():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return json.loads(content) if content else {}
        except json.JSONDecodeError:
            print(f"[Error] Could not parse {STATE_FILE}.")
    return {}

def save_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=4)

def get_diff():
    state = load_state()
    seen_keys = []
    changes = {"new": [], "modified": [], "deleted": []}

    for source_root, source_id in SOURCES:
        source_root = source_root.expanduser()
        if not source_root.exists(): continue

        current_files = [f for f in source_root.rglob("*") if f.is_file()]
        for src_path in current_files:
            relative_path = str(src_path.relative_to(source_root))
            state_key = f"{source_id}:{relative_path}"
            seen_keys.append(state_key)
            
            current_hash = get_file_hash(src_path)
            if state_key not in state:
                changes["new"].append({"key": state_key, "path": src_path, "rel": relative_path, "id": source_id, "hash": current_hash, "type": "new"})
            elif state[state_key].get('hash') != current_hash:
                changes["modified"].append({"key": state_key, "path": src_path, "rel": relative_path, "id": source_id, "hash": current_hash, "type": "modified"})

    deleted_keys = set(state.keys()) - set(seen_keys)
    for k in deleted_keys:
        changes["deleted"].append({"key": k, "type": "deleted"})
    return state, changes

class CheckboxTree(ttk.Treeview):
    """A custom Treeview that handles checkboxes properly."""
    def __init__(self, master, **kwargs):
        kwargs.update({"selectmode": "none", "columns": ("status", "rel_path")})
        super().__init__(master, **kwargs)
        
        self.heading("#0", text="  Name", anchor="w")
        self.heading("status", text="Status", anchor="w")
        self.heading("rel_path", text="Relative Path", anchor="w")
        
        self.column("#0", width=450, stretch=True)
        self.column("status", width=100, anchor="center")
        self.column("rel_path", width=350, stretch=True)

        # Custom checkbox 'images' using Unicode for simplicity but styled via tags
        self.tag_configure("checked", text="  ☑  ")
        self.tag_configure("unchecked", text="  ☐  ")
        self.tag_configure("partial", text="  ▣  ")

        self.bind("<Button-1>", self._on_click)
        self.node_states = {} # item_id -> bool (True/False/None for partial)

    def _on_click(self, event):
        item_id = self.identify_row(event.y)
        column = self.identify_column(event.x)
        element = self.identify_element(event.x, event.y)

        # If user clicked the text or the area where the checkbox would be (not the expand button)
        if item_id and column == "#0" and element != "tree":
            self.toggle_item(item_id)

    def toggle_item(self, item_id, force_state=None):
        current_state = self.node_states.get(item_id, False)
        new_state = not current_state if force_state is None else force_state
        
        self.node_states[item_id] = new_state
        self._update_visual(item_id)
        
        # Propagate to children
        for child in self.get_children(item_id):
            self.toggle_item(child, force_state=new_state)
            
        # Propagate to parents
        self._update_parent_state(self.parent(item_id))

    def _update_parent_state(self, parent_id):
        if not parent_id: return
        
        children = self.get_children(parent_id)
        child_states = [self.node_states.get(c, False) for c in children]
        
        if all(s is True for s in child_states):
            new_state = True
        elif all(s is False for s in child_states):
            new_state = False
        else:
            new_state = None # Partial
            
        self.node_states[parent_id] = new_state
        self._update_visual(parent_id)
        self._update_parent_state(self.parent(parent_id))

    def _update_visual(self, item_id):
        state = self.node_states.get(item_id, False)
        text = self.item(item_id, "text")
        # Extract original text if already has icon
        clean_text = text[5:] if text.startswith("  ") else text
        
        icon = "  ☐  "
        if state is True: icon = "  ☑  "
        elif state is None: icon = "  ▣  "
        
        self.item(item_id, text=f"{icon}{clean_text}")

class CommitGui:
    def __init__(self, state, diff):
        self.state = state
        self.diff = diff
        self.root = tk.Tk()
        self.root.title("Zensical Sync Monitor")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f8f9fa")

        self.setup_styles()
        
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)

        header = ttk.Label(main_frame, text="Synchronize Content", font=("Segoe UI", 16, "bold"))
        header.pack(anchor="w", pady=(0, 5))
        
        subheader = ttk.Label(main_frame, text="Select files to port to your website repository.", font=("Segoe UI", 10))
        subheader.pack(anchor="w", pady=(0, 20))

        # Treeview Area
        tree_container = tk.Frame(main_frame, bg="white", highlightthickness=1, highlightbackground="#dee2e6")
        tree_container.pack(fill="both", expand=True)

        self.tree = CheckboxTree(tree_container)
        
        vsb = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        # Color Tags
        self.tree.tag_configure("new", foreground=COLOR_NEW)
        self.tree.tag_configure("modified", foreground=COLOR_MODIFIED)
        self.tree.tag_configure("deleted", foreground=COLOR_DELETED)
        self.tree.tag_configure("folder", font=("Segoe UI", 10, "bold"), foreground=COLOR_FOLDER)

        self.item_data = {}
        self._populate_tree()

        # Footer
        footer = ttk.Frame(main_frame, padding=(0, 20, 0, 0))
        footer.pack(fill="x")
        
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(footer, textvariable=self.status_var, font=("Segoe UI", 9, "italic")).pack(side="left")

        ttk.Button(footer, text="Commit Changes", command=self.perform_commit, style="Accent.TButton").pack(side="right", padx=(10, 0))
        ttk.Button(footer, text="Cancel", command=self.root.destroy).pack(side="right")

    def setup_styles(self):
        style = ttk.Style()
        # Modern Look
        style.theme_use('clam')
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30, borderwidth=0)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#e9ecef")
        style.map("Treeview", background=[('selected', '#e7f1ff')], foreground=[('selected', '#000000')])
        
        style.configure("Accent.TButton", padding=6, font=("Segoe UI", 10, "bold"))

    def _populate_tree(self):
        all_items = self.diff["new"] + self.diff["modified"] + self.diff["deleted"]
        structure = {}
        
        for item in all_items:
            sid = item.get("id") or item["key"].split(":")[0]
            if sid not in structure: structure[sid] = {}
            rel_path = item.get("rel", item["key"].split(":", 1)[-1])
            parts = Path(rel_path).parts
            
            curr = structure[sid]
            for part in parts[:-1]:
                if part not in curr or not isinstance(curr[part], dict):
                    curr[part] = {}
                curr = curr[part]
            curr[parts[-1]] = item

        def insert_recursive(parent, name, content):
            if isinstance(content, dict) and not ("type" in content and "key" in content):
                fid = self.tree.insert(parent, "end", text=f"  ☐  {name}", open=True, tags=("folder",))
                self.tree.node_states[fid] = False
                for k, v in sorted(content.items(), key=lambda x: (not isinstance(x[1], dict), x[0])):
                    insert_recursive(fid, k, v)
            else:
                item = content
                file_id = self.tree.insert(parent, "end", text=f"  ☐  {name}", 
                                         values=(item["type"].upper(), item.get("rel", "")),
                                         tags=(item["type"],))
                self.tree.node_states[file_id] = False
                self.item_data[file_id] = item

        for sid, content in sorted(structure.items()):
            root_id = self.tree.insert("", "end", text=f"  ☐  Source: {sid}", open=True, tags=("folder",))
            self.tree.node_states[root_id] = False
            for k, v in sorted(content.items(), key=lambda x: (not isinstance(x[1], dict), x[0])):
                insert_recursive(root_id, k, v)
        
        # Initial Select All
        for child in self.tree.get_children(""):
            self.tree.toggle_item(child, force_state=True)

    def perform_commit(self):
        to_commit = [item for node, item in self.item_data.items() if self.tree.node_states.get(node) is True]
        if not to_commit:
            messagebox.showwarning("No Selection", "Please select at least one file.")
            return

        if not messagebox.askyesno("Confirm Sync", f"Apply {len(to_commit)} changes to the destination?"):
            return

        count = 0
        for item in to_commit:
            key = item["key"]
            if item['type'] == "deleted":
                if key in self.state:
                    del self.state[key]
                    count += 1
            else:
                dest_path = DEST_DIR / item['rel']
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(item['path'], dest_path)
                    self.state[key] = {"source_id": item['id'], "relative_path": item['rel'], "hash": item['hash'], "dest_path": str(item['rel'])}
                    count += 1
                except Exception as e:
                    print(f"Error copying {key}: {e}")

        save_state(self.state)
        messagebox.showinfo("Success", f"Successfully synced {count} items.")
        self.root.destroy()

def main():
    state, diff = get_diff()
    if not any(diff.values()):
        print("Nothing to sync, working tree clean.")
        return
    
    gui = CommitGui(state, diff)
    gui.mainloop()

if __name__ == "__main__":
    main()