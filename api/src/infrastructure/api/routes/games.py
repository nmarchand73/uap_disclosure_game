"""Game session REST routes."""
from typing import Callable

from fastapi import APIRouter, Depends, HTTPException

from src.domain.game import Game
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.use_cases.create_game import create_game as create_game_uc
from src.application.use_cases.join_game import join_game as join_game_uc
from src.application.use_cases.game_action import (
    perform_move,
    spin_spinner,
    submit_answer,
    get_pending_question,
)
from src.application.dto import game_to_public_dto
from src.application.schemas import CreateGameBody, JoinGameBody, GameActionBody
from src.infrastructure.di import get_game_repository, get_card_repository
from src.infrastructure.logging_config import get_logger

router = APIRouter(prefix="/api", tags=["games"])
logger = get_logger(__name__)


@router.post("/games")
def create_game(
    body: CreateGameBody,
    game_repo=Depends(get_game_repository),
    card_repo=Depends(get_card_repository),
):
    """Create a new game. Body: player_name, character_id, character_variant, mode (optional), lang (optional, en|fr)."""
    game = create_game_uc(
        game_repo=game_repo,
        card_repo=card_repo,
        player_name=body.player_name,
        character_id=body.character_id,
        character_variant=body.character_variant,
        mode=body.mode,
        lang=body.lang,
    )
    logger.info("game_created game_id=%s players=1 lang=%s", game.id, body.lang)
    return game_to_public_dto(game)


@router.post("/games/{game_id}/join")
def join_game(
    game_id: str,
    body: JoinGameBody,
    game_repo=Depends(get_game_repository),
    card_repo=Depends(get_card_repository),
):
    """Join an existing game. Body: player_name, character_id, character_variant."""
    game = join_game_uc(
        game_repo=game_repo,
        card_repo=card_repo,
        game_id=game_id,
        player_name=body.player_name,
        character_id=body.character_id,
        character_variant=body.character_variant,
    )
    if not game:
        logger.warning("join_failed game_id=%s reason=not_found_or_full", game_id)
        raise HTTPException(status_code=400, detail="Cannot join (game not found, not in lobby, or full)")
    logger.info("game_joined game_id=%s player_count=%s", game_id, len(game.players))
    return game_to_public_dto(game)


@router.get("/games/{game_id}")
def get_game(
    game_id: str,
    game_repo=Depends(get_game_repository),
):
    """Get full game state (for polling)."""
    game = game_repo.get(game_id)
    if not game:
        logger.debug("get_game not_found game_id=%s", game_id)
        raise HTTPException(status_code=404, detail="Game not found")
    return game_to_public_dto(game)


@router.get("/games/{game_id}/question")
def get_question(
    game_id: str,
    game_repo=Depends(get_game_repository),
    card_repo=Depends(get_card_repository),
):
    """Get the current question (no correct answer) when phase is QUESTION."""
    game = game_repo.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    q = get_pending_question(card_repo, game)
    if not q:
        return None
    return q


def _handle_move(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    body: GameActionBody,
) -> Game | None:
    return perform_move(game_repo, card_repo, game_id, seed=body.seed)


def _handle_spin(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    body: GameActionBody,
) -> Game | None:
    return spin_spinner(game_repo, card_repo, game_id, seed=body.seed)


def _handle_submit_answer(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    body: GameActionBody,
) -> Game | None:
    return submit_answer(game_repo, card_repo, game_id, body.answer_index)


ACTION_HANDLERS: dict[str, Callable[..., Game | None]] = {
    "move": _handle_move,
    "spin": _handle_spin,
    "submit_answer": _handle_submit_answer,
}


@router.post("/games/{game_id}/action")
def game_action(
    game_id: str,
    body: GameActionBody,
    game_repo=Depends(get_game_repository),
    card_repo=Depends(get_card_repository),
):
    """Submit an action: move, spin, submit_answer. Body: action, [answer_index], [seed]."""
    game = game_repo.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    handler = ACTION_HANDLERS.get(body.action)
    if not handler:
        logger.warning("game_action unknown action=%s game_id=%s", body.action, game_id)
        raise HTTPException(status_code=400, detail=f"Unknown action: {body.action}")

    result = handler(game_repo, card_repo, game_id, body)
    if not result:
        logger.info("game_action rejected game_id=%s action=%s phase=%s", game_id, body.action, game.phase)
        raise HTTPException(status_code=400, detail="Action not allowed in current phase")
    logger.info("game_action game_id=%s action=%s phase_after=%s", game_id, body.action, result.phase)
    return game_to_public_dto(result)
