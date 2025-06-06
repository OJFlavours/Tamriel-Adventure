# quest_utils.py
import random
from typing import List, Dict, Any, Optional

from locations import LocationManager
from items import generate_random_item as gr_item_func # For generate_reward
from quest_config import QUEST_REWARDS_TEMPLATE # For generate_reward
# Quest import will be needed if list_player_quests_for_display uses Quest type hint directly
# from quest_entities import Quest # For list_player_quests_for_display type hint

# Global variable to store the location index
# Global variable to store the NPC name index
NPC_NAME_INDEX = {}
LOCATION_INDEX = {}

# Helper function to find locations by tag
def find_locations_by_tag(tag: str) -> List[Dict]:
    """
    Finds locations by tag using the location index.
    Returns a list of matching location dictionaries.
    """
    global LOCATION_INDEX
    if not LOCATION_INDEX:
        location_manager = LocationManager()
        LOCATION_INDEX = index_locations_by_tag(location_manager.locations.values())
    return LOCATION_INDEX.get(tag, [])
# Index locations by tag for faster lookup
def index_locations_by_tag(locations: List) -> Dict[str, List[Dict]]:
    """
    Indexes the LOCATIONS data structure by tag for faster lookup.
    Returns a dictionary that maps tags to lists of locations.
    """
    index: Dict[str, List[Dict]] = {}
    for loc in locations:
        if hasattr(loc, 'tags'):
            tags = loc.tags
        else:
            tags = loc.get("tags", [])
        for tag in tags:
            if tag not in index:
                index[tag] = []
            index[tag].append({"id": loc.id, "name": loc.name, "tags": loc.tags})
        if hasattr(loc, 'sub_locations'):
            sub_locations = loc.sub_locations
        else:
            sub_locations = loc.get("sub_locations", [])
        for sub_id in sub_locations:
            location_manager = LocationManager()
            sub = location_manager.get_location(sub_id)
            if sub:
                if hasattr(sub, 'tags'):
                    sub_tags = sub.tags
                else:
                    sub_tags = sub.get("tags", [])
                for tag in sub_tags:
                    if tag not in index:
                        index[tag] = []
                    sub_copy = {"id": sub.id, "name": sub.name, "tags": sub.tags}
                    sub_copy["parent_name"] = loc.name if hasattr(loc, 'name') else loc["name"]
                    index[tag].append(sub_copy)
                if hasattr(sub, 'sub_locations'):
                    sub2_locations = sub.sub_locations
                else:
                    sub2_locations = sub.get("sub_locations", [])
                for sub2_id in sub2_locations:
                    sub2 = location_manager.get_location(sub2_id)
                    if sub2:
                        if hasattr(sub2, 'tags'):
                            sub2_tags = sub2.tags
                        else:
                            sub2_tags = sub2.get("tags", [])
                        for tag in sub2_tags:
                            if tag not in index:
                                index[tag] = []
                            sub2_copy = {"id": sub2.id, "name": sub2.name, "tags": sub2.tags}
                            sub2_copy["parent_name"] = f'{loc.name if hasattr(loc, "name") else loc["name"]} -> {sub.name if hasattr(sub, "name") else sub["name"]}'
                            index[tag].append(sub2_copy)
    return index

# Helper to get NPC name by role hint
def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    """
    Retrieves a random NPC name and its unique ID from NAME_POOLS based on a role hint.
    Prioritizes specific IDs if the hint matches a known NPC.
    """
    global NPC_NAME_INDEX
    from npc_names import NAME_POOLS # Import NAME_POOLS from npc_names.py
    # Index NPC names by role hint for faster lookup
    def index_npc_names_by_role_hint(name_pools: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
        """
        Indexes the NAME_POOLS data structure by role hint for faster lookup.
        Returns a dictionary that maps role hints to NPC names and IDs.
        """
        index: Dict[str, Dict[str, str]] = {}
        for race_data in name_pools.values():
            for name_type_data in race_data.values():
                for gender_name_list in name_type_data.values():
                    for name_id in gender_name_list:
                        role_hint = name_id.split('_')[0].capitalize()
                        if role_hint not in index:
                            index[role_hint] = {}
                        index[role_hint] = {"name": name_id.split('_')[0].capitalize(), "id": name_id}
        return index
    if not NPC_NAME_INDEX:
        NPC_NAME_INDEX = index_npc_names_by_role_hint(NAME_POOLS)
    if role_hint in NPC_NAME_INDEX:
        return NPC_NAME_INDEX[role_hint]

    random_race = random.choice(list(NAME_POOLS.keys()))
    random_gender = random.choice(["male", "female"])
    name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, None)
    if not name_pool_entry:
        name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"] # Default

    chosen_name_with_id = random.choice(name_pool_entry)
    name_display = chosen_name_with_id.split('_')[0].capitalize()
    return {"name": name_display, "id": chosen_name_with_id}

