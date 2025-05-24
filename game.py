import time
import random
import traceback

try:
    from locations import LOCATIONS
    from stats import Player, Stats, RACES, CLASSES
    from npc import NPC, FRIENDLY_ROLES, HOSTILE_ROLES, NAME_POOLS
    from combat import Combat
    from tags import TAGS, FLAVOR_VIGNETTES, RUMOR_POOL
    from ui import UI
    from items import generate_random_item, Item
    from events import trigger_random_event, explore_location
    from quests import (
        list_player_quests,
        QuestLog,
        generate_location_appropriate_quest,
        add_quest_to_log,
        generate_reward
    )
except ImportError as e:
    print(f"Error importing modules: {e}")
    input("Press Enter to exit...")
    exit(1)

# Global variables for tracking discovered locations, NPCs and current encounter details.
known_locations = set()
npc_registry = {}
current_location = None
random_encounters = {}

ALL_LOCATIONS = LOCATIONS

ENCOUNTER_NAMES = {
    "cave": ["Frostbite Cave", "Whispering Cave", "Dark Hollow", "Bandit's Grotto"],
    "bandit_camp": ["Raider's Camp", "Highwaymen's Hideout", "Deserter's Camp", "Brigand's Nest"],
    "ruin": ["Old Tower", "Ancient Cairn", "Forgotten Shrine", "Haunted Ruins"]
}
ENCOUNTER_DESCRIPTIONS = {
    "cave": "A dark and damp cave, rumored to be home to dangerous creatures.",
    "bandit_camp": "A makeshift camp, likely inhabited by bandits or other unsavory characters.",
    "ruin": "The crumbling remains of an ancient structure, hinting at a forgotten past."
}

def slow_print(text, delay=0.015):
    try:
        UI.slow_print(text, delay)
    except Exception as e:
        print(f"Error in slow_print: {e}")
        print(text)

def clear_screen():
    try:
        UI.clear()
    except Exception as e:
        print(f"Error in clear_screen: {e}")

def get_flavor_text(tags, category, ensure_vignette=True):
    try:
        available_vignettes = [FLAVOR_VIGNETTES.get(tag, "") for tag in tags if tag in FLAVOR_VIGNETTES]
        vignette_count = min(3, len(available_vignettes)) if available_vignettes and ensure_vignette else 0
        selected_vignettes = random.sample(available_vignettes, vignette_count) if vignette_count else []
        return " ".join(v for v in selected_vignettes if v)
    except Exception as e:
        print(f"Error in get_flavor_text: {e}")
        return "The air hums with the promise of adventure."

def discover_connected_locations(location):
    try:
        connections = location.get("travel", {}).get("roads", []) + location.get("travel", {}).get("paths", [])
        for conn in connections:
            match = next((l for l in ALL_LOCATIONS if l["name"].lower() == conn.lower()), None)
            if match:
                known_locations.add(match["id"])
    except Exception as e:
        print(f"Error in discover_connected_locations: {e}")

def generate_random_encounter(hold_tags):
    try:
        encounter_type = random.choice(["cave", "bandit_camp", "ruin"])
        name = random.choice(ENCOUNTER_NAMES[encounter_type])
        desc = ENCOUNTER_DESCRIPTIONS[encounter_type]
        tags = [encounter_type] + hold_tags
        new_id = max(loc["id"] for loc in LOCATIONS) + len(random_encounters) + 1
        encounter = {
            "id": new_id,
            "name": name,
            "desc": desc,
            "tags": tags,
            "demographics": {"Nord": 70, "Bandit": 30} if encounter_type == "bandit_camp" else {"Nord": 100},
            "travel": {"roads": [], "paths": []}
        }
        return encounter
    except Exception as e:
        print(f"Error in generate_random_encounter: {e}")
        return None

