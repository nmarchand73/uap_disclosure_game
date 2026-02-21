"""FastAPI app: composition root, include routers."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.api.routes import cards, games
from src.infrastructure.logging_config import configure_logging, log_requests

configure_logging()

def create_app() -> FastAPI:
    app = FastAPI(title="UFO Disclosure Game API", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(log_requests)
    app.include_router(cards.router)
    app.include_router(games.router)

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
