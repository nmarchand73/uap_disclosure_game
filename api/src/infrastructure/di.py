"""Dependency injection: provide repository instances to FastAPI Depends()."""
import os

from src.application.ports.card_repository import ICardRepository
from src.application.ports.game_repository import IGameRepository
from src.infrastructure.persistence.card_repository_json import CardRepositoryJson
from src.infrastructure.persistence.game_repository_memory import GameRepositoryMemory

_card_repo: ICardRepository | None = None
_game_repo: IGameRepository | None = None


def get_card_repository() -> ICardRepository:
    global _card_repo
    if _card_repo is None:
        _card_repo = CardRepositoryJson()
    return _card_repo


def get_game_repository() -> IGameRepository:
    global _game_repo
    if _game_repo is None:
        url = os.environ.get("SUPABASE_URL") or os.environ.get("SUPABASE_SERVICE_URL", "")
        key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_SERVICE_KEY", "")
        if url and key:
            try:
                from src.infrastructure.persistence.game_repository_supabase import GameRepositorySupabase
                _game_repo = GameRepositorySupabase(url=url, key=key)
            except Exception as e:
                import logging
                logging.getLogger(__name__).warning("Supabase game repo init failed, using memory: %s", e)
                _game_repo = GameRepositoryMemory()
        else:
            _game_repo = GameRepositoryMemory()
    return _game_repo
