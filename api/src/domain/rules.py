"""Pure game rules: spinner outcome, token progression, win condition (no I/O)."""
import random
from src.domain.game import DisclosurePath
from src.domain.cards import Authority

SPINNER_OUTCOME_OBSTACLE = "obstacle"
SPINNER_OUTCOME_SPECIAL = "special"

SPINNER_AUTHORITY_VALUES = (Authority.GOVERNMENT.value, Authority.MILITARY.value, Authority.SCIENTIFIC.value)

# Spinner outcome cumulative probabilities (GDD: ~20% gov, ~20% mil, ~20% sci, ~25% obstacle, ~15% special)
PROB_GOVERNMENT = 0.20
PROB_MILITARY = 0.20
PROB_SCIENTIFIC = 0.20
PROB_OBSTACLE = 0.25
PROB_SPECIAL = 0.15


def spin_result(seed: int | None = None) -> str:
    """Return one of: government, military, scientific, obstacle, special."""
    rng = random.Random(seed)
    roll = rng.random()
    if roll < PROB_GOVERNMENT:
        return Authority.GOVERNMENT.value
    if roll < PROB_GOVERNMENT + PROB_MILITARY:
        return Authority.MILITARY.value
    if roll < PROB_GOVERNMENT + PROB_MILITARY + PROB_SCIENTIFIC:
        return Authority.SCIENTIFIC.value
    if roll < PROB_GOVERNMENT + PROB_MILITARY + PROB_SCIENTIFIC + PROB_OBSTACLE:
        return SPINNER_OUTCOME_OBSTACLE
    return SPINNER_OUTCOME_SPECIAL


def roll_dice(seed: int | None = None) -> int:
    """Return 1–6."""
    rng = random.Random(seed)
    return rng.randint(1, 6)


def is_authority_confirmed(path: DisclosurePath, authority: str) -> bool:
    """True if this authority has 3 tokens."""
    thresholds = {
        Authority.GOVERNMENT.value: path.government,
        Authority.MILITARY.value: path.military,
        Authority.SCIENTIFIC.value: path.scientific,
    }
    return thresholds.get(authority, 0) >= 3


def has_full_disclosure(path: DisclosurePath) -> bool:
    """True if all three authorities are confirmed (win condition)."""
    return (
        path.government >= 3
        and path.military >= 3
        and path.scientific >= 3
    )


def coop_shared_path(players: list) -> dict[str, int]:
    """GDD 6.2: sum tokens across all players for cooperative mode."""
    gov = mil = sci = 0
    for p in players:
        path = getattr(p, "disclosure_path", None)
        if path:
            gov += getattr(path, "government", 0) or 0
            mil += getattr(path, "military", 0) or 0
            sci += getattr(path, "scientific", 0) or 0
    return {"government": gov, "military": mil, "scientific": sci}


def has_coop_win(players: list) -> bool:
    """True if team has 3+ tokens per authority (coop win)."""
    sp = coop_shared_path(players)
    return sp["government"] >= 3 and sp["military"] >= 3 and sp["scientific"] >= 3
