"""Use case: roll dice and move current player."""
from datetime import datetime, timezone
import random

from src.domain.game import Game, Player, TurnPhase
from src.domain.cards import CONTINENTS_MOVEMENT_ORDER
from src.domain.hotspots import get_hotspots_for_continent
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang
from src.application.use_cases.actions.spin import _add_token_gov_or_mil, _add_token_scientific


def _continent_matches_event(
    card_repo: ICardRepository, event_ids: list[str], continent: str, lang: str
) -> bool:
    """True if any of the player's event cards is for the given continent."""
    for eid in event_ids:
        ev = card_repo.get_event(eid, lang=lang)
        if ev and ev.get("continent") == continent:
            return True
    return False


def perform_move(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    seed: int | None = None,
) -> Game | None:
    """Roll dice and move current player by N continents. GDD 5.2: skip turn if flagged, apply penalty/bonus, draw event on no match."""
    game = game_repo.get(game_id)
    if not game or not game.players:
        return None
    if game.phase not in (TurnPhase.LOBBY, TurnPhase.MOVEMENT, TurnPhase.END_TURN):
        return None

    if game.phase == TurnPhase.END_TURN:
        game.current_turn_index = (game.current_turn_index + 1) % len(game.players)
        game.phase = TurnPhase.MOVEMENT
        game.turn_state = {}

    if game.phase == TurnPhase.LOBBY:
        game.phase = TurnPhase.MOVEMENT

    player = game.players[game.current_turn_index]

    # GDD 8.4: Skeptic fail → perdre son prochain tour
    if player.skip_next_turn:
        player.skip_next_turn = False
        game.current_turn_index = (game.current_turn_index + 1) % len(game.players)
        game.turn_state = {"skipped_turn": True}
        game.updated_at = datetime.now(timezone.utc).isoformat()
        game_repo.save(game)
        return game

    rng = random.Random(seed)
    dice = rng.randint(1, 6)
    # GDD 8.5: Debunker fail → -1 case de déplacement au prochain tour
    steps = max(1, dice - player.movement_penalty)
    player.movement_penalty = 0
    # GDD 5.2: Mauvaise Autorité → bonus mineur (+1 move)
    steps += player.next_move_bonus
    player.next_move_bonus = 0

    lang = normalize_lang(game)
    idx = (
        CONTINENTS_MOVEMENT_ORDER.index(player.continent)
        if player.continent in CONTINENTS_MOVEMENT_ORDER
        else 0
    )
    new_idx = (idx + steps) % len(CONTINENTS_MOVEMENT_ORDER)
    player.continent = CONTINENTS_MOVEMENT_ORDER[new_idx]

    # GDD 7.1: apply hotspot bonuses when landing (zone51, rendlesham, ruwa; hessdalen applied in spin)
    for hotspot_id, effect_type in get_hotspots_for_continent(player.continent):
        if hotspot_id in player.hotspot_used:
            continue
        if effect_type == "token_gov_mil" and _add_token_gov_or_mil(player):
            player.hotspot_used.append(hotspot_id)
            game.turn_state["hotspot"] = hotspot_id
        elif effect_type == "debunker_immunity":
            game.turn_state["debunker_immunity"] = True
            player.hotspot_used.append(hotspot_id)
            game.turn_state["hotspot"] = hotspot_id
        elif effect_type == "token_scientific" and _add_token_scientific(player):
            player.hotspot_used.append(hotspot_id)
            game.turn_state["hotspot"] = hotspot_id
        # next_event_preview (hessdalen) applied in spin when phase is SPINNER

    if _continent_matches_event(card_repo, player.event_card_ids, player.continent, lang):
        game.phase = TurnPhase.SPINNER
        game.turn_state = {"dice_roll": dice, "steps": steps}
    else:
        # GDD 5.2 Phase 2: Piocher une carte Event si disponible
        drawn_event: str | None = None
        if game.deck_event_ids:
            drawn_event = game.deck_event_ids.pop(0)
            player.event_card_ids.append(drawn_event)
        game.phase = TurnPhase.END_TURN
        game.turn_state = {"dice_roll": dice, "steps": steps, "no_event_match": True, "drew_event": drawn_event is not None}

    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
