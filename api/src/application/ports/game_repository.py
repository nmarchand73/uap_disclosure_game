"""Port: game session persistence."""
from abc import ABC, abstractmethod
from src.domain.game import Game


class IGameRepository(ABC):
    @abstractmethod
    def get(self, game_id: str) -> Game | None:
        ...

    @abstractmethod
    def save(self, game: Game) -> None:
        ...

    @abstractmethod
    def create(self, game: Game) -> None:
        ...
