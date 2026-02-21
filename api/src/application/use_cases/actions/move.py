"""Use case: roll dice and move current player."""
from datetime import datetime, timezone
import random

from src.domain.game import Game, Player, TurnPhase
from src.domain.cards import CONTINENTS_MOVEMENT_ORDER
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang


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
    """Roll dice and move current player by N continents. If continent matches an event card, set phase to SPINNER; else end turn."""
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

    rng = random.Random(seed)
    steps = rng.randint(1, 6)
    player = game.players[game.current_turn_index]
    lang = normalize_lang(game)
    idx = (
        CONTINENTS_MOVEMENT_ORDER.index(player.continent)
        if player.continent in CONTINENTS_MOVEMENT_ORDER
        else 0
    )
    new_idx = (idx + steps) % len(CONTINENTS_MOVEMENT_ORDER)
    player.continent = CONTINENTS_MOVEMENT_ORDER[new_idx]

    if _continent_matches_event(card_repo, player.event_card_ids, player.continent, lang):
        game.phase = TurnPhase.SPINNER
        game.turn_state = {"dice_roll": steps}
    else:
        game.phase = TurnPhase.END_TURN
        game.turn_state = {"dice_roll": steps, "no_event_match": True}

    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
