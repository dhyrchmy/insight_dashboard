import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def generate_sample_csv(filepath: str, days: int = 365) -> None:
    """Generate sample CSV with 1 year of hourly random-walk data."""
    hours = days * 24
    start_date = datetime(2025, 1, 1)
    timestamps = [start_date + timedelta(hours=i) for i in range(hours)]
    
    np.random.seed(42)
    
    base_temp = 20.0
    temp_changes = np.random.normal(0, 0.5, hours)
    temperature = base_temp + np.cumsum(temp_changes)
    temperature = np.clip(temperature, -10, 40)
    
    base_humidity = 60.0
    humidity_changes = np.random.normal(0, 1, hours)
    humidity = base_humidity + np.cumsum(humidity_changes)
    humidity = np.clip(humidity, 0, 100)
    
    base_pressure = 1013.25
    pressure_changes = np.random.normal(0, 0.3, hours)
    pressure = base_pressure + np.cumsum(pressure_changes)
    pressure = np.clip(pressure, 950, 1050)
    
    df = pd.DataFrame({
        "timestamp": timestamps,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    })
    
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else ".", exist_ok=True)
    df.to_csv(filepath, index=False)
    return filepath