def list_locations():
    try:
        UI.header("Lands Known To You")
        if not known_locations:
            slow_print("No paths yet trodden are known to you.")
            UI.divider()
            return

        locations = [loc for loc in ALL_LOCATIONS if loc["id"] in known_locations]
        for loc in locations:
            brief_desc = loc['desc'].split('.')[0] + '.'
            print(f"[{loc['id']:>2}] {loc['name']:<30} — {brief_desc}")
            if "city" in loc.get("tags", []) and current_location and loc["id"] == current_location.get("id"):
                for sub_loc in loc.get("sub_locations", []):
                    sub_brief = sub_loc['desc'].split('.')[0] + '.'
                    print(f"    [{sub_loc['id']:>2}] {sub_loc['name']:<26} — {sub_brief}")

        if current_location and current_location["id"] in random_encounters:
            print("\n-- Nearby Encounters --")
            for i, encounter in enumerate(random_encounters[current_location["id"]], 1):
                print(f"[R{i:>1}] {encounter['name']:<30} — {encounter['desc'].split('.')[0]}.")
        UI.divider()
        sel = input("Seek more knowledge of which place? (0 to return): ").strip()
        if sel.isdigit():
            loc_id = int(sel)
            if loc_id == 0:
                return
            loc = next((l for l in ALL_LOCATIONS if l["id"] == loc_id and l["id"] in known_locations), None)
            if loc:
                UI.stylized(loc['name'])
                slow_print(f"{loc['desc']}", delay=0.005)
                slow_print(get_flavor_text(loc['tags'], "location_tags", ensure_vignette=True), delay=0.005)
                for sub_loc in loc.get("sub_locations", []):
                    UI.stylized(sub_loc['name'])
                    slow_print(f"{sub_loc['desc']}", delay=0.005)
                    inheritable_tags = {"nordic", "imperial", "stormcloak", "thieves", "corrupt", "military", "bards"}
                    if "tavern" not in sub_loc.get("tags", []):
                        inheritable_tags.add("city")
                    filtered_loc_tags = [t for t in loc['tags'] if t in inheritable_tags]
                    slow_print(get_flavor_text(sub_loc['tags'] + filtered_loc_tags, "location_tags", ensure_vignette=True), delay=0.005)
                UI.divider()
            else:
                slow_print("That place remains shrouded in mystery or lies beyond your reach.")
        elif sel.startswith("R"):
            encounter_index = int(sel[1:]) - 1
            if current_location and current_location["id"] in random_encounters and 0 <= encounter_index < len(random_encounters[current_location["id"]]):
                encounter = random_encounters[current_location["id"]][encounter_index]
                UI.stylized(encounter['name'])
                slow_print(f"{encounter['desc']}", delay=0.005)
                slow_print(get_flavor_text(encounter['tags'], "location_tags", ensure_vignette=True), delay=0.005)
                UI.divider()
            else:
                slow_print("That place remains shrouded in mystery or lies beyond your reach.")
    except Exception as e:
        print(f"Error in list_locations: {e}")
        traceback.print_exc()

