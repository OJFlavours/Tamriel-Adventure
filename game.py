#!/usr/bin/env python3
import time
import random
import traceback
from datetime import datetime

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

# Global variables for tracking game state
known_locations = set()
npc_registry = {}
current_location = None
random_encounters = {}
game_start_time = None

ALL_LOCATIONS = LOCATIONS

def clear_screen():
    """Clear the terminal screen."""
    print("\033[H\033[J", end="")

def slow_print(text, delay=0.03):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_flavor_text(tags, category, ensure_vignette=False):
    """Get appropriate flavor text based on location tags."""
    available_text = []
    for tag in tags:
        if tag in FLAVOR_VIGNETTES.get(category, {}):
            available_text.extend(FLAVOR_VIGNETTES[category][tag])
    
    if not available_text and ensure_vignette:
        return "The air is thick with untold stories."
    return random.choice(available_text) if available_text else ""

def discover_connected_locations(location):
    """Discover locations connected to the current one."""
    global known_locations
    if "travel" in location:
        for path_type in ["roads", "paths"]:
            if path_type in location["travel"]:
                for dest in location["travel"][path_type]:
                    dest_loc = next((loc for loc in ALL_LOCATIONS if loc["name"] == dest), None)
                    if dest_loc:
                        known_locations.add(dest_loc["id"])

def generate_random_encounter(tags):
    """Generate a random encounter based on location tags."""
    available_encounters = []
    for tag in tags:
        if tag in ENCOUNTER_NAMES:
            available_encounters.extend(ENCOUNTER_NAMES[tag])
    
    if available_encounters:
        encounter = random.choice(available_encounters)
        return {
            "id": random.randint(10000, 99999),
            "name": encounter["name"],
            "desc": encounter["desc"],
            "tags": tags + [encounter["type"]]
        }
    return None

def list_locations():
    """Display known locations to the player."""
    clear_screen()
    UI.header("Known Realms")
    if not known_locations:
        slow_print("Your map remains blank, awaiting discovery.")
        UI.divider()
        return
    
    for loc in [l for l in ALL_LOCATIONS if l["id"] in known_locations]:
        brief_desc = loc['desc'].split('.')[0] + '.'
        print(f"[{loc['id']:>2}] {loc['name']:<30} — {brief_desc}")
    UI.divider()

def travel_menu(player):
    """Handle player movement between locations."""
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
        
        if sel == "0":
            return None
            
        if sel.startswith("R"):
            return handle_encounter_selection(sel, player)
        
        try:
            loc_id = int(sel)
            return handle_location_selection(loc_id, player)
        except ValueError:
            slow_print("Your intent is unclear.")
            return None
            
    except Exception as e:
        print(f"Error in travel_menu: {e}")
        traceback.print_exc()
        return None

def handle_encounter_selection(sel, player):
    """Handle player selection of a random encounter."""
    try:
        encounter_index = int(sel[1:]) - 1
        if (current_location and 
            current_location["id"] in random_encounters and 
            0 <= encounter_index < len(random_encounters[current_location["id"]])):
            
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
    except ValueError:
        slow_print("Invalid encounter selection.")
        return None

def handle_location_selection(loc_id, player):
    """Handle player selection of a location."""
    global current_location
    
    if loc_id not in known_locations:
        slow_print("That land is unknown to you, adventurer.")
        return None

    loc = next((l for l in ALL_LOCATIONS if l["id"] == loc_id), None)
    if not loc:
        return None

    if current_location and loc["id"] == current_location.get("id"):
        return handle_sublocation_selection(loc, player)
    
    current_location = loc
    known_locations.add(loc["id"])
    discover_connected_locations(loc)
    slow_print(f"You have ventured to {loc['name']}.\n")
    slow_print(get_flavor_text(loc['tags'], "location_tags", ensure_vignette=True))
    trigger_random_event(loc['tags'], player, UI)
    generate_npcs_for_location(loc)
    return loc

def handle_sublocation_selection(loc, player):
    """Handle player selection of a sublocation within current location."""
    global current_location
    
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

