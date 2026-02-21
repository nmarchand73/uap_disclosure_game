"""In-memory game repository (for dev / single-instance). Supabase can be added later."""
from src.application.ports.game_repository import IGameRepository
from src.domain.game import Game

_store: dict[str, Game] = {}


class GameRepositoryMemory(IGameRepository):
    def get(self, game_id: str) -> Game | None:
        return _store.get(game_id)

    def save(self, game: Game) -> None:
        _store[game.id] = game

    def create(self, game: Game) -> None:
        _store[game.id] = game
