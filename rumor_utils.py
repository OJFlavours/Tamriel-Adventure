import random
from typing import List, Dict, Any

from ui import UI
from items import generate_random_item as gr_item_func
from locations import LocationManager
from quests import find_locations_by_tag # Ensure Quest class is not needed here directly

# Import data from rumor_data.py
from rumor_data import (
    QUEST_REWARDS_TEMPLATE,
    RANDOM_MOUNTAIN_RANGES,
    RANDOM_ITEM_TYPES,
    RANDOM_CREATURE_TYPES,
    RANDOM_RUIN_TYPES,
    RANDOM_NOBLE_FAMILY_NAMES,
    RANDOM_GUILD_NAMES,
    RANDOM_DIVINE_NAMES,
    RANDOM_DAEDRIC_PRINCE_NAMES,
    RANDOM_JASCO_ADJECTIVES,
    RANDOM_ENEMIES,
    FLAVOR_RUMOR_TEMPLATES # Needed for _replace_placeholders_in_rumor indirectly via _get_dynamic_placeholder if it were to use it
)

# --- Helper Functions ---
def _get_random_from_list(lst: List[Any]) -> Any:
    return random.choice(lst) if lst else None

def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    try:
        from npc_names import NAME_POOLS # Corrected import
        if role_hint in NAME_POOLS:
            race_data = NAME_POOLS[role_hint]
            name_type = next(iter(race_data))
            gender = next(iter(race_data[name_type]))
            name_pool_entry = race_data[name_type][gender]
        else:
            random_race = random.choice(list(NAME_POOLS.keys()))
            if random_race in ["undead_nord", "undead_skeleton", "spirit", "falmer", "dwemer_construct_race", "wolf_creature", "bear_creature", "spider_creature", "chaurus_creature"]:
                random_race = "nord"

            random_gender = random.choice(["male", "female"])
            name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, NAME_POOLS["nord"]["commoner"]["male"])
        
        if not name_pool_entry:
             name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"]

        chosen_name_with_id = random.choice(name_pool_entry)
        name_display = chosen_name_with_id.split('_')[0].capitalize()
        return {"name": name_display, "id": chosen_name_with_id}
    except (ImportError, KeyError) as e:
        UI.print_warning(f"DEBUG: Error in get_npc_name_by_role_hint for '{role_hint}': {e}. Using fallback.")
        return {"name": role_hint.replace("_", " ").title(), "id": f"{role_hint}_{random.randint(1000,9999)}"}

def generate_reward(player_level: int, quest_tags: List[str]) -> Dict[str, Any]:
    reward: Dict[str, Any] = {}
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)
    if random.random() < 0.7:
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)
    
    chosen_item_quality = "common"
    for level_range, qualities in QUEST_REWARDS_TEMPLATE["item_quality_levels"].items():
        if level_range[0] <= player_level <= level_range[1]:
            chosen_item_quality = random.choice(qualities)
            break
    
    if ("item" in quest_tags or not quest_tags) and random.random() < 0.45:
        item_category_choice = random.choice(["weapon", "armor", "potion", "jewelry", "misc", "scroll"])
        reward_item = gr_item_func(item_category_choice, player_level) 
        if reward_item: reward["item"] = reward_item
            
    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3:
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list): reward[chosen_type] = _get_random_from_list(value_source)
        else: reward[chosen_type] = random.randint(value_source["min"], value_source["max"])
    return reward

def _get_dynamic_placeholder(placeholder_type: str, current_location: Dict[str, Any] = None) -> str:
    """Helper to get a random value for a placeholder based on type."""
    if placeholder_type == "[NPC_Name_Local]": return get_npc_name_by_role_hint(random.choice(["merchant", "farmer", "guard", "innkeeper"]))["name"]
    if placeholder_type == "[NPC_Name_Suspicious]": return get_npc_name_by_role_hint(random.choice(["thief", "smuggler", "shady character"]))["name"]
    if placeholder_type == "[Location_Name_Nearby_Minor]":
        if current_location and current_location.get("parent_name"):
            parent_hold_name = current_location["parent_name"]
            location_manager = LocationManager()
            hold_obj = next((loc for loc in location_manager.locations.values() if loc.name == parent_hold_name), None)
            if hold_obj and hold_obj.sub_locations:
                minor_locs = [location_manager.get_location(s_loc_id).name for s_loc_id in hold_obj.sub_locations if any(tag in location_manager.get_location(s_loc_id).tags for tag in ["village", "camp", "cave", "mine", "shack"])]
                if minor_locs: return random.choice(minor_locs)
        return random.choice(["a nearby cave", "an old watchtower", "that farmstead down the road"])
    if placeholder_type == "[Item_Type_Common]": return random.choice(["axe", "some firewood", "a healing poultice", "some bread"])
    if placeholder_type == "[Item_Type_Valuable]": return random.choice(RANDOM_ITEM_TYPES)
    if placeholder_type == "[Creature_Type_Common]": return random.choice(["wolf", "skeever", "mudcrab"])
    if placeholder_type == "[Creature_Type_Dangerous]": return random.choice(RANDOM_CREATURE_TYPES)
    if placeholder_type == "[Ruin_Name_Specific]":
        ruin_locs = find_locations_by_tag("ruin") + find_locations_by_tag("barrow") + find_locations_by_tag("dwemer_ruin")
        return random.choice(ruin_locs)["name"] if ruin_locs else "some old ruins"
    if placeholder_type == "[Ruin_Type]": return random.choice(RANDOM_RUIN_TYPES)
    if placeholder_type == "[Mountain_Range]": return random.choice(RANDOM_MOUNTAIN_RANGES)
    if placeholder_type == "[Noble_Family_Name]": return random.choice(RANDOM_NOBLE_FAMILY_NAMES)
    if placeholder_type == "[Guild_Name]": return random.choice(RANDOM_GUILD_NAMES)
    if placeholder_type == "[Divine_Name]": return random.choice(RANDOM_DIVINE_NAMES)
    if placeholder_type == "[Daedric_Prince_Name]": return random.choice(RANDOM_DAEDRIC_PRINCE_NAMES)
    if placeholder_type == "[Jarl_Name_Current_Hold]":
        if current_location and current_location.get("parent_name"):
            hold_jarls = {"Whiterun Hold": "Balgruuf", "Eastmarch": "Ulfric", "Haafingar": "Elisif", "The Reach": "Igmund", "The Rift": "Laila", "Falkreath Hold": "Siddgeir", "Hjaalmarch":"Idgrod", "The Pale":"Skald", "Winterhold Hold": "Korir"}
            return hold_jarls.get(current_location["parent_name"], "the Jarl")
        return "the Jarl"
    if placeholder_type == "[Enemy_Type_Plural]": return random.choice(RANDOM_ENEMIES)
    if placeholder_type == "[Adjective_Mysterious]": return random.choice(RANDOM_JASCO_ADJECTIVES)

    return placeholder_type

