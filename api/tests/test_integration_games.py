"""Integration tests: HTTP endpoints for games and game action."""
import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_post_games_creates_game():
    """POST /api/games returns 200 and creates a game in lobby."""
    resp = client.post(
        "/api/games",
        json={
            "player_name": "TestPlayer",
            "character_id": "journalist",
            "character_variant": "investigation",
            "lang": "en",
        },
    )
    assert resp.status_code == 200
    body = resp.json()
    assert "id" in body
    assert body["phase"] == "lobby"
    assert len(body["players"]) == 1
    assert body["players"][0]["name"] == "TestPlayer"


def test_post_games_action_move():
    """POST /api/games then POST /api/games/{id}/action (move) returns 200 and updates phase."""
    create = client.post(
        "/api/games",
        json={
            "player_name": "P1",
            "character_id": "journalist",
            "character_variant": "investigation",
            "lang": "en",
        },
    )
    assert create.status_code == 200
    game_id = create.json()["id"]

    action = client.post(
        f"/api/games/{game_id}/action",
        json={"action": "move"},
    )
    assert action.status_code == 200
    body = action.json()
    assert body["phase"] in ("spinner", "end_turn")
    assert "turn_state" in body
    assert "dice_roll" in body["turn_state"]