def travel_menu(player):
    global current_location
    try:
        clear_screen()
        UI.header("Chart a Course")
        if not known_locations:
            slow_print("No destinations are marked upon your map, traveler.")
            UI.divider()
            return None

        locations = [loc for loc in ALL_LOCATIONS if loc["id"] in known_locations]
        for loc in locations:
            brief_desc = loc['desc'].split('.')[0] + '.'
            print(f"[{loc['id']:>2}] {loc['name']:<30} — {brief_desc}")

        if current_location and current_location["id"] in random_encounters:
            print("\n-- Nearby Encounters --")
            for i, encounter in enumerate(random_encounters[current_location["id"]], 1):
                print(f"[R{i:>1}] {encounter['name']:<30} — {encounter['desc'].split('.')[0]}.")
        UI.divider()
        sel = input("Whither do you journey? (0 to remain): ").strip()
        loc_id = None

        if sel.isdigit():
            try:
                loc_id = int(sel)
                if loc_id == 0:
                    return None
            except ValueError:
                slow_print("Your intent is unclear.")
                return None

        if sel.startswith("R"):
            encounter_index = int(sel[1:]) - 1
            if current_location and current_location["id"] in random_encounters and 0 <= encounter_index < len(random_encounters[current_location["id"]]):
                encounter = random_encounters[current_location["id"]][encounter_index]
                current_location = encounter
                known_locations.add(encounter["id"])
                slow_print(f"You have ventured to {encounter['name']}.\n")
                slow_print(get_flavor_text(encounter['tags'], "location_tags", ensure_vignette=True))
                trigger_random_event(encounter['tags'], player, UI)
                generate_npcs_for_location(encounter)
                return encounter
            else:
                slow_print("That place remains shrouded in mystery or lies beyond your reach.")
                return None

        if loc_id is None or loc_id not in known_locations:
            slow_print("That land is unknown to you, adventurer.")
            return None

        loc = next((l for l in LOCATIONS if l["id"] == loc_id), None)
        if loc:
            if current_location and loc["id"] == current_location.get("id"):
                sub_locs = loc.get("sub_locations", [])
                if not sub_locs:
                    slow_print("You are already present in this place.")
                    UI.divider()
                    return None
                UI.header(f"Realms Within {loc['name']}")
                for sub_loc in sub_locs:
                    brief_desc = sub_loc['desc'].split('.')[0] + '.'
                    print(f"[{sub_loc['id']:>2}] {sub_loc['name']:<30} — {brief_desc}")
                UI.divider()
                try:
                    sub_id = int(input("Which haven within do you seek? (0 to linger): "))
                    if sub_id == 0:
                        return None
                except ValueError:
                    slow_print("Your path is obscured.")
                    return None
                sub_loc = next((sl for sl in sub_locs if sl["id"] == sub_id), None)
                if sub_loc:
                    current_location = sub_loc
                    slow_print(f"You have ventured to {sub_loc['name']} in {loc['name']}.\n")
                    inheritable_tags = {"nordic", "imperial", "stormcloak", "thieves", "corrupt", "military", "bards"}
                    if "tavern" not in sub_loc.get("tags", []):
                        inheritable_tags.add("city")
                    filtered_loc_tags = [t for t in loc['tags'] if t in inheritable_tags]
                    slow_print(get_flavor_text(sub_loc['tags'] + filtered_loc_tags, "location_tags", ensure_vignette=True))
                    trigger_random_event(sub_loc['tags'] + filtered_loc_tags, player, UI)
                    generate_npcs_for_location(sub_loc)
                else:
                    slow_print("That place holds no welcome for you.")
                    return None
            else:
                current_location = loc
                known_locations.add(loc["id"])
                discover_connected_locations(loc)
                slow_print(f"You have ventured to {loc['name']}.\n")
                slow_print(get_flavor_text(loc['tags'], "location_tags", ensure_vignette=True))
                trigger_random_event(loc['tags'], player, UI)
                generate_npcs_for_location(loc)
            return loc
        return None
    except Exception as e:
        print(f"Error in travel_menu: {e}")
        traceback.print_exc()
        return None

