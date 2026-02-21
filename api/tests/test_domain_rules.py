"""Unit tests for domain rules (pure, no I/O)."""
import pytest
from src.domain import rules
from src.domain.game import DisclosurePath


def test_spin_result_deterministic():
    r1 = rules.spin_result(seed=42)
    r2 = rules.spin_result(seed=42)
    assert r1 == r2


def test_spin_result_valid_outcomes():
    valid = {"government", "military", "scientific", "obstacle", "special"}
    for seed in range(100):
        assert rules.spin_result(seed=seed) in valid


def test_roll_dice_range():
    for seed in range(50):
        n = rules.roll_dice(seed=seed)
        assert 1 <= n <= 6


def test_has_full_disclosure():
    assert rules.has_full_disclosure(DisclosurePath(3, 3, 3)) is True
    assert rules.has_full_disclosure(DisclosurePath(3, 3, 2)) is False
    assert rules.has_full_disclosure(DisclosurePath(0, 0, 0)) is False


def test_is_authority_confirmed():
    path = DisclosurePath(3, 1, 0)
    assert rules.is_authority_confirmed(path, "government") is True
    assert rules.is_authority_confirmed(path, "military") is False
    assert rules.is_authority_confirmed(path, "scientific") is False
