import requests
import json
import urllib.parse
from pathlib import Path

# I tried to write a lot of this myself, but I cant take credit for anything.
# I took inspiration from the WeirdGloop osrs-dps-calc repo, and used their generate python scripts to troubleshoot issues
QUERY_LIST = [
    "Size",
    "Monster attribute",
    "Max hit",
    "Attack style",
    "Attack speed",
    "Hitpoints",
    "Attack level",
    "Strength level",
    "Defence level",
    "Magic level",
    "Ranged level",
    "Attack bonus",
    "Strength bonus",
    "Magic attack bonus",
    "Magic Damage bonus",
    "Range attack bonus",
    "Ranged Strength bonus",
    "Stab defence bonus",
    "Slash defence bonus",
    "Crush defence bonus",
    "Magic defence bonus",
    "Range defence bonus",
    "Poisonous",
    "Examine",
    "Immune to poison",
    "Immune to venom",
    "NPC ID",
    "Category",
    "Combat level",
    "Slayer category",
]

base_url = "https://oldschool.runescape.wiki/api.php"

script_path = Path(__file__).resolve().parent
data_path = script_path.parent / "data"


def get_monster_stats():
    # This is practically ripped from the above mentioned DPS calc, I couldnt get the way I wanted to work
    # So I ended up using their way of polling the api. I was probably just being stupid, but if it aint broke...

    query_count = 0
    monster_stats = {}

    HEADERS = {
        "User-Agent": "osrs-combat-simulator",
    }

    while True:
        DATA = {
            "action": "ask",
            "format": "json",
            "query": "[[Uses infobox::Monster]]|?"
            + "|?".join(QUERY_LIST)
            + f"|limit=500|offset={query_count}",  # append query list
        }

        r = requests.get(base_url + "?" + urllib.parse.urlencode(DATA), headers=HEADERS)
        query_data = r.json()

        if "query" not in query_data or "results" not in query_data["query"]:
            print("No data or error returned")
            break

        monster_stats.update(query_data["query"]["results"])

        if "query-continue-offset" not in query_data:
            break
        else:
            query_count = query_data["query-continue-offset"]
    return monster_stats


