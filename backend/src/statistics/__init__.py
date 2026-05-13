import numpy as np
from scipy import stats
from typing import List, Tuple, Optional

def calculate_mean(data: List[float]) -> float:
    """Calculate arithmetic mean using numpy."""
    if not data:
        return 0.0
    result = np.mean(data)
    return 0.0 if np.isnan(result) else float(result)

def calculate_median(data: List[float]) -> float:
    """Calculate median using numpy."""
    if not data:
        return 0.0
    result = np.median(data)
    return 0.0 if np.isnan(result) else float(result)

def calculate_std(data: List[float]) -> float:
    """Calculate standard deviation using numpy."""
    if not data:
        return 0.0
    result = np.std(data, ddof=1)
    return 0.0 if np.isnan(result) else float(result)

def calculate_min(data: List[float]) -> float:
    """Calculate minimum value using numpy."""
    if not data:
        return 0.0
    return float(np.min(data))

def calculate_max(data: List[float]) -> float:
    """Calculate maximum value using numpy."""
    if not data:
        return 0.0
    return float(np.max(data))

def calculate_count(data: List[float]) -> int:
    """Count of non-null values."""
    return int(len(data))

def calculate_skewness(data: List[float]) -> float:
    """Calculate skewness using scipy."""
    if not data or len(data) < 4:
        return 0.0
    result = stats.skew(data)
    return 0.0 if np.isnan(result) else float(result)

def calculate_kurtosis(data: List[float]) -> float:
    """Calculate kurtosis using scipy."""
    if not data or len(data) < 4:
        return 0.0
    result = stats.kurtosis(data)
    return 0.0 if np.isnan(result) else float(result)

def linear_regression(data: List[float]) -> Tuple[float, float, float]:
    """
    Perform linear regression using numpy.
    Returns: (slope, intercept, r_squared)
    """
    if not data or len(data) < 2:
        return 0.0, 0.0, 0.0
    
    x = np.arange(len(data))
    y = np.array(data)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    if np.isnan(slope):
        return 0.0, 0.0, 0.0
    
    r_squared = r_value ** 2
    
    return float(slope), float(intercept), float(r_squared)

def rolling_average(data: List[float], window: int) -> List[Optional[float]]:
    """
    Calculate rolling average using numpy.
    Returns list with None for first (window-1) elements.
    """
    if not data or window < 1:
        return list(data) if data else []
    
    result = []
    
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            window_data = data[i - window + 1:i + 1]
            result.append(float(np.mean(window_data)))
    
    return result

def detect_anomalies(data: List[float], threshold: float = 2.0) -> Tuple[List[int], List[float]]:
    """
    Detect anomalies using z-score method.
    Returns: (indices of anomalies, z-scores of anomalies)
    """
    if len(data) < 3:
        return [], []
    
    z_scores = np.abs(stats.zscore(data))
    anomaly_indices = np.where(z_scores > threshold)[0].tolist()
    anomaly_values = [data[i] for i in anomaly_indices]
    
    return anomaly_indices, anomaly_values

def calculate_all_stats(data: List[float]) -> dict:
    """Calculate all statistics at once."""
    if not data or len(data) == 0:
        return {
            "mean": 0, "median": 0, "std": 0, "min": 0, "max": 0, "count": 0,
            "skewness": 0, "kurtosis": 0, "regression_slope": 0, "r_squared": 0,
            "anomaly_count": 0
        }
    
    anomaly_indices, _ = detect_anomalies(data)
    
    return {
        "mean": calculate_mean(data),
        "median": calculate_median(data),
        "std": calculate_std(data),
        "min": calculate_min(data),
        "max": calculate_max(data),
        "count": calculate_count(data),
        "skewness": calculate_skewness(data),
        "kurtosis": calculate_kurtosis(data),
        "regression_slope": linear_regression(data)[0],
        "r_squared": linear_regression(data)[2],
        "anomaly_count": len(anomaly_indices)
    }