# generated by fastapi-codegen:
#   filename:  /home/noob/projects/api_schema.yaml
#   timestamp: 2023-11-26T04:32:06+00:00

from __future__ import annotations

from datetime import date, datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, EmailStr, conint


class Campaign(BaseModel):
    campaignName: str
    description: str
    dungeonMaster: str
    players: List[str]
    startDate: date
    endDate: Optional[date] = None
    world: str
    mainStory: str
    sideQuests: Optional[List[str]] = None
    majorEvents: Optional[List[str]] = None
    notes: Optional[str] = None


class Attributes(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class Skills(BaseModel):
    acrobatics: Optional[int] = None
    animalHandling: Optional[int] = None
    arcana: Optional[int] = None
    athletics: Optional[int] = None
    deception: Optional[int] = None
    history: Optional[int] = None
    insight: Optional[int] = None
    intimidation: Optional[int] = None
    investigation: Optional[int] = None
    medicine: Optional[int] = None
    nature: Optional[int] = None
    perception: Optional[int] = None
    performance: Optional[int] = None
    persuasion: Optional[int] = None
    religion: Optional[int] = None
    sleightOfHand: Optional[int] = None
    stealth: Optional[int] = None
    survival: Optional[int] = None


class HitPoints(BaseModel):
    maximum: Optional[int] = None
    current: Optional[int] = None
    temporary: Optional[int] = None


class Character(BaseModel):
    characterName: str
    classAndLevel: str
    race: str
    background: Optional[str] = None
    alignment: Optional[str] = None
    playerName: Optional[str] = None
    experiencePoints: Optional[int] = None
    attributes: Attributes
    skills: Skills
    hitPoints: HitPoints
    equipment: Optional[List[str]] = None
    featuresAndTraits: Optional[List[str]] = None
    personalityTraits: Optional[str] = None
    ideals: Optional[str] = None
    bonds: Optional[str] = None
    flaws: Optional[str] = None


class Room(BaseModel):
    roomName: Optional[str] = None
    description: Optional[str] = None
    monsters: Optional[List[str]] = None
    items: Optional[List[str]] = None
    traps: Optional[str] = None
    treasure: Optional[str] = None


class Dungeon(BaseModel):
    dungeonName: str
    description: str
    location: str
    maps: Optional[List[str]] = None
    rooms: List[Room]
    history: Optional[str] = None
    challenges: Optional[List[str]] = None
    notes: Optional[str] = None


class Rewards(BaseModel):
    experiencePoints: Optional[int] = None
    items: Optional[List[str]] = None


class Encounter(BaseModel):
    encounterName: str
    description: str
    location: str
    difficulty: str
    monsters: List[str]
    npcs: Optional[List[str]] = None
    environment: Optional[str] = None
    rewards: Optional[Rewards] = None
    triggers: Optional[List[str]] = None
    outcome: Optional[List[str]] = None


class Value(BaseModel):
    gold: Optional[int] = None
    silver: Optional[int] = None
    copper: Optional[int] = None


class Effect(BaseModel):
    effectName: Optional[str] = None
    effectDescription: Optional[str] = None


class Item(BaseModel):
    itemName: str
    itemType: str
    description: str
    weight: float
    value: Value
    properties: Optional[List[str]] = None
    rarity: Optional[str] = None
    requiresAttunement: Optional[bool] = None
    effects: Optional[List[Effect]] = None
    quantity: Optional[conint(ge=1)] = None


class HitPoints1(BaseModel):
    average: Optional[int] = None
    formula: Optional[str] = None


class Attributes1(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class SpecialAbility(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Action(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class LegendaryAction(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Monster(BaseModel):
    name: str
    type: str
    size: Optional[str] = None
    alignment: Optional[str] = None
    challengeRating: str
    hitPoints: HitPoints1
    armorClass: int
    speed: Optional[str] = None
    attributes: Attributes1
    skills: Optional[Dict[str, int]] = None
    senses: Optional[str] = None
    languages: Optional[str] = None
    specialAbilities: Optional[List[SpecialAbility]] = None
    actions: Optional[List[Action]] = None
    legendaryActions: Optional[List[LegendaryAction]] = None


class Attributes2(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class NPC(BaseModel):
    npcName: str
    role: str
    alignment: str
    race: str
    attributes: Attributes2
    hitPoints: int
    armorClass: int
    skills: Optional[Dict[str, int]] = None
    languages: Optional[str] = None
    equipment: Optional[List[str]] = None
    background: Optional[str] = None
    personalityTraits: Optional[str] = None
    ideals: Optional[str] = None
    bonds: Optional[str] = None
    flaws: Optional[str] = None


class Rewards1(BaseModel):
    experiencePoints: Optional[int] = None
    items: Optional[List[str]] = None
    gold: Optional[int] = None


class Quest(BaseModel):
    questName: str
    description: str
    questGiver: str
    objectives: List[str]
    location: str
    rewards: Rewards1
    requiredLevel: Optional[int] = None
    recommendedPartySize: Optional[int] = None
    status: Optional[str] = None
    storyline: Optional[str] = None
    notes: Optional[str] = None


class Session(BaseModel):
    sessionNumber: int
    campaignID: str
    date: datetime
    duration: str
    location: Optional[str] = None
    participants: List[str]
    summary: str
    keyEvents: Optional[List[str]] = None
    notes: Optional[str] = None
    nextSession: Optional[datetime] = None


class Components(BaseModel):
    verbal: Optional[bool] = None
    somatic: Optional[bool] = None
    material: Optional[bool] = None
    materialDescription: Optional[str] = None


class Spell(BaseModel):
    spellName: str
    level: int
    school: str
    castingTime: str
    range: str
    components: Components
    duration: str
    description: str
    higherLevel: Optional[str] = None
    ritual: Optional[bool] = None
    concentration: Optional[bool] = None
    classes: Optional[List[str]] = None


class Preferences(BaseModel):
    theme: Optional[str] = None
    notifications: Optional[bool] = None


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    userType: str
    characters: Optional[List[str]] = None
    campaigns: Optional[List[str]] = None
    preferences: Optional[Preferences] = None
    dateJoined: date
    lastLogin: Optional[datetime] = None
    notes: Optional[str] = None


class Geography(BaseModel):
    continents: Optional[List[str]] = None
    oceans: Optional[List[str]] = None
    mountains: Optional[List[str]] = None
    forests: Optional[List[str]] = None
    rivers: Optional[List[str]] = None
    deserts: Optional[List[str]] = None


class Kingdom(BaseModel):
    name: Optional[str] = None
    ruler: Optional[str] = None
    capital: Optional[str] = None
    alliances: Optional[List[str]] = None


class Politics(BaseModel):
    kingdoms: Optional[List[Kingdom]] = None


class World(BaseModel):
    worldName: str
    description: str
    geography: Geography
    politics: Politics
