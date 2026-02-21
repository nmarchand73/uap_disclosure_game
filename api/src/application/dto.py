"""Input/Output DTOs for use cases."""
from typing import Any


def game_to_public_dto(game: Any) -> dict[str, Any]:
    """Serialize game for API response."""
    return game.to_dict()
