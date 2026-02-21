"""Use case: submit answer to trivia or obstacle question."""
from datetime import datetime, timezone

from src.domain.game import Game, Player, TurnPhase
from src.domain.cards import Authority
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang


def _add_authority_token(player: Player, authority: str) -> None:
    """Add one token to the player's disclosure path for the given authority (cap at 3)."""
    if authority == Authority.GOVERNMENT.value:
        player.disclosure_path.government = min(3, player.disclosure_path.government + 1)
    elif authority == Authority.MILITARY.value:
        player.disclosure_path.military = min(3, player.disclosure_path.military + 1)
    elif authority == Authority.SCIENTIFIC.value:
        player.disclosure_path.scientific = min(3, player.disclosure_path.scientific + 1)


def submit_answer(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    answer_index: int,
) -> Game | None:
    """Check answer; if correct add token to current player's disclosure path. Then end turn."""
    game = game_repo.get(game_id)
    if not game or not game.players:
        return None
    if game.phase != TurnPhase.QUESTION:
        return None

    qid = game.turn_state.get("pending_question_id")
    authority = game.turn_state.get("pending_authority")
    is_skeptic = game.turn_state.get("is_skeptic") is True
    if not qid:
        game.phase = TurnPhase.END_TURN
        game.turn_state = {}
        game_repo.save(game)
        return game

    lang = normalize_lang(game)
    if is_skeptic:
        card = card_repo.get_skeptic(qid, lang=lang)
    else:
        card = card_repo.get_trivia(qid, lang=lang)
    if not card or "answers" not in card:
        game.phase = TurnPhase.END_TURN
        game.turn_state = {}
        game_repo.save(game)
        return game

    answers = card["answers"]
    correct = 0 <= answer_index < len(answers) and answers[answer_index].get("correct") is True

    player = game.players[game.current_turn_index]
    if correct and not is_skeptic and authority:
        _add_authority_token(player, authority)

    game.turn_state["answer_correct"] = correct
    game.turn_state["correct_index"] = next((i for i, a in enumerate(answers) if a.get("correct")), 0)
    game.phase = TurnPhase.END_TURN
    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
