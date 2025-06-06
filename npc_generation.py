# npc_generation.py
import random
from stats import RACES
from npc import NPC # NPC class itself
from npc_roles import FRIENDLY_ROLES, HOSTILE_ROLES # Roles are now in npc_roles.py
from ui import UI # Added for print_failure
from locations import RAW_LOCATION_DATA_MAP # Import for accessing raw location data
from fixed_npc_data import FIXED_NPC_DATA

def determine_npc_count(tags_list):
    """Determines the number of NPCs to generate based on location tags."""
    if any(t in tags_list for t in ["city", "capital"]):
        return random.randint(12, 20)  # Increased
    elif any(t in tags_list for t in ["tavern", "inn"]):
         return random.randint(6, 12)   # Increased
    elif any(t in tags_list for t in ["town", "village", "market", "keep"]):
        return random.randint(6, 10)   # Increased
    elif any(t in tags_list for t in ["camp", "dungeon", "ruin", "mine", "watchtower", "lair"]):
        return random.randint(3, 7)    # Increased
    else:
        return random.randint(2, 4)     # Increased

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
    except ValueError: # Should not happen if weights sum correctly and are positive
        return random.choice(list(RACES.keys())) if cultures else random.choice(list(RACES.keys())) # Fallback

def determine_npc_role(tags_list, base_role_pool):
    """Determines an NPC's role based on location tags and a base pool of roles."""
    if "college" in tags_list or "mage_guild" in tags_list:
        return random.choice(["mage_apprentice", "scholar", "magic_lecturer", "college_guard"])
    if "companions" in tags_list:
        return random.choice(["companion_warrior", "new_blood", "circle_member"])
    if "thieves_guild_den" in tags_list or ("thieves" in tags_list and "underground" in tags_list):
        return random.choice(["thief_lookout", "pickpocket", "guild_rogue"])
    if "darkbrotherhood_sanctuary" in tags_list:
        return random.choice(["db_assassin", "db_initiate", "sanctuary_speaker"])
    if "dwemer_ruin" in tags_list:
        if random.random() < 0.6: return random.choice(["dwarven_sphere_damaged", "dwarven_spider_worker", "falmer_skulker"])
        else: return "explorer"
    if "mine" in tags_list and "abandoned" not in tags_list and "infested" not in tags_list:
        return "miner" if random.random() < 0.7 else "mine_foreman"
    if "bandit_camp" in tags_list or ("camp" in tags_list and "bandit" in tags_list) or "bandit_hideout" in tags_list:
        return random.choice(["bandit", "bandit_thug", "bandit_archer", "bandit_leader"])
    if any(indicator in tags_list for indicator in ["bandit", "dungeon", "ruin", "forsworn", "necromancer", "vampire_lair", "monster_den", "lair"]):
        return random.choice(list(HOSTILE_ROLES))
    if "forsworn_camp" in tags_list or "forsworn_redoubt" in tags_list:
        return random.choice(["forsworn_raider", "forsworn_shaman", "forsworn_briarheart"])
    if ("temple" in tags_list or "shrine" in tags_list) and "ruined" not in tags_list and "abandoned" not in tags_list:
        return random.choice(["priest", "pilgrim", "temple_guardian", "healer"])
    if "military_fort" in tags_list or "watchtower_manned" in tags_list:
        faction = "stormcloak_soldier" if "stormcloak_controlled" in tags_list else "imperial_soldier"
        if "officer_quarters" in tags_list: faction = faction.replace("soldier","officer")
        return faction
    if "farm" in tags_list:
        return random.choice(["farmer", "farm_hand", "farmer_spouse"])
    if "shop" in tags_list or "market" in tags_list:
        return random.choice(["merchant", "stall_owner", "shop_assistant", "city_guard_patrolling"])
    if "port" in tags_list:
        return random.choice(["sailor", "dock_worker", "ship_captain_ashore", "fishmonger"])
    
    # Add logic for Beggar and Elder
    if "city" in tags_list or "town" in tags_list or "village" in tags_list:
        if random.random() < 0.1:  # 10% chance of being a beggar
            return "beggar"
        if random.random() < 0.05: # 5% chance of being an elder
            return "elder"

    if not base_role_pool:
        return random.choice(list(FRIENDLY_ROLES | HOSTILE_ROLES))
        
    return random.choice(list(base_role_pool))

