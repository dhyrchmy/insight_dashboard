from fastapi import APIRouter, Query
from typing import Optional, List
from ..services.csv_loader import CSVLoader
from ..config import get_csv_path

router = APIRouter()
_loader = CSVLoader(get_csv_path())

@router.get("/columns")
async def get_columns() -> List[str]:
    """Get list of numeric columns from CSV."""
    return _loader.get_columns()

@router.get("/data")
async def get_data(
    column: str = Query(...),
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    """Get data for a specific column with optional date range filtering."""
    timestamps, values = _loader.get_data(column, start_date, end_date)
    
    from ..statistics import rolling_average, detect_anomalies, linear_regression
    
    valid_values = [v for v in values if v is not None]
    ma7 = rolling_average(valid_values, 7) if valid_values else []
    ma30 = rolling_average(valid_values, 30) if valid_values else []
    anomalies_idx, anomalies_val = detect_anomalies(valid_values)
    
    slope, intercept, r_squared = linear_regression(valid_values) if valid_values else (0, 0, 0)
    
    regression_line = []
    for i in range(len(valid_values)):
        regression_line.append(slope * i + intercept)
    
    return {
        "timestamps": timestamps,
        "values": values,
        "moving_averages": {
            "period7": ma7,
            "period30": ma30
        },
        "anomalies": {
            "indices": anomalies_idx,
            "values": anomalies_val
        },
        "regression": {
            "line": regression_line,
            "slope": slope,
            "intercept": intercept,
            "r_squared": r_squared
        }
    }