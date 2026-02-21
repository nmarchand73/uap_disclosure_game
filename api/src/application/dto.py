"""Input/Output DTOs for use cases."""
from typing import Any

from src.domain.rules import has_full_disclosure, has_coop_win, coop_shared_path


def game_to_public_dto(game: Any) -> dict[str, Any]:
    """Serialize game for API response. Adds shared_path and won when mode is coop."""
    d = game.to_dict()
    if getattr(game, "mode", "solo") == "coop" and getattr(game, "players", None):
        d["shared_path"] = coop_shared_path(game.players)
        d["won"] = has_coop_win(game.players)
    else:
        # Solo/competitive: won if current player has full disclosure (or any player for simplicity)
        won = False
        for p in getattr(game, "players", []) or []:
            if has_full_disclosure(p.disclosure_path):
                won = True
                break
        d["won"] = won
    return d
