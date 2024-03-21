import requests
import json
import urllib.parse
from pathlib import Path

# I tried to write a lot of this myself, but I cant take credit for anything.
# I took inspiration from the WeirdGloop osrs-dps-calc repo, and used their generate python scripts to troubleshoot issues
QUERY_LIST = [
    "Crush attack bonus",
    "Crush defence bonus",
    "Equipment slot",
    "Item ID",
    "Magic Damage bonus",
    "Magic attack bonus",
    "Magic defence bonus",
    "Prayer bonus",
    "Range attack bonus",
    "Ranged Strength bonus",
    "Range defence bonus",
    "Slash attack bonus",
    "Slash defence bonus",
    "Stab attack bonus",
    "Stab defence bonus",
    "Strength bonus",
    "Version anchor",
    "Weapon attack range",
    "Weapon attack speed",
    "Combat style",
]

base_url = "https://oldschool.runescape.wiki/api.php"

script_path = Path(__file__).resolve().parent
data_path = script_path.parent / "data"


def get_equipment_stats():
    # This is practically ripped from the above mentioned DPS calc, I couldnt get the way I wanted to work
    # So I ended up using their way of polling the api. I was probably just being stupid, but if it aint broke...

    query_count = 0
    equipment_stats = {}

    HEADERS = {
        "User-Agent": "osrs-combat-simulator",
    }

    while True:
        DATA = {
            "action": "ask",
            "format": "json",
            "query": "[[Equipment slot::+]][[Item ID::+]]|?"
            + "|?".join(QUERY_LIST)
            + f"|limit=500|offset={query_count}",  # append query list
        }

        r = requests.get(base_url + "?" + urllib.parse.urlencode(DATA), headers=HEADERS)
        query_data = r.json()

        if "query" not in query_data or "results" not in query_data["query"]:
            print("No data or error returned")
            break

        equipment_stats.update(query_data["query"]["results"])

        if "query-continue-offset" not in query_data:
            break
        else:
            query_count = query_data["query-continue-offset"]
    return equipment_stats


# This function is a lot more pulled from the osrs dps calc, I like their data format more for equipment.
def transform_equipment_stats(equipment_stats: dict):
    new_gear = {}
    for equipment, stats in equipment_stats.items():
        transformed_gear = {}
        for stat, value in stats["printouts"].items():
            if len(value) == 0:
                transformed_gear[stat] = None
            else:
                transformed_gear[stat] = value[0]

        new_gear[equipment] = {
            "name": equipment.rsplit("#", 1)[0],
            "id": transformed_gear["Item ID"],
            "version": transformed_gear["Version anchor"],
            "slot": transformed_gear["Equipment slot"],
            "speed": transformed_gear["Weapon attack speed"] or 0,
            "category": transformed_gear["Combat style"],
            "prayer_bonus": transformed_gear["Prayer bonus"],
            "bonuses": {
                "melee_strength": transformed_gear["Strength bonus"],
                "range_strength": transformed_gear["Ranged Strength bonus"],
                "magic_strength": transformed_gear["Magic Damage bonus"],
            },
            "offensive": {
                "stab": transformed_gear["Stab attack bonus"],
                "slash": transformed_gear["Slash attack bonus"],
                "crush": transformed_gear["Crush attack bonus"],
                "magic": transformed_gear["Magic attack bonus"],
                "ranged": transformed_gear["Range attack bonus"],
            },
            "defensive": {
                "stab": transformed_gear["Stab defence bonus"],
                "slash": transformed_gear["Slash defence bonus"],
                "crush": transformed_gear["Crush defence bonus"],
                "magic": transformed_gear["Magic defence bonus"],
                "ranged": transformed_gear["Range defence bonus"],
            },
            "isTwoHanded": False,
        }

        if new_gear[equipment]["slot"] == "2h":
            new_gear[equipment]["slot"] = "weapon"
            new_gear[equipment]["isTwoHanded"] = True

    return new_gear


def write_stats_to_file(stats: dict, name: str, path: Path) -> None:
    filepath = path / f"{name}.json"
    json_stats = json.dumps(stats, indent=4)
    filepath.write_text(json_stats)


if __name__ == "__main__":
    queried_equipment_data = get_equipment_stats()
    new_data = transform_equipment_stats(queried_equipment_data)
    write_stats_to_file(new_data, "equipment_stats", data_path)
