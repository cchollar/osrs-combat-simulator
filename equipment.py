from abc import ABC, abstractmethod
from typing import List, Union, Dict
from dataclasses import dataclass, field
from pathlib import Path
import json

script_path = Path(__file__).resolve()
data_path = script_path.parent / "data"


class AttackType:
    pass


class StabAttackType(AttackType):
    pass


class SlashAttackType(AttackType):
    pass


class CrushAttackType(AttackType):
    pass


class RangeAttackType(AttackType):
    pass


class MagicAttackType(AttackType):
    pass


class WeaponStyle:
    pass


class AccurateMeleeStyle(WeaponStyle):
    pass


class AggressiveStyle(WeaponStyle):
    pass


class DefensiveStyle(WeaponStyle):
    pass


class ControlledStyle(WeaponStyle):
    pass


class AccurateRangeStyle(WeaponStyle):
    pass


class RapidStyle(WeaponStyle):
    pass


class LongrangeStyle(WeaponStyle):
    pass


class ShortFuseStyle(WeaponStyle):
    pass


class MediumFuseStyle(WeaponStyle):
    pass


class LongFuseStyle(WeaponStyle):
    pass


class AccurateMagicStyle(WeaponStyle):
    pass


class DefensiveAutocastStyle(WeaponStyle):
    pass


class AutocastStyle(WeaponStyle):
    pass


class WeaponStance:
    def __init__(self, attack_type: AttackType, weapon_style: WeaponStyle):
        self.attack_type = attack_type
        self.weapon_style = weapon_style


@dataclass
class StrengthBonuses:
    melee_strength: int
    range_strength: int
    magic_strength: int


@dataclass
class AttackBonuses:
    stab: int
    slash: int
    crush: int
    magic: int
    ranged: int


@dataclass
class DefenceBonuses:
    stab: int
    slash: int
    crush: int
    magic: int
    ranged: int


@dataclass
class Gear(ABC):
    name: str
    id: int
    slot: str
    speed: int
    category: str
    prayer_bonus: int
    strength_bonuses: StrengthBonuses
    attack_bonuses: AttackBonuses
    defence_bonuses: DefenceBonuses


@dataclass
class Weapon(Gear):
    name: str
    id: int
    slot: str
    speed: int
    category: str
    prayer_bonus: int
    is_2h: bool
    current_weapon_stance: WeaponStance = field(init=False)
    available_weapon_stances: Dict[str, WeaponStance]
    strength_bonuses: StrengthBonuses
    attack_bonuses: AttackBonuses
    defence_bonuses: DefenceBonuses

    def __post_init__(self):
        first_stance_key = next(iter(self.available_weapon_stances))
        self.current_weapon_stance = self.available_weapon_stances[first_stance_key]

    def select_stance(self, stance_name):
        selected_stance = self.available_weapon_stances.get(stance_name)
        if selected_stance:
            self.current_weapon_stance = selected_stance
            print(f"Selected stance is now: {self.current_weapon_stance}")
            return
        else:
            print(f"{selected_stance} is not an option for this weapon")
            return


@dataclass
class Armour(Gear):
    name: str
    id: int
    slot: str
    speed: int
    category: str
    prayer_bonus: int
    strength_bonuses: StrengthBonuses
    attack_bonuses: AttackBonuses
    defence_bonuses: DefenceBonuses


@dataclass
class Head(Armour):
    pass


@dataclass
class Neck(Armour):
    pass


@dataclass
class Body(Armour):
    pass


@dataclass
class Legs(Armour):
    pass


@dataclass
class Feet(Armour):
    pass


@dataclass
class Cape(Armour):
    pass


@dataclass
class Hands(Armour):
    pass


@dataclass
class Shield(Armour):
    pass


@dataclass
class Ammo(Armour):
    pass


