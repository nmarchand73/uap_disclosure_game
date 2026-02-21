"""
Netlify Function entry: expose FastAPI app via Mangum.
When deployed, Netlify bundles api/ so we add api_dir to path and use "src".
For local run use api/run_local.py (PYTHONPATH=api, src.main:app).
"""
import os
import sys

_this_dir = os.path.dirname(os.path.abspath(__file__))
# Deployed: bundle is api/ (netlify_api.py + src/ + data/). Local: repo root on PYTHONPATH.
if _this_dir not in sys.path:
    sys.path.insert(0, _this_dir)

from mangum import Mangum
from src.main import app

# Netlify expects handler(event, context)
handler = Mangum(app, lifespan="off")
