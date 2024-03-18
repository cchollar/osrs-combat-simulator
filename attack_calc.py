import math
def calc_effective_strength_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    effective_strength_level = (base_level + boost) * prayer
    effective_strength_level = math.floor(effective_strength_level)
    effective_strength_level += stance_bonus
    effective_strength_level += 8
    if void:
        effective_strength_level *= 1.1

    effective_strength_level = math.floor(effective_strength_level)
    return effective_strength_level

def calc_max_melee_hit(effective_strength_level: int, equipment_bonus: int, target_bonus: float = 1.0) -> int:
    max_hit = effective_strength_level * (equipment_bonus + 64)
    max_hit += 320
    max_hit = math.floor(max_hit / 640)
    max_hit = math.floor(max_hit * target_bonus)
    return max_hit

# Potential DRY violation, but I dont want to assume attack and strength effective levels are generic
def calc_effective_attack_level(base_level: int, boost: int, prayer: float, stance_bonus: int, void: bool = False) -> int:
    effective_attack_level = (base_level + boost) * prayer
    effective_attack_level = math.floor(effective_attack_level)
    effective_attack_level += stance_bonus
    effective_attack_level += 8
    if void:
        effective_attack_level *= 1.1

    effective_attack_level = math.floor(effective_attack_level)
    return effective_attack_level

def calc_max_attack_roll(effective_attack_level: int, equipment_bonus: int, target_bonus: float = 1.0) -> int:
    attack_roll = effective_attack_level * (equipment_bonus + 64)
    attack_roll *= target_bonus
    attack_roll = math.floor(attack_roll)
    return attack_roll

def calc_max_defence_roll(base_level: int, style_bonus: int) -> int:
    defence_roll = (base_level + 9) * (style_bonus + 64)
    return defence_roll

def calc_hit_chance(attack_roll: int, defence_roll: int) -> float:
    if attack_roll > defence_roll:
        return (1 - ( (defence_roll + 2) / (2 * (attack_roll + 1)) ) )
    else:
        return (attack_roll / (2 * (defence_roll + 1)))
