"""Request/response schemas for the games API (validation and docs)."""
from typing import Literal

from pydantic import BaseModel, Field


class CreateGameBody(BaseModel):
    """Body for POST /api/games."""

    player_name: str = Field(default="Player", description="Display name")
    character_id: str = Field(default="journalist", description="Character id from cards")
    character_variant: str = Field(default="investigation", description="Variant")
    mode: str = Field(default="solo", description="Game mode")
    lang: str = Field(default="en", description="Preferred language (en|fr)")


class JoinGameBody(BaseModel):
    """Body for POST /api/games/{game_id}/join."""

    player_name: str = Field(default="Player", description="Display name")
    character_id: str = Field(default="journalist", description="Character id from cards")
    character_variant: str = Field(default="investigation", description="Variant")


class GameActionBody(BaseModel):
    """Body for POST /api/games/{game_id}/action."""

    action: Literal["move", "spin", "submit_answer", "use_skill"] = Field(..., description="Action to perform")
    seed: int | None = Field(default=None, description="Optional RNG seed (for tests)")
    answer_index: int = Field(default=0, ge=0, description="Answer index (for submit_answer)")
