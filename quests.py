# quests.py
import random
from typing import List, Dict, Any # Import specific typing hints
from locations import LOCATIONS # Assuming LOCATIONS is fully defined and imported
import tags # Assuming tags.py contains TAGS dictionary
import flavor # Assuming flavor.py contains get_flavor function
# Import Item class from items.py for reward generation and type hinting
from items import Item, generate_random_item as gr_item_func, generate_item_from_key # Using alias for generate_random_item
from ui import UI # Import UI for debug messages

# Constant defined for quest rewards, used elsewhere if needed.
QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item_quality_levels": { # Defines item tier based on player level
        (1, 5): ["common", "uncommon"],
        (6, 10): ["uncommon", "rare"],
        (11, 20): ["rare", "epic"],
        (21, 99): ["epic", "legendary"]
    },
    "reputation": {"min": 5, "max": 15}, # Reputation gain
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold"] # Abstract favor
}

# --- NEW: QUEST TEMPLATES for diverse, lore-friendly quests ---
# Each template defines a quest type, its structure, and requirements.
QUEST_TEMPLATES = [
    # --- Basic Kill Quest (Bandits) ---
    {
        "id": "clear_bandit_camp",
        "title_template": "Bandit Menace at [LOCATION_NAME]",
        "desc_template": "A group of ruthless bandits has set up a camp near [LOCATION_NAME], preying on travelers and merchants. Their presence disrupts trade and frightens the locals. You must eliminate their leader and scatter their ranks.",
        "objectives_template": [
            {"type": "kill", "target_name": "bandit", "target_id": "bandit_leader", "count": 1},
            {"type": "kill", "target_name": "bandit", "target_id": "bandit_thug", "count": 3}
        ],
        "reward_tags": ["gold", "experience", "item"],
        "lore_tags": ["bandits", "road_safety"],
        "location_tags_required": ["camp", "bandit", "ruin"],
        "level_range": (1, 5),
        "flavor_tags": {"quest": {"type": ["hunt", "clear"]}},
        "turn_in_role_hint": ["guard", "merchant", "jarl"]
    },
    # --- Fetch Quest (Specific Item/Lore) ---
    {
        "id": "ancient_relic_retrieval",
        "title_template": "The Echoes of Saarthal",
        "desc_template": "An ancient Nordic relic, a 'Glyph of Unraveling', has been reported deep within Saarthal. It hums with a strange magic and holds forgotten knowledge, but it's guarded by the restless dead. Farengar Secret-Fire in Whiterun would pay handsomely for its recovery.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "Saarthal"},
            {"type": "collect_item", "item_key": "glyph_of_unraveling", "count": 1},
            {"type": "kill", "target_name": "draugr death overlord", "target_id": "draugr_death_overlord", "count": 1} # Boss
        ],
        "reward_tags": ["gold", "experience", "unique_spell_tome"],
        "lore_tags": ["saarthal", "ancient_nords", "magic", "mages_guild"],
        "location_tags_required": ["barrow", "dungeon", "undead"],
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["fetch", "investigate"]}},
        "turn_in_role_hint": ["scholar", "court_mage", "priest"]
    },
    # --- Talk/Diplomacy Quest ---
    {
        "id": "settle_land_dispute",
        "title_template": "A Farmer's Plea",
        "desc_template": "A long-standing land dispute between two neighboring farmers, [FARMER1_NAME] and [FARMER2_NAME], has escalated. Their squabbles threaten the harvest and the peace of [LOCATION_NAME]. You must mediate and find a peaceful resolution.",
        "objectives_template": [
            {"type": "talk_to_npc", "npc_name": "[FARMER1_NAME]", "npc_id": "[FARMER1_ID]"},
            {"type": "talk_to_npc", "npc_name": "[FARMER2_NAME]", "npc_id": "[FARMER2_ID]"},
            # A more complex objective could be: {"type": "choice", "options": ["favor_farmer1", "favor_farmer2", "compromise"]}
        ],
        "reward_tags": ["gold", "reputation", "favor"],
        "lore_tags": ["farming", "community", "dispute"],
        "location_tags_required": ["village", "farm"],
        "level_range": (1, 3),
        "flavor_tags": {"quest": {"type": ["negotiate", "diplomacy"]}},
        "turn_in_role_hint": ["farmer", "jarl", "village_elder"]
    },
    # --- Investigation/Environmental Hazard Quest ---
    {
        "id": "investigate_strange_weather",
        "title_template": "The Unnatural Chill of [LOCATION_NAME]",
        "desc_template": "An unnatural frost has gripped [LOCATION_NAME], even outside of winter. Livestock are dying, and the ground remains frozen. Locals whisper of ancient spirits or a necromancer's foul play. Investigate the source of this chill and put a stop to it.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "[SPECIFIC_SITE]"}, # e.g., Hob's Fall Cave
            {"type": "kill", "target_name": "necromancer", "target_id": "necromancer_unique_id", "count": 1},
            {"type": "collect_item", "item_key": "unholy_frost_rune", "count": 1}
        ],
        "reward_tags": ["gold", "experience", "magic_item"],
        "lore_tags": ["necromancy", "cold_magic", "nature_corruption"],
        "location_tags_required": ["snow", "marsh", "frozen"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "purge"]}},
        "turn_in_role_hint": ["priest", "healer", "jarl"]
    },
    # --- Collection/Alchemy Quest with Lore ---
    {
        "id": "crimson_nirnroot_sample",
        "title_template": "Crimson's Whisper",
        "desc_template": "Master [ALCHEMIST_NAME] at [LOCATION_NAME] requires samples of Crimson Nirnroot, a rare and potent alchemical ingredient found only in the deepest, most irradiated parts of certain Dwemer ruins, particularly Blackreach. This is a dangerous but rewarding task for an alchemist.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "Blackreach"},
            {"type": "collect_item", "item_key": "crimson_nirnroot_rare", "count": 5}
        ],
        "reward_tags": ["gold", "experience", "rare_potion"],
        "lore_tags": ["nirnroot", "blackreach", "dwemer", "alchemy"],
        "location_tags_required": ["dwemer", "underground"],
        "level_range": (10, 15),
        "flavor_tags": {"quest": {"type": ["fetch", "explore"]}},
        "turn_in_role_hint": ["alchemist", "scholar"]
    },
    # --- Rescue Quest (Social/Moral Choice potential) ---
    {
        "id": "rescue_kidnapped_civilian",
        "title_template": "The Missing Caravan Guard",
        "desc_template": "A caravan guard, [GUARD_NAME], hired to protect a vital shipment, has gone missing in the vicinity of [LOCATION_NAME]. Rumors suggest he was captured by a reclusive band of Forsworn who mistake all outsiders for enemies. His family, and the merchant, are desperate for his return.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "[FORSWORN_HIDEOUT_NAME]"},
            {"type": "talk_to_npc", "npc_name": "[GUARD_NAME]", "npc_id": "[GUARD_ID]"}, # Talk to the captive
            {"type": "kill", "target_name": "forsworn", "target_id": "forsworn_raider", "count": 5} # Clear out some guards
        ],
        "reward_tags": ["gold", "experience", "reputation"],
        "lore_tags": ["forsworn", "reachmen", "caravan_attack"],
        "location_tags_required": ["mountain", "forsworn", "camp"],
        "level_range": (8, 13),
        "flavor_tags": {"quest": {"type": ["rescue", "social"]}},
        "turn_in_role_hint": ["merchant", "guard", "jarl"]
    },
    # --- Divine/Shrine Quest ---
    {
        "id": "divine_blessing_restore",
        "title_template": "Akatosh's Silent Flame",
        "desc_template": "The Shrine of Akatosh near [LOCATION_NAME] has fallen silent, its eternal flame extinguished by unknown means. This blights the land and fills the faithful with dread. You must journey to the shrine, cleanse it of any malevolent influence, and rekindle the sacred flame.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "[LOCATION_NAME]"}, # Shrine location itself
            {"type": "kill", "target_name": "daedric worshiper", "target_id": "daedric_cultist", "count": 3}, # Or a specific monster
            {"type": "collect_item", "item_key": "dragon_scale_pure", "count": 1} # Symbolic offering/cleansing item
        ],
        "reward_tags": ["gold", "experience", "blessing_buff"],
        "lore_tags": ["akatosh", "divines", "shrines", "daedra"],
        "location_tags_required": ["holy", "ruin"],
        "level_range": (10, 15),
        "flavor_tags": {"quest": {"type": ["restore", "holy"]}},
        "turn_in_role_hint": ["priest", "paladin"]
    },
]

