import pytest
import numpy as np
from backend.src.statistics import (
    calculate_mean,
    calculate_median,
    calculate_std,
    calculate_min,
    calculate_max,
    calculate_count,
    calculate_skewness,
    calculate_kurtosis,
    linear_regression,
    rolling_average,
    detect_anomalies,
    calculate_all_stats
)

class TestStatistics:
    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        assert calculate_mean(data) == 3.0
    
    def test_calculate_mean_empty(self):
        assert calculate_mean([]) == 0.0
    
    def test_calculate_median_odd(self):
        data = [1, 2, 3, 4, 5]
        assert calculate_median(data) == 3.0
    
    def test_calculate_median_even(self):
        data = [1, 2, 3, 4]
        assert calculate_median(data) == 2.5
    
    def test_calculate_median_empty(self):
        assert calculate_median([]) == 0.0
    
    def test_calculate_std(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        assert abs(calculate_std(data) - 2.138) < 0.01
    
    def test_calculate_std_empty(self):
        assert calculate_std([]) == 0.0
    
    def test_calculate_min(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        assert calculate_min(data) == 1
    
    def test_calculate_min_empty(self):
        assert calculate_min([]) == 0.0
    
    def test_calculate_max(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        assert calculate_max(data) == 9
    
    def test_calculate_max_empty(self):
        assert calculate_max([]) == 0.0
    
    def test_calculate_count(self):
        data = [1, 2, 3, 4, 5]
        assert calculate_count(data) == 5
    
    def test_calculate_count_empty(self):
        assert calculate_count([]) == 0
    
    def test_calculate_skewness_normal(self):
        np.random.seed(42)
        data = np.random.normal(0, 1, 1000).tolist()
        skew = calculate_skewness(data)
        assert abs(skew) < 0.2
    
    def test_calculate_skewness_empty(self):
        assert calculate_skewness([]) == 0.0
    
    def test_calculate_kurtosis_normal(self):
        np.random.seed(42)
        data = np.random.normal(0, 1, 1000).tolist()
        kurt = calculate_kurtosis(data)
        assert abs(kurt) < 0.5
    
    def test_calculate_kurtosis_empty(self):
        assert calculate_kurtosis([]) == 0.0
    
    def test_linear_regression(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        slope, intercept, r_squared = linear_regression(data)
        assert abs(slope - 1.0) < 0.01
        assert abs(intercept - 1.0) < 0.1
        assert r_squared > 0.99
    
    def test_linear_regression_empty(self):
        slope, intercept, r_squared = linear_regression([])
        assert slope == 0 and intercept == 0 and r_squared == 0
    
    def test_linear_regression_constant(self):
        data = [5, 5, 5, 5, 5]
        slope, intercept, r_squared = linear_regression(data)
        assert slope == 0
    
    def test_rolling_average_window_3(self):
        data = [1, 2, 3, 4, 5]
        result = rolling_average(data, 3)
        assert result[0] is None
        assert result[1] is None
        assert abs(result[2] - 2.0) < 0.01
        assert abs(result[3] - 3.0) < 0.01
        assert abs(result[4] - 4.0) < 0.01
    
    def test_rolling_average_window_1(self):
        data = [1, 2, 3, 4, 5]
        result = rolling_average(data, 1)
        assert result == data
    
    def test_rolling_average_empty(self):
        result = rolling_average([], 3)
        assert result == []
    
    def test_detect_anomalies(self):
        data = [1, 2, 3, 4, 5, 100]
        indices, values = detect_anomalies(data, threshold=2.0)
        assert 5 in indices
        assert 100 in values
    
    def test_detect_anomalies_no_anomalies(self):
        data = [1, 2, 3, 4, 5, 6]
        indices, values = detect_anomalies(data, threshold=2.0)
        assert len(indices) == 0
    
    def test_detect_anomalies_empty(self):
        indices, values = detect_anomalies([], threshold=2.0)
        assert indices == [] and values == []
    
    def test_detect_anomalies_insufficient_data(self):
        data = [1, 2]
        indices, values = detect_anomalies(data, threshold=2.0)
        assert indices == [] and values == []
    
    def test_calculate_all_stats(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stats = calculate_all_stats(data)
        
        assert stats["mean"] == 5.5
        assert stats["median"] == 5.5
        assert stats["min"] == 1
        assert stats["max"] == 10
        assert stats["count"] == 10
        assert "std" in stats
        assert "skewness" in stats
        assert "kurtosis" in stats
        assert "regression_slope" in stats
        assert "r_squared" in stats
        assert "anomaly_count" in stats
    
    def test_calculate_all_stats_empty(self):
        stats = calculate_all_stats([])
        
        assert stats["mean"] == 0
        assert stats["count"] == 0