class ArmourFactory:
    @staticmethod
    def create_armour(armour_name: str, armour_data: dict) -> Armour:
        if armour_name in armour_data:
            strength_bonuses = StrengthBonuses(**armour_data["bonuses"])
            attack_bonuses = AttackBonuses(**armour_data["offensive"])
            defence_bonuses = DefenceBonuses(**armour_data["defensive"])
            id = armour_data["id"]
            name = armour_data["name"]
            slot = armour_data["slot"]
            speed = armour_data["speed"]
            category = armour_data["category"]
            prayer_bonus = armour_data["prayer_bonus"]

            match slot:
                case "head":
                    return Head(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "neck":
                    return Neck(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "body":
                    return Body(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "legs":
                    return Legs(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "feet":
                    return Feet(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "cape":
                    return Cape(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "hands":
                    return Hands(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "shield":
                    return Shield(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )
                case "ammo":
                    return Ammo(
                        strength_bonuses=strength_bonuses,
                        attack_bonuses=attack_bonuses,
                        defence_bonuses=defence_bonuses,
                        id=id,
                        name=name,
                        slot=slot,
                        speed=speed,
                        category=category,
                        prayer_bonus=prayer_bonus,
                    )


class StanceOptionsFactory:
    @staticmethod
    def create_stance_options(weapon_category):
        stance_options = {}
        for combat_style, options in weapon_category.items():
            match options["attack_type"]:
                case "stab":
                    attack_type = StabAttackType()
                case "slash":
                    attack_type = SlashAttackType()
                case "crush":
                    attack_type = CrushAttackType()
                case "ranged":
                    attack_type = RangeAttackType()
                case "magic":
                    attack_type = MagicAttackType()

            match options["weapon_style"]:
                case "accurate":
                    if isinstance(attack_type, RangeAttackType):
                        weapon_style = AccurateRangeStyle()
                    elif isinstance(attack_type, MagicAttackType):
                        weapon_style = AccurateMagicStyle()
                    else:
                        weapon_style = AccurateMeleeStyle()
                case "aggressive":
                    weapon_style = AggressiveStyle()
                case "defensive":
                    weapon_style = DefensiveStyle()
                case "controlled":
                    weapon_style = ControlledStyle()
                case "rapid":
                    weapon_style = RapidStyle()
                case "longrange":
                    weapon_style = LongrangeStyle()
                case "short_fuse":
                    weapon_style = ShortFuseStyle()
                case "medium_fuse":
                    weapon_style = MediumFuseStyle()
                case "long_fuse":
                    weapon_style = LongFuseStyle()
                case "defensive_autocast":
                    weapon_style = DefensiveAutocastStyle()
                case "autocast":
                    weapon_style = AutocastStyle()
            stance_option = WeaponStance(attack_type, weapon_style)
            stance_options.update({combat_style: stance_option})

        return stance_options


class WeaponFactory:
    @staticmethod
    def create_weapon(weapon_name, weapons_data, weapon_types):
        if weapon_name in weapons_data:
            weapon_data = weapons_data[weapon_name]
            weapon_category = weapon_data.get("category")
            if weapon_category in weapon_types:
                available_weapon_stances = StanceOptionsFactory.create_stance_options(
                    weapon_types[weapon_category]
                )
                weapon_strength_bonuses = StrengthBonuses(**weapon_data["bonuses"])
                weapon_attack_bonuses = AttackBonuses(**weapon_data["offensive"])
                weapon_defence_bonuses = DefenceBonuses(**weapon_data["defensive"])

                weapon = Weapon(
                    strength_bonuses=weapon_strength_bonuses,
                    attack_bonuses=weapon_attack_bonuses,
                    defence_bonuses=weapon_defence_bonuses,
                    available_weapon_stances=available_weapon_stances,
                    id=weapon_data["id"],
                    name=weapon_data["name"],
                    slot=weapon_data["slot"],
                    speed=weapon_data["speed"],
                    category=weapon_category,
                    prayer_bonus=weapon_data["prayer_bonus"],
                    is_2h=weapon_data["is_2h"],
                )

                return weapon

            else:
                raise ValueError(f"Weapon category {weapon_category} not found in data")

        else:
            raise ValueError(f"Weapon {weapon_name} not found in data")


if __name__ == "__main__":

    weapon_stats = json.loads((data_path / "equipment_stats.json").read_text())
    weapon_types = json.loads((data_path / "weapon_types.json").read_text())

    ags = WeaponFactory.create_weapon("Armadyl godsword", weapon_stats, weapon_types)

    print(vars(ags))
    print(ags.current_weapon_stance.weapon_style)

    ags.select_stance("slash")
    print(ags.current_weapon_stance.weapon_style)

    print(vars(ags))