# --- Helper for Quest Generation ---
def _get_random_from_list(lst: List[Any]) -> Any:
    """Helper to get a random element from a list, or None if empty."""
    return random.choice(lst) if lst else None

def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    """
    Attempts to get a suitable NPC name and a pseudo-unique ID based on a role hint.
    This is a simplification; in a full game, you'd pick a real, existing NPC.
    """
    from npc import NAME_POOLS # Import here to avoid circular dependency
    # Attempt to derive a race and gender, fallback to Nord Male Commoner
    random_race = random.choice(list(NAME_POOLS.keys()))
    random_gender = random.choice(["male", "female"])
    
    name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, None)
    if not name_pool_entry: # Fallback to a very generic name if specific pool fails
        UI.print_system_message(f"DEBUG: Could not find specific name pool for role hint '{role_hint}'. Falling back to Nord commoner male.")
        name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"]
    
    chosen_name_with_id = random.choice(name_pool_entry)
    name_display = chosen_name_with_id.split('_')[0].capitalize() # Extract display name

    return {"name": name_display, "id": chosen_name_with_id} # Return both for use


# Utility function to generate a reward based on quest_tags and player level.
def generate_reward(player_level: int, quest_tags: List[str]) -> Dict[str, Any]:
    """
    Generate a diverse reward (gold, experience, item, etc.) based on quest type and player level.
    Returns a dictionary of rewards.
    """
    reward: Dict[str, Any] = {}
    
    # Gold reward
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)
    
    # Experience reward
    if random.random() < 0.7: # 70% chance for experience
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)

    # Item reward based on player level and quality hints
    chosen_item_quality = "common"
    for level_range, qualities in QUEST_REWARDS_TEMPLATE["item_quality_levels"].items():
        if level_range[0] <= player_level <= level_range[1]:
            chosen_item_quality = random.choice(qualities)
            break

    if random.random() < 0.4: # 40% chance for an item
        # In a more advanced system, generate_random_item would use 'chosen_item_quality'
        # For now, it mainly uses level for scaling.
        reward_item = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level)
        reward["item"] = reward_item

    # Add a chance for an additional diverse reward (reputation or favor)
    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3: # 30% chance for another reward type
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list): # For "favor"
            reward[chosen_type] = _get_random_from_list(value_source)
        else: # For "reputation"
            reward[chosen_type] = random.randint(value_source["min"], value_source["max"])

    return reward

