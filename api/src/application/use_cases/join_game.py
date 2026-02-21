"""Use case: join an existing game as a new player."""
import random
from datetime import datetime, timezone

from src.domain.game import Game, Player, DisclosurePath
from src.application.ports.game_repository import IGameRepository
from src.application.ports.card_repository import ICardRepository
from src.application.lang import normalize_lang
from src.application.use_cases.create_game import _starting_continent_for_character


def join_game(
    game_repo: IGameRepository,
    card_repo: ICardRepository,
    game_id: str,
    player_name: str,
    character_id: str,
    character_variant: str,
) -> Game | None:
    """Add a new player to the game. Fails if game not found or not in lobby."""
    game = game_repo.get(game_id)
    if not game:
        return None
    if game.phase.value != "lobby":
        return None
    if len(game.players) >= 6:
        return None

    lang = normalize_lang(game)
    events = card_repo.list_events(lang=lang)
    event_ids = [e["id"] for e in events] if events else []
    random.shuffle(event_ids)
    player_event_ids = event_ids[:3] if len(event_ids) >= 3 else event_ids.copy()

    start_continent = _starting_continent_for_character(card_repo, character_id, lang)
    new_id = f"p{len(game.players) + 1}"
    player = Player(
        id=new_id,
        name=player_name,
        character_id=character_id,
        character_variant=character_variant,
        continent=start_continent,
        disclosure_path=DisclosurePath(),
        event_card_ids=player_event_ids,
    )
    game.players.append(player)
    game.updated_at = datetime.now(timezone.utc).isoformat()
    game_repo.save(game)
    return game
