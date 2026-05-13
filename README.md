# Insight Dashboard

A local web dashboard for time series data visualization with statistics and snapshot features.

## Features

- **CSV Data Loading**: Reads from CSV file (path from .env) or auto-generates sample data
- **Interactive Chart**: Line chart with zoom/pan, hover tooltips, anomaly markers (red), regression trend line
- **Moving Averages**: Toggleable 7-period and 30-period moving averages
- **Statistics Sidebar**: Mean, median, std dev, min, max, count, skewness, kurtosis, regression slope, R², anomaly count
- **Snapshots**: Save current view as CSV, auto-git-committed, downloadable history

## Tech Stack

- **Backend**: FastAPI (Python 3.11)
- **Frontend**: Chart.js (bundled locally)
- **Data Processing**: pandas, numpy, scipy
- **Testing**: pytest with 99% coverage on statistics module

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Or use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Run the dashboard
python -m uvicorn backend.src.main:app --reload --port 8000
```

Then open http://localhost:8000

## Configuration

Edit `.env` file:
- Leave `CSV_PATH=` empty to auto-generate sample data (1 year hourly)
- Or set `CSV_PATH=/path/to/your/data.csv` to load your own CSV

CSV format: First column must be `timestamp`, followed by numeric columns (e.g., temperature, humidity, pressure)

## Testing

```bash
# Run tests with coverage
pytest backend/tests/statistics/test_stats.py -v --cov=backend/src/statistics
```

## License

MIT