# Define a Quest class with integrated location and completion condition.
class Quest:
    def __init__(self, title: str, description: str, reward: Dict[str, Any], level_requirement: int, location: Dict[str, Any],
                 objectives: List[Dict[str, Any]],
                 quest_id: int | None = None, status: str = "active", turn_in_npc_id: str | None = None):
        self.quest_id = quest_id or random.randint(1000, 9999)
        self.title = title
        self.description = description
        self.reward = reward 
        self.level_requirement = level_requirement
        self.location = location # The primary location related to the quest
        self.objectives = objectives # List of objective dictionaries
        self.status = status # "active", "completed", "turned_in", "failed"
        self.turn_in_npc_id = turn_in_npc_id # Unique ID of NPC to turn in quest (optional)
        self.tags: Dict[str, Any] = {} # Store quest-specific tags
        self.add_tag("quest", "type", "generic") # Default type, should be updated by generator

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        """Adds a tag to the quest instance."""
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

    def is_objective_met(self, objective: Dict[str, Any], player: Any) -> bool: # 'player' type hinted as Any to avoid circular imports
        """Checks if a single objective is met by the player's current state."""
        obj_type = objective["type"]
        
        if obj_type == "kill":
            target_id = objective["target_id"]
            required_count = objective["count"]
            current_count = player.defeated_enemies_tracker.get(target_id, 0)
            # Update objective's 'current' for display purposes (not persistent for saving)
            objective['current'] = current_count 
            return current_count >= required_count
        
        elif obj_type == "collect_item":
            item_key = objective["item_key"]
            required_count = objective["count"]
            current_count = sum(1 for item in player.stats.inventory if item.name.lower().replace(' ', '_') == item_key.lower().replace(' ', '_')) # Match by key
            objective['current'] = current_count
            return current_count >= required_count
        
        elif obj_type == "reach_location":
            location_name = objective["location_name"]
            # Check if player is currently at the location OR has discovered it
            return (player.current_location_obj and player.current_location_obj["name"].lower() == location_name.lower()) or \
                   any(loc_obj["name"].lower() == location_name.lower() for loc_obj in player.known_locations_objects)
        
        elif obj_type == "talk_to_npc":
            npc_id = objective["npc_id"]
            return npc_id in player.talked_to_npcs
        
        # Add more objective types as needed (e.g., "discover_lore", "persuade_npc")
        return False

    def check_all_objectives_met(self, player: Any) -> bool: # 'player' type hinted as Any
        """
        Checks if all objectives for this quest are met.
        Updates quest status to "completed" if all are met.
        """
        if self.status == "completed":
            return True # Already completed
            
        all_met = True
        for obj in self.objectives:
            if not self.is_objective_met(obj, player):
                all_met = False
                break
        
        if all_met:
            self.status = "completed"
            return True
        return False

    def __str__(self) -> str:
        """Returns a formatted string representation of the quest."""
        reward_str_parts = []
        for key, value in self.reward.items():
            if isinstance(value, Item):
                reward_str_parts.append(f"{value.name} (Item)")
            else:
                reward_str_parts.append(f"{value} {key.capitalize()}")
        reward_display = ", ".join(reward_str_parts)

        objectives_display = []
        for obj in self.objectives:
            current_progress_str = f" ({obj.get('current', 0)}/{obj['count']})" if "count" in obj else "" # Only for countable objectives
            if obj["type"] == "kill":
                objectives_display.append(f"Defeat {obj['count']} {obj['target_name']}s{current_progress_str}")
            elif obj["type"] == "collect_item":
                objectives_display.append(f"Collect {obj['count']} {obj['item_key'].replace('_', ' ').title()}{current_progress_str}")
            elif obj["type"] == "reach_location":
                objectives_display.append(f"Reach {obj['location_name']}")
            elif obj["type"] == "talk_to_npc":
                objectives_display.append(f"Talk to {obj['npc_name']}")
            # Add more objective types as needed
        
        # Dynamically get flavor text relevant to the quest's tags
        flavor_texts = flavor.get_flavor(self) 
        description_prefix = f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at {self.location.get('name', 'Unknown')} [Status: {self.status.capitalize()}]:"
        
        full_description = f"{description_prefix}\n  Objective: {self.description}\n"
        if objectives_display:
            full_description += "  Tasks:\n" + "\n".join([f"    - {task}" for task in objectives_display])
        full_description += f"\n  Reward: {reward_display}"
        
        if flavor_texts:
            full_description += f"\n  Lore: {' '.join(flavor_texts)}"
            
        return full_description

