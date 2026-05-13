import subprocess
import os
from datetime import datetime

def git_add_commit(file_path: str, message: str) -> bool:
    """Add and commit a file using git subprocess."""
    try:
        repo_root = find_git_root()
        if not repo_root:
            return False
        
        abs_file_path = os.path.abspath(file_path)
        relative_path = os.path.relpath(abs_file_path, repo_root)
        
        subprocess.run(["git", "-C", repo_root, "add", relative_path], check=True)
        
        subprocess.run(
            ["git", "-C", repo_root, "commit", "-m", message],
            check=True,
            capture_output=True,
            text=True
        )
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def find_git_root() -> str:
    """Find the git repository root directory."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_snapshot_commit_message() -> str:
    """Generate commit message for snapshot."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"snapshot: save snapshot at {timestamp}"