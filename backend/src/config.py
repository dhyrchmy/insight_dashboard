import os
from dotenv import load_dotenv

load_dotenv()

def get_csv_path() -> str:
    """Get CSV file path from environment variable."""
    return os.getenv("CSV_PATH", "")

def get_host() -> str:
    """Get server host from environment."""
    return os.getenv("HOST", "0.0.0.0")

def get_port() -> int:
    """Get server port from environment."""
    return int(os.getenv("PORT", "8000"))