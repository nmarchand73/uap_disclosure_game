"""Use case: create a new game."""
import random
import uuid
from datetime import datetime, timezone

from src.domain.game import Game, Player, DisclosurePath, TurnPhase
from src.domain.cards import DEFAULT_START_CONTINENT
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang


def _starting_continent_for_character(card_repo: ICardRepository, character_id: str, lang: str) -> str:
    """GDD 5.1 / 4: each character starts on their starting continent. Fallback: DEFAULT_START_CONTINENT."""
    chars = card_repo.list_characters(lang=lang)
    for c in chars:
        if c.get("id") == character_id:
            starts = c.get("starting_continents") or []
            if starts:
                return starts[0]
            break
    return DEFAULT_START_CONTINENT


def create_game(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    player_name: str,
    character_id: str,
    character_variant: str,
    mode: str = "solo",
    lang: str = "en",
) -> Game:
    """Create a new game with one player; draw initial event cards from deck."""
    game_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()
    lang = normalize_lang(lang)

    events = card_repo.list_events(lang=lang)
    event_ids = [e["id"] for e in events] if events else []
    trivia_ids = [t["id"] for t in card_repo.list_trivia(lang=lang)] if card_repo.list_trivia(lang=lang) else []

    random.shuffle(event_ids)
    player_event_ids = event_ids[:3] if len(event_ids) >= 3 else event_ids.copy()
    random.shuffle(trivia_ids)

    start_continent = _starting_continent_for_character(card_repo, character_id, lang)
    player = Player(
        id="p1",
        name=player_name,
        character_id=character_id,
        character_variant=character_variant,
        continent=start_continent,
        disclosure_path=DisclosurePath(),
        event_card_ids=player_event_ids,
    )

    game = Game(
        id=game_id,
        players=[player],
        current_turn_index=0,
        phase=TurnPhase.LOBBY,
        deck_event_ids=event_ids,
        deck_trivia_ids=trivia_ids,
        deck_deduction_ids=[],
        created_at=now,
        updated_at=now,
        preferred_lang=lang,
    )

    game_repo.create(game)
    return game
