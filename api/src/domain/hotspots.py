"""GDD 7.1: Hotspot definitions (continent -> hotspot id and effect)."""
from typing import Any

# Continent -> list of (hotspot_id, effect_type). Effect: zone51_roswell = +1 gov or mil; rendlesham = debunker immunity; ruwa = +1 scientific; hessdalen = preview next event (applied in spin).
HOTSPOTS_BY_CONTINENT: dict[str, list[tuple[str, str]]] = {
    "north_america": [("zone51_roswell", "token_gov_mil")],
    "europe": [("rendlesham", "debunker_immunity"), ("hessdalen", "next_event_preview")],
    "africa": [("ruwa", "token_scientific")],
}


def get_hotspots_for_continent(continent: str) -> list[tuple[str, str]]:
    """Return list of (hotspot_id, effect_type) for the continent."""
    return HOTSPOTS_BY_CONTINENT.get(continent, [])
