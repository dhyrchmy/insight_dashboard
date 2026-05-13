from fastapi import APIRouter, Query
from typing import Optional
from ..services.csv_loader import CSVLoader
from ..statistics import calculate_all_stats
from ..config import get_csv_path

router = APIRouter()
_loader = CSVLoader(get_csv_path())

@router.get("/stats")
async def get_stats(
    column: str = Query(...),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """Get statistical metrics for a column."""
    timestamps, values = _loader.get_data(column, start_date, end_date)
    
    valid_values = [v for v in values if v is not None]
    
    stats = calculate_all_stats(valid_values)
    
    return stats