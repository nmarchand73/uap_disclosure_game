"""Card repository: load from bundled JSON files, cache in module global."""
import json
from pathlib import Path
from typing import Any

from src.application.ports.card_repository import ICardRepository
from src.domain.cards import event_card_from_dict, trivia_card_from_dict

# Module-level cache (reused across Lambda invocations). Key: (name, lang)
_CACHE: dict[tuple[str, str], list[dict[str, Any]]] = {}


def _data_dir() -> Path:
    # From api/src/infrastructure/persistence -> api/data
    this_file = Path(__file__).resolve()
    api_src = this_file.parent.parent.parent  # api/src
    api_root = api_src.parent  # api
    return api_root / "data"


def _load_json(name: str, lang: str = "en") -> list[dict[str, Any]]:
    cache_key = (name, lang)
    if cache_key in _CACHE:
        return _CACHE[cache_key]
    data_dir = _data_dir()
    if lang == "fr":
        path = data_dir / "fr" / f"{name}.json"
        if not path.exists():
            path = data_dir / f"{name}.json"
    else:
        path = data_dir / f"{name}.json"
    if not path.exists():
        _CACHE[cache_key] = []
        return _CACHE[cache_key]
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    _CACHE[cache_key] = data if isinstance(data, list) else [data]
    return _CACHE[cache_key]


class CardRepositoryJson(ICardRepository):
    def list_events(self, lang: str = "en", pack: str | None = None) -> list[dict[str, Any]]:
        raw = _load_json("events", lang)
        out = [event_card_from_dict(e) for e in raw]
        if pack:
            out = [e for e in out if e.get("pack") == pack]
        return out

    def get_event(self, event_id: str, lang: str = "en") -> dict[str, Any] | None:
        for e in self.list_events(lang=lang):
            if e.get("id") == event_id:
                return e
        return None

    def list_trivia(
        self,
        lang: str = "en",
        authority: str | None = None,
        level: int | None = None,
    ) -> list[dict[str, Any]]:
        raw = _load_json("trivia", lang)
        out = [trivia_card_from_dict(t) for t in raw]
        if authority:
            out = [t for t in out if t.get("authority") == authority]
        if level is not None:
            out = [t for t in out if t.get("level") == level]
        return out

    def get_trivia(self, trivia_id: str, lang: str = "en") -> dict[str, Any] | None:
        for t in self.list_trivia(lang=lang):
            if t.get("id") == trivia_id:
                return t
        return None

    def list_characters(self, lang: str = "en") -> list[dict[str, Any]]:
        return _load_json("characters", lang)

    def list_continents(self, lang: str = "en") -> list[dict[str, Any]]:
        return _load_json("continents", lang)

    def list_skeptic(self, lang: str = "en") -> list[dict[str, Any]]:
        raw = _load_json("skeptic", lang)
        return [{"id": s.get("id"), "question": s.get("question"), "answers": s.get("answers", []), "context": s.get("context", "")} for s in raw]

    def get_skeptic(self, skeptic_id: str, lang: str = "en") -> dict[str, Any] | None:
        for s in self.list_skeptic(lang=lang):
            if s.get("id") == skeptic_id:
                return s
        return None

    def list_debunker(self, lang: str = "en") -> list[dict[str, Any]]:
        raw = _load_json("debunker", lang)
        return [
            {"id": d.get("id"), "question": d.get("question"), "answers": d.get("answers", []), "context": d.get("context", "")}
            for d in raw
        ]

    def get_debunker(self, debunker_id: str, lang: str = "en") -> dict[str, Any] | None:
        for d in self.list_debunker(lang=lang):
            if d.get("id") == debunker_id:
                return d
        return None

    def list_deduction(self, lang: str = "en", authority: str | None = None) -> list[dict[str, Any]]:
        raw = _load_json("deduction", lang)
        out = [{"id": d.get("id"), "question": d.get("question"), "answers": d.get("answers", []), "authority": d.get("authority", ""), "context": d.get("context", "")} for d in raw]
        if authority:
            out = [x for x in out if x.get("authority") == authority]
        return out

    def get_deduction(self, deduction_id: str, lang: str = "en") -> dict[str, Any] | None:
        for d in self.list_deduction(lang=lang):
            if d.get("id") == deduction_id:
                return d
        return None