def generate_tavern_npcs(location, tags_list, demographics, npc_registry, filled_roles: set):
    # Ensure one innkeeper is generated, if not already fixed
    if "publican" in filled_roles:
        return  # Do not generate a random innkeeper if there's a fixed publican
    if "innkeeper" not in filled_roles:
        innkeeper_culture = determine_npc_culture(demographics)
        innkeeper_race = innkeeper_culture if innkeeper_culture else "Nord"
        innkeeper = NPC(name=None, race=innkeeper_race, role="innkeeper", level=random.randint(4, 8))
        npc_registry[location.id].append(innkeeper)
        filled_roles.add("innkeeper") # Mark as filled

    # Increase patron count
    patron_count = random.randint(3, 7)
    patron_role_pool = {"adventurer", "farmer", "hunter", "traveler", "mercenary", "patron"} # Added generic "patron"
    if "trade" in tags_list or "city" in tags_list or "market" in tags_list: patron_role_pool.add("merchant")
    if "companions" in tags_list: patron_role_pool.add("warrior")
    if "stormcloak" in tags_list: patron_role_pool.add("stormcloak_supporter")
    if "imperial" in tags_list: patron_role_pool.add("imperial_citizen")
    if "bards_college_nearby" in tags_list or "bards" in tags_list: patron_role_pool.add("bard_student")

    # Adjust mercenary count based on location type
    if any(t in tags_list for t in ["city", "capital"]):
        num_mercenaries = random.randint(1, 2)  # Major city: 1-2 mercenaries
    elif any(t in tags_list for t in ["town", "village"]):
        num_mercenaries = random.randint(0, 1)  # Small town: 0-1 mercenaries
    else:
        num_mercenaries = 0  # Other locations: no mercenaries

    for _ in range(num_mercenaries):
        patron_culture = determine_npc_culture(demographics)
        patron_race = patron_culture if patron_culture else "Nord"
        patron = NPC(name=None, race=patron_race, role="mercenary", level=random.randint(1,5))
        npc_registry[location.id].append(patron)

    for _ in range(patron_count - num_mercenaries): #Adjust patron count to account for mercenaries
        patron_culture = determine_npc_culture(demographics)
        patron_race = patron_culture if patron_culture else "Nord"
        patron_role = random.choice(list(patron_role_pool - {"mercenary"})) if patron_role_pool else "local" #Ensure no duplicate mercenaries
        patron = NPC(name=None, race=patron_race, role=patron_role, level=random.randint(1,5))
        npc_registry[location.id].append(patron) # Changed location["id"] to location.id

    if random.random() < 0.7 and "bards" not in patron_role_pool: # Ensure bard is not already a common patron role
        bard_culture = determine_npc_culture(demographics)
        bard_race = bard_culture if bard_culture else "Nord"
        bard = NPC(name=None, race=bard_race, role="bard", level=random.randint(2,6))
        npc_registry[location.id].append(bard)

    # Potentially add tavern staff for larger/busier taverns
    if any(t in tags_list for t in ["city", "capital"]) and random.random() < 0.5:
        num_staff_to_generate = random.randint(1, 2)
        possible_staff_roles = ["server", "cook"] # Roles we might want to generate

        for _ in range(num_staff_to_generate):
            # Find roles that are not yet filled and are in our list of possible staff roles
            available_roles_for_staff = [role for role in possible_staff_roles if role not in filled_roles]

            if not available_roles_for_staff:
                break # No more staff roles to fill

            chosen_role = random.choice(available_roles_for_staff)
            
            staff_culture = determine_npc_culture(demographics)
            staff_race = staff_culture if staff_culture else "Nord"
            staff_member = NPC(name=None, race=staff_race, role=chosen_role, level=random.randint(2,5))
            npc_registry[location.id].append(staff_member)
            filled_roles.add(chosen_role) # Mark this specific role as filled

