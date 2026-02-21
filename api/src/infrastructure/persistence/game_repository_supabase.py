"""Supabase game repository: persist game state in PostgreSQL (optional)."""
from src.application.ports.game_repository import IGameRepository
from src.domain.game import Game


class GameRepositorySupabase(IGameRepository):
    """Store game state as JSON in Supabase table 'games' (id, state, updated_at)."""

    def __init__(self, url: str, key: str, table: str = "games"):
        try:
            from supabase import create_client
        except ImportError:
            raise ImportError("supabase package required for GameRepositorySupabase")
        self._client = create_client(url, key)
        self._table = table

    def get(self, game_id: str) -> Game | None:
        try:
            r = self._client.table(self._table).select("state").eq("id", game_id).execute()
            if not r.data or len(r.data) == 0:
                return None
            row = r.data[0]
            state = row.get("state") if isinstance(row, dict) else None
            if not state:
                return None
            return Game.from_dict(state)
        except Exception:
            return None

    def save(self, game: Game) -> None:
        self.create(game)

    def create(self, game: Game) -> None:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc).isoformat()
        payload = {"id": game.id, "state": game.to_dict(), "updated_at": now}
        try:
            self._client.table(self._table).upsert([payload], on_conflict="id").execute()
        except Exception:
            existing = self.get(game.id)
            if existing:
                self._client.table(self._table).update({"state": game.to_dict(), "updated_at": now}).eq("id", game.id).execute()
            else:
                self._client.table(self._table).insert(payload).execute()
