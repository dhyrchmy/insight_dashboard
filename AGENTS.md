<!-- SPECKIT START -->
## Project Plan

**Feature**: TimeSeries Insight Dashboard
**Spec**: `specs/001-timeseries-dashboard/spec.md`
**Plan**: `specs/001-timeseries-dashboard/plan.md`

## Technology Stack
- **Backend**: FastAPI (Python 3.11)
- **Frontend**: Chart.js (bundled locally)
- **Data Processing**: pandas, numpy, scipy

## Key Requirements
- CSV loader with pandas (auto-generate sample if no file)
- Statistics module with numpy/scipy (mean, median, std, skewness, kurtosis, regression, anomaly detection)
- Interactive Chart.js line chart with zoom/pan, tooltips, moving averages
- Snapshot feature with git integration

## Test Coverage
- 70% minimum on statistics module

## Commands
- Run: `uvicorn backend.src.main:app --reload --port 8000`
- Tests: `pytest --cov=backend/src/statistics tests/`
<!-- SPECKIT END -->