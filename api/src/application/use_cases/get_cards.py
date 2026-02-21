"""Use case: get card content (events, trivia, characters, continents)."""
from typing import Any

from src.application.ports.card_repository import ICardRepository


def get_events(card_repo: ICardRepository, lang: str = "en", pack: str | None = None) -> list[dict[str, Any]]:
    return card_repo.list_events(lang=lang, pack=pack)


def get_trivia(card_repo: ICardRepository, lang: str = "en", authority: str | None = None, level: int | None = None) -> list[dict[str, Any]]:
    return card_repo.list_trivia(lang=lang, authority=authority, level=level)


def get_characters(card_repo: ICardRepository, lang: str = "en") -> list[dict[str, Any]]:
    return card_repo.list_characters(lang=lang)


def get_continents(card_repo: ICardRepository, lang: str = "en") -> list[dict[str, Any]]:
    return card_repo.list_continents(lang=lang)


def get_skeptic_list(card_repo: ICardRepository, lang: str = "en") -> list[dict[str, Any]]:
    return card_repo.list_skeptic(lang=lang)


def get_debunker_list(card_repo: ICardRepository, lang: str = "en") -> list[dict[str, Any]]:
    return card_repo.list_debunker(lang=lang)
