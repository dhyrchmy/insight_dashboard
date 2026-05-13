from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

from .routes import data, stats, snapshot

app = FastAPI(title="TimeSeries Insight Dashboard")

app.include_router(data.router, prefix="/api", tags=["data"])
app.include_router(stats.router, prefix="/api", tags=["stats"])
app.include_router(snapshot.router, prefix="/api", tags=["snapshot"])

static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open(os.path.join(static_dir, "index.html"), "r") as f:
        return f.read()

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)