"""Card value objects (no I/O)."""
from enum import Enum
from typing import Any


class Authority(str, Enum):
    GOVERNMENT = "government"
    MILITARY = "military"
    SCIENTIFIC = "scientific"


class Continent(str, Enum):
    NORTH_AMERICA = "north_america"
    SOUTH_AMERICA = "south_america"
    EUROPE = "europe"
    AFRICA = "africa"
    ASIA = "asia"
    OCEANIA = "oceania"


DEFAULT_START_CONTINENT = Continent.NORTH_AMERICA.value

CONTINENTS_MOVEMENT_ORDER = [
    Continent.NORTH_AMERICA.value,
    Continent.EUROPE.value,
    Continent.ASIA.value,
    Continent.OCEANIA.value,
    Continent.AFRICA.value,
    Continent.SOUTH_AMERICA.value,
]


def event_card_from_dict(d: dict[str, Any]) -> dict[str, Any]:
    """Validate and return event card dict (id, title, year, continent, authority, level, ...)."""
    return {
        "id": d.get("id", ""),
        "title": d.get("title", ""),
        "year": d.get("year", 0),
        "continent": d.get("continent", ""),
        "authority": d.get("authority", ""),
        "level": d.get("level", 1),
        "description": d.get("description", ""),
        "image": d.get("image", ""),
        "linked_trivia": d.get("linked_trivia", []),
        "linked_deduction": d.get("linked_deduction", []),
    }


def trivia_card_from_dict(d: dict[str, Any]) -> dict[str, Any]:
    """Validate and return trivia card dict."""
    return {
        "id": d.get("id", ""),
        "type": "trivia",
        "level": d.get("level", 1),
        "authority": d.get("authority", ""),
        "theme": d.get("theme", ""),
        "question": d.get("question", ""),
        "answers": d.get("answers", []),
        "context": d.get("context", ""),
        "linked_event": d.get("linked_event", ""),
        "timer_normal": d.get("timer_normal", 30),
        "timer_expert": d.get("timer_expert", 15),
    }