def generate_standard_npcs(location, tags_list, npc_count, role_pool, demographics, npc_registry, filled_roles: set):
    generated_names = set() # Keep track of names generated for this location
    
    # Filter out roles that are already filled by fixed NPCs
    available_role_pool = list((set(role_pool) - filled_roles) - {"local"}) # Remove "local" from the role pool
    if not available_role_pool and role_pool: # If all specific roles are filled, fall back to the original pool (might create duplicates if not careful)
        available_role_pool = list(role_pool)

    for _ in range(npc_count):
        if not available_role_pool: # No more roles to pick from
            break
            
        role = determine_npc_role(tags_list, available_role_pool) # Use available pool
        
        # If a role is determined that was actually fixed but somehow not in filled_roles (e.g. specific logic in determine_npc_role),
        # it's complex to handle perfectly without more state. For now, we assume determine_npc_role respects the pool.
        # A simple check: if role in filled_roles, try to pick another one.
        if role in filled_roles:
            temp_pool = [r for r in available_role_pool if r != role]
            if not temp_pool: continue # Skip if no other role available
            role = random.choice(temp_pool)

        culture = determine_npc_culture(demographics)
        npc_race = culture if culture else random.choice(list(RACES.keys()))
        
        if npc_race == "dwemer" and role not in ["dwemer_construct", "dwemer_ghost", "ancient_scholar_spirit"]:
            role = random.choice(["dwemer_construct", "dwemer_ghost"]) if random.random() < 0.7 else "lingering_echo"

        raw_loc_data_for_level = RAW_LOCATION_DATA_MAP.get(location.id, {})
        npc_level_min, npc_level_max = raw_loc_data_for_level.get("level_range", (1, 5))
        npc_level = random.randint(npc_level_min, npc_level_max)
        npc_level = max(1, npc_level + random.randint(-1,1))

        # Attempt to generate a unique name for this location
        attempts = 0
        new_npc = None
        while attempts < 5: # Try up to 5 times to get a unique name
            new_npc = NPC(name=None, race=npc_race, role=role, level=npc_level)
            if new_npc.name not in generated_names:
                generated_names.add(new_npc.name)
                break
            attempts += 1
        if new_npc: # Use the NPC even if name is not unique after attempts
             npc_registry[location.id].append(new_npc) # Changed location["id"] to location.id