# Helper function to find a location and its parent chain
def _find_loc_and_parents_recursive(target_id: str, current_level_list: List, parent_chain_from_root: List[Dict]) -> Optional[List[Dict]]:
    """
    Recursively searches for a location by ID within the LOCATIONS structure.
    Returns a list: [target_loc_dict, parent1_dict (immediate parent), ..., root_level_dict]
    parent_chain_from_root is the chain from the ultimate root down to the parent of current_level_list.
    """
    for loc_dict in current_level_list:
        if hasattr(loc_dict, 'id') and loc_dict.id == target_id:
            # Found the target. The chain is [target] + reversed parents from this path
            return [loc_dict] + parent_chain_from_root # parent_chain_from_root is already root -> immediate_parent
        
        if hasattr(loc_dict, 'sub_locations'):
            sub_locations = [location_manager.get_location(sub_id) for sub_id in loc_dict.sub_locations]
            # When going deeper, loc_dict becomes the most recent parent.
            # Add loc_dict to the end of the chain being passed down (root -> ... -> loc_dict)
            found_in_sub = _find_loc_and_parents_recursive(target_id, sub_locations, parent_chain_from_root + [loc_dict])
            if found_in_sub:
                return found_in_sub
    return None

# DummyRumor class for flavor tag compatibility
class DummyRumor: # Used by generate_location_appropriate_quest for flavor text
    def __init__(self):
        self.tags = {}

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

# Generate reward
def generate_reward(player_level: int, quest_tags: List[str]) -> Dict[str, Any]:
    """
    Generates a dictionary of rewards (gold, experience, items, reputation, favor)
    based on player level and quest tags.
    """
    reward: Dict[str, Any] = {}
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level,
                                     QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)
    if random.random() < 0.7:
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level,
                                                QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)

    chosen_item_quality = "common"
    for level_range, qualities in QUEST_REWARDS_TEMPLATE["item_quality_levels"].items():
        if level_range[0] <= player_level <= level_range[1]:
            chosen_item_quality = random.choice(qualities)
            break
    if random.random() < 0.4:
        # Pass chosen_item_quality to gr_item_func if it accepts it
        try:
            reward_item = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level, chosen_item_quality)
        except TypeError: # Fallback if gr_item_func doesn't take quality
            reward_item = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level)
        reward["item"] = reward_item

    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if
                               rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3:
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list):
            reward[chosen_type] = random.choice(value_source)
        else:
            reward[chosen_type] = random.randint(value_source["min"], value_source["max"])
    return reward

# Utility function
def list_player_quests_for_display(player: Any) -> List[Any]: # Changed List[Quest] to List[Any] to avoid circular import for now
    # from quest_entities import Quest # This would be ideal if no circular dependency
    if hasattr(player, 'quest_log') and player.quest_log:
        return player.quest_log.list_quests() # QuestLog.list_quests() returns List[Quest]
    return []
# New Utility Functions

def check_quest_condition(player: Any, quest: Dict[str, Any], condition: Dict[str, Any]) -> bool:
    """
    Checks if a specific quest condition is met.
    """
    try:
        # Implement condition checking logic here
        return False  # Placeholder
    except Exception as e:
        print(f"Error in check_quest_condition: {e}")
        return False

def find_quest_targets(quest: Dict[str, Any], target_type: str, count: int) -> List[Any]:
    """
    Finds a specified number of quest targets of a given type.
    """
    try:
        # Implement target finding logic here
        return []  # Placeholder
    except Exception as e:
        print(f"Error in find_quest_targets: {e}")
        return []

def award_quest_rewards(player: Any, quest: Dict[str, Any]) -> None:
    """
    Awards the player with the rewards for completing a quest.
    """
    try:
        # Implement reward awarding logic here
        pass  # Placeholder
    except Exception as e:
        print(f"Error in award_quest_rewards: {e}")

def fail_quest(player: Any, quest: Dict[str, Any]) -> None:
    """
    Handles quest failure logic.
    """
    try:
        # Implement quest failure logic here
        pass  # Placeholder
    except Exception as e:
        print(f"Error in fail_quest: {e}")