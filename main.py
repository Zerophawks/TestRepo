# generated by fastapi-codegen:
#   filename:  api_schema.yaml
#   timestamp: 2023-11-26T04:32:06+00:00

from __future__ import annotations

from typing import List

from fastapi import FastAPI, Path

from .models import (
    NPC,
    Campaign,
    Character,
    Dungeon,
    Encounter,
    Item,
    Monster,
    Quest,
    Session,
    Spell,
    User,
    World,
)

app = FastAPI()


@app.get('/campaigns', response_model=List[Campaign])
def get_campaigns() -> List[Campaign]:
    """
    Get a list of campaigns
    """
    pass


@app.post('/campaigns', response_model=None)
def post_campaigns(body: Campaign) -> None:
    """
    Create a new campaign
    """
    pass


@app.get('/characters', response_model=List[Character])
def get_characters() -> List[Character]:
    """
    Get a list of characters
    """
    pass


@app.post('/characters', response_model=None)
def post_characters(body: Character) -> None:
    """
    Create a new character
    """
    pass


@app.get('/dungeons', response_model=List[Dungeon])
def get_dungeons() -> List[Dungeon]:
    """
    List all dungeons
    """
    pass


@app.post('/dungeons', response_model=None)
def post_dungeons(body: Dungeon) -> None:
    """
    Create a new dungeon
    """
    pass


@app.get('/dungeons/{dungeonId}', response_model=Dungeon)
def get_dungeons_dungeon_id(dungeon_id: str = Path(..., alias='dungeonId')) -> Dungeon:
    """
    Get a dungeon by ID
    """
    pass


@app.put('/dungeons/{dungeonId}', response_model=None)
def put_dungeons_dungeon_id(
    dungeon_id: str = Path(..., alias='dungeonId'), body: Dungeon = ...
) -> None:
    """
    Update a dungeon by ID
    """
    pass


@app.delete('/dungeons/{dungeonId}', response_model=None)
def delete_dungeons_dungeon_id(dungeon_id: str = Path(..., alias='dungeonId')) -> None:
    """
    Delete a dungeon by ID
    """
    pass


@app.get('/encounters', response_model=List[Encounter])
def get_encounters() -> List[Encounter]:
    """
    Get a list of encounters
    """
    pass


@app.post('/encounters', response_model=None)
def post_encounters(body: Encounter) -> None:
    """
    Create a new encounter
    """
    pass


@app.get('/encounters/{encounterId}', response_model=Encounter)
def get_encounters_encounter_id(
    encounter_id: str = Path(..., alias='encounterId')
) -> Encounter:
    """
    Get an encounter by ID
    """
    pass


@app.put('/encounters/{encounterId}', response_model=None)
def put_encounters_encounter_id(
    encounter_id: str = Path(..., alias='encounterId'), body: Encounter = ...
) -> None:
    """
    Update an encounter by ID
    """
    pass


@app.delete('/encounters/{encounterId}', response_model=None)
def delete_encounters_encounter_id(
    encounter_id: str = Path(..., alias='encounterId')
) -> None:
    """
    Delete an encounter by ID
    """
    pass


@app.get('/items', response_model=List[Item])
def get_items() -> List[Item]:
    """
    Get a list of items
    """
    pass


@app.post('/items', response_model=None)
def post_items(body: Item) -> None:
    """
    Create a new item
    """
    pass


@app.get('/items/{itemId}', response_model=Item)
def get_items_item_id(item_id: str = Path(..., alias='itemId')) -> Item:
    """
    Get an item by ID
    """
    pass


@app.put('/items/{itemId}', response_model=None)
def put_items_item_id(
    item_id: str = Path(..., alias='itemId'), body: Item = ...
) -> None:
    """
    Update an item by ID
    """
    pass


@app.delete('/items/{itemId}', response_model=None)
def delete_items_item_id(item_id: str = Path(..., alias='itemId')) -> None:
    """
    Delete an item by ID
    """
    pass


@app.get('/monsters', response_model=List[Monster])
def get_monsters() -> List[Monster]:
    """
    Get a list of monsters
    """
    pass


@app.post('/monsters', response_model=None)
def post_monsters(body: Monster) -> None:
    """
    Create a new monster
    """
    pass


@app.get('/monsters/{monsterId}', response_model=Monster)
def get_monsters_monster_id(monster_id: str = Path(..., alias='monsterId')) -> Monster:
    """
    Get a monster by ID
    """
    pass


@app.put('/monsters/{monsterId}', response_model=None)
def put_monsters_monster_id(
    monster_id: str = Path(..., alias='monsterId'), body: Monster = ...
) -> None:
    """
    Update a monster by ID
    """
    pass


@app.delete('/monsters/{monsterId}', response_model=None)
def delete_monsters_monster_id(monster_id: str = Path(..., alias='monsterId')) -> None:
    """
    Delete a monster by ID
    """
    pass


@app.get('/npcs', response_model=List[NPC])
def get_npcs() -> List[NPC]:
    """
    Get a list of NPCs
    """
    pass


