import os
import hashlib
import json
import shutil
import sys
import argparse
from pathlib import Path
import argcomplete

# --- CONFIGURATION ---
# Define multiple source folders to monitor. 
# Added .expanduser() to handle '~' shorthand correctly.
SOURCES = [
    (Path("~/Files/Obsidian/ALevel").expanduser(), "alevel"),
    (Path("~/Files/Obsidian/AP").expanduser(), "ap"),
    (Path("~/Academics/01_HFLSSenior/25_Q4_G11_Sem1/04_Chemistry/04_Chem_Mindmap").expanduser(), "chem_mindmap"),
]

# Path to your destination folder (e.g., website content, project repo)
DEST_DIR = Path("./content").expanduser() 

# State file stored in your destination repo to track changes
STATE_FILE = Path("./sync-state.json").expanduser()

def get_file_hash(filepath):
    """Calculate SHA-256 hash of a file to detect content changes."""
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
    """Load the existing sync state from the JSON file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except json.JSONDecodeError:
            print(f"[Error] Could not parse {STATE_FILE}. Starting with empty state.")
    return {}

def save_state(state):
    """Save the current sync state to the JSON file."""
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=4)

def get_diff():
    """Compares sources to current state and returns pending changes."""
    state = load_state()
    seen_keys = []
    changes = {
        "new": [],      # (state_key, src_path, relative_path, source_id, hash)
        "modified": [], # (state_key, src_path, relative_path, source_id, hash)
        "deleted": []   # state_key
    }

    for source_root, source_id in SOURCES:
        # Ensure path is expanded even if changed in config
        source_root = source_root.expanduser()
        
        if not source_root.exists():
            print(f"[Warning] Source path does not exist: {source_root}")
            continue

        # Use rglob("*") and filter for files to ensure we catch everything
        current_files = [f for f in source_root.rglob("*") if f.is_file()]
        
        for src_path in current_files:
            relative_path = str(src_path.relative_to(source_root))
            state_key = f"{source_id}:{relative_path}"
            seen_keys.append(state_key)
            
            current_hash = get_file_hash(src_path)
            
            if state_key not in state:
                changes["new"].append((state_key, src_path, relative_path, source_id, current_hash))
            elif state[state_key].get('hash') != current_hash:
                changes["modified"].append((state_key, src_path, relative_path, source_id, current_hash))

    deleted_keys = set(state.keys()) - set(seen_keys)
    changes["deleted"] = list(deleted_keys)
    
    return state, changes

def get_pending_targets(prefix, parsed_args, **kwargs):
    """Helper for argcomplete to provide Tab-completion choices."""
    _, diff = get_diff()
    # Collect all keys that have pending changes
    pending = [item[0] for item in (diff["new"] + diff["modified"])]
    pending.extend(diff["deleted"])
    pending.append(".")
    return [p for p in pending if p.startswith(prefix)]

def show_status():
    """Prints the current status of files (staged/unstaged)."""
    _, diff = get_diff()
    
    has_changes = any(diff.values())
    
    if not has_changes:
        print("Nothing to sync, working tree clean.")
        return

    if diff["new"]:
        print(f"\nNew files ({len(diff['new'])}):")
        for item in diff["new"]:
            print(f"  (new)      {item[0]}")
            
    if diff["modified"]:
        print(f"\nModified files ({len(diff['modified'])}):")
        for item in diff["modified"]:
            print(f"  (modified) {item[0]}")

    if diff["deleted"]:
        print(f"\nDeleted in source ({len(diff['deleted'])}):")
        for key in diff["deleted"]:
            print(f"  (deleted)  {key}")
    print("")

def commit(target):
    """Syncs the target file(s) and updates the state."""
    state, diff = get_diff()
    to_sync = []
    to_remove_from_state = []

    # Filter changes based on target
    if target == ".":
        to_sync = diff["new"] + diff["modified"]
        to_remove_from_state = diff["deleted"]
    else:
        # User specified a specific state_key (e.g. obsidian:MyNote.md)
        to_sync = [item for item in (diff["new"] + diff["modified"]) if item[0] == target]
        if target in diff["deleted"]:
            to_remove_from_state = [target]
        
        if not to_sync and not to_remove_from_state:
            print(f"Error: No changes found for '{target}'")
            return

    # Perform Sync
    updates_made = False
    
    for state_key, src_path, relative_path, source_id, current_hash in to_sync:
        print(f"Syncing: {state_key}")
        dest_path = DEST_DIR / relative_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            shutil.copy2(src_path, dest_path)
            state[state_key] = {
                "source_id": source_id,
                "relative_path": relative_path,
                "hash": current_hash,
                "dest_path": str(relative_path)
            }
            updates_made = True
        except Exception as e:
            print(f"  [Error] Failed to copy {state_key}: {e}")

    for key in to_remove_from_state:
        print(f"Removing from state: {key}")
        if key in state:
            del state[key]
            updates_made = True

    if updates_made:
        save_state(state)
        print("Done.")
    else:
        print("No updates performed.")

def main():
    parser = argparse.ArgumentParser(description="Sync Monitor - A Git-like tool for porting notes.")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Status command
    subparsers.add_parser("status", help="Show changes between source and destination.")

    # Commit command
    commit_parser = subparsers.add_parser("commit", help="Sync changes and update state.")
    target_arg = commit_parser.add_argument("target", help="The file ID to sync, or '.' for all.")
    
    # Register the completer function for the 'target' argument
    if argcomplete:
        target_arg.completer = get_pending_targets
        argcomplete.autocomplete(parser)

    args = parser.parse_args()

    if args.command == "status":
        show_status()
    elif args.command == "commit":
        commit(args.target)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()