from abc import ABC, abstractmethod
from typing import List, Union
from dataclasses import dataclass, field
from pathlib import Path
import json


@dataclass
class CombatStats:
    hitpoints: int
    strength: int
    attack: int
    defence: int
    range: int
    magic: int


@dataclass
class MonsterAggressiveStats:
    melee_attack_bonus: int
    melee_strength_bonus: int
    magic_attack_bonus: int
    magic_strength_bonus: int
    range_attack_bonus: int
    range_strength_bonus: int


@dataclass
class MonsterDefensiveStats:
    stab_defence: int
    slash_defence: int
    crush_defence: int
    magic_defence: int
    range_defence: int


@dataclass
class MonsterCombatInfo:
    size: int
    combat_level: int
    attributes: list
    attack_speed: Union[int, list]
    poisonous: bool


@dataclass
class MonsterImmunities:
    poison_immune: Union[bool, None]
    venom_immune: Union[bool, None]


@dataclass
class MonsterMetadata:
    examine: Union[list, str, None]
    category: Union[list, str, None]
    npc_id: Union[list, int]


class Character(ABC):
    @abstractmethod
    def __init__(self, combat_stats: CombatStats):
        self.combat_stats = combat_stats

    @abstractmethod
    def attempt_attack(self, target: "Character"):
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        pass

    @abstractmethod
    def die(self):
        pass


class Player(Character):
    def __init__(self, combat_stats: CombatStats):
        self.combat_stats = combat_stats

        self.stab_bonus: int = 0
        self.slash_bonus: int = 0
        self.crush_bonus: int = 0
        self.strength_bonus: int = 0
        self.magic_attack_bonus: int = 0
        self.magic_strength_bonus: int = 0
        self.range_attack_bonus: int = 0
        self.range_strength_bonus: int = 0

        self.stab_defence: int = 0
        self.slash_defence: int = 0
        self.crush_defence: int = 0
        self.magic_defence: int = 0
        self.range_defence: int = 0

        self.poison_immune: bool = False

        self.attack_timer: int = 0
        self.eat_timer: int = 0
        self.pot_timer: int = 0
        self.karam_timer: int = 0

        self.attack_speed: int = 4

    def attempt_attack():
        pass

    def take_damage(self, damage_value):
        self.combat_stats.hitpoints -= damage_value

    def die():
        pass


class Monster(Character):
    def __init__(
        self,
        combat_stats: CombatStats,
        aggressive_stats: MonsterAggressiveStats,
        defensive_stats: MonsterDefensiveStats,
        combat_info: MonsterCombatInfo,
        immunities: MonsterImmunities,
        metadata: MonsterMetadata,
    ):
        self.combat_stats = combat_stats
        self.aggressive_stats = aggressive_stats
        self.defensive_stat = defensive_stats
        self.combat_info = combat_info
        self.immunities = immunities
        self.metadata = metadata

    def attempt_attack(self, target: Character):
        pass

    def take_damage(self, damage_value):
        self.combat_stats.hitpoints -= damage_value

    def die(self):
        pass


def search_and_construct_monster(monster_string) -> Monster:
    base_path = Path(__file__).resolve().parent
    monsters_path = base_path / data / "monster_stats.json"
    monsters_stats = json.loads(monsters_path.read())

    monster_search_result = monsters_stats.get(monster_string)
