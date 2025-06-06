# npc_generation.py
import random
from stats import RACES
from npc_entities import NPC
from npc_roles import FRIENDLY_ROLES, HOSTILE_ROLES # Import role sets
from ui import UI
from locations import RAW_LOCATION_DATA_MAP

def determine_npc_count(tags_list, location_data):
    """Determines the number of NPCs to generate based on location tags and density."""
    density = location_data.get("density", "average") # Default to average

    if density == "bustling":
        return random.randint(12, 20)
    elif density == "average":
        if any(t in tags_list for t in ["city", "capital"]):
            return random.randint(8, 15)
        elif any(t in tags_list for t in ["town", "village", "market", "keep"]):
            return random.randint(5, 10)
        elif any(t in tags_list for t in ["tavern", "inn"]):
            return random.randint(4, 8)
        else: # Dungeons, camps, etc.
            return random.randint(3, 7)
    elif density == "sparse":
        return random.randint(1, 4)
    elif density == "empty":
        return 0

    # Fallback based on tags if density isn't specified or recognized
    if any(t in tags_list for t in ["city", "capital"]):
        return random.randint(12, 20)
    elif any(t in tags_list for t in ["tavern", "inn"]):
         return random.randint(6, 12)
    elif any(t in tags_list for t in ["town", "village", "market", "keep"]):
        return random.randint(6, 10)
    elif any(t in tags_list for t in ["camp", "dungeon", "ruin", "mine", "watchtower", "lair"]):
        return random.randint(3, 7)
    else:
        return random.randint(2, 4)

def determine_npc_culture(demographics):
    """Determines an NPC's culture/race based on location demographics."""
    culture_weights = []
    cultures = []
    for race_name_key, percentage in demographics.items():
        valid_race_key = race_name_key.lower()
        if valid_race_key in RACES and valid_race_key != "others":
            cultures.append(valid_race_key)
            culture_weights.append(percentage)

    if not cultures:
        return random.choice(list(RACES.keys()))
    try:
        return random.choices(cultures, weights=culture_weights, k=1)[0]
    except ValueError:
        return random.choice(list(RACES.keys()))

def determine_npc_role(tags_list, base_role_pool):
    """Determines an NPC's role based on location tags and a base pool of roles."""
    # High-priority context-specific roles
    if "college" in tags_list or "mage_guild" in tags_list:
        return random.choice(["college_mage", "scholar"])
    # ... more specific role logic can be added here ...

    # Contextual Role Filtering
    filtered_role_pool = set(base_role_pool)
    is_settlement = any(t in tags_list for t in ["city", "town", "village"])
    if not is_settlement:
        filtered_role_pool -= {"farmer", "shopkeeper", "merchant", "laborer", "beggar", "child"}

    is_coastal_or_river = any(t in tags_list for t in ["coastal", "docks", "river_delta", "port"])
    if not is_coastal_or_river:
        filtered_role_pool -= {"sailor", "dock_worker", "fishmonger", "ferryman"}

    is_dungeon = any(t in tags_list for t in ["dungeon", "ruin", "barrow", "cave", "lair"])
    if is_dungeon:
        if random.random() < 0.85:
            hostile_dungeon_roles = filtered_role_pool.intersection(HOSTILE_ROLES)
            if hostile_dungeon_roles:
                return random.choice(list(hostile_dungeon_roles))
        return "adventurer" # A non-hostile option for dungeons

    final_pool = list(filtered_role_pool) if filtered_role_pool else list(base_role_pool)
    if not final_pool:
        return "traveler"
    return random.choice(final_pool)


def generate_npcs_for_location(location_obj, npc_registry, find_hierarchy_func):
    try:
        raw_location_data = RAW_LOCATION_DATA_MAP.get(location_obj.id, {})
        if raw_location_data.get("is_encounter"): return
        if location_obj.id in npc_registry: return

        npc_registry[location_obj.id] = []
        
        # --- FIXED NPC SPAWNING ---
        # (Assuming you create fixed_npc_data.py and import FIXED_NPC_DATA)
        # from fixed_npc_data import FIXED_NPC_DATA
        # if location_obj.id in FIXED_NPC_DATA:
        #     for npc_data in FIXED_NPC_DATA[location_obj.id]:
        #         # ... logic to create and add fixed NPCs ...

        # --- RANDOM NPC GENERATION ---
        parent_hold, parent_city, _ = find_hierarchy_func(location_obj.id)
        
        # Determine location context for name generation
        hold_name_for_context = parent_hold.name.lower().replace(" ", "_") if parent_hold else "generic"
        location_context = {"hold_name": hold_name_for_context}
        
        # Determine demographics source
        demographics_source = location_obj
        raw_demographics_source_data = RAW_LOCATION_DATA_MAP.get(demographics_source.id, {})
        if not raw_demographics_source_data.get("demographics"):
            if parent_city:
                raw_parent_city_data = RAW_LOCATION_DATA_MAP.get(parent_city.id, {})
                if raw_parent_city_data.get("demographics"):
                    demographics_source = parent_city
            elif parent_hold:
                raw_parent_hold_data = RAW_LOCATION_DATA_MAP.get(parent_hold.id, {})
                if raw_parent_hold_data.get("demographics"):
                    demographics_source = parent_hold
        
        demographics = RAW_LOCATION_DATA_MAP.get(demographics_source.id, {}).get("demographics", {"Nord": 100})
        
        location_tags = list(raw_location_data.get("tags", []))
        npc_count = determine_npc_count(location_tags, raw_location_data)
        
        # Determine the base role pool (friendly or hostile)
        is_hostile_area = any(tag in location_tags for tag in HOSTILE_ROLES)
        role_pool = HOSTILE_ROLES if is_hostile_area else FRIENDLY_ROLES

        for _ in range(npc_count):
            npc_role = determine_npc_role(location_tags, role_pool)
            npc_race = determine_npc_culture(demographics)
            npc_level = random.randint(1, 10) # Simplified level, can be refined

            # Pass location_context to the NPC constructor
            new_npc = NPC(
                name=None,
                race=npc_race,
                role=npc_role,
                level=npc_level,
                location_context=location_context
            )
            npc_registry[location_obj.id].append(new_npc)

    except Exception as e:
        location_name_for_error = getattr(location_obj, 'name', 'Unknown Location')
        UI.print_failure(f"Error generating NPCs for {location_name_for_error}: {e}")

# This is a placeholder for the create_npc function if needed elsewhere
def create_npc(name: str, race: str, role: str, level: int, template: dict = None) -> NPC:
    # ... implementation ...
    pass