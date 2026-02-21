"""Use case: use skill token (GDD 6.3). One-time +1 token on any authority."""
from datetime import datetime, timezone

from src.domain.game import Game, TurnPhase
from src.application.ports.game_repository import IGameRepository
from src.application.use_cases.actions.spin import _add_token_any_authority


def use_skill(
    game_repo: IGameRepository,
    game_id: str,
) -> Game | None:
    """Use skill token: +1 token on any authority (once per game). Allowed in movement or spinner phase."""
    game = game_repo.get(game_id)
    if not game or not game.players:
        return None
    if game.phase not in (TurnPhase.MOVEMENT, TurnPhase.SPINNER):
        return None
    player = game.players[game.current_turn_index]
    if player.skill_used:
        return None
    player.skill_used = True
    _add_token_any_authority(player)
    game.turn_state["skill_used"] = True
    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