# Define a QuestLog class to hold and manage multiple quests.
class QuestLog:
    def __init__(self):
        self.active_quests: List[Quest] = []
        self.completed_quests: List[Quest] = [] # Use this to store successfully turned-in quests

    def add_quest(self, quest: Quest) -> bool:
        """Adds a quest to the active quest log, preventing duplicates."""
        # Prevent adding duplicates by quest_id
        if quest.quest_id not in [q.quest_id for q in self.active_quests] and \
           quest.quest_id not in [q.quest_id for q in self.completed_quests]:
            self.active_quests.append(quest)
            return True
        return False

    def remove_quest(self, quest_id: int) -> bool:
        """
        Removes a quest from active quests. If its status is 'completed',
        it moves it to the completed_quests list.
        """
        quest_to_remove = next((q for q in self.active_quests if q.quest_id == quest_id), None)
        if quest_to_remove:
            self.active_quests.remove(quest_to_remove)
            if quest_to_remove.status == "completed": # Only add to completed if it was actually marked completed
                self.completed_quests.append(quest_to_remove)
            return True
        return False

    def get_quest_by_id(self, quest_id: int) -> Quest | None:
        """Retrieves a quest by its ID from active or completed lists."""
        for q in self.active_quests:
            if q.quest_id == quest_id:
                return q
        for q in self.completed_quests:
            if q.quest_id == quest_id:
                return q
        return None

    def list_quests(self) -> List[Quest]:
        """Returns a combined list of active and completed quests (for display)."""
        return self.active_quests + self.completed_quests 

    def get_quests_for_turn_in(self, npc_id: str) -> List[Quest]:
        """Returns quests that are completed and ready to be turned in to a specific NPC."""
        return [q for q in self.active_quests if q.status == "completed" and q.turn_in_npc_id == npc_id]


# Utility function to list a player's current quests (used by UI).
def list_player_quests_for_display(player: Any) -> List[Quest]: # Player hinted as Any
    """
    Returns a list of quests assigned to the player (from their quest_log).
    """
    if hasattr(player, 'quest_log') and player.quest_log:
        return player.quest_log.list_quests()
    return []

