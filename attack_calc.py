import math
import random as rand

def calc_effective_melee_strength_level(base_level: int, boost: int, prayer: float, stance_bonus: int = 0, void: bool = False) -> int:
    """Calcuate a player's effective melee strength level

    Args:
        base_level (int): Non boosted strength stat, from 1 to 99
        boost (int): additional boost caused by potion, overload, smelling salts, etc
        prayer (float): a postive multiplier from the strength-boosting offensive prayers like Piety
        stance_bonus (int): combat stance in-game, typically +3 if stance is aggressive. Defaults to 0
        void (bool, optional): Whether the player is wearing Void Melee. Defaults to False.

    Returns:
        int: An effective melee strength level
    """
    effective_level = (base_level + boost) * prayer
    effective_level = math.floor(effective_level)
    effective_level += stance_bonus
    effective_level += 8
    if void:
        effective_level *= 1.1

    effective_level = math.floor(effective_level)
    return effective_level

# Potential DRY violations here, but I want granularity between the effective level calculations for now esp with elite / reg void, future refactors may include combining functions
def calc_effective_melee_attack_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    """Calcuate a player's effective melee attack level

    Args:
        base_level (int): Non boosted attack stat, from 1 to 99
        boost (int): additional boost caused by potion, overload, smelling salts, etc
        prayer (float): a postive multiplier from the attack-boosting offensive prayers like Piety
        stance_bonus (int): combat stance in-game, typically +3 if stance is accurate. Defaults to 0
        void (bool, optional): Whether the player is wearing Void Melee. Defaults to False.

    Returns:
        int: An effective melee attack level
    """
    effective_level = (base_level + boost) * prayer
    effective_level = math.floor(effective_level)
    effective_level += stance_bonus
    effective_level += 8
    if void:
        effective_level *= 1.1

    effective_level = math.floor(effective_level)
    return effective_level

def calc_effective_range_attack_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    """Calcuate a player's effective range level

    Args:
        base_level (int): Non boosted range stat, from 1 to 99
        boost (int): additional boost caused by potion, overload, smelling salts, etc
        prayer (float): a postive multiplier from the range-attack-boosting offensive prayers like Rigour
        stance_bonus (int): combat stance in-game, typically +3 if stance is accurate. Defaults to 0
        void (bool, optional): Whether the player is wearing Elite Void Range. Defaults to False.

    Returns:
        int: An effective range attack level
    """
    effective_level = (base_level + boost) * prayer
    effective_level = math.floor(effective_level)
    effective_level += stance_bonus
    effective_level += 8
    if void:
        effective_level *= 1.1
    effective_level = math.floor(effective_level)
    return effective_level

def calc_effective_range_strength_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    """Calcuate a player's effective range strength level

    Args:
        base_level (int): Non boosted range stat, from 1 to 99
        boost (int): additional boost caused by potion, overload, smelling salts, etc
        prayer (float): a postive multiplier from the range-attack-boosting offensive prayers like Rigour
        stance_bonus (int): combat stance in-game, typically +3 if stance is accurate. Defaults to 0
        void (bool, optional): Whether the player is wearing Elite Void Range. Defaults to False.

    Returns:
        int: An effective range strength level
    """
    effective_level = (base_level + boost) * prayer
    effective_level = math.floor(effective_level)
    effective_level += stance_bonus
    effective_level += 8
    if void:
        effective_level *= 1.1
    effective_level = math.floor(effective_level)
    return effective_level

def calc_effective_magic_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    effective_level = (base_level + boost) * prayer
    effective_level = math.floor(effective_level)
    effective_level += stance_bonus
    effective_level += 8
    if void:
        effective_level *= 1.45
    effective_level = math.floor(effective_level)
    return effective_level

def calc_max_melee_hit(effective_strength_level: int, equipment_bonus: int, target_bonus: float = 1.0) -> int:
    """Calculates the maximum rollable hit for a melee attack

    Args:
        effective_strength_level (int): effective strength level stat
        equipment_bonus (int): strength bonus shown on equipment screen
        target_bonus (float, optional): Multiplier for exclusive damage buffs like slayer helmet or salve amulet. Defaults to 1.0.

    Returns:
        int: Maximum rollable hit for selected gear and stats
    """
    max_hit = effective_strength_level * (equipment_bonus + 64)
    max_hit += 320
    max_hit = math.floor(max_hit / 640)
    max_hit = math.floor(max_hit * target_bonus)
    return max_hit

def calc_range_max_hit(effective_range_level: int, equipment_bonus: int, target_bonus: float = 1.0) -> int:
    max_hit = effective_range_level * (equipment_bonus + 64)
    max_hit += 320
    max_hit = math.floor(max_hit / 640)
    max_hit = math.floor(max_hit * target_bonus)
    return max_hit

def calc_max_attack_roll(effective_attack_level: int, equipment_bonus: int, target_bonus: float = 1.0) -> int:
    attack_roll = effective_attack_level * (equipment_bonus + 64)
    attack_roll *= target_bonus
    attack_roll = math.floor(attack_roll)
    return attack_roll

def calc_npc_max_defence_roll(base_level: int, style_bonus: int) -> int:
    defence_roll = (base_level + 9) * (style_bonus + 64)
    return defence_roll

def calc_player_max_magic_defence_roll(magic_level: int, magic_boost: int, effective_defence_level: int, equipment_bonus: int, prayer: float = 1.0) -> int:
    effective_defence_level = math.floor(effective_defence_level * 0.3)
    
    magic_level = (magic_level + magic_boost) * prayer
    magic_level = math.floor(magic_level)
    effective_magic_level = math.floor(magic_level * 0.7)

    effective_level = effective_magic_level + effective_defence_level
    
    magic_defence_roll = effective_level * (equipment_bonus + 64)

    return magic_defence_roll

def roll_attack(max_attack_roll: int, max_defence_roll: int) -> bool:
    attack_roll = rand.randrange(max_attack_roll)
    defence_roll = rand.randrange(max_defence_roll)

    return attack_roll > defence_roll
    
def calc_hit_chance(attack_roll: int, defence_roll: int) -> float:
    if attack_roll > defence_roll:
        return (1 - ( (defence_roll + 2) / (2 * (attack_roll + 1)) ) )
    else:
        return (attack_roll / (2 * (defence_roll + 1)))
