"""Use case: spin the spinner and draw trivia or obstacle question."""
from datetime import datetime, timezone
import random

from src.domain.game import Game, TurnPhase
from src.domain import rules
from src.domain.rules import SPINNER_OUTCOME_OBSTACLE
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang


def _draw_trivia_for_spinner(
    card_repo: ICardRepository, lang: str, authority: str, seed: int | None
) -> dict | None:
    """Pick a random trivia card for the given authority. Returns card dict or None."""
    trivia_list = card_repo.list_trivia(lang=lang, authority=authority)
    if not trivia_list:
        return None
    return random.Random(seed).choice(trivia_list)


def _draw_obstacle_for_spinner(
    card_repo: ICardRepository, lang: str, seed: int | None
) -> tuple[str, dict] | None:
    """Pick a random skeptic or debunker card. Returns (obstacle_type, card) or None."""
    skeptic_list = card_repo.list_skeptic(lang=lang)
    debunker_list = card_repo.list_debunker(lang=lang)
    combined: list[tuple[str, dict]] = []
    if skeptic_list:
        combined.append(("skeptic", random.Random(seed).choice(skeptic_list)))
    if debunker_list:
        combined.append(("debunker", random.Random(seed).choice(debunker_list)))
    if not combined:
        return None
    obstacle_type, q = random.Random(seed + 1).choice(combined)
    return (obstacle_type, q)


def spin_spinner(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    seed: int | None = None,
) -> Game | None:
    """Spin the spinner. If authority: draw a trivia question and set phase QUESTION. Else: end turn."""
    game = game_repo.get(game_id)
    if not game or not game.players:
        return None
    if game.phase != TurnPhase.SPINNER:
        return None

    result = rules.spin_result(seed=seed)
    game.turn_state["spinner_result"] = result
    lang = normalize_lang(game)

    if result in rules.SPINNER_AUTHORITY_VALUES:
        q = _draw_trivia_for_spinner(card_repo, lang, result, seed)
        if q:
            game.turn_state["pending_question_id"] = q.get("id", "")
            game.turn_state["pending_authority"] = result
            game.turn_state["is_skeptic"] = False
            game.phase = TurnPhase.QUESTION
        else:
            game.turn_state = {}
            game.phase = TurnPhase.END_TURN
    elif result == SPINNER_OUTCOME_OBSTACLE:
        drawn = _draw_obstacle_for_spinner(card_repo, lang, seed)
        if drawn:
            obstacle_type, q = drawn
            game.turn_state["pending_question_id"] = q.get("id", "")
            game.turn_state["pending_authority"] = None
            game.turn_state["is_skeptic"] = True
            game.turn_state["obstacle_type"] = obstacle_type
            game.phase = TurnPhase.QUESTION
        else:
            game.turn_state = {}
            game.phase = TurnPhase.END_TURN
    else:
        game.turn_state = {}
        game.phase = TurnPhase.END_TURN

    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
