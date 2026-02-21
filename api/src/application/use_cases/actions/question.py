"""Use case: get current pending question for the client (no correct answer)."""
from src.domain.game import Game
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang


def get_pending_question(
    card_repo: ICardRepository,
    game: Game,
) -> dict | None:
    """Return the current question payload for the client (no correct answer)."""
    qid = game.turn_state.get("pending_question_id")
    if not qid:
        return None
    is_skeptic = game.turn_state.get("is_skeptic") is True
    obstacle_type = game.turn_state.get("obstacle_type", "skeptic")
    is_deduction = game.turn_state.get("is_deduction") is True
    lang = normalize_lang(game)
    if is_skeptic:
        t = card_repo.get_debunker(qid, lang=lang) if obstacle_type == "debunker" else card_repo.get_skeptic(qid, lang=lang)
    elif is_deduction:
        t = card_repo.get_deduction(qid, lang=lang)
    else:
        t = card_repo.get_trivia(qid, lang=lang)
    if not t:
        return None
    out = dict(t)
    if "answers" in out:
        out["answers"] = [{"text": a.get("text", "")} for a in out["answers"]]
    out["is_skeptic"] = is_skeptic
    if is_skeptic:
        out["obstacle_type"] = game.turn_state.get("obstacle_type", "skeptic")
    return out
