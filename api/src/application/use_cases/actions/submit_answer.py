"""Use case: submit answer to trivia or obstacle. GDD 5.2 Phase 4: 3 questions; 8.4/8.5: obstacle penalties."""
import random
from datetime import datetime, timezone

from src.domain.game import Game, Player, TurnPhase
from src.domain.cards import Authority
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang
from src.application.use_cases.actions.spin import (
    _add_token_any_authority,
    _draw_trivia_for_spinner,
    _draw_deduction_for_spinner,
)


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
    seed: int | None = None,
) -> Game | None:
    """Check answer. GDD: 3-question disclosure path; skeptic fail = skip next turn; debunker fail = movement penalty."""
    game = game_repo.get(game_id)
    if not game or not game.players:
        return None
    if game.phase != TurnPhase.QUESTION:
        return None

    qid = game.turn_state.get("pending_question_id")
    authority = game.turn_state.get("pending_authority")
    is_skeptic = game.turn_state.get("is_skeptic") is True
    obstacle_type = game.turn_state.get("obstacle_type", "skeptic")
    disclosure_index = game.turn_state.get("disclosure_question_index", 0)
    if not qid:
        game.phase = TurnPhase.END_TURN
        game.turn_state = {}
        game_repo.save(game)
        return game

    lang = normalize_lang(game)
    is_deduction = game.turn_state.get("is_deduction") is True
    if is_skeptic:
        card = card_repo.get_debunker(qid, lang=lang) if obstacle_type == "debunker" else card_repo.get_skeptic(qid, lang=lang)
    elif is_deduction:
        card = card_repo.get_deduction(qid, lang=lang)
    else:
        card = card_repo.get_trivia(qid, lang=lang)
    if not card or "answers" not in card:
        game.phase = TurnPhase.END_TURN
        game.turn_state = {}
        game_repo.save(game)
        return game

    answers = card["answers"]
    correct = 0 <= answer_index < len(answers) and answers[answer_index].get("correct") is True
    game.turn_state["answer_correct"] = correct
    game.turn_state["correct_index"] = next((i for i, a in enumerate(answers) if a.get("correct")), 0)

    player = game.players[game.current_turn_index]

    if is_skeptic:
        # GDD 8.4 Skeptic: wrong → perdre son prochain tour
        if obstacle_type == "skeptic" and not correct:
            player.skip_next_turn = True
        # GDD 8.5 Debunker: correct → bonus +1 token; wrong → -1 movement next turn
        if obstacle_type == "debunker":
            if game.turn_state.get("debunker_immunity"):
                pass  # GDD 7.1 Rendlesham: no penalty
            elif correct:
                _add_token_any_authority(player)
            else:
                player.movement_penalty = 1
        game.phase = TurnPhase.END_TURN
        game.turn_state = {k: v for k, v in game.turn_state.items() if k in ("answer_correct", "correct_index")}
    else:
        # GDD 5.2 Phase 4: 3 questions; all correct → +1 token; any wrong → exit path, end turn
        if not correct:
            game.phase = TurnPhase.END_TURN
            game.turn_state = {k: v for k, v in game.turn_state.items() if k in ("answer_correct", "correct_index")}
        elif disclosure_index < 2:
            game.turn_state["disclosure_question_index"] = disclosure_index + 1
            use_deduction = bool(game.deck_deduction_ids) and random.random() < 0.5
            next_q = _draw_deduction_for_spinner(card_repo, lang, authority, seed) if use_deduction else _draw_trivia_for_spinner(card_repo, lang, authority, seed)
            if use_deduction:
                game.turn_state["is_deduction"] = True
            else:
                game.turn_state["is_deduction"] = False
            if next_q:
                game.turn_state["pending_question_id"] = next_q.get("id", "")
                game.turn_state["pending_authority"] = authority
                game.phase = TurnPhase.QUESTION
            else:
                _add_authority_token(player, authority)
                game.phase = TurnPhase.END_TURN
                game.turn_state = {k: v for k, v in game.turn_state.items() if k in ("answer_correct", "correct_index")}
        else:
            _add_authority_token(player, authority)
            game.phase = TurnPhase.END_TURN
            game.turn_state = {k: v for k, v in game.turn_state.items() if k in ("answer_correct", "correct_index")}

    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