def generate_npcs_for_location(location):
    """Generate NPCs appropriate for the location."""
    try:
        if location["id"] in npc_registry:
            return
            
        npc_registry[location["id"]] = []
        parent_loc = next((loc for loc in LOCATIONS if any(sub_loc["id"] == location["id"] 
                    for sub_loc in loc.get("sub_locations", []))), None)
        
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

        npc_count = determine_npc_count(tags)
        role_pool = FRIENDLY_ROLES if "tavern" in tags else (FRIENDLY_ROLES | HOSTILE_ROLES)
        
        # Generate NPCs based on location type
        if "tavern" in tags:
            generate_tavern_npcs(location, tags)
        else:
            generate_standard_npcs(location, tags, npc_count, role_pool, demographics)
            
    except Exception as e:
        print(f"Error in generate_npcs_for_location: {e}")
        traceback.print_exc()

def determine_npc_count(tags):
    """Determine how many NPCs should be in a location."""
    if "city" in tags or "tavern" in tags:
        return random.randint(6, 12)
    elif "village" in tags or "town" in tags:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)

def generate_tavern_npcs(location, tags):
    """Generate NPCs specific to a tavern environment."""
    # Add innkeeper
    innkeeper = NPC(role_tag="innkeeper", culture_tag="nord")
    npc_registry[location["id"]].append(innkeeper)
    
    # Add patrons
    patron_count = random.randint(3, 8)
    patron_roles = ["merchant", "adventurer", "hunter", "farmer"]
    for _ in range(patron_count):
        patron = NPC(role_tag=random.choice(patron_roles), culture_tag="nord")
        npc_registry[location["id"]].append(patron)
    
    # Add a bard
    bard = NPC(role_tag="bard", culture_tag="nord")
    npc_registry[location["id"]].append(bard)

def generate_standard_npcs(location, tags, npc_count, role_pool, demographics):
    """Generate NPCs for non-tavern locations."""
    for _ in range(npc_count):
        role = determine_npc_role(tags, role_pool)
        culture = determine_npc_culture(demographics)
        npc = NPC(role_tag=role, culture_tag=culture)
        npc_registry[location["id"]].append(npc)

def determine_npc_role(tags, role_pool):
    """Determine appropriate role for an NPC based on location."""
    tag_roles = {
        "companions": ["warrior"] * 3 + ["blacksmith"],
        "thieves": ["rogue"] * 3 + ["merchant"],
        "college": ["mage"] * 3 + ["scholar"],
        "temple": ["priest"] * 2 + ["healer"],
        "stormcloak": ["soldier"] * 3 + ["scout"],
        "imperial": ["soldier"] * 3 + ["officer"],
        "darkbrotherhood": ["assassin"] * 2,
        "forsworn": ["barbarian"] * 2 + ["shaman"],
    }
    
    tag_role_pool = []
    for tag in tags:
        if tag in tag_roles:
            tag_role_pool.extend(tag_roles[tag])
            
    if tag_role_pool and random.random() < 0.5:
        return random.choice(tag_role_pool)
    return random.choice(list(role_pool))

def determine_npc_culture(demographics):
    """Determine NPC culture based on location demographics."""
    culture_weights = []
    cultures = []
    
    for race, percentage in demographics.items():
        race_key = race.lower()
        if race_key != "others":
            cultures.append(race_key)
            culture_weights.append(percentage)
            
    if not cultures:
        return "nord"
        
    return random.choices(cultures, weights=culture_weights, k=1)[0]

def list_npcs_at_location(location, player):
    """Display and handle interaction with NPCs at current location."""
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
    """Share a random rumor based on current location."""
    try:
        if not current_location:
            return
        rumors = RUMOR_POOL.get(current_location["tags"][0], ["A strange tale circulates..."])
        slow_print(random.choice(rumors))
    except Exception as e:
        print(f"Error in share_random_rumor: {e}")

