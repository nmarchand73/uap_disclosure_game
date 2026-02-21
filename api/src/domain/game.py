"""Game and player entities, value objects, turn phase."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from src.domain.cards import DEFAULT_START_CONTINENT


class TurnPhase(str, Enum):
    LOBBY = "lobby"
    MOVEMENT = "movement"
    SPINNER = "spinner"
    QUESTION = "question"
    OBSTACLE = "obstacle"
    END_TURN = "end_turn"


@dataclass
class DisclosurePath:
    """Per-player progression: 3 tokens per authority (government, military, scientific)."""
    government: int = 0
    military: int = 0
    scientific: int = 0

    def to_dict(self) -> dict[str, int]:
        return {
            "government": self.government,
            "military": self.military,
            "scientific": self.scientific,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "DisclosurePath":
        return cls(
            government=d.get("government", 0),
            military=d.get("military", 0),
            scientific=d.get("scientific", 0),
        )


@dataclass
class Player:
    """Player in a game."""
    id: str
    name: str
    character_id: str
    character_variant: str
    continent: str
    disclosure_path: DisclosurePath
    event_card_ids: list[str] = field(default_factory=list)
    skill_used: bool = False
    # GDD 8.4 / 8.5: obstacle penalties
    skip_next_turn: bool = False
    movement_penalty: int = 0
    # GDD 5.2: wrong authority on spinner → bonus mineur (+1 move next turn)
    next_move_bonus: int = 0
    # GDD 7.1: hotspots used this game (zone51_roswell, rendlesham, ruwa, hessdalen)
    hotspot_used: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "character_id": self.character_id,
            "character_variant": self.character_variant,
            "continent": self.continent,
            "disclosure_path": self.disclosure_path.to_dict(),
            "event_card_ids": self.event_card_ids,
            "skill_used": self.skill_used,
            "skip_next_turn": self.skip_next_turn,
            "movement_penalty": self.movement_penalty,
            "next_move_bonus": self.next_move_bonus,
            "hotspot_used": list(self.hotspot_used),
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Player":
        return cls(
            id=d.get("id", ""),
            name=d.get("name", ""),
            character_id=d.get("character_id", ""),
            character_variant=d.get("character_variant", ""),
            continent=d.get("continent", DEFAULT_START_CONTINENT),
            disclosure_path=DisclosurePath.from_dict(d.get("disclosure_path", {})),
            event_card_ids=list(d.get("event_card_ids", [])),
            skill_used=d.get("skill_used", False),
            skip_next_turn=d.get("skip_next_turn", False),
            movement_penalty=int(d.get("movement_penalty", 0)),
            next_move_bonus=int(d.get("next_move_bonus", 0)),
            hotspot_used=list(d.get("hotspot_used", [])),
        )


@dataclass
class Game:
    """Game session state."""
    id: str
    players: list[Player]
    current_turn_index: int
    phase: TurnPhase
    deck_event_ids: list[str]
    deck_trivia_ids: list[str]
    deck_deduction_ids: list[str]
    created_at: str = ""
    updated_at: str = ""
    preferred_lang: str = "en"
    mode: str = "solo"  # "solo" | "coop" (GDD 6.2: shared path win)
    # Turn state: spinner_result, pending_question_id, pending_authority (for question flow)
    turn_state: dict = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "players": [p.to_dict() for p in self.players],
            "current_turn_index": self.current_turn_index,
            "phase": self.phase.value,
            "deck_event_ids": self.deck_event_ids,
            "deck_trivia_ids": self.deck_trivia_ids,
            "deck_deduction_ids": self.deck_deduction_ids,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "preferred_lang": self.preferred_lang,
            "mode": self.mode,
            "turn_state": self.turn_state,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Game":
        phase_val = d.get("phase", "lobby")
        try:
            phase = TurnPhase(phase_val)
        except ValueError:
            phase = TurnPhase.LOBBY
        return cls(
            id=d.get("id", ""),
            players=[Player.from_dict(p) for p in d.get("players", [])],
            current_turn_index=int(d.get("current_turn_index", 0)),
            phase=phase,
            deck_event_ids=list(d.get("deck_event_ids", [])),
            deck_trivia_ids=list(d.get("deck_trivia_ids", [])),
            deck_deduction_ids=list(d.get("deck_deduction_ids", [])),
            created_at=d.get("created_at", ""),
            updated_at=d.get("updated_at", ""),
            preferred_lang=d.get("preferred_lang", "en"),
            mode=d.get("mode", "solo"),
            turn_state=dict(d.get("turn_state", {})),
        )