# Helper function to search the LOCATIONS structure by matching tags.
def find_locations_by_tag(tag: str) -> List[Dict]:
    matching = []
    # Search top-level locations
    for loc in LOCATIONS:
        if tag in loc.get("tags", []):
            matching.append(loc)
        # Search sub_locations (level 1)
        for sub in loc.get("sub_locations", []):
            if tag in sub.get("tags", []):
                sub_copy = sub.copy()
                sub_copy["parent_name"] = loc["name"] # Add parent for context
                matching.append(sub_copy)
            # Search sub_locations (level 2, venues)
            for sub2 in sub.get("sub_locations", []):
                if tag in sub2.get("tags", []):
                    sub2_copy = sub2.copy()
                    sub2_copy["parent_name"] = f'{loc["name"]} -> {sub["name"]}' # Add hierarchical parent
                    matching.append(sub2_copy)
    return matching

def generate_location_appropriate_quest(player_level: int, location_tags: List[str], quest_giver_id: str | None = None) -> Quest | None:
    """
    Generate a quest appropriate for a player's level and location, using templates.
    """
    possible_templates = []
    
    # Filter templates based on location tags and player level
    for template in QUEST_TEMPLATES:
        # Check level range
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]):
            continue
        
        # Check required location tags
        if template["location_tags_required"]:
            if not all(tag in location_tags for tag in template["location_tags_required"]):
                continue
        
        possible_templates.append(template)

    if not possible_templates:
        # Fallback to generic quest generation if no specific templates match
        UI.print_system_message(f"DEBUG: No specific quest template matched for level {player_level} and tags {location_tags}. Generating generic quest.")
        
        chosen_location = random.choice(LOCATIONS) # Use a generic location
        
        title = "A Simple Request"
        description = f"A local resident needs help in {chosen_location.get('name', 'the area')} with a minor issue."
        objectives = [{"type": "reach_location", "location_name": chosen_location["name"]}]
        reward = generate_reward(player_level, location_tags)
        
        quest = Quest(
            title=title,
            description=description,
            reward=reward,
            level_requirement=player_level,
            location=chosen_location,
            objectives=objectives,
            status="active",
            turn_in_npc_id=quest_giver_id
        )
        quest.add_tag("quest", "type", "generic")
        return quest

    # Choose a random template from the filtered list
    chosen_template = random.choice(possible_templates)
    
    # --- Hydrate the template with specific details ---
    
    # Choose a specific location relevant to the template's required tags
    # Prioritize locations that directly match the template's tags
    relevant_locations = []
    for tag in chosen_template["location_tags_required"]:
        relevant_locations.extend(find_locations_by_tag(tag))
    relevant_locations = list({loc["name"]: loc for loc in relevant_locations}.values()) # Remove duplicates
    
    # If no specific relevant locations are found, fallback to current location or a general one
    if not relevant_locations:
        UI.print_system_message(f"DEBUG: No specific relevant location found for quest template '{chosen_template['id']}' based on tags. Falling back to random major location.")
        final_quest_location = random.choice(LOCATIONS) # Fallback to any major location
    else:
        final_quest_location = random.choice(relevant_locations) # Choose one from relevant locations

    # Replace placeholders in title and description
    title = chosen_template["title_template"].replace("[LOCATION_NAME]", final_quest_location["name"])
    description = chosen_template["desc_template"].replace("[LOCATION_NAME]", final_quest_location["name"])

    # Handle special placeholders for NPC names or specific sites within the quest
    if "[ALCHEMIST_NAME]" in description:
        npc_info = get_npc_name_by_role_hint("alchemist")
        description = description.replace("[ALCHEMIST_NAME]", npc_info["name"])
        # Update objectives if necessary, or store this NPC_ID for later
    if "[FARMER1_NAME]" in description:
        farmer1_info = get_npc_name_by_role_hint("farmer")
        farmer2_info = get_npc_name_by_role_hint("farmer")
        description = description.replace("[FARMER1_NAME]", farmer1_info["name"])
        description = description.replace("[FARMER2_NAME]", farmer2_info["name"])
        # Update objectives for talk_to_npc with actual IDs
        for obj in chosen_template["objectives_template"]:
            if obj["type"] == "talk_to_npc":
                if obj["npc_name"] == "[FARMER1_NAME]": obj["npc_id"] = farmer1_info["id"]
                if obj["npc_name"] == "[FARMER2_NAME]": obj["npc_id"] = farmer2_info["id"]
    if "[SPECIFIC_SITE]" in chosen_template["objectives_template"][0].get("location_name", ""):
        # Example: Choose a specific cave/ruin near the current location's hold
        possible_sites = find_locations_by_tag("cave") + find_locations_by_tag("ruin") + find_locations_by_tag("barrow")
        possible_sites = [s for s in possible_sites if s.get("name") not in [final_quest_location["name"]]] # Avoid current location
        if possible_sites:
            specific_site = random.choice(possible_sites)
            for obj in chosen_template["objectives_template"]:
                if obj["type"] == "reach_location" and obj["location_name"] == "[SPECIFIC_SITE]":
                    obj["location_name"] = specific_site["name"]
        else: # Fallback if no specific sites found
            UI.print_system_message(f"DEBUG: No specific site found for quest template '{chosen_template['id']}' for '[SPECIFIC_SITE]' placeholder. Using generic description.")
            for obj in chosen_template["objectives_template"]:
                if obj["type"] == "reach_location" and obj["location_name"] == "[SPECIFIC_SITE]":
                    obj["location_name"] = f"a mysterious site in {final_quest_location['name']}"


    # Process objectives from template
    objectives = []
    for obj_template in chosen_template["objectives_template"]:
        new_obj = obj_template.copy() # Make a copy to avoid modifying template
        if new_obj["type"] == "kill" and new_obj["target_name"] == "bandit":
            new_obj["target_id"] = "bandit_raider_generic" # Ensure a consistent ID
        elif new_obj["type"] == "kill" and new_obj["target_name"] == "draugr death overlord":
             new_obj["target_id"] = "draugr_death_overlord"
        # Update other target_ids/item_keys as needed based on chosen template
        objectives.append(new_obj)


    # Generate rewards based on reward_tags
    reward = generate_reward(player_level, chosen_template.get("reward_tags", []))

    quest = Quest(
        title=title,
        description=description,
        reward=reward,
        level_requirement=player_level,
        location=final_quest_location, # Use the selected location for the quest
        objectives=objectives,
        status="active",
        turn_in_npc_id=quest_giver_id # Assign quest giver ID from the NPC who offered it
    )
    quest.add_tag("quest", "type", chosen_template["id"])
    
    # Add flavor tags from the template
    if "flavor_tags" in chosen_template:
        for cat, types_dict in chosen_template["flavor_tags"].items():
            for t_type, t_value in types_dict.items():
                if isinstance(t_value, list):
                    for val in t_value:
                        quest.add_tag(cat, t_type, val)
                else:
                    quest.add_tag(cat, t_type, t_value)


    # Ensure the quest has at least one objective (safety check)
    if not quest.objectives:
        UI.print_system_message(f"DEBUG: Quest '{quest.title}' generated without objectives. Adding default 'reach_location'.")
        quest.objectives.append({"type": "reach_location", "location_name": final_quest_location["name"]})

    return quest

# Function to apply quest rewards to the player (moved to quests.py)
def process_quest_rewards(player: Any, quest: Quest) -> None: # Player hinted as Any
    """Applies the rewards of a completed quest to the player."""
    # Importing UI here to avoid circular dependency at top level
    from ui import UI 
    
    UI.print_subheading(f"Quest Completed: {quest.title}!")
    UI.slow_print("You have received your rewards:")

    for reward_type, reward_value in quest.reward.items():
        if reward_type == "gold":
            player.stats.gold += reward_value
            UI.print_success(f"- {reward_value} Gold.")
        elif reward_type == "experience":
            player.gain_experience(reward_value) # Player method to gain XP
            UI.print_success(f"- {reward_value} Experience.")
        elif reward_type == "item" and isinstance(reward_value, Item):
            if player.add_item(reward_value):
                UI.print_success(f"- {reward_value.name} (Item).")
            else:
                UI.print_warning(f"- You found {reward_value.name}, but your inventory is full!")
        elif reward_type == "reputation":
            # This would integrate with a future reputation system
            UI.print_success(f"- {reward_value} Reputation with local factions.")
        elif reward_type == "favor":
            # This would integrate with a future favor system
            UI.print_success(f"- A favor {reward_value}.")
    
    UI.press_enter()