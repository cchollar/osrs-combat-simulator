import attack_calc as AC

# Sitution: Maxed player, naked, dscim, salted, piety, against solo Baba no path, 300 invo level


player_base_level = 99
player_boost = 26
player_strength_prayer = 1.23
player_attack_prayer = 1.20
player_attack_stance = 0
player_strength_stance = 3
player_strength_equipment_bonus = 66
player_attack_equipment_bonus = 67

enemy_base_defense = 135
enemy_defence_bonus = 20

eff_str = AC.calc_effective_strength_level(base_level = player_base_level, boost = player_boost, prayer = player_strength_prayer, stance_bonus = player_strength_stance)
print(f"effective strength level: {eff_str}")

scim_max_hit = AC.calc_max_melee_hit(effective_strength_level = eff_str, equipment_bonus = player_strength_equipment_bonus)
print(f"effective max hit of {scim_max_hit}")

eff_atk = AC.calc_effective_attack_level(base_level = player_base_level, boost = player_boost, prayer = player_attack_prayer, stance_bonus = player_attack_stance)
print(f"effective attack level: {eff_atk}")

atk_roll = AC.calc_max_attack_roll(effective_attack_level = eff_atk, equipment_bonus = player_attack_equipment_bonus)
print(f"max attack roll: {atk_roll}")

def_roll = AC.calc_max_defence_roll(base_level = enemy_base_defense, style_bonus = enemy_defence_bonus)
print(f"max defence roll: {def_roll}")

if atk_roll > def_roll:
    print(f"Atk is bigger than def, rolling top formula")
else:
    print(f"Def is bigger than atk, rolling bottom formula")

hit_per = AC.calc_hit_chance(attack_roll = atk_roll, defence_roll = def_roll)

print(f"hit probability is {hit_per}")

print(f"hit prob of wiki numbers is {AC.calc_hit_chance(20698, 43859)}")
