"""Port: card and content read-only repository."""
from abc import ABC, abstractmethod
from typing import Any


class ICardRepository(ABC):
    @abstractmethod
    def list_events(self, lang: str = "en", pack: str | None = None) -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def get_event(self, event_id: str, lang: str = "en") -> dict[str, Any] | None:
        ...

    @abstractmethod
    def list_trivia(self, lang: str = "en", authority: str | None = None, level: int | None = None) -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def get_trivia(self, trivia_id: str, lang: str = "en") -> dict[str, Any] | None:
        ...

    @abstractmethod
    def list_characters(self, lang: str = "en") -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def list_continents(self, lang: str = "en") -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def list_skeptic(self, lang: str = "en") -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def get_skeptic(self, skeptic_id: str, lang: str = "en") -> dict[str, Any] | None:
        ...

    @abstractmethod
    def list_debunker(self, lang: str = "en") -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def get_debunker(self, debunker_id: str, lang: str = "en") -> dict[str, Any] | None:
        ...