def _replace_placeholders_in_rumor(rumor_template: str, current_location: Dict[str, Any]) -> str:
    """Replaces placeholders in a rumor string with dynamic content."""
    rumor = rumor_template

    rumor = rumor.replace("[LocationName]", current_location.get("name", "this strange place"))
    parent_name = current_location.get("parent_name")
    if not parent_name and "hold" in current_location.get("tags",[]):
        parent_name = current_location.get("name")
    elif not parent_name:
        parent_name = "the nearest major city"
    rumor = rumor.replace("[ParentLocationName]", parent_name)
    rumor = rumor.replace("[Jarl_Name_Current_Hold]", _get_dynamic_placeholder("[Jarl_Name_Current_Hold]", current_location))

    placeholders = [
        "[NPC_Name_Local]", "[NPC_Name_Guard]", "[NPC_Name_Suspicious]", "[Innkeeper_Name]", "[Merchant_Name]", "[Suspicious_Merchant_Name]", "[Local_Figure_Name]", "[Competitor_Shop_Owner_Name]", "[NPC_Name_Local_Youth]",
        "[Location_Name_Nearby_Minor]", "[Ruin_Name_Specific]", "[CaveName_or_DungeonName]", "[HillName_or_MountainName]", "[RiverName_or_Landmark]",
        "[Item_Type_Common]", "[Item_Type_Valuable]",
        "[Creature_Type_Common]", "[Creature_Type_Dangerous]",
        "[Food_Type]", "[Material_Type]", "[Ingredient_Type]", "[Plant_or_Mushroom_Type]",
        "[Race_Minority]", "[Noble_Family_Name]", "[Guild_Name]", "[Divine_Name]", "[Daedric_Prince_Name]",
        "[Ruin_Type]", "[Mountain_Range]", "[Wilderness_Type]", "[Local_Building_Type]",
        "[Enemy_Type_Plural]", "[Adjective_Mysterious]", "[Adjective_Mead_Quality]"
    ]
    adjective_mead_quality = random.choice(["strong", "weak", "surprisingly good", "terrible", "passable"])

    # Import NAME_POOLS here if get_npc_name_by_role_hint needs it and it's not already globally available
    # from npc import NAME_POOLS # Already imported at module level if needed by get_npc_name_by_role_hint

    for ph in placeholders:
        if ph in rumor:
            if ph == "[Innkeeper_Name]": replacement = get_npc_name_by_role_hint("innkeeper")["name"]
            elif ph == "[Merchant_Name]": replacement = get_npc_name_by_role_hint("merchant")["name"]
            elif ph == "[Suspicious_Merchant_Name]": replacement = get_npc_name_by_role_hint("thief")["name"]
            elif ph == "[NPC_Name_Guard]": replacement = get_npc_name_by_role_hint("guard")["name"]
            elif ph == "[Local_Figure_Name]": replacement = get_npc_name_by_role_hint(random.choice(["noble","mage","warrior"]))["name"]
            elif ph == "[Competitor_Shop_Owner_Name]": replacement = get_npc_name_by_role_hint("merchant")["name"]
            elif ph == "[NPC_Name_Local_Youth]":
                try:
                    from npc_names import NAME_POOLS # Corrected import
                    replacement = get_npc_name_by_role_hint("child")["name"] if "child" in NAME_POOLS else get_npc_name_by_role_hint("peasant")["name"]
                except ImportError:
                    replacement = get_npc_name_by_role_hint("peasant")["name"] # Fallback if NAME_POOLS can't be imported
            elif ph == "[Race_Minority]": replacement = random.choice(["Dunmer", "Argonian", "Khajiit", "Bosmer"])
            elif ph == "[Food_Type]": replacement = random.choice(["apples", "fish", "venison", "potatoes"])
            elif ph == "[Material_Type]": replacement = random.choice(["iron ore", "firewood", "linen", "hides"])
            elif ph == "[Ingredient_Type]": replacement = random.choice(["nightshade", "deathbell", "mountain flower", "nirnroot"])
            elif ph == "[Plant_or_Mushroom_Type]": replacement = random.choice(["glowing mushrooms", "bloodgrass", "mana bloom"])
            elif ph == "[Local_Building_Type]": replacement = random.choice(["old mill", "abandoned shack", "ruined tower", "fishery"])
            elif ph == "[Adjective_Mead_Quality]": replacement = adjective_mead_quality
            else: replacement = _get_dynamic_placeholder(ph, current_location)
            rumor = rumor.replace(ph, replacement, 1)

    return rumor