import pandas as pd
import os
from typing import Optional, Tuple
from .csv_generator import generate_sample_csv

class CSVLoader:
    def __init__(self, csv_path: Optional[str] = None):
        self.csv_path = csv_path
        self._df: Optional[pd.DataFrame] = None
    
    def load(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> pd.DataFrame:
        if self._df is None:
            if self.csv_path and os.path.exists(self.csv_path):
                self._df = pd.read_csv(self.csv_path)
            else:
                sample_path = "data/sample.csv"
                generate_sample_csv(sample_path)
                self._df = pd.read_csv(sample_path)
        
        df = self._df.copy()
        
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        
        if start_date:
            df = df[df["timestamp"] >= pd.to_datetime(start_date)]
        if end_date:
            df = df[df["timestamp"] <= pd.to_datetime(end_date)]
        
        df = df.ffill().bfill()
        
        return df
    
    def get_columns(self) -> list:
        if self._df is None:
            self.load()
        
        numeric_cols = self._df.select_dtypes(include=["number"]).columns.tolist()
        return numeric_cols
    
    def get_data(self, column: str, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Tuple[list, list]:
        df = self.load(start_date, end_date)
        
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found")
        
        timestamps = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S").tolist()
        values = df[column].tolist()
        
        return timestamps, values