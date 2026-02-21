"""Use case: spin the spinner and draw trivia or obstacle question."""
from datetime import datetime, timezone
import random

from src.domain.game import Game, Player, TurnPhase
from src.domain import rules
from src.domain.rules import SPINNER_OUTCOME_OBSTACLE, SPINNER_OUTCOME_SPECIAL
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


def _draw_deduction_for_spinner(
    card_repo: ICardRepository, lang: str, authority: str, seed: int | None
) -> dict | None:
    """Pick a random deduction card for the given authority. GDD Mixed mode."""
    deduction_list = card_repo.list_deduction(lang=lang, authority=authority)
    if not deduction_list:
        return None
    return random.Random(seed).choice(deduction_list)


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


def _event_authority_for_continent(
    card_repo: ICardRepository, event_ids: list[str], continent: str, lang: str
) -> str | None:
    """Authority of the first event card matching the continent."""
    for eid in event_ids:
        ev = card_repo.get_event(eid, lang=lang)
        if ev and ev.get("continent") == continent:
            return ev.get("authority")
    return None


def _add_token_any_authority(player: Player) -> bool:
    """Add +1 token to first authority not yet at 3. Return True if added."""
    path = player.disclosure_path
    if path.government < 3:
        path.government += 1
        return True
    if path.military < 3:
        path.military += 1
        return True
    if path.scientific < 3:
        path.scientific += 1
        return True
    return False


def _add_token_gov_or_mil(player: Player) -> bool:
    """Add +1 token to government or military (first non-full). GDD Zone 51/Roswell."""
    path = player.disclosure_path
    if path.government < 3:
        path.government += 1
        return True
    if path.military < 3:
        path.military += 1
        return True
    return False


def _add_token_scientific(player: Player) -> bool:
    """Add +1 token to scientific. GDD Ruwa."""
    path = player.disclosure_path
    if path.scientific < 3:
        path.scientific += 1
        return True
    return False


def _resolve_special(
    game: Game, card_repo: ICardRepository, seed: int | None
) -> None:
    """GDD 8.6: resolve special sector (Whistleblower, MIB, Hoax, Mass Sighting). Modifies game in place."""
    rng = random.Random(seed)
    kind = rng.randint(1, 4)
    current = game.players[game.current_turn_index]
    continent = current.continent
    if kind == 1:
        _add_token_any_authority(current)
        game.turn_state["special"] = "whistleblower"
    elif kind == 2:
        current.skip_next_turn = True
        game.turn_state["special"] = "mib"
    elif kind == 3:
        if current.event_card_ids and game.deck_event_ids:
            current.event_card_ids.pop(0)
            current.event_card_ids.append(game.deck_event_ids.pop(0))
        game.turn_state["special"] = "hoax"
    else:
        for p in game.players:
            if p.continent == continent:
                _add_token_any_authority(p)
        game.turn_state["special"] = "mass_sighting"


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

    player = game.players[game.current_turn_index]
    # GDD 7.1 Hessdalen: see next event before spin (once per game)
    if "hessdalen" not in player.hotspot_used and player.continent == "europe":
        player.hotspot_used.append("hessdalen")
        if game.deck_event_ids:
            game.turn_state["next_event_preview"] = game.deck_event_ids[0]
        game.turn_state["hotspot"] = "hessdalen"

    result = rules.spin_result(seed=seed)
    game.turn_state["spinner_result"] = result
    lang = normalize_lang(game)
    event_authority = _event_authority_for_continent(
        card_repo, player.event_card_ids, player.continent, lang
    )

    if result in rules.SPINNER_AUTHORITY_VALUES:
        # GDD 5.2: bonne Autorité → Phase 4 (3 questions); mauvaise → bonus mineur
        if event_authority and result == event_authority:
            # GDD Mixed mode: 50% trivia, 50% deduction when deduction deck available
            use_deduction = (
                game.deck_deduction_ids
                and random.Random(seed).random() < 0.5
            )
            q = _draw_deduction_for_spinner(card_repo, lang, result, seed) if use_deduction else _draw_trivia_for_spinner(card_repo, lang, result, seed)
            if q:
                game.turn_state["is_deduction"] = use_deduction
                game.turn_state["pending_question_id"] = q.get("id", "")
                game.turn_state["pending_authority"] = result
                game.turn_state["is_skeptic"] = False
                game.turn_state["disclosure_question_index"] = 0
                game.phase = TurnPhase.QUESTION
            else:
                game.turn_state = {}
                game.phase = TurnPhase.END_TURN
        else:
            player.next_move_bonus = 1
            game.turn_state["wrong_authority"] = True
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
    elif result == SPINNER_OUTCOME_SPECIAL:
        _resolve_special(game, card_repo, seed)
        game.phase = TurnPhase.END_TURN
    else:
        game.turn_state = {}
        game.phase = TurnPhase.END_TURN

    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
