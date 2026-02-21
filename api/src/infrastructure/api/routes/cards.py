"""Card and content REST routes."""
from fastapi import APIRouter, Depends, Query

from src.application.use_cases.get_cards import (
    get_events,
    get_trivia,
    get_characters,
    get_continents,
    get_skeptic_list,
    get_debunker_list,
)
from src.infrastructure.di import get_card_repository

router = APIRouter(prefix="/api/cards", tags=["cards"])


@router.get("/events")
def list_events(
    lang: str = Query("en", alias="lang"),
    pack: str | None = Query(None),
    card_repo=Depends(get_card_repository),
):
    return get_events(card_repo, lang=lang, pack=pack)


@router.get("/trivia")
def list_trivia(
    lang: str = Query("en", alias="lang"),
    authority: str | None = Query(None),
    level: int | None = Query(None),
    card_repo=Depends(get_card_repository),
):
    return get_trivia(card_repo, lang=lang, authority=authority, level=level)


@router.get("/characters")
def list_characters(
    lang: str = Query("en", alias="lang"),
    card_repo=Depends(get_card_repository),
):
    return get_characters(card_repo, lang=lang)


@router.get("/continents")
def list_continents(
    lang: str = Query("en", alias="lang"),
    card_repo=Depends(get_card_repository),
):
    return get_continents(card_repo, lang=lang)


@router.get("/skeptic")
def list_skeptic(
    lang: str = Query("en", alias="lang"),
    card_repo=Depends(get_card_repository),
):
    return get_skeptic_list(card_repo, lang=lang)


@router.get("/debunker")
def list_debunker(
    lang: str = Query("en", alias="lang"),
    card_repo=Depends(get_card_repository),
):
    return get_debunker_list(card_repo, lang=lang)