def generate_npcs_for_location(location):
    try:
        if location["id"] in npc_registry:
            return
        npc_registry[location["id"]] = []
        parent_loc = next((loc for loc in LOCATIONS if any(sub_loc["id"] == location["id"] for sub_loc in loc.get("sub_locations", []))), None)
        if parent_loc:
            inheritable_tags = {"nordic", "imperial", "stormcloak", "thieves", "corrupt", "military", "bards"}
            if "tavern" not in location.get("tags", []):
                inheritable_tags.add("city")
            filtered_loc_tags = [t for t in parent_loc['tags'] if t in inheritable_tags]
            tags = set(location.get("tags", []) + filtered_loc_tags)
            demographics = parent_loc.get("demographics", {"Nord": 100})
        else:
            tags = set(location.get("tags", []))
            demographics = location.get("demographics", {"Nord": 100})

        if "city" in tags or "tavern" in tags:
            npc_count = random.randint(6, 12)
            role_pool = FRIENDLY_ROLES
        elif "village" in tags or "town" in tags:
            npc_count = random.randint(3, 6)
            role_pool = FRIENDLY_ROLES
        else:
            npc_count = random.randint(1, 3)
            role_pool = FRIENDLY_ROLES | HOSTILE_ROLES

        valid_cultures = set(NAME_POOLS.keys()) | {"imperial", "redguard", "bosmer", "altmer", "khajiit", "argonian", "reachmen", "snow elf", "orc", "draugr", "dwemer", "falmer"}
        cultures = []
        weights = []
        for race, percentage in demographics.items():
            race_key = race.lower()
            if race_key in valid_cultures:
                cultures.append(race_key)
                weights.append(percentage)
            elif race_key == "others":
                minority_races = ["redguard", "bosmer", "altmer", "khajiit", "argonian"]
                for mr in minority_races:
                    cultures.append(mr)
                    weights.append(percentage / len(minority_races))

        if not cultures:
            cultures = ["nord"]
            weights = [100]

        tag_roles = {
            "companions": ["warrior"] * 3 + ["blacksmith"],
            "thieves": ["rogue"] * 3 + ["merchant"],
            "college": ["mage"] * 3 + ["scholar"],
            "temple": ["priest"] * 2 + ["healer"],
            "stormcloak": ["soldier"] * 3 + ["scout"],
            "imperial": ["soldier"] * 3 + ["officer"],
            "darkbrotherhood": ["assassin"] * 2,
            "forsworn": ["barbarian"] * 2 + ["shaman"],
            "undead": ["necromancer"] * 2,
            "barrow": ["draugr"] * 2,
            "dwemer": ["automaton"] * 2,
            "falmer": ["falmer"] * 2
        }

        DRAUGR_ALLOWED_TAGS = {"barrow", "undead"}

        for _ in range(npc_count):
            if tags & DRAUGR_ALLOWED_TAGS:
                role = "draugr"
                culture = "draugr"
            elif tags & {"dwemer"}:
                role = "automaton"
                culture = "dwemer"
            elif tags & {"falmer"}:
                role = "falmer"
                culture = "falmer"
            else:
                tag_role_pool = []
                for tag in tags:
                    if tag in tag_roles:
                        tag_role_pool.extend(tag_roles[tag])
                if tag_role_pool and random.random() < 0.5:
                    role = random.choice(tag_role_pool)
                else:
                    role = random.choice(list(role_pool))
                culture = random.choices(cultures, weights, k=1)[0]
            npc = NPC(culture_tag=culture, role_tag=role, level=random.randint(1, 5))
            npc_registry[location["id"]].append(npc)
    except Exception as e:
        print(f"Error in generate_npcs_for_location: {e}")
        traceback.print_exc()

def list_npcs_at_location(location, player):
    try:
        npcs = npc_registry.get(location["id"], [])
        if not npcs:
            slow_print("No souls linger here, save the whispers of the wind.")
            return
        UI.header("Kindred Spirits Nearby")
        for i, npc in enumerate(npcs, 1):
            print(f"[{i}] {npc.name} — {npc}")
        UI.divider()

        sel = input("With whom do you wish to parley? (0 to pass): ").strip()
        if sel.isdigit():
            i = int(sel)
            if 1 <= i <= len(npcs):
                npc = npcs[i - 1]
                if npc.alignment == "hostile":
                    slow_print(f"{npc.name} draws steel, their eyes burning with malice!")
                    combat = Combat(player, [npc], location)
                    combat.run()
                else:
                    npc.dialogue(player, location)
            elif i != 0:
                slow_print("No such soul stands before you.")
    except Exception as e:
        print(f"Error in list_npcs_at_location: {e}")
        traceback.print_exc()

