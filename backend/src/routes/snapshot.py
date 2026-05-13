from fastapi import APIRouter, Body
from typing import List, Dict
import os
from datetime import datetime
from ..services.git_integration import git_add_commit, get_snapshot_commit_message

router = APIRouter()

SNAPSHOTS_DIR = "snapshots"

@router.post("/snapshot")
async def save_snapshot(data: Dict):
    """Save current view data as CSV snapshot."""
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"snapshot_{timestamp}.csv"
    filepath = os.path.join(SNAPSHOTS_DIR, filename)
    
    timestamps = data.get("timestamps", [])
    values = data.get("values", [])
    column = data.get("column", "data")
    
    with open(filepath, "w") as f:
        f.write("timestamp,value\n")
        for ts, val in zip(timestamps, values):
            f.write(f"{ts},{val}\n")
    
    msg = get_snapshot_commit_message()
    git_add_commit(filepath, msg)
    
    return {"status": "saved", "filename": filename}

@router.get("/snapshots")
async def get_snapshots():
    """Get list of past snapshots."""
    import subprocess
    
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)
    
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--pretty=format:%H|%s|%ci", "--", SNAPSHOTS_DIR],
            capture_output=True,
            text=True,
            check=True
        )
        
        commits = []
        for line in result.stdout.strip().split("\n"):
            if line:
                parts = line.split("|")
                if len(parts) >= 3:
                    commits.append({
                        "hash": parts[0][:8],
                        "message": parts[1],
                        "date": parts[2]
                    })
        
        return commits
    except:
        files = []
        if os.path.exists(SNAPSHOTS_DIR):
            for f in os.listdir(SNAPSHOTS_DIR):
                if f.endswith(".csv"):
                    files.append({"filename": f})
        return files

@router.get("/snapshots/{filename}")
async def download_snapshot(filename: str):
    """Download a snapshot CSV file."""
    from fastapi.responses import FileResponse
    
    filepath = os.path.join(SNAPSHOTS_DIR, filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="text/csv", filename=filename)
    return {"error": "File not found"}