@app.post('/npcs', response_model=None)
def post_npcs(body: NPC) -> None:
    """
    Create a new NPC
    """
    pass


@app.get('/npcs/{npcId}', response_model=NPC)
def get_npcs_npc_id(npc_id: str = Path(..., alias='npcId')) -> NPC:
    """
    Get an NPC by ID
    """
    pass


@app.put('/npcs/{npcId}', response_model=None)
def put_npcs_npc_id(npc_id: str = Path(..., alias='npcId'), body: NPC = ...) -> None:
    """
    Update an NPC by ID
    """
    pass


@app.delete('/npcs/{npcId}', response_model=None)
def delete_npcs_npc_id(npc_id: str = Path(..., alias='npcId')) -> None:
    """
    Delete an NPC by ID
    """
    pass


@app.get('/quests', response_model=List[Quest])
def get_quests() -> List[Quest]:
    """
    Get a list of quests
    """
    pass


@app.post('/quests', response_model=None)
def post_quests(body: Quest) -> None:
    """
    Create a new quest
    """
    pass


@app.get('/quests/{questId}', response_model=Quest)
def get_quests_quest_id(quest_id: str = Path(..., alias='questId')) -> Quest:
    """
    Get a quest by ID
    """
    pass


@app.put('/quests/{questId}', response_model=None)
def put_quests_quest_id(
    quest_id: str = Path(..., alias='questId'), body: Quest = ...
) -> None:
    """
    Update a quest by ID
    """
    pass


@app.delete('/quests/{questId}', response_model=None)
def delete_quests_quest_id(quest_id: str = Path(..., alias='questId')) -> None:
    """
    Delete a quest by ID
    """
    pass


@app.get('/sessions', response_model=List[Session])
def get_sessions() -> List[Session]:
    """
    Get a list of sessions
    """
    pass


@app.post('/sessions', response_model=None)
def post_sessions(body: Session) -> None:
    """
    Create a new session
    """
    pass


@app.get('/sessions/{sessionId}', response_model=Session)
def get_sessions_session_id(session_id: str = Path(..., alias='sessionId')) -> Session:
    """
    Get a session by ID
    """
    pass


@app.put('/sessions/{sessionId}', response_model=None)
def put_sessions_session_id(
    session_id: str = Path(..., alias='sessionId'), body: Session = ...
) -> None:
    """
    Update a session by ID
    """
    pass


@app.delete('/sessions/{sessionId}', response_model=None)
def delete_sessions_session_id(session_id: str = Path(..., alias='sessionId')) -> None:
    """
    Delete a session by ID
    """
    pass


@app.get('/spells', response_model=List[Spell])
def get_spells() -> List[Spell]:
    """
    Get a list of spells
    """
    pass


@app.post('/spells', response_model=None)
def post_spells(body: Spell) -> None:
    """
    Create a new spell
    """
    pass


@app.get('/spells/{spellId}', response_model=Spell)
def get_spells_spell_id(spell_id: str = Path(..., alias='spellId')) -> Spell:
    """
    Get a spell by ID
    """
    pass


@app.put('/spells/{spellId}', response_model=None)
def put_spells_spell_id(
    spell_id: str = Path(..., alias='spellId'), body: Spell = ...
) -> None:
    """
    Update a spell by ID
    """
    pass


@app.delete('/spells/{spellId}', response_model=None)
def delete_spells_spell_id(spell_id: str = Path(..., alias='spellId')) -> None:
    """
    Delete a spell by ID
    """
    pass


@app.get('/users', response_model=List[User])
def get_users() -> List[User]:
    """
    Get a list of users
    """
    pass


@app.post('/users', response_model=None)
def post_users(body: User) -> None:
    """
    Create a new user
    """
    pass


@app.get('/users/{userId}', response_model=User)
def get_users_user_id(user_id: str = Path(..., alias='userId')) -> User:
    """
    Get a user by ID
    """
    pass


@app.put('/users/{userId}', response_model=None)
def put_users_user_id(
    user_id: str = Path(..., alias='userId'), body: User = ...
) -> None:
    """
    Update a user by ID
    """
    pass


@app.delete('/users/{userId}', response_model=None)
def delete_users_user_id(user_id: str = Path(..., alias='userId')) -> None:
    """
    Delete a user by ID
    """
    pass


@app.get('/worlds', response_model=List[World])
def get_worlds() -> List[World]:
    """
    Get a list of worlds
    """
    pass


@app.post('/worlds', response_model=None)
def post_worlds(body: World) -> None:
    """
    Create a new world
    """
    pass


@app.get('/worlds/{worldId}', response_model=World)
def get_worlds_world_id(world_id: str = Path(..., alias='worldId')) -> World:
    """
    Get a world by ID
    """
    pass


@app.put('/worlds/{worldId}', response_model=None)
def put_worlds_world_id(
    world_id: str = Path(..., alias='worldId'), body: World = ...
) -> None:
    """
    Update a world by ID
    """
    pass


@app.delete('/worlds/{worldId}', response_model=None)
def delete_worlds_world_id(world_id: str = Path(..., alias='worldId')) -> None:
    """
    Delete a world by ID
    """
    pass
