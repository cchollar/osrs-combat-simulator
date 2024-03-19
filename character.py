from abc import ABC, abstractmethod
from typing import List


class Character(ABC):
    @abstractmethod
    def __init__(
        self,
        hitpoints: int,
        strength: int,
        attack: int,
        defence: int,
        range: int,
        magic: int,
    ):
        self.hitpoints = hitpoints
        self.strength = strength
        self.attack = attack
        self.defence = defence
        self.range = range
        self.magic = magic

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
    def __init__(
        self,
        hitpoints: int,
        strength: int,
        attack: int,
        defence: int,
        range: int,
        magic: int,
    ):
        self.hitpoints = hitpoints
        self.strength = strength
        self.attack = attack
        self.defence = defence
        self.range = range
        self.magic = magic

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

    def take_damage():
        pass

    def die():
        pass


class NPC(Character):
    def __init__(
        self,
        size: int,
        attributes: List[str],
        attack_styles: List[str],
        attack_speed: int,
        hitpoints: int,
        attack: int,
        strength: int,
        defence: int,
        magic: int,
        range: int,
        melee_attack_bonus: int,
        melee_strength_bonus: int,
        magic_attack_bonus: int,
        magic_strength_bonus: int,
        range_attack_bonus: int,
        range_strength_bonus: int,
        stab_defence: int,
        slash_defence: int,
        crush_defence: int,
        magic_defence: int,
        range_defence: int,
        poison_immune: bool,
        venom_immune: bool,
        cannon_immune: bool,
        thrall_immune: bool,
    ):
        self.size = size
        self.attributes = attributes
        self.attack_styles = attack_styles
        self.attack_speed = attack_speed
        self.hitpoints = hitpoints
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.range = range
        self.melee_attack_bonus = melee_attack_bonus
        self.melee_strength_bonus = melee_strength_bonus
        self.magic_attack_bonus = magic_attack_bonus
        self.magic_strength_bonus = magic_strength_bonus
        self.range_attack_bonus = range_attack_bonus
        self.range_strength_bonus = range_strength_bonus
        self.stab_defence = stab_defence
        self.slash_defence = slash_defence
        self.crush_defence = crush_defence
        self.magic_defence = magic_defence
        self.range_defence = range_defence
        self.poison_immune = poison_immune
        self.venom_immune = venom_immune
        self.cannon_immune = cannon_immune
        self.thrall_immune = thrall_immune

    def attempt_attack():
        pass

    def take_damage():
        pass

    def die():
        pass


p = Player(hitpoints=10, strength=10, attack=10, defence=10, range=10, magic=10)
n = NPC()