def transform_monster_stats(monster_stats: dict) -> dict:
    # This unholy function is all my idea, all I wanted was to get the data normalized
    # And formated / grouped in a logical way... feel free to refactor if there is a better way
    # I hate it.

    INTEGER_STATS = [
        "Size",
        "Attack style",
        "Attack speed",
        "Hitpoints",
        "Attack level",
        "Strength level",
        "Defence level",
        "Magic level",
        "Ranged level",
        "Attack bonus",
        "Strength bonus",
        "Magic attack bonus",
        "Magic stregnth bonus",
        "Range attack bonus",
        "Range strength bonus",
        "Stab defence bonus",
        "Slash defence bonus",
        "Crush defence bonus",
        "Range defence bonus",
        "NPC ID",
    ]
    new_stats = {}

    for monster, data in monster_stats.items():
        transformed_subdata = {}
        for stat, value in data["printouts"].items():
            if len(value) == 0:
                if stat in INTEGER_STATS:
                    transformed_subdata[stat] = 0
                else:
                    transformed_subdata[stat] = None
            elif len(value) == 1:

                if stat == "Poisonous":
                    transformed_subdata[stat] = True if value[0] == "t" else False

                elif stat == "Immune to venom":
                    match value[0]:
                        case "Immune":
                            transformed_subdata[stat] = True
                        case "Not immune":
                            transformed_subdata[stat] = False
                        case _:
                            transformed_subdata[stat] = None
                elif stat == "Immune to poison":
                    match value[0]:
                        case "Immune":
                            transformed_subdata[stat] = True
                        case "Not immune":
                            transformed_subdata[stat] = False
                        case _:
                            transformed_subdata[stat] = None

                else:
                    transformed_subdata[stat] = value[0]
            else:
                transformed_subdata[stat] = value

        if transformed_subdata["Category"] and len(transformed_subdata["Category"]) > 0:
            category_list = []
            for category in transformed_subdata["Category"]:
                category_list.append(category.get("fulltext"))
            transformed_subdata["Category"] = category_list

        new_monster = {
            "combat_info": {},
            "combat_stats": {},
            "aggressive_stats": {},
            "defensive_stats": {},
            "immunities": {},
            "metadata": {},
        }

        new_monster["combat_info"]["size"] = transformed_subdata["Size"]
        new_monster["combat_info"]["combat_level"] = transformed_subdata["Combat level"]
        new_monster["combat_info"]["monster_attributes"] = transformed_subdata[
            "Monster attribute"
        ]
        new_monster["combat_info"]["slayer_category"] = transformed_subdata[
            "Slayer category"
        ]
        new_monster["combat_info"]["attack_style"] = transformed_subdata["Attack style"]
        new_monster["combat_info"]["attack_speed"] = transformed_subdata["Attack speed"]
        new_monster["combat_info"]["poisonous"] = transformed_subdata["Poisonous"]
        new_monster["combat_stats"]["hitpoints"] = transformed_subdata["Hitpoints"]
        new_monster["combat_stats"]["attack"] = transformed_subdata["Attack level"]
        new_monster["combat_stats"]["strength"] = transformed_subdata["Strength level"]
        new_monster["combat_stats"]["defence"] = transformed_subdata["Defence level"]
        new_monster["combat_stats"]["magic"] = transformed_subdata["Magic level"]
        new_monster["combat_stats"]["range"] = transformed_subdata["Ranged level"]
        new_monster["aggressive_stats"]["melee_attack_bonus"] = transformed_subdata[
            "Attack bonus"
        ]
        new_monster["aggressive_stats"]["melee_strength_bonus"] = transformed_subdata[
            "Strength bonus"
        ]
        new_monster["aggressive_stats"]["magic_attack_bonus"] = transformed_subdata[
            "Magic attack bonus"
        ]
        new_monster["aggressive_stats"]["magic_strength_bonus"] = transformed_subdata[
            "Magic Damage bonus"
        ]
        new_monster["aggressive_stats"]["range_attack_bonus"] = transformed_subdata[
            "Range attack bonus"
        ]
        new_monster["aggressive_stats"]["range_strength_bonus"] = transformed_subdata[
            "Ranged Strength bonus"
        ]
        new_monster["defensive_stats"]["stab_defence_bonus"] = transformed_subdata[
            "Stab defence bonus"
        ]
        new_monster["defensive_stats"]["slash_defence_bonus"] = transformed_subdata[
            "Slash defence bonus"
        ]
        new_monster["defensive_stats"]["crush_defence_bonus"] = transformed_subdata[
            "Crush defence bonus"
        ]
        new_monster["defensive_stats"]["magic_defence_bonus"] = transformed_subdata[
            "Crush defence bonus"
        ]
        new_monster["defensive_stats"]["range_defence_bonus"] = transformed_subdata[
            "Magic defence bonus"
        ]
        new_monster["metadata"]["examine"] = transformed_subdata["Examine"]
        new_monster["immunities"]["immune_to_poison"] = transformed_subdata[
            "Immune to poison"
        ]
        new_monster["immunities"]["immune_to_venom"] = transformed_subdata[
            "Immune to venom"
        ]
        new_monster["metadata"]["npc_id"] = transformed_subdata["NPC ID"]
        new_monster["metadata"]["category"] = transformed_subdata["Category"]

        new_stats[monster] = new_monster
    return new_stats


def write_stats_to_file(stats: dict, name: str, path: Path) -> None:
    filepath = path / f"{name}.json"
    json_stats = json.dumps(stats, indent=4)
    filepath.write_text(json_stats)


if __name__ == "__main__":
    queried_monster_data = get_monster_stats()
    new_data = transform_monster_stats(queried_monster_data)
    write_stats_to_file(new_data, "monster_stats", data_path)
