"""Run FastAPI locally with uvicorn (for dev). Run from repo root: python api/run_local.py"""
import os
import sys

_api_dir = os.path.dirname(os.path.abspath(__file__))
if _api_dir not in sys.path:
    sys.path.insert(0, _api_dir)

import uvicorn

from src.infrastructure.logging_config import configure_logging, get_logger

if __name__ == "__main__":
    configure_logging()
    logger = get_logger("run")
    logger.info("Starting API on http://127.0.0.1:9999 (reload=True)")
    uvicorn.run("src.main:app", host="127.0.0.1", port=9999, reload=True)
