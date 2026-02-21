"""Tests for game action use cases (with mocked repos)."""
import pytest
from src.domain.game import Game, Player, DisclosurePath, TurnPhase
from src.application.use_cases.game_action import _continent_matches_event


class MockCardRepo:
    def get_event(self, event_id: str, lang: str = "en"):
        if event_id == "E01":
            return {"id": "E01", "continent": "north_america"}
        if event_id == "E13":
            return {"id": "E13", "continent": "north_america"}
        if event_id == "E20":
            return {"id": "E20", "continent": "europe"}
        return None

    def list_events(self, lang: str = "en", pack: str | None = None):
        return [
            {"id": "E01", "continent": "north_america"},
            {"id": "E20", "continent": "europe"},
        ]


def test_continent_matches_event():
    repo = MockCardRepo()
    assert _continent_matches_event(repo, ["E01"], "north_america", "en") is True
    assert _continent_matches_event(repo, ["E01"], "europe", "en") is False
    assert _continent_matches_event(repo, ["E20"], "europe", "en") is True
    assert _continent_matches_event(repo, [], "north_america", "en") is False
    assert _continent_matches_event(repo, ["E01", "E20"], "europe", "en") is True