def generate_npcs_for_location(location_obj, npc_registry, find_hierarchy_func):
    try:
        raw_location_data = RAW_LOCATION_DATA_MAP.get(location_obj.id, {})

        if raw_location_data.get("is_encounter"):
            return

        if location_obj.id in npc_registry and npc_registry[location_obj.id]:
            return

        npc_registry[location_obj.id] = []
        filled_roles = set()

        # --- NEW SECTION: Spawn fixed NPCs first ---
        if location_obj.id in FIXED_NPC_DATA:
            for npc_data in FIXED_NPC_DATA[location_obj.id]:
                # Create the NPC instance from the fixed data
                fixed_npc = NPC(
                    name=npc_data["name"],
                    race=npc_data["race"],
                    role=npc_data["role"],
                    level=npc_data.get("level", 5) # Default level if not specified
                )
                npc_registry[location_obj.id].append(fixed_npc)
                filled_roles.add(npc_data["role"].lower()) # Mark role as filled to avoid duplicates
        # --- END OF NEW SECTION ---

        # _find_hierarchy returns (hold_obj, primary_obj, specific_obj)
        # We map parent_hold to hold_obj and parent_city to primary_obj
        parent_hold, parent_city, _ = find_hierarchy_func(location_obj.id)
        combined_tags_for_npc_gen = list(raw_location_data.get("tags", []))

        inheritable_npc_context_tags = {
            "nordic", "imperial", "stormcloak", "thieves", "corrupt", "college", "companions", "darkbrotherhood",
            "military", "bards", "city", "town", "village", "hold", "dwemer", "forsworn", "undead", "vampire", "mage_guild"
        }

        contextual_parent = None
        # parent_city and parent_hold are Location objects or None
        if parent_city and parent_city.id != location_obj.id:
            raw_parent_city_data = RAW_LOCATION_DATA_MAP.get(parent_city.id, {})
            if any(sub_loc.get("id") == location_obj.id for sub_loc in raw_parent_city_data.get("sub_locations", [])):
                contextual_parent = parent_city
        elif parent_hold and parent_hold.id != location_obj.id:
            raw_parent_hold_data = RAW_LOCATION_DATA_MAP.get(parent_hold.id, {})
            if any(sub_loc.get("id") == location_obj.id for sub_loc in raw_parent_hold_data.get("sub_locations", [])):
                 contextual_parent = parent_hold
        elif "city" in combined_tags_for_npc_gen and parent_hold and parent_hold.id != location_obj.id:
             contextual_parent = parent_hold

        if contextual_parent: # contextual_parent is a Location object
            raw_contextual_parent_data = RAW_LOCATION_DATA_MAP.get(contextual_parent.id, {})
            combined_tags_for_npc_gen.extend([
                t for t in raw_contextual_parent_data.get("tags", []) if t in inheritable_npc_context_tags
            ])
        combined_tags_for_npc_gen = list(set(combined_tags_for_npc_gen))
        
        demographics_source = location_obj # This is a Location object
        raw_demographics_source_data = RAW_LOCATION_DATA_MAP.get(demographics_source.id, {})

        if not raw_demographics_source_data.get("demographics") and contextual_parent:
            raw_contextual_parent_data = RAW_LOCATION_DATA_MAP.get(contextual_parent.id, {})
            if raw_contextual_parent_data.get("demographics"):
                demographics_source = contextual_parent # Update to Location object
                raw_demographics_source_data = raw_contextual_parent_data # Update raw data accordingly

        if not raw_demographics_source_data.get("demographics") and parent_hold:
            raw_parent_hold_data = RAW_LOCATION_DATA_MAP.get(parent_hold.id, {})
            if raw_parent_hold_data.get("demographics"):
                demographics_source = parent_hold # Update to Location object
                raw_demographics_source_data = raw_parent_hold_data # Update raw data accordingly
        
        # After determining the correct demographics_source (Location object), get its demographics
        demographics = RAW_LOCATION_DATA_MAP.get(demographics_source.id, {}).get("demographics", {"Nord": 100})


        base_npc_count = determine_npc_count(combined_tags_for_npc_gen)
        # Adjust count based on already spawned fixed NPCs.
        # This assumes npc_count is a target total, not additional random NPCs.
        # If fixed NPCs should be *in addition* to random ones, this adjustment isn't needed.
        # For now, let's assume npc_count is the target total.
        npc_count_to_generate_randomly = max(0, base_npc_count - len(npc_registry[location_obj.id]))

        
        role_pool = set(FRIENDLY_ROLES) - {"local"}
        hostile_location_indicators = ["bandit", "dungeon", "ruin", "forsworn", "necromancer", "vampire_lair", "monster_den", "lair"]
        # Use location_obj.name directly as it's an attribute
        if any(indicator in tag for tag in combined_tags_for_npc_gen for indicator in hostile_location_indicators) or \
           any(indicator in location_obj.name.lower() for indicator in hostile_location_indicators) or \
           "bandit_hideout" in combined_tags_for_npc_gen:  # Explicitly add HOSTILE_ROLES for bandit hideouts
            role_pool.update(HOSTILE_ROLES)
        if "city" not in combined_tags_for_npc_gen and "town" not in combined_tags_for_npc_gen:
            role_pool = role_pool - {"merchant", "noble", "bard", "scholar"}

        # More robust check for tavern/inn locations
        is_tavern_or_inn = any(t in combined_tags_for_npc_gen for t in ["tavern", "inn", "settlement_features_tavern", "structure_type_inn_building"])

        if is_tavern_or_inn:
            # Pass filled_roles to generate_tavern_npcs
            generate_tavern_npcs(location_obj, combined_tags_for_npc_gen, demographics, npc_registry, filled_roles)
        
        # Generate standard NPCs if count is still positive (can be 0 if fixed NPCs met the quota)
        # Also, taverns might have other standard NPCs besides tavern-specific ones.
        # The role_pool for standard NPCs should also respect filled_roles.
        if npc_count_to_generate_randomly > 0:
            generate_standard_npcs(location_obj, combined_tags_for_npc_gen, npc_count_to_generate_randomly, role_pool, demographics, npc_registry, filled_roles)

    except Exception as e:
        # Use getattr for safe access to name in case location_obj is not fully initialized
        location_name_for_error = getattr(location_obj, 'name', 'Unknown Location')
        UI.print_failure(f"Error in generate_npcs_for_location for {location_name_for_error}: {e}")

def create_npc(name: str, race: str, role: str, level: int, template: dict = None) -> NPC:
    """Creates a new NPC based on a template."""
    try:
        if template:
            # Use the template to create the NPC
            npc = NPC(name=template.get("name", name),
                      race=template.get("race", race),
                      role=template.get("role", role),
                      level=template.get("level", level),
                      disposition=template.get("disposition", 50),
                      gold=template.get("gold", 0),
                      patrol_route=template.get("patrol_route", []))
        else:
            # Create a default NPC
            npc = NPC(name=name, race=race, role=role, level=level)
        return npc
    except Exception as e:
        print(f"Error creating NPC: {e}")
        return None