def share_random_rumor():
    try:
        rumors = RUMOR_POOL.get(current_location["tags"][0], ["A strange tale circulates..."])
        slow_print(random.choice(rumors))
    except Exception as e:
        print(f"Error in share_random_rumor: {e}")

def combat_demo(player):
    try:
        enemy = NPC(name="Bandit Raider", level=player.level, culture_tag="nord", role_tag="bandit")
        combat = Combat(player, [enemy], current_location)
        combat.run()
    except Exception as e:
        print(f"Error in combat_demo: {e}")
        traceback.print_exc()

def start_game():
    try:
        # Race selection
        print("Choose your race:")
        for race_id, race_name in RACES.items():
            print(f"[{race_id}] {race_name}")
        race_choice = input("> ").strip()
        if race_choice not in RACES:
            print("Invalid race choice. Defaulting to Nord.")
            player_race = "Nord"
        else:
            player_race = RACES[race_choice]

        # Class selection
        print("\nChoose your class:")
        for class_id, class_data in CLASSES.items():
            print(f"[{class_id}] {class_data['name']} - {class_data['desc']}")
        class_choice = input("> ").strip()
        if class_choice not in CLASSES:
            print("Invalid class choice. Defaulting to Warrior.")
            class_choice = "1"

        # Subclass selection
        print(f"\nChoose your {CLASSES[class_choice]['name']} subclass:")
        for subclass_id, subclass_data in CLASSES[class_choice]["subclasses"].items():
            print(f"[{subclass_id}] {subclass_data['name']}")
        subclass_choice = input("> ").strip()
        if subclass_choice not in CLASSES[class_choice]["subclasses"]:
            print(f"Invalid subclass choice. Defaulting to the first subclass.")
            subclass_choice = "1"

        # Player name
        player_name = ""
        while not player_name:
            player_name = input("Speak your name, traveler: ").strip()
            if not player_name:
                print("A name is required for your legend to be sung in the halls of Sovngarde.")

        # Create Player object
        selected_class = CLASSES[class_choice]
        selected_subclass = selected_class["subclasses"][subclass_choice]
        player = Player(player_name, player_race, selected_class["name"], selected_subclass["name"],
                        attributes=selected_subclass["attributes"],
                        skills=selected_subclass["skills"])

        # Add starting inventory and equipment
        for item_name in selected_class["inventory"]:
            item = generate_random_item(item_name.lower().replace(" ", "_"), player.level)
            player.add_item(item)
            if item.category in ["weapon", "armor"]:
                player.equip_item(item)

        player.quest_log = QuestLog()

        # Random starting location (tavern in a city)
        city_locations = [loc for loc in ALL_LOCATIONS if "city" in loc.get("tags", []) and "sub_locations" in loc]
        global current_location
        if city_locations:
            start_city = random.choice(city_locations)
            tavern_locations = [sub_loc for sub_loc in start_city.get("sub_locations", []) if "tavern" in sub_loc.get("tags", [])]
            if tavern_locations:
                current_location = random.choice(tavern_locations)
                known_locations.add(start_city["id"])
                known_locations.add(current_location["id"])
                discover_connected_locations(start_city)
                generate_npcs_for_location(current_location)
            else:
                print("Could not find a tavern in the starting city. Starting in main city.")
                current_location = start_city
                known_locations.add(start_city["id"])
                discover_connected_locations(start_city)
                generate_npcs_for_location(start_city)
        else:
            print("Could not find any cities. Starting in first available location.")
            current_location = ALL_LOCATIONS[0]
            known_locations.add(ALL_LOCATIONS[0]["id"])
            discover_connected_locations(ALL_LOCATIONS[0])
            generate_npcs_for_location(ALL_LOCATIONS[0])

        if current_location["id"] not in random_encounters:
            random_encounters[current_location["id"]] = []
            for _ in range(random.randint(1, 3)):
                encounter = generate_random_encounter(current_location["tags"])
                if encounter:
                    random_encounters[current_location["id"]].append(encounter)

        UI.stylized(f"You awaken in {current_location['name']}...")
        slow_print("By the grace of the Divines, your tale begins.\n")
        slow_print(get_flavor_text(current_location['tags'], "location_tags", ensure_vignette=True))

        # Generate an initial quest using the current location's tags.
        starter_quest = generate_location_appropriate_quest(player.level, current_location["tags"])
        # Generate an additional reward piece based on quest tags.
        extra_reward = generate_reward(current_location["tags"])
        starter_quest.reward += f" and {extra_reward} gold"
        add_quest_to_log(player_state=player.__dict__, quest=starter_quest)
        UI.slow_print(f"A patron asks you to: {starter_quest.description}. Reward: {starter_quest.reward}")
        player.quest_log.add_quest(starter_quest)

        # Main game loop.
        while True:
            # Apply encumbrance penalty
            if player.stats.current_encumbrance > player.stats.encumbrance_limit:
                player.stats.speed = max(10, player.stats.speed - 10)
                player.stats.dodge_chance = max(0.05, player.stats.dodge_chance - 0.1)
                slow_print("Your heavy load slows your steps and hinders your agility.")
            else:
                player.stats.speed = player.attributes["speed"]
                player.stats.dodge_chance = min(0.05 + player.attributes["agility"] / 200, 0.3)

            print("\nChoose Your Path:")
            print("1) Seek Known Realms")
            print("2) Journey Forth")
            print("3) Parley with Souls")
            print("4) Behold Thy Spirit")
            print("5) Test Thy Steel")
            print("6) Inspect Thy Possessions")
            print("7) Explore the Area")
            print("8) Review Quest Log")
            print("9) Use Item")
            print("0) Depart This Realm")
            choice = input("What is your will? ").strip()
            if choice == "1":
                list_locations()
            elif choice == "2":
                travel_menu(player)
            elif choice == "3":
                if current_location:
                    list_npcs_at_location(current_location, player)
                else:
                    slow_print("First, you must tread a path to meet the living.")
            elif choice == "4":
                print(f"\n{player}")
                print(player.stats)
                print("Skills:", ", ".join([f"{k}: {v}" for k, v in player.skills.items()]))
            elif choice == "5":
                combat_demo(player)
            elif choice == "6":
                print("Inventory:", ", ".join([str(item) for item in player.inventory]))
                print("Equipment:", ", ".join([str(item) for item in player.equipment]))
                print(f"Encumbrance: {player.stats.current_encumbrance}/{player.stats.encumbrance_limit}")
            elif choice == "7":
                explore_location(player, current_location, random_encounters, npc_registry, LOCATIONS, UI)
            elif choice == "8":
                # Display the player's quest log.
                print("\n--- Quest Log ---")
                print(player.quest_log)
            elif choice == "9":
                print("Inventory:")
                for i, item in enumerate(player.inventory, 1):
                    print(f"[{i}] {item}")
                item_index = input("Which item do you want to use? (Enter the item number, 0 to cancel): ")
                if item_index.isdigit():
                    item_index = int(item_index) - 1
                    if 0 <= item_index < len(player.inventory):
                        item = player.inventory[item_index]
                        item.use(player)
                        player.stats.current_encumbrance -= item.weight
                    else:
                        print("Invalid item number.")
                else:
                    print("Invalid input.")
            elif choice == "0":
                slow_print("Farewell, until the stars call you back!")
                break
            else:
                slow_print("Your will wavers.")
            if current_location:
                trigger_random_event(current_location['tags'], player, UI)
            # Regenerate resources
            player.stats.regenerate_fatigue(5)
            player.stats.regenerate_magicka(5)
    except Exception as e:
        print(f"Error in start_game: {e}")
        traceback.print_exc()
        input("Press Enter to exit...")
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    start_game()