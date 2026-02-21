"""Supported languages and normalization for game/content (application layer)."""
from typing import Any, Union

SUPPORTED_LANGUAGES = ("en", "fr")
DEFAULT_LANG = "en"


def normalize_lang(lang_or_game: Union[str, None, Any]) -> str:
    """Return a supported language code. Accepts raw lang string or a Game with preferred_lang."""
    if lang_or_game is None:
        return DEFAULT_LANG
    if isinstance(lang_or_game, str):
        return lang_or_game if lang_or_game in SUPPORTED_LANGUAGES else DEFAULT_LANG
    lang = getattr(lang_or_game, "preferred_lang", None) or DEFAULT_LANG
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANG
