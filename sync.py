import os
import hashlib
import json
import shutil
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# --- CONFIGURATION ---
# Define multiple source folders to monitor.
SOURCES = [
    (Path("~/Files/Obsidian/ALevel").expanduser(), "alevel"),
    (Path("~/Files/Obsidian/AP").expanduser(), "ap"),
    (Path("~/Academics/01_HFLSSenior/25_Q4_G11_Sem1/04_Chemistry/04_Chem_Mindmap").expanduser(), "chem_mindmap"),
]

# Path to your destination folder (local to where the script is)
DEST_DIR = Path("./content").expanduser() 

# State file stored in your destination repo
STATE_FILE = Path("./sync-state.json").expanduser()

# Constants for Checkbox UI
CHECKED = "☑"
UNCHECKED = "☐"
PARTIAL = "▣"

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
    """Load the existing sync state."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return json.loads(content) if content else {}
        except json.JSONDecodeError:
            print(f"[Error] Could not parse {STATE_FILE}.")
    return {}

def save_state(state):
    """Save the current sync state."""
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=4)

def get_diff():
    """Compares sources to current state."""
    state = load_state()
    seen_keys = []
    changes = {
        "new": [],      
        "modified": [], 
        "deleted": []   
    }

    for source_root, source_id in SOURCES:
        source_root = source_root.expanduser()
        if not source_root.exists():
            continue

        current_files = [f for f in source_root.rglob("*") if f.is_file()]
        for src_path in current_files:
            relative_path = str(src_path.relative_to(source_root))
            state_key = f"{source_id}:{relative_path}"
            seen_keys.append(state_key)
            
            current_hash = get_file_hash(src_path)
            
            if state_key not in state:
                changes["new"].append({
                    "key": state_key, "path": src_path, "rel": relative_path, 
                    "id": source_id, "hash": current_hash, "type": "new"
                })
            elif state[state_key].get('hash') != current_hash:
                changes["modified"].append({
                    "key": state_key, "path": src_path, "rel": relative_path, 
                    "id": source_id, "hash": current_hash, "type": "modified"
                })

    deleted_keys = set(state.keys()) - set(seen_keys)
    for k in deleted_keys:
        changes["deleted"].append({"key": k, "type": "deleted"})
    
    return state, changes

class CommitGui:
    def __init__(self, state, diff):
        self.state = state
        self.diff = diff
        self.root = tk.Tk()
        self.root.title("Sync Commit Tool")
        self.root.geometry("1000x700")
        
        # UI Styles
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        label = ttk.Label(main_frame, text="Review Changes (Hierarchical View)", font=("Arial", 12, "bold"))
        label.pack(pady=(0, 10))

        tree_container = ttk.Frame(main_frame)
        tree_container.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(tree_container, columns=("Status",), selectmode="none")
        self.tree.heading("#0", text="Folder / File", anchor="w")
        self.tree.heading("Status", text="Status", anchor="w")
        self.tree.column("#0", width=600)
        self.tree.column("Status", width=150)

        scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Tags for coloring
        self.tree.tag_configure("new", foreground="green")
        self.tree.tag_configure("modified", foreground="blue")
        self.tree.tag_configure("deleted", foreground="red")
        self.tree.tag_configure("folder", font=("Arial", 10, "bold"))

        self.item_data = {}  # Map tree node to file info
        self.node_states = {} # Map node to checkbox state
        
        self._populate_tree()

        # Bind click for checkbox toggle
        self.tree.bind("<Button-1>", self.on_click)

        # Bottom Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill="x", pady=10)
        
        ttk.Button(btn_frame, text="Commit Selected", command=self.perform_commit).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.root.destroy).pack(side="right", padx=5)

    def _get_checkbox_text(self, state, text):
        return f"{state} {text}"

    def _populate_tree(self):
        all_items = self.diff["new"] + self.diff["modified"] + self.diff["deleted"]
        
        # Group by source and build folder structure
        structure = {}
        for item in all_items:
            sid = item.get("id") or item["key"].split(":")[0]
            if sid not in structure:
                structure[sid] = {}
            
            # Navigate/Build hierarchy
            rel_path = item.get("rel", item["key"].split(":", 1)[-1])
            parts = Path(rel_path).parts
            
            current_level = structure[sid]
            for part in parts[:-1]:
                # We need to distinguish between folders and files at this level
                if part not in current_level or not isinstance(current_level[part], dict):
                    current_level[part] = {}
                current_level = current_level[part]
            
            # The leaf is the item itself
            current_level[parts[-1]] = item

        # Recursively insert into tree
        def insert_node(parent, name, content):
            if isinstance(content, dict):
                # Check if it's actually a folder or a file masquerading as a dict
                # In our structure, folders are dicts, file items are dicts with a "type" key
                if "type" in content and "key" in content:
                    # It's a file item
                    item = content
                    file_id = self.tree.insert(
                        parent, "end", 
                        text=self._get_checkbox_text(CHECKED, name), 
                        values=(item["type"].upper(),),
                        tags=(item["type"],)
                    )
                    self.node_states[file_id] = CHECKED
                    self.item_data[file_id] = item
                else:
                    # It's a folder
                    folder_id = self.tree.insert(parent, "end", text=self._get_checkbox_text(CHECKED, name), open=True, tags=("folder",))
                    self.node_states[folder_id] = CHECKED
                    for k, v in content.items():
                        insert_node(folder_id, k, v)
            else:
                # Should not reach here based on structure logic, but for safety:
                pass

        for sid, content in structure.items():
            root_id = self.tree.insert("", "end", text=self._get_checkbox_text(CHECKED, f"Source: {sid}"), open=True, tags=("folder",))
            self.node_states[root_id] = CHECKED
            for k, v in content.items():
                insert_node(root_id, k, v)

    def on_click(self, event):
        item_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        
        # Only toggle if clicking the tree label area (where checkbox is)
        if not item_id or column != "#0":
            return

        # Toggle state
        current_state = self.node_states.get(item_id)
        new_state = UNCHECKED if current_state in [CHECKED, PARTIAL] else CHECKED
        
        self._update_node_and_children(item_id, new_state)
        self._update_parents(item_id)

    def _update_node_and_children(self, node, state):
        self.node_states[node] = state
        # Update Visual
        current_text = self.tree.item(node, "text")[2:]
        self.tree.item(node, text=f"{state} {current_text}")
        
        # Recurse to children
        for child in self.tree.get_children(node):
            self._update_node_and_children(child, state)

    def _update_parents(self, node):
        parent = self.tree.parent(node)
        if not parent:
            return
        
        children = self.tree.get_children(parent)
        child_states = [self.node_states[c] for c in children]
        
        if all(s == CHECKED for s in child_states):
            new_p_state = CHECKED
        elif all(s == UNCHECKED for s in child_states):
            new_p_state = UNCHECKED
        else:
            new_p_state = PARTIAL
            
        if self.node_states[parent] != new_p_state:
            self.node_states[parent] = new_p_state
            current_text = self.tree.item(parent, "text")[2:]
            self.tree.item(parent, text=f"{new_p_state} {current_text}")
            self._update_parents(parent)

    def perform_commit(self):
        # Gather all checked file nodes
        to_commit = []
        for node, item in self.item_data.items():
            if self.node_states[node] == CHECKED:
                to_commit.append(item)

        if not to_commit:
            messagebox.showwarning("No Selection", "Please select at least one file to commit.")
            return

        confirm = messagebox.askyesno("Confirm", f"Commit {len(to_commit)} changes?")
        if not confirm:
            return

        updates_made = False
        for item in to_commit:
            key = item["key"]
            if item['type'] == "deleted":
                if key in self.state:
                    del self.state[key]
                    updates_made = True
            else:
                dest_path = DEST_DIR / item['rel']
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy2(item['path'], dest_path)
                    self.state[key] = {
                        "source_id": item['id'],
                        "relative_path": item['rel'],
                        "hash": item['hash'],
                        "dest_path": str(item['rel'])
                    }
                    updates_made = True
                except Exception as e:
                    print(f"Error copying {key}: {e}")

        if updates_made:
            save_state(self.state)
            messagebox.showinfo("Success", f"Synced {len(to_commit)} items successfully.")
        
        self.root.destroy()

    def run(self):
        self.root.mainloop()

def main():
    state, diff = get_diff()
    if not any(diff.values()):
        print("Nothing to sync, working tree clean.")
        return
    
    gui = CommitGui(state, diff)
    gui.run()

if __name__ == "__main__":
    main()