def combat_demo(player):
    """Run a combat demonstration with a test enemy."""
    try:
        enemy = NPC(name="Bandit Raider", level=player.level, culture_tag="nord", role_tag="bandit")
        combat = Combat(player, [enemy], current_location)
        combat.run()
    except Exception as e:
        print(f"Error in combat_demo: {e}")
        traceback.print_exc()

def initialize_player():
    """Create and initialize a new player character."""
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
        return player

    except Exception as e:
        print(f"Error in initialize_player: {e}")
        traceback.print_exc()
        return None

def initialize_starting_location():
    """Initialize the player's starting location in a random tavern."""
    global current_location
    
    # Find all cities with taverns
    city_locations = [loc for loc in ALL_LOCATIONS if "city" in loc.get("tags", []) and "sub_locations" in loc]
    
    if city_locations:
        start_city = random.choice(city_locations)
        # Get all taverns in the city
        tavern_locations = [
            sub_loc for sub_loc in start_city.get("sub_locations", []) 
            if any(tag in sub_loc.get("tags", []) for tag in ["tavern", "inn"])
        ]
        
        if tavern_locations:
            current_location = random.choice(tavern_locations)
            known_locations.add(start_city["id"])
            known_locations.add(current_location["id"])
            discover_connected_locations(start_city)
            generate_npcs_for_location(current_location)
            
            UI.stylized(f"You awaken in {current_location['name']}, a cozy tavern in {start_city['name']}...")
            slow_print("The warm fire crackles as patrons share tales over mugs of mead.")
            return True
            
    # Fallback to Whiterun if no suitable tavern is found
    print("Starting in Whiterun...")
    default_location = next((loc for loc in ALL_LOCATIONS if loc["name"] == "Whiterun Hold"), ALL_LOCATIONS[0])
    current_location = default_location
    known_locations.add(current_location["id"])
    discover_connected_locations(current_location)
    generate_npcs_for_location(current_location)
    return False

def initialize_game_state():
    """Initialize the game state and starting conditions."""
    global game_start_time
    game_start_time = datetime.utcnow()
    
    # Clear any existing state
    known_locations.clear()
    npc_registry.clear()
    random_encounters.clear()

def start_game():
    """Main game entry point and loop."""
    try:
        initialize_game_state()
        
        player = initialize_player()
        if not player:
            return
            
        started_in_tavern = initialize_starting_location()
        
        # Generate initial random encounters
        if current_location["id"] not in random_encounters:
            random_encounters[current_location["id"]] = []
            for _ in range(random.randint(1, 3)):
                encounter = generate_random_encounter(current_location["tags"])
                if encounter:
                    random_encounters[current_location["id"]].append(encounter)

        # Set up initial quest
        starter_quest = generate_location_appropriate_quest(player.level, current_location["tags"])
        extra_reward = generate_reward(current_location["tags"])
        starter_quest.reward = f"{starter_quest.reward} and {extra_reward} gold"
        add_quest_to_log(player_state=player.__dict__, quest=starter_quest)
        
        if started_in_tavern:
            UI.slow_print("As you sip your drink, you overhear: ")
        UI.slow_print(f"A patron asks you to: {starter_quest.description}. Reward: {starter_quest.reward}")
        player.quest_log.add_quest(starter_quest)

        # Main game loop
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
            
            if choice == "0":
                slow_print("Farewell, until the stars call you back!")
                break
                
            handle_player_choice(choice, player)
            
            if current_location:
                trigger_random_event(current_location['tags'], player, UI)
                
            # Regenerate resources
            player.stats.regenerate_fatigue(5)
            player.stats.regenerate_magicka(5)
            
    except Exception as e:
        print(f"Error in start_game: {e}")
        traceback.print_exc()
    finally:
        input("Press Enter to exit...")

def handle_player_choice(choice, player):
    """Handle player's menu choice."""
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
        print("\n--- Quest Log ---")
        print(player.quest_log)
    elif choice == "9":
        handle_item_use(player)
    else:
        slow_print("Your will wavers.")

def handle_item_use(player):
    """Handle the player using an item from their inventory."""
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

if __name__ == "__main__":
    start_game()