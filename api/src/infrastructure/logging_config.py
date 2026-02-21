"""Central logging configuration: format, level from env, request logging."""
import logging
import os
import time
from typing import Callable

from fastapi import Request, Response

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = "%(asctime)s | %(levelname)-5s | %(name)s | %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def configure_logging() -> None:
    """Configure root logger and common loggers. Call once at app startup."""
    level = getattr(logging, LOG_LEVEL, logging.INFO)
    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        force=True,
    )
    # Reduce noise from third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """Return a logger for the given module name (e.g. __name__)."""
    return logging.getLogger(name)


async def log_requests(request: Request, call_next: Callable) -> Response:
    """Middleware: log method, path, status and duration for each request."""
    logger = get_logger("http")
    start = time.perf_counter()
    method = request.method
    path = request.url.path
    status_code = 500
    try:
        response = await call_next(request)
        status_code = response.status_code
        return response
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info("%s %s %d %.1fms", method, path, status_code, duration_ms)
