# quests.py
import random
from typing import List, Dict, Any, Optional
from locations import LOCATIONS # Assuming LOCATIONS is fully defined here
import tags
import flavor
from items import Item, generate_random_item as gr_item_func, generate_item_from_key
from ui import UI  # Ensure UI is imported for capitalization


# Constant defined for quest rewards
QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item_quality_levels": {
        (1, 5): ["common", "uncommon"],
        (6, 10): ["uncommon", "rare"],
        (11, 20): ["uncommon", "epic"],
        (21, 99): ["epic", "legendary"] # Adjusted max level range for epic/legendary
    },
    "reputation": {"min": 5, "max": 15},
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold", "with Thieves Guild", "with Companions", "with Imperial Legion", "with Stormcloaks", "with a Daedric Prince (minor)"]
}


# Helper function to find locations by tag (from your original code)
def find_locations_by_tag(tag: str) -> List[Dict]:
    """
    Recursively searches the LOCATIONS data structure for locations that have the specified tag.
    Returns a list of matching location dictionaries, including parent names for sub-locations.
    """
    matching = []
    for loc in LOCATIONS:
        if tag in loc.get("tags", []):
            matching.append(loc)
        for sub in loc.get("sub_locations", []):
            if tag in sub.get("tags", []):
                sub_copy = sub.copy()
                sub_copy["parent_name"] = loc["name"]
                matching.append(sub_copy)
            for sub2 in sub.get("sub_locations", []):
                if tag in sub2.get("tags", []):
                    sub2_copy = sub2.copy()
                    sub2_copy["parent_name"] = f'{loc["name"]} -> {sub["name"]}'
                    matching.append(sub2_copy)
    return matching

# Helper to get NPC name by role hint (from your original code)
def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    """
    Retrieves a random NPC name and its unique ID from NAME_POOLS based on a role hint.
    Prioritizes specific IDs if the hint matches a known NPC.
    """
    from npc import NAME_POOLS
    # Check if the role_hint directly matches a known unique_id pattern
    # This is a simplification; in a real game, you'd have a global NPC instance registry
    # For now, we'll try to find a matching ID in NAME_POOLS.
    for race_data in NAME_POOLS.values():
        for name_type_data in race_data.values():
            for gender_name_list in name_type_data.values():
                for name_id in gender_name_list:
                    # If the role hint is something like "runil_priest_of_arkay", try to match it
                    if name_id.startswith(role_hint.lower().replace(" ", "_")):
                        return {"name": name_id.split('_')[0].capitalize(), "id": name_id}

    # Fallback to general role-based name generation if specific ID not found or not a direct NPC ID
    # This part should ideally be in npc.py, but for dynamic quest generation, it's here.
    random_race = random.choice(list(NAME_POOLS.keys()))
    random_gender = random.choice(["male", "female"])

    name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, None)
    if not name_pool_entry:
        name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"] # Default to Nord commoner male

    chosen_name_with_id = random.choice(name_pool_entry)
    name_display = chosen_name_with_id.split('_')[0].capitalize()

    return {"name": name_display, "id": chosen_name_with_id}

# Generate reward (from your original code)
def generate_reward(player_level: int, quest_tags: List[str]) -> Dict[str, Any]:
    """
    Generates a dictionary of rewards (gold, experience, items, reputation, favor)
    based on player level and quest tags.
    """
    reward: Dict[str, Any] = {}

    # Base gold reward scaled by player level
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level,
                                     QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)

    # Chance for experience reward
    if random.random() < 0.7:
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level,
                                               QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)

    # Determine item quality based on player level
    chosen_item_quality = "common"
    for level_range, qualities in QUEST_REWARDS_TEMPLATE["item_quality_levels"].items():
        if level_range[0] <= player_level <= level_range[1]:
            chosen_item_quality = random.choice(qualities)
            break

    # Chance for an item reward
    if random.random() < 0.4:
        # Generate a random item, possibly influenced by quest_tags for lore-friendliness
        # (This is a conceptual improvement, requires more logic in generate_random_item)
        reward_item = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level)
        reward["item"] = reward_item

    # Chance for additional reward types (reputation, favor)
    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if
                               rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3:
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list):
            reward[chosen_type] = random.choice(value_source) # Using random.choice for list
        else:
            reward[chosen_type] = random.randint(value_source["min"], value_source["max"])

    return reward

# Quest class (Enhanced)
class Quest:
    """
    Represents a multi-stage quest with objectives, rewards, and optional branching paths.
    """
    def __init__(self, title: str, description: str, reward: Dict[str, Any], level_requirement: int,
                 location: Dict[str, Any],
                 stages: List[Dict[str, Any]], # List of dictionaries, each dict represents a quest stage
                 quest_id: str | None = None, status: str = "active", turn_in_npc_id: str | None = None,
                 tags: Dict[str, Any] | None = None,
                 initial_flavor_text: str = ""
                 ):
        self.quest_id = quest_id or f"quest_{random.randint(1000, 9999)}" # Use string ID for templates
        self.title = title
        self.description = description # Overall quest description
        self.reward = reward
        self.level_requirement = level_requirement
        self.location = location # Primary location associated with the quest
        self.stages = stages # List of dictionaries, each dict represents a quest stage
        self.current_stage_index = 0
        self.status = status # active, completed, failed, available, unavailable
        self.turn_in_npc_id = turn_in_npc_id # NPC ID to turn in the quest to
        self.tags = tags if tags else {} # Tags for filtering and flavor
        self.initial_flavor_text = initial_flavor_text

        # Track progress for current stage's objectives
        self.current_stage_progress: Dict[str, Any] = {}
        self._initialize_stage_progress()

        self.add_tag("quest", "type", "generic") # Default tag

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        """Adds a tag to the quest instance."""
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

    def _initialize_stage_progress(self) -> None:
        """Initializes tracking for the current stage's objectives."""
        if self.current_stage_index < len(self.stages):
            current_stage = self.stages[self.current_stage_index]
            for obj in current_stage.get("objectives", []):
                obj_id = obj.get("id", f"obj_{random.randint(1,1000)}") # Ensure unique ID for objective
                self.current_stage_progress[obj_id] = {"met": False, "current_count": 0}

    @property
    def current_stage(self) -> Optional[Dict[str, Any]]:
        """Returns the current active quest stage."""
        if self.current_stage_index < len(self.stages):
            return self.stages[self.current_stage_index]
        return None

    def check_objective_met(self, objective: Dict[str, Any], player: Any) -> bool:
        """
        Checks if a single objective is met based on player's current state.
        Updates the internal progress tracker for this objective.
        """
        obj_type = objective["type"]
        obj_id = objective.get("id")
        if not obj_id or obj_id not in self.current_stage_progress:
            # Handle newly added objectives dynamically, or ignore if not tracked
            self.current_stage_progress[obj_id] = {"met": False, "current_count": 0}

        if self.current_stage_progress[obj_id]["met"]:
            return True # Already met

        if obj_type == "kill":
            target_id = objective["target_id"]
            required_count = objective["count"]
            current_count = player.defeated_enemies_tracker.get(target_id, 0)
            self.current_stage_progress[obj_id]["current_count"] = current_count
            if current_count >= required_count:
                self.current_stage_progress[obj_id]["met"] = True
                return True
            return False

        elif obj_type == "collect_item":
            item_key = objective["item_key"]
            required_count = objective["count"]
            current_count = sum(1 for item in player.stats.inventory if item.name.lower().replace(' ', '_') == item_key.lower().replace(' ', '_'))
            self.current_stage_progress[obj_id]["current_count"] = current_count
            if current_count >= required_count:
                self.current_stage_progress[obj_id]["met"] = True
                return True
            return False

        elif obj_type == "reach_location":
            location_name = objective["location_name"]
            # Check if player is currently in the location OR if it's a known location
            if (player.current_location_obj and player.current_location_obj["name"].lower() == location_name.lower()) or \
               any(loc_obj["name"].lower() == location_name.lower() for loc_obj in player.known_locations_objects):
                self.current_stage_progress[obj_id]["met"] = True
                return True
            return False

        elif obj_type == "talk_to_npc":
            npc_id = objective["npc_id"]
            if npc_id in player.talked_to_npcs:
                self.current_stage_progress[obj_id]["met"] = True
                return True
            return False

        elif obj_type in ["skill_check", "choice", "protect", "destroy", "craft", "confront", "track", "investigate", "use_item", "repair", "sell_item", "event_trigger"]:
            # These objectives are typically marked as met by external game logic (e.g., player action, event system).
            # This function simply reflects their current 'met' status.
            return self.current_stage_progress[obj_id]["met"]

        return False

    def check_all_current_stage_objectives_met(self, player: Any) -> bool:
        """Checks if all primary objectives for the current stage are met. Ignores 'optional' objectives."""
        if not self.current_stage:
            return False

        all_primary_objectives_met = True
        for obj in self.current_stage.get("objectives", []):
            if obj.get("type") == "optional": # Skip optional objectives for stage completion check
                continue
            obj_id = obj.get("id")
            if not obj_id or not self.current_stage_progress.get(obj_id, {}).get("met"):
                all_primary_objectives_met = False
                break
        return all_primary_objectives_met

    def advance_quest_stage(self) -> bool:
        """Advances the quest to the next stage."""
        if self.current_stage_index + 1 < len(self.stages):
            self.current_stage_index += 1
            UI.print_system_message(f"Quest '{self.title}' has advanced to Stage {self.current_stage_index + 1}!")
            self._initialize_stage_progress() # Re-initialize progress for new stage
            return True
        else:
            self.status = "completed"
            UI.print_system_message(f"All stages for quest '{self.title}' are complete. Return to your quest giver to turn it in!")
            return False

    def fail_quest(self, reason: str = "unknown") -> None:
        """Marks the quest as failed."""
        self.status = "failed"
        UI.print_system_message(f"Quest '{self.title}' has FAILED due to: {reason}.")
        # Additional logic for consequences of failure can be added here (e.g., reputation loss)

    def __str__(self) -> str:
        """Returns a formatted string representation of the quest for display."""
        reward_str_parts = []
        for key, value in self.reward.items():
            if isinstance(value, Item):
                reward_str_parts.append(f"{value.name} (Item)")
            else:
                reward_str_parts.append(f"{value} {key.capitalize()}")
        reward_display = ", ".join(reward_str_parts)

        objectives_display = []
        current_stage_objectives = self.current_stage.get("objectives", []) if self.current_stage else []
        for obj in current_stage_objectives:
            obj_note = obj.get("note", f"Complete {obj['type']} objective.")
            progress_str = ""
            if "count" in obj and (obj.get("type") == "kill" or obj.get("type") == "collect_item"): # Only for count-based objectives
                current_count = self.current_stage_progress.get(obj.get("id"), {}).get("current_count", 0)
                if not self.current_stage_progress.get(obj.get("id"), {}).get("met"):
                    progress_str = f" ({current_count}/{obj['count']})"
                else:
                    progress_str = " (Completed)"
            elif self.current_stage_progress.get(obj.get("id"), {}).get("met"):
                progress_str = " (Completed)" # For non-count objectives once met
            
            # Indicate optional objectives
            status_prefix = "[ ]"
            if self.current_stage_progress.get(obj.get("id"), {}).get("met"):
                status_prefix = "[X]"
            if obj.get("type") == "optional":
                status_prefix += " (Optional)"

            objectives_display.append(f"  {status_prefix} {obj_note}{progress_str}")

        flavor_texts = flavor.get_flavor(self)
        flavor_display = f"\n  Lore: {' '.join(flavor_texts)}" if flavor_texts else ""

        status_display = self.status.capitalize()
        if self.status == "completed" and self.turn_in_npc_id:
            status_display += " (Ready for Turn-in)"

        full_description = f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at {self.location.get('name', 'Unknown')}\n" \
                           f"Status: {status_display} | Stage: {self.current_stage_index + 1}/{len(self.stages) if self.stages else 1}\n" \
                           f"Overall: {self.description}\n" \
                           f"Current Tasks:\n" + "\n".join(objectives_display) + \
                           f"\nReward: {reward_display}" + \
                           flavor_display
        return full_description

# QuestLog class (from your original code, adapted for new Quest class)
class QuestLog:
    """
    Manages the player's active, completed, and failed quests.
    """
    def __init__(self):
        self.active_quests: List[Quest] = []
        self.completed_quests: List[Quest] = []
        self.failed_quests: List[Quest] = []

    def add_quest(self, quest: Quest) -> bool:
        """Adds a quest to the active quest log if not already present."""
        if quest.quest_id not in [q.quest_id for q in self.active_quests] and \
           quest.quest_id not in [q.quest_id for q in self.completed_quests] and \
           quest.quest_id not in [q.quest_id for q in self.failed_quests]:
            self.active_quests.append(quest)
            UI.print_system_message(f"New quest added: '{quest.title}'! Check your journal.")
            return True
        return False

    def remove_quest(self, quest_id: str) -> bool:
        """Removes a quest from active and moves it to completed/failed lists."""
        quest_to_remove = next((q for q in self.active_quests if q.quest_id == quest_id), None)
        if quest_to_remove:
            self.active_quests.remove(quest_to_remove)
            if quest_to_remove.status == "completed":
                self.completed_quests.append(quest_to_remove)
            elif quest_to_remove.status == "failed":
                self.failed_quests.append(quest_to_remove)
            return True
        return False

    def get_quest_by_id(self, quest_id: str) -> Quest | None:
        """Retrieves a quest by its ID from any list."""
        for q in self.active_quests:
            if q.quest_id == quest_id:
                return q
        for q in self.completed_quests:
            if q.quest_id == quest_id:
                return q
        for q in self.failed_quests:
            if q.quest_id == quest_id:
                return q
        return None

    def list_quests(self) -> List[Quest]:
        """Returns a combined list of all quests."""
        return self.active_quests + self.completed_quests + self.failed_quests

    def get_quests_for_turn_in(self, npc_id: str) -> List[Quest]:
        """Returns a list of completed quests ready to be turned in to a specific NPC."""
        return [q for q in self.active_quests if q.status == "completed" and q.turn_in_npc_id == npc_id]

# Utility function (from your original code)
def list_player_quests_for_display(player: Any) -> List[Quest]:
    """Returns all quests from the player's quest log for display purposes."""
    if hasattr(player, 'quest_log') and player.quest_log:
        return player.quest_log.list_quests()
    return []

# DummyRumor class for flavor tag compatibility (from your original code)
class DummyRumor:
    """A dummy class to hold tags for flavor text generation."""
    def __init__(self):
        self.tags = {}

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

# =================================================================================================================
# EXPANDED AND REFINED QUEST TEMPLATES FOR DEEPER LORE AND GAMEPLAY
# =================================================================================================================

QUEST_TEMPLATES = [
    # =============================================================================================================
    # GENERAL / INTRODUCTORY QUESTS (Can appear early, less location-specific)
    # =============================================================================================================
    {
        "id": "clear_bandit_camp",
        "title_template": "The Shadowed Road: Clearing [LOCATION_NAME]",
        "desc_template": "A vile band of cutthroats has established a menacing camp near **[LOCATION_NAME]**, choking the life out of trade routes and terrorizing honest travelers. The local populace lives in fear. You must venture forth, eliminate their ruthless leader, and scatter their ranks to restore peace to these lands.",
        "lore_tags": ["bandits", "road_safety", "road_danger", "wilderness_threat"],
        "location_tags_required": ["camp", "bandit", "ruin", "wilderness"],
        "level_range": (1, 5),
        "flavor_tags": {"quest": {"type": ["hunt", "clear", "protection"], "difficulty": ["easy", "medium"], "moral": ["ethical", "just"]}},
        "turn_in_role_hint": ["guard", "merchant", "jarl", "caravan_master"],
        "stages": [
            {
                "stage_name": "Reclaim the Road",
                "objectives": [
                    {"id": "obj_bandit_leader", "type": "kill", "target_name": "bandit", "target_id": "bandit_leader", "count": 1, "note": "Silence the **bandit leader**, the architect of this misery."},
                    {"id": "obj_bandit_thugs", "type": "kill", "target_name": "bandit", "target_id": "bandit_thug", "count": 3, "note": "Cull the remaining **bandit thugs** to break their stranglehold."},
                    {"id": "obj_bandit_missive_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "bandit_missive", "count": 1, "note": " (Optional) Seek out any incriminating **documents or hidden plans** among their belongings. Who truly backs these ruffians?"}}
                ],
                "on_completion_dialogue": "The air in the camp is still, save for the whisper of the wind. The road to [LOCATION_NAME] is clear. You should carry word of your success to [QUEST_GIVER_NAME]; they await news anxiously.",
                "branch_options": []
            }
        ]
    },
    {
        "id": "wolf_infestation",
        "title_template": "The Howling Scourge of [FARM_NAME]",
        "desc_template": "A terrifying infestation of bloodthirsty wolves has descended upon **[FARM_NAME]**, a solitary homestead nestled near **[LOCATION_NAME]**. Their relentless attacks have decimated livestock and instilled terror in the farmer's heart. You must aid them in protecting their remaining animals and eradicate this savage threat from the wilds.",
        "lore_tags": ["wolves", "farm", "protection", "rural_life", "wilderness_danger", "survival"],
        "location_tags_required": ["farm", "rural", "village"],
        "level_range": (2, 6),
        "flavor_tags": {"quest": {"type": ["hunt", "defend", "aid"], "moral": ["ethical", "compassionate"], "urgency": ["important", "immediate"]}},
        "turn_in_role_hint": ["farmer", "villager", "steward"],
        "stages": [
            {
                "stage_name": "Silence the Predator's Call",
                "objectives": [
                    {"id": "obj_kill_wolves", "type": "kill", "target_name": "wolf", "target_id": "wolf_alpha", "count": 5, "note": "Silence the **howling pack** that plagues the farm. Fewer wolves mean safer herds."},
                    {"id": "obj_protect_livestock", "type": "protect", "object": "livestock", "count": 2, "note": "Stand guard and **ensure the safety of the farmer's precious livestock**. Be ready; the wolves may strike again."} # This objective might require a trigger from game logic
                ],
                "on_completion_dialogue": "The sounds of the pack have faded into the quiet wilderness. The immediate threat to the farm is lifted, and a relieved sigh escapes the farmer. Report your success to [QUEST_GIVER_NAME].",
                "branch_options": []
            },
            {
                "stage_name": "Optional: A Stronger Defense",
                "objectives": [
                    {"id": "obj_craft_wolf_traps", "type": "optional", "objective": {"type": "craft", "item_key": "wolf_trap", "count": 3, "note": " (Optional) Forge and strategically place **wolf traps** around the farm's perimeter to deter future attacks. This requires a keen eye and skill in smithing or woodcutting."}}
                ],
                "on_completion_dialogue": "With the traps expertly set, the farmer expresses profound gratitude. This extra measure of security brings them true peace of mind. Your foresight and dedication will not be forgotten.",
                "reward_modifier": {"reputation_local_bonus": 5, "gold_bonus": 50}, # Specific reputation gain
                "optional_completion_stage": True # Indicate this stage is optional for overall quest completion
            }
        ]
    },
    {
        "id": "the_missing_farmer",
        "title_template": "The Empty Plow: The Missing Farmer of [FARM_NAME]",
        "desc_template": "Panic grips the humble homestead of **[FARM_NAME]**. Old Man Theron (or a similar placeholder), a beloved farmer, has vanished without a trace after venturing into the perilous **[WILDERNESS_TYPE]** to gather essential supplies. His worried family fears the worst. You are implored to track his path, discover his fate, and ensure his safe return to his distraught kin.",
        "lore_tags": ["farmer", "missing_person", "wilderness", "rural_danger", "rescue", "humanitarian"],
        "location_tags_required": ["farm", "rural", "wilderness"],
        "level_range": (1, 6),
        "flavor_tags": {"quest": {"type": ["search", "rescue", "aid"], "moral": ["ethical", "compassionate"], "urgency": ["urgent", "desperate"]}},
        "turn_in_role_hint": ["farmer_spouse", "villager_elder", "local_guard"],
        "stages": [
            {
                "stage_name": "Search the Wilderness",
                "objectives": [
                    {"id": "obj_search_area", "type": "investigate", "location_name": "[WILDERNESS_TYPE]", "note": "Search the specified wilderness area for signs of the missing farmer (Survival check DC 10)."},
                    {"id": "obj_find_clue", "type": "collect_item", "item_key": "torn_clothing_fragment", "count": 1, "note": "Find a clue indicating the farmer's direction or what happened."}
                ],
                "on_completion_dialogue": "You've found a chilling trail. It seems the farmer was dragged away into a dark, nearby **[CAVE_TYPE]**! His fate hangs in the balance.",
                "branch_options": []
            },
            {
                "stage_name": "A Desperate Rescue",
                "objectives": [
                    {"id": "obj_reach_lair", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Brave the gloom and enter the **[CAVE_TYPE]** where the farmer was taken captive. Prepare for a confrontation."},
                    {"id": "obj_kill_captor", "type": "kill", "target_name": "bandit", "target_id": "bandit_thug", "count": 2, "note": "Overwhelm and **defeat the vile captors** holding the innocent farmer hostage."},
                    {"id": "obj_talk_to_farmer", "type": "talk_to_npc", "npc_id": "missing_farmer_ID", "note": "Speak to the **rescued farmer** to ensure he is safe and uninjured."}
                ],
                "on_completion_dialogue": "The farmer, though shaken and bruised, is safe thanks to your swift intervention. A wave of immense relief washes over him. Now, escort him back to the warmth and safety of his home.",
                "reward_modifier": {"reputation_local": 10, "gold_bonus": 75},
                "final_stage": True
            }
        ]
    },
    {
        "id": "the_plague_of_rats",
        "title_template": "The Gnawing Menace: Plague of [CITY_NAME] Sewers",
        "desc_template": "A grotesque **swarm of giant rats** has erupted from the putrid depths of the sewers, infesting the lower districts of **[CITY_NAME]**. Their relentless scuttling spreads disease, gnaws through provisions, and sows chaos among the terrified populace. You are needed to descend into the festering darkness, eliminate the heart of this infestation, and cleanse the city of this vile plague.",
        "lore_tags": ["city", "plague", "pest_control", "sewers", "disease", "urban_threat", "sanitation"],
        "location_tags_required": ["city", "sewers", "underground"],
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["hunt", "clear", "cleansing"], "moral": ["ethical", "public_service"], "urgency": ["urgent", "spreading_threat"]}},
        "turn_in_role_hint": ["guard_captain", "city_official", "healer", "head_of_sanitation"],
        "stages": [
            {
                "stage_name": "Into the Stench",
                "objectives": [
                    {"id": "obj_reach_sewers", "type": "reach_location", "location_name": "[CITY_NAME] Sewers", "note": "Brave the foul air and dripping darkness to **venture into the infested sewers** beneath [CITY_NAME]. The source of the plague awaits."}
                ],
                "on_completion_dialogue": "The stench of decay and vermin assaults your senses. You've found their gnawing, squealing lair. The true horror of the infestation reveals itself.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Underbelly",
                "objectives": [
                    {"id": "obj_kill_rats", "type": "kill", "target_name": "giant rat", "target_id": "giant_rat", "count": 20, "note": "Relentlessly **cull the swarming population of giant rats**. Leave no corner untouched."},
                    {"id": "obj_destroy_nests", "type": "destroy", "object": "rat_nest", "count": 5, "note": "Locate and **destroy the vile rat nests** to prevent further breeding and resurgence of the plague."},
                    {"id": "obj_collect_poison_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "rat_poison_ingredients", "count": 3, "note": " (Optional) Gather specific, noxious herbs and fungi to **create a stronger rat poison**, ensuring their complete eradication. (Requires Alchemy check)."}}
                ],
                "on_completion_dialogue": "The horrifying squealing has ceased, replaced by an unsettling quiet. The sewers are largely clear, their foul occupants reduced to lifeless piles. You have done the city a great service. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 100, "experience_bonus": 50, "reputation_local_bonus": 10},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # WHITERUN HOLD QUESTS (Commerce, Companions, Plains, Imperial/Nordic balance)
    # =============================================================================================================
    {
        "id": "whiterun_lost_shipment_investigation",
        "title_template": "The Missing Caravan from Whiterun",
        "desc_template": "A merchant caravan carrying valuable goods from Whiterun has gone missing on the plains. Investigate its disappearance and recover what you can.",
        "lore_tags": ["whiterun", "commerce", "trade", "plains", "investigation"],
        "location_tags_required": ["whiterun", "plains", "trade"],
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["investigate", "fetch"], "difficulty": ["medium"], "moral": ["ethical"]}},
        "turn_in_role_hint": ["merchant", "guard", "jarl"],
        "stages": [
            {
                "stage_name": "Search the Plains",
                "objectives": [
                    {"id": "obj_search_plains", "type": "investigate", "location_name": "Whiterun Hold", "note": "Search the plains outside Whiterun for signs of the missing caravan (Survival check DC 12)."},
                    {"id": "obj_find_wreckage", "type": "reach_location", "location_name": "Caravan Wreckage Site", "note": "Locate the wreckage of the caravan."}
                ],
                "on_completion_dialogue": "You find the remains of the caravan, clearly ambushed. Bandits, perhaps? Or something worse... A survivor might still be here.",
                "branch_options": []
            },
            {
                "stage_name": "Uncover the Truth",
                "objectives": [
                    {"id": "obj_talk_survivor", "type": "talk_to_npc", "npc_id": "caravan_survivor_ID", "note": "Speak to the lone, injured survivor of the attack."},
                    {"id": "obj_collect_manifest", "type": "collect_item", "item_key": "caravan_manifest", "count": 1, "note": "Retrieve the caravan's manifest from the wreckage."}
                ],
                "on_completion_dialogue": "The survivor points to a nearby cave, [CAVE_TYPE], as the raiders' lair. They were not bandits, but a strange cult seeking specific artifacts listed on the manifest. You have a choice: pursue the cult or report back to the merchant.",
                "branch_options": [
                    {"choice_id": "pursue_cult", "text": "Pursue the cult to recover the artifacts.", "next_stage_index": 2},
                    {"choice_id": "report_back", "text": "Report back to [QUEST_GIVER_NAME] with the manifest and survivor's tale.", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Pursue Cult
                "stage_name": "Confront the Cult",
                "objectives": [
                    {"id": "obj_reach_cult_lair", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Infiltrate the cult's lair."},
                    {"id": "obj_kill_cult_leader", "type": "kill", "target_name": "cultist", "target_id": "cult_leader", "count": 1, "note": "Defeat the cult leader."},
                    {"id": "obj_recover_artifacts", "type": "collect_item", "item_key": "stolen_cult_artifact", "count": 3, "note": "Recover the stolen artifacts."}
                ],
                "on_completion_dialogue": "The cult is dispersed, and the artifacts are retrieved. You now have a choice: return them to the merchant, or seek a scholar at the College of Winterhold who might pay more for them.",
                "branch_options": [
                    {"choice_id": "return_to_merchant", "text": "Return artifacts to [QUEST_GIVER_NAME].", "next_stage_index": 4},
                    {"choice_id": "seek_scholar", "text": "Seek a scholar at the College of Winterhold.", "next_stage_index": 5}
                ]
            },
            { # Stage 3: Report Back (Early Completion)
                "stage_name": "Report Findings",
                "objectives": [
                    {"id": "obj_report_to_giver", "type": "talk_to_npc", "npc_id": "[QUEST_GIVER_ID]", "note": "Report your findings to [QUEST_GIVER_NAME]."}
                ],
                "on_completion_dialogue": "You've provided crucial information, though the goods remain lost. [QUEST_GIVER_NAME] thanks you for your honesty.",
                "reward_modifier": {"gold_bonus": 50, "reputation_merchant_guild": 5},
                "final_stage": True,
                "failure_state": True # Considered a "partial success" or "failure" for full recovery
            },
            { # Stage 4: Return to Merchant (Full Reward)
                "stage_name": "Return Artifacts to Merchant",
                "objectives": [
                    {"id": "obj_return_artifacts_merchant", "type": "talk_to_npc", "npc_id": "[QUEST_GIVER_ID]", "note": "Return the recovered artifacts to [QUEST_GIVER_NAME]."}
                ],
                "on_completion_dialogue": "The merchant is overjoyed! These artifacts are more valuable than the original goods. Your efforts are greatly appreciated.",
                "reward_modifier": {"gold_bonus": 300, "experience_bonus": 150, "reputation_merchant_guild": 15, "item_bonus": "rare_trade_item"},
                "final_stage": True
            },
            { # Stage 5: Seek Scholar (Alternative Reward)
                "stage_name": "Seek Scholar at College",
                "objectives": [
                    {"id": "obj_reach_college", "type": "reach_location", "location_name": "College of Winterhold", "note": "Travel to the College of Winterhold."},
                    {"id": "obj_talk_scholar_artifacts", "type": "talk_to_npc", "npc_id": "college_scholar_ID", "note": "Present the artifacts to a scholar at the College."}
                ],
                "on_completion_dialogue": "The scholar is fascinated by the artifacts' unique properties and offers a generous sum, along with some arcane knowledge.",
                "reward_modifier": {"gold_bonus": 400, "experience_bonus": 200, "reputation_college_of_winterhold": 10, "item_bonus": "apprentice_tome_random"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "whiterun_companions_initiation",
        "title_template": "Proving Your Worth to the Companions",
        "desc_template": "The Companions of Jorrvaskr in Whiterun seek new recruits. Prove your strength and loyalty by undertaking a task for them, perhaps clearing a local beast den or recovering a lost weapon.",
        "lore_tags": ["whiterun", "companions_guild", "warrior_guild", "honor"],
        "location_tags_required": ["whiterun", "meadhall", "companions_guild"],
        "level_range": (1, 4),
        "flavor_tags": {"quest": {"type": ["hunt", "trial"], "difficulty": ["easy"], "moral": ["ethical"]}},
        "turn_in_role_hint": ["companion_warrior"],
        "stages": [
            {
                "stage_name": "Seek Out the Companions",
                "objectives": [
                    {"id": "obj_reach_jorrvaskr", "type": "reach_location", "location_name": "Jorrvaskr", "note": "Travel to Jorrvaskr in Whiterun."},
                    {"id": "obj_talk_kodlak", "type": "talk_to_npc", "npc_id": "kodlak_whitemane_ID", "note": "Speak to Kodlak Whitemane, the Harbinger of the Companions."}
                ],
                "on_completion_dialogue": "Kodlak has a task for you: clear out a troublesome [BEAST_DEN_TYPE] near [LOCATION_NAME]. A simple test of your mettle.",
                "branch_options": []
            },
            {
                "stage_name": "Clear the Beast Den",
                "objectives": [
                    {"id": "obj_reach_den", "type": "reach_location", "location_name": "[BEAST_DEN_NAME]", "note": "Journey to the beast den."},
                    {"id": "obj_kill_beasts", "type": "kill", "target_name": "wolf", "target_id": "wolf_alpha", "count": 3, "note": "Eliminate the beasts within the den."},
                    {"id": "obj_collect_trophy", "type": "collect_item", "item_key": "beast_fang_trophy", "count": 1, "note": "Collect a trophy as proof of your success."}
                ],
                "on_completion_dialogue": "The den is clear. The beasts are no more. Return to Jorrvaskr with your trophy.",
                "reward_modifier": {"reputation_companions": 10, "gold_bonus": 80, "item_bonus": "steel_sword"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # THE PALE QUESTS (Mining, Cold, Stormcloak leaning, Nightmares, Vaermina)
    # =============================================================================================================
    {
        "id": "pale_nightmare_investigation",
        "title_template": "The Whispering Dreams of Dawnstar",
        "desc_template": "The residents of Dawnstar are plagued by terrible nightmares. Investigate the cause of these unsettling dreams, which some attribute to the abandoned Nightcaller Temple.",
        "lore_tags": ["pale", "dawnstar", "nightmares", "vaermina", "daedric_influence", "mystery"],
        "location_tags_required": ["dawnstar", "temple_sealed", "daedric_influence_vaermina"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "supernatural"], "difficulty": ["hard"], "moral": ["ethical", "gray"], "urgency": ["urgent"]}},
        "turn_in_role_hint": ["jarl", "priest", "scholar"],
        "stages": [
            {
                "stage_name": "Gather Information in Dawnstar",
                "objectives": [
                    {"id": "obj_talk_jarl_dawnstar", "type": "talk_to_npc", "npc_id": "jarl_skald_ID", "note": "Speak to Jarl Skald the Elder about the nightmares."},
                    {"id": "obj_talk_innkeeper_dawnstar", "type": "talk_to_npc", "npc_id": "innkeeper_windpeak_ID", "note": "Gather rumors from the Windpeak Inn about the dreams."}
                ],
                "on_completion_dialogue": "The Jarl and locals confirm the nightmares are widespread and point to Nightcaller Temple as the source. A priestess of Mara might know more about such dark magic.",
                "branch_options": []
            },
            {
                "stage_name": "Investigate Nightcaller Temple",
                "objectives": [
                    {"id": "obj_reach_nightcaller", "type": "reach_location", "location_name": "Nightcaller Temple", "note": "Travel to the eerie Nightcaller Temple overlooking Dawnstar."},
                    {"id": "obj_find_entrance", "type": "investigate", "location_name": "Nightcaller Temple", "note": "Find a way to enter the sealed temple (Lockpicking check DC 15)."},
                    {"id": "obj_deal_with_cultists", "type": "kill", "target_name": "vaermina cultist", "target_id": "vaermina_cultist", "count": 5, "note": "Deal with the cultists within the temple."}
                ],
                "on_completion_dialogue": "You've entered the temple and cleared a path. The source of the nightmares is deeper within. A decision awaits: cleanse the temple or harness its power?",
                "branch_options": [
                    {"choice_id": "cleanse_temple", "text": "Cleanse the temple to end the nightmares (Ethical/Good).", "next_stage_index": 2},
                    {"choice_id": "harness_power", "text": "Harness the temple's power for yourself (Gray/Selfish).", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Cleanse Temple
                "stage_name": "Cleanse the Temple",
                "objectives": [
                    {"id": "obj_perform_cleansing", "type": "use_item", "item_key": "cleansing_ritual_scroll", "location_name": "Nightcaller Temple", "note": "Perform a cleansing ritual at the temple's core (Restoration/Willpower check DC 16)."},
                    {"id": "obj_defeat_boss_cleanse", "type": "kill", "target_name": "dream_corruptor", "target_id": "dream_corruptor_spirit", "count": 1, "note": "Defeat the lingering spirit of Vaermina's influence."}
                ],
                "on_completion_dialogue": "The nightmares cease. A quiet peace settles over Dawnstar. You feel a sense of righteous accomplishment. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_dawnstar": 20, "gold_bonus": 300, "experience_bonus": 200, "item_bonus": "amulet_of_mara"},
                "final_stage": True
            },
            { # Stage 3: Harness Power
                "stage_name": "Harness the Temple's Power",
                "objectives": [
                    {"id": "obj_perform_harnessing", "type": "use_item", "item_key": "power_siphon_tome", "location_name": "Nightcaller Temple", "note": "Perform a ritual to siphon the temple's power (Destruction/Conjuration check DC 18)."},
                    {"id": "obj_defeat_boss_harness", "type": "kill", "target_name": "vaermina_aspect", "target_id": "vaermina_aspect_shadow", "count": 1, "note": "Overcome the manifestation of the temple's power."}
                ],
                "on_completion_dialogue": "The temple's dark power is now yours to command, though its whispers may linger. You feel a surge of arcane might. Return to [QUEST_GIVER_NAME] (or keep the secret).",
                "reward_modifier": {"gold_bonus": 400, "experience_bonus": 250, "item_bonus": "staff_of_nightmares", "magicka_gain": 20},
                "final_stage": True,
                "failure_state": True # Can be considered a morally grey/failed outcome for the town
            }
        ]
    },
    {
        "id": "pale_ice_troll_hunt",
        "title_template": "The Ice Troll of [MOUNTAIN_NAME]",
        "desc_template": "A monstrous Ice Troll has made its lair in the mountains near [LOCATION_NAME], terrorizing travelers and hunters. Hunt down the beast and make the roads safe.",
        "lore_tags": ["pale", "troll", "hunt", "mountain", "cold"],
        "location_tags_required": ["mountain", "wilderness", "arctic"],
        "level_range": (5, 9),
        "flavor_tags": {"quest": {"type": ["hunt"], "difficulty": ["medium"], "moral": ["ethical"]}},
        "turn_in_role_hint": ["hunter", "guard"],
        "stages": [
            {
                "stage_name": "Track the Troll",
                "objectives": [
                    {"id": "obj_track_troll", "type": "track", "target_name": "ice troll", "note": "Follow the tracks of the Ice Troll into its mountain lair (Survival check DC 13)."},
                    {"id": "obj_reach_troll_lair", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Locate the Ice Troll's cave."}
                ],
                "on_completion_dialogue": "You've found the troll's lair. Its growls echo from within.",
                "branch_options": []
            },
            {
                "stage_name": "Slay the Beast",
                "objectives": [
                    {"id": "obj_kill_ice_troll", "type": "kill", "target_name": "ice troll", "target_id": "ice_troll_alpha", "count": 1, "note": "Slay the monstrous Ice Troll."},
                    {"id": "obj_collect_trophy_troll", "type": "collect_item", "item_key": "troll_skull_trophy", "count": 1, "note": "Collect a trophy as proof."}
                ],
                "on_completion_dialogue": "The Ice Troll is defeated. Its reign of terror is over. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 180, "experience_bonus": 100, "item_bonus": "frost_resist_potion"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # WINTERHOLD HOLD QUESTS (Magic, College, Ancient Ruins, Great Collapse)
    # =============================================================================================================
    {
        "id": "ancient_relic_retrieval",
        "title_template": "The Echoes of Saarthal",
        "desc_template": "An ancient Nordic relic has been reported deep within Saarthal. Retrieve the Glyph and return it to the College of Winterhold.",
        "lore_tags": ["saarthal", "ancient_nords", "magic", "mages_guild", "dungeon_exploration", "dragon_word_ancient"],
        "location_tags_required": ["barrow", "dungeon", "undead", "college"], # College implies importance
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["fetch", "investigate"], "difficulty": ["medium", "hard"], "urgency": ["important"]}},
        "turn_in_role_hint": ["scholar", "court_mage", "priest"],
        "stages": [
            {
                "stage_name": "Venture into Saarthal",
                "objectives": [
                    {"id": "obj_reach_saarthal", "type": "reach_location", "location_name": "Saarthal", "note": "Venture into the ancient ruins of Saarthal. Be wary of the restless dead."}
                ],
                "on_completion_dialogue": "You have entered Saarthal. The air here hums with ancient magic, and the shadows seem to move on their own...",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve the Glyph and Defeat its Guardian",
                "objectives": [
                    {"id": "obj_collect_glyph", "type": "collect_item", "item_key": "glyph_of_unraveling", "count": 1, "note": "Find the Glyph of Unraveling within Saarthal's depths."},
                    {"id": "obj_kill_draugr_overlord", "type": "kill", "target_name": "draugr death overlord", "target_id": "draugr_death_overlord", "count": 1, "note": "Defeat the powerful Draugr guarding the relic."},
                    {"id": "obj_saarthal_puzzle_optional", "type": "optional", "objective": {"type": "solve_puzzle", "object": "saarthal_puzzle", "note": " (Optional) Decipher and solve the ancient Nordic puzzle to unlock a hidden chamber containing additional lore."}}
                ],
                "on_completion_dialogue": "The Glyph of Unraveling is now yours, and its guardian defeated. It pulses with a strange energy. Return to [QUEST_GIVER_NAME] at the College of Winterhold.",
                "reward_modifier": {"reputation_college_of_winterhold": 15, "gold_bonus": 250, "experience_bonus": 150, "item_bonus": "apprentice_tome_random"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "winterhold_college_research_materials",
        "title_template": "Rare Arcane Reagents",
        "desc_template": "A Master Wizard at the College of Winterhold requires rare arcane reagents from the treacherous Hob's Fall Cave for a delicate experiment. Retrieve them for a handsome reward.",
        "lore_tags": ["winterhold", "college", "magic", "alchemy", "necromancy_potential"],
        "location_tags_required": ["college", "cave", "necromancer_lair_potential"],
        "level_range": (8, 14),
        "flavor_tags": {"quest": {"type": ["fetch"], "difficulty": ["medium", "hard"], "moral": ["ethical"]}},
        "turn_in_role_hint": ["college_mage", "scholar"],
        "stages": [
            {
                "stage_name": "Enter Hob's Fall Cave",
                "objectives": [
                    {"id": "obj_reach_hobs_fall", "type": "reach_location", "location_name": "Hob's Fall Cave", "note": "Travel to Hob's Fall Cave, a known haunt of necromancers."}
                ],
                "on_completion_dialogue": "The cave is dark and reeks of death. You hear unsettling whispers...",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve Reagents and Deal with Necromancers",
                "objectives": [
                    {"id": "obj_collect_reagents", "type": "collect_item", "item_key": "glowing_fungus_rare", "count": 5, "note": "Collect the rare glowing fungus and other reagents."},
                    {"id": "obj_kill_necromancers", "type": "kill", "target_name": "necromancer", "target_id": "necromancer_apprentice", "count": 3, "note": "Neutralize the necromancers defiling the cave."}
                ],
                "on_completion_dialogue": "You have the reagents, and the necromancers are dealt with. Return to [QUEST_GIVER_NAME] at the College.",
                "reward_modifier": {"reputation_college_of_winterhold": 12, "gold_bonus": 300, "experience_bonus": 180, "item_bonus": "enchanted_ring_magicka"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # HJAALMARCH QUESTS (Marsh, Superstition, Vampires, Ustengrav)
    # =============================================================================================================
    {
        "id": "hjaalmarch_vampire_investigation",
        "title_template": "The Shadow Over Morthal",
        "desc_template": "Strange deaths and whispers of vampirism plague Morthal. Investigate the unsettling occurrences and uncover the truth behind the shadow creeping over the marsh.",
        "lore_tags": ["hjaalmarch", "morthal", "vampire", "superstition", "mystery"],
        "location_tags_required": ["morthal", "marsh", "vampire_rumors"],
        "level_range": (6, 11),
        "flavor_tags": {"quest": {"type": ["investigate"], "difficulty": ["medium", "hard"], "moral": ["ethical"], "urgency": ["urgent"]}},
        "turn_in_role_hint": ["jarl", "healer", "citizen"],
        "stages": [
            {
                "stage_name": "Gather Clues in Morthal",
                "objectives": [
                    {"id": "obj_talk_jarl_morthal", "type": "talk_to_npc", "npc_id": "jarl_idgrod_ID", "note": "Speak to Jarl Idgrod Ravencrone about the nightmares."},
                    {"id": "obj_investigate_burned_house", "type": "investigate", "location_name": "Burned House", "note": "Examine the recently burned house for clues (Investigation check DC 14)."},
                    {"id": "obj_talk_falion", "type": "talk_to_npc", "npc_id": "falion_wizard_ID", "note": "Consult Falion, Morthal's wizard, about the nature of the evil."}
                ],
                "on_completion_dialogue": "Falion confirms your fears: a powerful vampire is responsible, hiding in Movarth's Lair. He offers a way to deal with it, but you'll need to be prepared.",
                "branch_options": []
            },
            {
                "stage_name": "Confront the Vampire",
                "objectives": [
                    {"id": "obj_reach_movarth_lair", "type": "reach_location", "location_name": "Movarth's Lair", "note": "Infiltrate Movarth's Lair, the vampire's den."},
                    {"id": "obj_kill_movarth", "type": "kill", "target_name": "master vampire", "target_id": "movarth_piquine", "count": 1, "note": "Slay Movarth Piquine, the master vampire."}
                ],
                "on_completion_dialogue": "Movarth is defeated. The shadow over Morthal lifts. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_morthal": 20, "gold_bonus": 350, "experience_bonus": 200, "item_bonus": "vampire_bane_dagger"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "hjaalmarch_lost_horn_of_jurgen",
        "title_template": "The Whispers of Windcaller",
        "desc_template": "The Greybeards of High Hrothgar seek a lost relic: the Horn of Jurgen Windcaller, believed to be hidden deep within the ancient Nordic tomb of Ustengrav in Hjaalmarch's marshes.",
        "lore_tags": ["hjaalmarch", "greybeards", "ustengrav", "way_of_the_voice", "ancient_nords", "relic_hunt"],
        "location_tags_required": ["barrow", "dungeon", "marsh", "greybeards_quest"],
        "level_range": (8, 13),
        "flavor_tags": {"quest": {"type": ["fetch", "explore"], "difficulty": ["hard"], "moral": ["ethical"], "urgency": ["important"]}},
        "turn_in_role_hint": ["greybeard", "scholar"],
        "stages": [
            {
                "stage_name": "Journey to Ustengrav",
                "objectives": [
                    {"id": "obj_reach_ustengrav", "type": "reach_location", "location_name": "Ustengrav", "note": "Travel to the ancient and treacherous tomb of Ustengrav."}
                ],
                "on_completion_dialogue": "Ustengrav's entrance looms, shrouded in mist. The air is heavy with ancient echoes.",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve the Horn",
                "objectives": [
                    {"id": "obj_navigate_ustengrav", "type": "investigate", "location_name": "Ustengrav", "note": "Navigate the complex traps and restless dead within Ustengrav (Perception/Acrobatics check DC 15)."},
                    {"id": "obj_collect_horn", "type": "collect_item", "item_key": "horn_of_jurgen_windcaller", "count": 1, "note": "Retrieve the Horn of Jurgen Windcaller."}
                ],
                "on_completion_dialogue": "You have the Horn. Its ancient power resonates in your hand. Return it to the Greybeards at High Hrothgar.",
                "reward_modifier": {"reputation_greybeards": 25, "gold_bonus": 400, "experience_bonus": 250, "item_bonus": "shout_knowledge_scroll"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # FALKREATH HOLD QUESTS (Forest, Graveyard, Imperial, Dark Brotherhood)
    # =============================================================================================================
    {
        "id": "falkreath_cursed_locket",
        "title_template": "A Glimmer of Sorrow",
        "desc_template": "A cursed silver locket found in a ruined area near Falkreath emanates sorrow. It seems to be tied to a vengeful spirit and a tragic love story. Uncover its history and put the spirit to rest.",
        "lore_tags": ["falkreath", "ghost", "cursed_item", "undead", "tragic_lore"],
        "location_tags_required": ["ruin", "graveyard", "falkreath", "barrow"],
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["investigate", "supernatural"], "moral": ["ethical", "gray"], "urgency": ["important"]}},
        "turn_in_role_hint": ["priest", "scholar", "local_elder"],
        "stages": [
            {
                "stage_name": "Examine the Locket and Seek Knowledge",
                "objectives": [
                    {"id": "obj_examine_locket", "type": "collect_item", "item_key": "silver_locket_ancient_cursed_sorrow", "count": 1, "note": "Obtain and examine the cursed locket."},
                    {"id": "obj_talk_to_priest", "type": "talk_to_npc", "npc_id": "runil_priest_of_arkay_ID", "note": "Consult Runil, the priest of Arkay in Falkreath, about the locket's history."},
                    {"id": "obj_visit_graveyard", "type": "reach_location", "location_name": "Falkreath Graveyard", "note": "Search the graveyard for clues about the locket's past."}
                ],
                "on_completion_dialogue": "The priest, Runil, tells you a tale of a jilted lover, a lost soldier named Kael, and a locket lost in battle, now stirring a vengeful spirit. You know where Kael's restless tomb is: [LOCATION_NAME].",
                "branch_options": []
            },
            {
                "stage_name": "Confront and Resolve the Spirit",
                "objectives": [
                    {"id": "obj_reach_kael_tomb", "type": "reach_location", "location_name": "[LOCATION_NAME]", "note": "Travel to Kael's restless tomb."},
                    {"id": "obj_commune_kael", "type": "talk_to_npc", "npc_id": "vengeful_spirit_kael_ID", "note": "Communicate with Kael's vengeful spirit."}
                ],
                "on_completion_dialogue": "Kael's spirit reveals its deepest sorrow: to be reunited with his love. You can help him find peace, or forcibly banish him.",
                "branch_options": [
                    {"choice_id": "help_kael_peace", "text": "Help Kael find peace by finding his lover's grave and placing the locket there (Persuasion/Restoration check DC 14).", "next_stage_index": 2},
                    {"choice_id": "banish_kael_force", "text": "Banish Kael's spirit by force (Destruction/Conjuration check DC 16, or combat).", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Help Kael Find Peace
                "stage_name": "Peaceful Resolution",
                "objectives": [
                    {"id": "obj_find_lover_grave", "type": "reach_location", "location_name": "Falkreath Graveyard", "note": "Find his lover's grave in the Falkreath Graveyard."},
                    {"id": "obj_place_locket", "type": "use_item", "item_key": "silver_locket_ancient_cursed_sorrow", "location_name": "Falkreath Graveyard", "note": "Place the locket at her grave."}
                ],
                "on_completion_dialogue": "Kael's spirit fades into a peaceful light. The locket's curse lifts, and a sense of calm fills the graveyard. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_falkreath": 15, "gold_bonus": 150, "experience_bonus": 100, "item_bonus": "amulet_of_arkay"},
                "final_stage": True
            },
            { # Stage 3: Banish Kael by Force
                "stage_name": "Forceful Banishment",
                "objectives": [
                    {"id": "obj_kill_kael_spirit", "type": "kill", "target_name": "vengeful spirit", "target_id": "vengeful_spirit_kael", "count": 1, "note": "Banish Kael's spirit by force."}
                ],
                "on_completion_dialogue": "Kael's spirit is gone, but the haunting lingers faintly. The place feels colder. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_falkreath": 10, "gold_bonus": 200, "experience_bonus": 120}, # Less reputation for forceful approach
                "final_stage": True
            }
        ]
    },
    {
        "id": "falkreath_dark_brotherhood_initiation",
        "title_template": "Whispers in the Dark",
        "desc_template": "Rumors speak of a child in Windhelm attempting the Black Sacrament. Investigate this dark ritual, which may lead you to the hidden sanctuary of the Dark Brotherhood near Falkreath.",
        "lore_tags": ["dark_brotherhood", "assassins", "black_sacrament", "falkreath", "windhelm", "secret_society"],
        "location_tags_required": ["windhelm", "falkreath", "dark_brotherhood_active"],
        "level_range": (10, 20),
        "flavor_tags": {"quest": {"type": ["investigate", "spy"], "difficulty": ["hard"], "moral": ["unethical", "gray"], "urgency": ["important"]}},
        "turn_in_role_hint": ["dark_brotherhood_member"], # Special turn-in
        "stages": [
            {
                "stage_name": "Investigate the Black Sacrament",
                "objectives": [
                    {"id": "obj_reach_windhelm_child", "type": "reach_location", "location_name": "Aretino Residence", "note": "Travel to Windhelm and investigate the Aretino Residence, where the Black Sacrament was performed."},
                    {"id": "obj_talk_avenuts", "type": "talk_to_npc", "npc_id": "aventus_aretino_ID", "note": "Speak to Aventus Aretino about his ritual."}
                ],
                "on_completion_dialogue": "Aventus confirms he performed the Black Sacrament to summon the Dark Brotherhood. He wants Grelod the Kind, the cruel orphanage matron, dead. You now have a choice: fulfill the contract or report it to the authorities.",
                "branch_options": [
                    {"choice_id": "fulfill_contract", "text": "Fulfill the contract and kill Grelod the Kind.", "next_stage_index": 1}, # Index 1 is Stage 2
                    {"choice_id": "report_contract", "text": "Report the contract to the local guards.", "next_stage_index": 2} # Index 2 is Stage 3
                ]
            },
            { # Stage 1: Fulfill Contract
                "stage_name": "Execute the Contract",
                "objectives": [
                    {"id": "obj_reach_orphanage", "type": "reach_location", "location_name": "Honorhall Orphanage", "note": "Travel to Honorhall Orphanage in Riften."},
                    {"id": "obj_kill_grelod", "type": "kill", "target_name": "grelod the kind", "target_id": "grelod_the_kind_ID", "count": 1, "note": "Assassinate Grelod the Kind."}
                ],
                "on_completion_dialogue": "Grelod is dead. You receive a mysterious note: 'We know.' Now, find the hidden sanctuary near Falkreath.",
                "branch_options": [] # Leads to next stage automatically
            },
            { # Stage 2: Report Contract (Quest Failure/Alternative)
                "stage_name": "Report the Contract",
                "objectives": [
                    {"id": "obj_talk_guard_contract", "type": "talk_to_npc", "npc_id": "riften_guard_ID", "note": "Report the Black Sacrament and Aventus's request to a Riften guard."},
                    {"id": "obj_witness_arrest", "type": "event_trigger", "event_type": "aventus_arrest", "note": "Witness Aventus being taken away by the guards."}
                ],
                "on_completion_dialogue": "Aventus is arrested. The Dark Brotherhood will not be pleased with your interference. This path ends here.",
                "reward_modifier": {"reputation_imperial_legion": 5, "reputation_dark_brotherhood": -20},
                "final_stage": True,
                "failure_state": True
            },
            { # Stage 3: Find Sanctuary (only if contract fulfilled)
                "stage_name": "Find the Sanctuary",
                "objectives": [
                    {"id": "obj_reach_sanctuary", "type": "reach_location", "location_name": "Dark Brotherhood Sanctuary (Falkreath Entrance)", "note": "Locate the hidden Dark Brotherhood Sanctuary near Falkreath."},
                    {"id": "obj_enter_sanctuary", "type": "talk_to_npc", "npc_id": "dark_brotherhood_door_ID", "note": "Gain entrance to the Sanctuary (requires answering a riddle)."}
                ],
                "on_completion_dialogue": "You are inside the Sanctuary. The Night Mother awaits. Your true initiation begins.",
                "reward_modifier": {"reputation_dark_brotherhood": 25, "gold_bonus": 500, "experience_bonus": 300, "item_bonus": "shrouded_armor_set"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # THE REACH QUESTS (Forsworn, Dwemer, Silver Mines, Markarth Intrigue)
    # =============================================================================================================
    {
        "id": "the_artifact_thief_markarth",
        "title_template": "The Silver-Blood Heirloom",
        "desc_template": "A valuable silver goblet, a family heirloom of the influential Silver-Blood family in Markarth, has been stolen. Recover it from the thief, who is rumored to be hiding in the city's underbelly.",
        "lore_tags": ["thieves", "markarth", "noble_intrigue", "corruption", "silver_blood"],
        "location_tags_required": ["city", "markarth", "thieves_guild"],
        "level_range": (4, 8),
        "flavor_tags": {"quest": {"type": ["investigate", "fetch"], "moral": ["gray"], "urgency": ["important"]}},
        "turn_in_role_hint": ["noble", "jarl"],
        "stages": [
            {
                "stage_name": "Investigate the Theft",
                "objectives": [
                    {"id": "s1_talk_to_guard", "type": "talk_to_npc", "npc_id": "markarth_city_guard_general_ID", "note": "Talk to a city guard in Markarth for clues."},
                    {"id": "s1_find_informant", "type": "talk_to_npc", "npc_id": "markarth_informant_ID", "note": "Find a local informant in Markarth's market."}
                ],
                "on_completion_dialogue": "The informant points you towards a known fence in the Ratway.",
                "branch_options": []
            },
            {
                "stage_name": "Confront the Fence",
                "objectives": [
                    {"id": "s2_reach_ratway", "type": "reach_location", "location_name": "The Ratway", "note": "Enter the Ratway beneath Markarth."},
                    {"id": "s2_talk_to_fence", "type": "talk_to_npc", "npc_id": "ratway_fence_ID", "note": "Speak to the fence about the heirloom."}
                ],
                "on_completion_dialogue": "The fence admits to having the goblet, but offers you a choice: buy it back, steal it, or expose the Silver-Blood family's dirty dealings.",
                "branch_options": [
                    {"choice_id": "s3_buy_goblet", "text": "Buy the goblet for 500 gold.", "next_stage_index": 2, "consequences": {"gold_cost": 500}}, # Index 2 is Stage 3
                    {"choice_id": "s3_steal_goblet", "text": "Attempt to steal the goblet from the fence (Sneak DC 15 or Pickpocket DC 14).", "next_stage_index": 3, "consequences": {"skill_challenge": {"skill": "stealth", "dc": 15}}}, # Index 3 is Stage 4
                    {"choice_id": "s3_expose_silverblood", "text": "Threaten the fence to expose the Silver-Blood family's involvement in criminal activity.", "next_stage_index": 4, "consequences": {"reputation_thalmor": 5, "reputation_silver_blood": -10}} # Index 4 is Stage 5
                ]
            },
            { # Stage 2: Return Goblet (Bought)
                "stage_name": "Return Goblet (Bought)",
                "objectives": [
                    {"id": "s3a_return_goblet", "type": "collect_item", "item_key": "silver_blood_goblet", "count": 1, "note": "You have the goblet. Return it to the Silver-Blood family."}
                ],
                "on_completion_dialogue": "You hand over the goblet. The Silver-Blood family thanks you for your discretion.",
                "reward_modifier": {"reputation_silver_blood": 10, "gold_bonus": 200},
                "final_stage": True
            },
            { # Stage 3: Return Goblet (Stolen)
                "stage_name": "Return Goblet (Stolen)",
                "objectives": [
                    {"id": "s4a_return_goblet", "type": "collect_item", "item_key": "silver_blood_goblet", "count": 1, "note": "You have the goblet. Return it to the Silver-Blood family."}
                ],
                "on_completion_dialogue": "You hand over the goblet. The Silver-Blood family thanks you, but a shadow of suspicion remains.",
                "reward_modifier": {"reputation_silver_blood": 5, "reputation_thieves_guild": 5},
                "final_stage": True
            },
            { # Stage 4: Expose Silver-Blood (Alternative Completion)
                "stage_name": "Expose Silver-Blood (Alternative Completion)",
                "objectives": [
                    {"id": "s5a_talk_to_jarl", "type": "talk_to_npc", "npc_id": "markarth_jarl_ID", "note": "Inform the Jarl of the Silver-Blood family's criminal dealings."},
                    {"id": "s5b_deal_with_fence", "type": "skill_check", "skill": "intimidation", "dc": 12, "note": "Successfully intimidate the fence to provide evidence."}
                ],
                "on_completion_dialogue": "Your actions have shaken Markarth's underworld, gaining you some unlikely allies and enemies. The goblet is lost, but justice might be served.",
                "reward_modifier": {"reputation_thieves_guild": 15, "reputation_silver_blood": -20, "gold_bonus": 100},
                "final_stage": True,
                "failure_state": True # Considered a "failure" of the original objective, but a path to player gain
            }
        ]
    },
    {
        "id": "reach_forsworn_threat",
        "title_template": "The Forsworn Threat at [LOCATION_NAME]",
        "desc_template": "A large and aggressive band of **Forsworn** has established a dangerous stronghold at **[LOCATION_NAME]**, terrorizing the local populace and disrupting trade. Their raids threaten the very stability of the Reach. You are tasked with eliminating their leader and scattering their forces to restore order to the region.",
        "lore_tags": ["the_reach", "forsworn_conflict", "mountain_danger", "rebellion", "combat", "justice"],
        "location_tags_required": ["forsworn_stronghold", "mountain_base_camp"],
        "level_range": (8, 15),
        "flavor_tags": {"quest": {"type": ["clear", "hunt", "combat"], "difficulty": ["hard"], "moral": ["ethical", "political"]}},
        "turn_in_role_hint": ["markarth_guard_captain", "jarl_igmund"],
        "stages": [
            {
                "stage_name": "Assault the Stronghold",
                "objectives": [
                    {"id": "obj_reach_forsworn_stronghold", "type": "reach_location", "location_name": "[LOCATION_NAME]", "note": "Travel to the formidable **Forsworn stronghold** and prepare for battle."},
                    {"id": "obj_defeat_forsworn_warriors", "type": "kill", "target_name": "forsworn warrior", "target_id": "forsworn_warrior", "count": 10, "note": "Engage and defeat the **Forsworn warriors** guarding the stronghold."},
                    {"id": "obj_eliminate_leader", "type": "kill", "target_name": "forsworn leader", "target_id": "forsworn_briarheart", "count": 1, "note": "Eliminate the **Forsworn leader** to break their command."}
                ],
                "on_completion_dialogue": "The Forsworn stronghold is cleared, its defenders scattered or slain. The immediate threat to the Reach is quelled. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 300, "experience_bonus": 150, "reputation_markarth_jarl": 15},
                "final_stage": True
            }
        ]
    },
    {
        "id": "reach_kolskeggr_reclamation",
        "title_template": "The Gold of Kolskeggr: A Miner's Desperate Plea",
        "desc_template": "The rich **Kolskeggr Mine**, a source of valuable gold east of Markarth, lies abandoned. Fierce and relentless **Forsworn attacks** have driven off the miners, threatening the economic stability of the Reach. Ogden, the mine foreman, seeks a brave soul to reclaim the mine, clear out the Forsworn, and restore the flow of precious gold.",
        "lore_tags": ["the_reach", "mine_gold_rich", "forsworn_conflict_severe", "reclamation", "economic_impact", "combat"],
        "location_tags_required": ["mine_gold_rich", "forsworn_conflict_severe"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["clear", "reclaim", "economic"], "difficulty": ["medium", "hard"], "moral": ["ethical", "mercenary"]}},
        "turn_in_role_hint": ["markarth_mine_foreman", "markarth_jarl_steward"],
        "stages": [
            {
                "stage_name": "A Vein of Trouble",
                "objectives": [
                    {"id": "obj_talk_to_ogden", "type": "talk_to_npc", "npc_id": "ogden_kolskeggr_ID", "note": "Speak with **Ogden**, the mine foreman, about the Forsworn infestation."},
                    {"id": "obj_reach_kolskeggr_mine", "type": "reach_location", "location_name": "Kolskeggr Mine", "note": "Travel to the deserted **Kolskeggr Mine**."},
                    {"id": "obj_clear_forsworn_exterior", "type": "kill", "target_name": "forsworn", "target_id": "forsworn_raider", "count": 5, "note": "Clear the **Forsworn encampment** outside the mine entrance."}
                ],
                "on_completion_dialogue": "The exterior of Kolskeggr is clear, but the mine's depths still echo with the shouts of Forsworn. The main threat is within.",
                "branch_options": []
            },
            {
                "stage_name": "Reclaiming the Gold",
                "objectives": [
                    {"id": "obj_clear_forsworn_interior", "type": "kill", "target_name": "forsworn", "target_id": "forsworn_raider", "count": 7, "note": "Clear the remaining **Forsworn** from deep within Kolskeggr Mine."},
                    {"id": "obj_defeat_forsworn_leader_mine", "type": "kill", "target_name": "forsworn shaman/leader", "target_id": "forsworn_shaman_leader_ID", "count": 1, "note": "Defeat the **Forsworn leader** guarding the richest veins."},
                    {"id": "obj_secure_mine_entrance", "type": "destroy", "object": "forsworn_barricades", "count": 3, "note": "Destroy any **Forsworn barricades or traps** to secure the mine for the miners' return."}
                ],
                "on_completion_dialogue": "Kolskeggr Mine is now free of the Forsworn menace! The gold once again awaits the miners. Return to [QUEST_GIVER_NAME] with the good news.",
                "reward_modifier": {"gold_bonus": 250, "experience_bonus": 120, "reputation_markarth_jarl": 10, "reputation_mercantile_guild": 8},
                "final_stage": True
            }
        ]
    },
    {
        "id": "reach_orc_stronghold_aid",
        "title_template": "The Shattered Code: Aid to Dushnikh Yal",
        "desc_template": "The mighty **Orc stronghold of Dushnikh Yal**, usually a bastion of strength and tradition, has been besieged by internal strife and a growing external threat from aggressive giants. The Code of Malacath is strained, and they seek an outsider to aid them in restoring order and proving their strength against their enemies. Prove your mettle, earn their respect, and aid the Orcs in their time of need.",
        "lore_tags": ["orc_stronghold", "tribal_conflict", "malacath_worship", "giant_threat", "aid", "honor", "warrior_culture"],
        "location_tags_required": ["orc_stronghold", "malacath_worship"],
        "level_range": (9, 14),
        "flavor_tags": {"quest": {"type": ["combat", "aid", "diplomacy"], "difficulty": ["medium", "hard"], "moral": ["ethical", "honor"]}},
        "turn_in_role_hint": ["burguk_orc_chief", "ghorza_orc_smith"],
        "stages": [
            {
                "stage_name": "A Chieftain's Burden",
                "objectives": [
                    {"id": "obj_talk_to_chief_dushnikh", "type": "talk_to_npc", "npc_id": "burguk_orc_chief_ID", "note": "Speak with **Chief Burguk** in Dushnikh Yal about the stronghold's troubles and how you can assist."},
                    {"id": "obj_deal_with_giants", "type": "kill", "target_name": "giant", "target_id": "giant", "count": 3, "note": "Drive back the **aggressive giants** threatening the stronghold's borders."}
                ],
                "on_completion_dialogue": "You've proven your strength against their ancestral foes. The giants are repelled. Now, the Chief needs your help to address an internal matter: a dispute over a sacred hunting ground, currently occupied by dangerous beasts or rival Orcs.",
                "branch_options": []
            },
            {
                "stage_name": "Reclaiming Sacred Ground",
                "objectives": [
                    {"id": "obj_reach_sacred_hunting_ground", "type": "reach_location", "location_name": "Sacred Orc Hunting Ground", "note": "Journey to the disputed **sacred hunting ground** near Dushnikh Yal."},
                    {"id": "obj_clear_beasts_or_rivals", "type": "kill", "target_name": "sabre cat/orc", "target_id": random.choice(["sabre_cat", "orc_rival"]), "count": 4, "note": "Clear the hunting ground of either **ferocious beasts or rival Orc hunters**."},
                    {"id": "obj_retrieve_sacred_totem_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "orc_sacred_totem", "count": 1, "note": " (Optional) Retrieve a **lost sacred totem** from the hunting ground, increasing the Orcs' faith in you."}}
                ],
                "on_completion_dialogue": "The hunting ground is secured, and the lost totem recovered. You've earned the respect of Dushnikh Yal. Return to [QUEST_GIVER_NAME]. Your actions speak louder than words in this stronghold.",
                "reward_modifier": {"reputation_tribal_bonus": 18, "gold_bonus": 280, "experience_bonus": 140, "item_bonus": "orcish_weapon_masterwork"},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # EASTMARCH SPECIFIC QUESTS (Volcanic, Stormcloak, Windhelm, Hot Springs)
    # =============================================================================================================
    {
        "id": "windhelm_blood_on_the_ice",
        "title_template": "Blood on the Ice: The Windhelm Butcher",
        "desc_template": "A series of brutal, ritualistic murders has terrified the citizens of **Windhelm**, particularly targeting women. The city guards are stumped, or perhaps deliberately ignoring the plight of the Gray Quarter. Investigating the chilling crime scenes, uncovering the identity of the 'Butcher,' and bringing the perpetrator to justice is paramount, before another life is lost.",
        "lore_tags": ["windhelm", "murder_mystery", "city_intrigue", "social_tension", "investigation", "dark_secrets", "justice", "serial_killer"],
        "location_tags_required": ["windhelm", "murder_investigation_connection"],
        "level_range": (8, 14),
        "flavor_tags": {"quest": {"type": ["investigate", "mystery", "justice"], "difficulty": ["hard", "dark"], "moral": ["ethical", "vengeance"]}},
        "turn_in_role_hint": ["windhelm_guard_captain", "jarl_ulfric_stormcloak", "hall_of_dead_helgird"],
        "stages": [
            {
                "stage_name": "The Trail of Blood",
                "objectives": [
                    {"id": "obj_investigate_first_murder", "type": "investigate", "location_name": "Windhelm (Hjerim area)", "note": "Investigate the **first murder scene** in Windhelm's stone quarter, looking for overlooked clues (requires Perception or Investigation check DC 14)."},
                    {"id": "obj_talk_to_witness_butcher", "type": "talk_to_npc", "npc_id": "suspect_house_carl_ID", "note": "Speak to the **local guard or housecarl** near the crime scene, who might be hesitant to share information."},
                    {"id": "obj_visit_hall_of_dead_windhelm", "type": "reach_location", "location_name": "Hall of the Dead (Windhelm)", "note": "Visit the **Hall of the Dead** to examine the victims' bodies and speak with Helgird, the priestess."}
                ],
                "on_completion_dialogue": "The clues point to a dark, ritualistic pattern. The victims have been dismembered. You find a strange amulet and disturbing pamphlets. The trail leads you to a grim, abandoned house in the city, **Hjerim**.",
                "branch_options": []
            },
            {
                "stage_name": "A House of Horrors",
                "objectives": [
                    {"id": "obj_reach_hjerim", "type": "reach_location", "location_name": "Hjerim (Windhelm)", "note": "Gain access to and explore **Hjerim**, the abandoned house suspected to be the Butcher's lair."},
                    {"id": "obj_uncover_butchers_identity", "type": "investigate", "object": "butcher's journal/clues", "note": "Within Hjerim, uncover the **Butcher's true identity** and motives (requires Investigation or Sneak check DC 15)."},
                    {"id": "obj_find_amulet_of_arvak_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "amulet_of_arvak", "count": 1, "note": " (Optional) Discover a strange **amulet** related to the Butcher's rituals, perhaps a sign of a dark Daedric pact."}}
                ],
                "on_completion_dialogue": "The truth is horrifying. The Butcher is not a single killer, but an individual driven by a dark power, linked to a cult. The next victim is already marked, or a planned ritual must be stopped.",
                "branch_options": []
            },
            {
                "stage_name": "The Final Confrontation",
                "objectives": [
                    {"id": "obj_confront_butcher", "type": "confront", "npc_id": "windhelm_butcher_ID", "note": "Confront the **Windhelm Butcher** at their next planned location (e.g., a secluded alley, the docks, or a ritual site)."},
                    {"id": "obj_defeat_butcher", "type": "kill", "target_name": "windhelm butcher", "target_id": "windhelm_butcher_ID", "count": 1, "note": "Bring down the **Windhelm Butcher** to end their reign of terror."}
                ],
                "on_completion_dialogue": "The Butcher's dark work is ended. Windhelm can finally breathe a sigh of relief, though the scars of the murders will linger. You have brought justice to the city. Report to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 350, "experience_bonus": 200, "reputation_local_bonus": 20, "item_bonus": "butchers_blade_unique"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "eastmarch_orc_stronghold_feud",
        "title_template": "The Ebony Blade of Narzulbur: A Chief's Dilemma",
        "desc_template": "The renowned **Narzulbur**, an Orc stronghold fiercely loyal to Malacath, faces a grave threat: its prized **Gloombound Mine** has been plagued by a strange, aggressive malevolence emanating from its deepest ebony veins. The Chief believes it's a test from Malacath, but the miners fear a growing infestation. You must investigate the mine's depths, quell the threat, and restore the stronghold's honor and prosperity.",
        "lore_tags": ["eastmarch", "orc_stronghold", "malacath_worship", "mine_ebony", "dungeon_danger", "tribal_conflict_internal", "honor", "resource_threat"],
        "location_tags_required": ["orc_stronghold_isolated", "mine_ebony_major"],
        "level_range": (10, 16),
        "flavor_tags": {"quest": {"type": ["clear", "investigate", "honor"], "difficulty": ["hard"], "moral": ["ethical", "tribal_honor"]}},
        "turn_in_role_hint": ["mauhulakh_orc_chief", "grogmar_orc"],
        "stages": [
            {
                "stage_name": "The Darkening Veins",
                "objectives": [
                    {"id": "obj_talk_to_chief_narz", "type": "talk_to_npc", "npc_id": "mauhulakh_orc_chief_ID", "note": "Speak with **Chief Mauhulakh** in Narzulbur about the troubles plaguing Gloombound Mine."},
                    {"id": "obj_investigate_gloombound_mine", "type": "investigate", "location_name": "Gloombound Mine (Ebony)", "note": "Descend into **Gloombound Mine** and investigate the source of the growing malevolence (requires Perception or One-Handed/Two-Handed check DC 15 to find clues amidst mining marks)."},
                    {"id": "obj_defeat_creatures_mine_entrance", "type": "kill", "target_name": "chaurus_hunter", "target_id": "chaurus_hunter", "count": 3, "note": "Clear the immediate mine entrance of any **unnatural creatures** that have appeared (e.g., Chaurus, Frost Atronachs)."}
                ],
                "on_completion_dialogue": "The mine's depths are tainted. You discover signs of an ancient, trapped magic, or perhaps a beast drawn to the ebony's essence. The true threat lies deeper, guarded by more formidable foes.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Ebonground",
                "objectives": [
                    {"id": "obj_reach_mine_deep", "type": "reach_location", "location_name": "Gloombound Mine (Deepest Veins)", "note": "Delve into the **deepest, most dangerous veins** of Gloombound Mine."},
                    {"id": "obj_defeat_ancient_threat", "type": "kill", "target_name": "ancient dwarven sphere/ebony elemental", "target_id": "ancient_dwemer_sphere", "count": 1, "note": "Confront and defeat the **ancient entity or creature** responsible for the mine's affliction (e.g., a rogue Dwemer sphere, an ebony elemental, or a powerful Frost Atronach)."},
                    {"id": "obj_extract_unique_ore_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "pure_ebony_vein", "count": 1, "note": " (Optional) Extract a **pure, unblemished vein of ebony** from the cleansed area, a rare prize (requires Smithing/Mining check DC 16)."}}
                ],
                "on_completion_dialogue": "The malevolence is gone, and the rich ebony veins pulse with renewed, clean energy. Narzulbur's prosperity is secured, and your aid has brought great honor to their stronghold. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_tribal_bonus": 20, "gold_bonus": 350, "experience_bonus": 180, "unique_item_orcish_legendary": "orcish_malacath_blade"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "eastmarch_witchmist_grove_extermination",
        "title_template": "The Witches' Weave: Purging Witchmist Grove",
        "desc_template": "The mystical **Witchmist Grove**, a place of natural beauty and potent magical energies in Eastmarch's hot springs region, has been defiled. A coven of malevolent witches, or perhaps a powerful Hagraven, has taken root, twisting its primal energies for dark rituals. Drive out this vile presence, cleanse the grove, and restore its natural tranquility.",
        "lore_tags": ["eastmarch", "grove_magical", "hagraven_lair_potential", "witch_coven_potential", "dark_ritual_site", "clearance", "nature_cleansing"],
        "location_tags_required": ["grove_magical", "hagraven_lair_potential"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["clear", "hunt", "spiritual"], "difficulty": ["medium", "hard"], "moral": ["ethical", "divine"]}},
        "turn_in_role_hint": ["local_hunter_eastmarch", "jarls_steward_windhelm"],
        "stages": [
            {
                "stage_name": "The Twisted Heart of the Grove",
                "objectives": [
                    {"id": "obj_reach_witchmist_grove", "type": "reach_location", "location_name": "Witchmist Grove", "note": "Travel to the once-sacred **Witchmist Grove**. Feel the oppressive, twisted magical presence in the air."},
                    {"id": "obj_defeat_witches_or_hagravens", "type": "kill", "target_name": "hagraven/witch", "target_id": random.choice(["hagraven", "witch_coven"]), "count": 4, "note": "Exterminate the **malevolent witches or hagravens** defiling the grove."},
                    {"id": "obj_destroy_ritual_components_optional", "type": "optional", "objective": {"type": "destroy", "object": "dark_ritual_components", "note": " (Optional) Destroy the **foul altars and ritual components** scattered throughout the grove to prevent their return."}}
                ],
                "on_completion_dialogue": "The dark energies have receded from Witchmist Grove. Its natural beauty begins to assert itself once more, cleansed by your actions. The grove is safe. Report to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 180, "experience_bonus": 90, "reputation_local_bonus": 10, "item_bonus": "rare_alchemy_ingredients_bundle"},
                "final_stage": True
            }
        ]
    },
    
    # =============================================================================================================
    # THE RIFT SPECIFIC QUESTS (Thieves Guild, Black-Briar, Autumnal Forests)
    # =============================================================================================================
    {
        "id": "riften_thieves_guild_initiation",
        "title_template": "A Chance in the Shadows: Riften's Underbelly",
        "desc_template": "The notorious **Thieves Guild of Riften**, masters of shadow and coin, seeks new blood. Brynjolf, their cunning recruiter, offers a test: prove your worth by framing a local merchant to demonstrate your skills in subterfuge and manipulation. This is your opportunity to join the ranks of Skyrim's most infamous criminal organization.",
        "lore_tags": ["riften", "thieves_guild_active", "criminal_initiation", "subterfuge", "deception", "corruption", "black_briar_influence_indirect"],
        "location_tags_required": ["riften", "thieves_guild_hq_active"],
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["infiltration", "deception", "crime"], "difficulty": ["medium"], "moral": ["unethical", "gray"]}},
        "turn_in_role_hint": ["brynjolf_thieves_guild"],
        "stages": [
            {
                "stage_name": "A Test of Cunning",
                "objectives": [
                    {"id": "obj_talk_to_brynjolf", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** in the Riften marketplace to receive your first task."},
                    {"id": "obj_plant_ring", "type": "use_item", "item_key": "stolen_ring_planted", "location_name": "Madesi's Strongbox", "note": "Discreetly **plant a stolen ring** in Madesi's strongbox in the Riften marketplace (requires Sneak or Pickpocket check DC 15)."},
                    {"id": "obj_create_diversion", "type": "event_trigger", "event_type": "marketplace_diversion", "note": "Create a **diversion** in the marketplace to draw attention away from your actions (e.g., pickpocketing, shouting)."}
                ],
                "on_completion_dialogue": "The ring is planted, and the diversion successful. Brynjolf is impressed by your cunning. 'You've got potential, lad/lass. Meet me down in the Ragged Flagon.' Your initiation into the Guild is at hand.",
                "branch_options": []
            },
            {
                "stage_name": "Joining the Shadows",
                "objectives": [
                    {"id": "obj_reach_ragged_flagon", "type": "reach_location", "location_name": "The Ragged Flagon", "note": "Find your way into the **Ragged Flagon**, the hidden tavern beneath Riften."},
                    {"id": "obj_talk_to_brynjolf_ragged_flagon", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** within the Ragged Flagon to officially join the Thieves Guild."}
                ],
                "on_completion_dialogue": "You are now a member of the Thieves Guild, a new life in the shadows begins. Your first true contract awaits. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_thieves_guild": 20, "gold_bonus": 100, "experience_bonus": 80, "item_bonus": "thieves_guild_armor_set"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "riften_black_briar_corruption",
        "title_template": "The Black-Briar's Grip: Unveiling Riften's Corruption",
        "desc_template": "The city of **Riften** groans under the iron fist of **Maven Black-Briar**, whose influence extends into every corner of the city, from the Jarl's court to the Thieves Guild. A desperate citizen or a disgruntled guard seeks your aid to expose her pervasive corruption and loosen her suffocating grip on the city's economy and politics. This is a dangerous game of shadows and power.",
        "lore_tags": ["riften", "black_briar_family", "corruption_political", "economic_monopoly", "city_intrigue", "investigation", "power_struggle", "justice_difficult"],
        "location_tags_required": ["riften", "black_briar_influence_total"],
        "level_range": (10, 18),
        "flavor_tags": {"quest": {"type": ["investigate", "political", "infiltration"], "difficulty": ["hard", "complex"], "moral": ["gray", "justice_challenging"]}},
        "turn_in_role_hint": ["riften_jarl_laila", "disgruntled_guard_riften", "maven_black_briar_rival"],
        "stages": [
            {
                "stage_name": "Whispers of Influence",
                "objectives": [
                    {"id": "obj_talk_to_disgruntled_guard", "type": "talk_to_npc", "npc_id": "riften_guard_disgruntled_ID", "note": "Speak with a **disgruntled Riften guard** who hints at Maven Black-Briar's pervasive influence."},
                    {"id": "obj_infiltrate_meadery_office", "type": "investigate", "location_name": "Black-Briar Meadery (Riften Office)", "note": "Infiltrate the **Black-Briar Meadery's private office** in Riften to find incriminating ledgers or communications (requires Sneak or Lockpicking check DC 16)."},
                    {"id": "obj_bribe_official_optional", "type": "optional", "objective": {"type": "talk_to_npc", "npc_id": "corrupt_city_official_ID", "note": " (Optional) **Bribe a corrupt city official** for information on Maven's dealings (requires Speech/Bribery check DC 15 and gold)."}}
                ],
                "on_completion_dialogue": "You've gathered initial evidence of Maven's widespread corruption. The trail leads to her manor, and perhaps even to the Jarl's court. This is bigger than you thought.",
                "branch_options": []
            },
            {
                "stage_name": "Exposing the Matriarch",
                "objectives": [
                    {"id": "obj_infiltrate_black_briar_manor", "type": "reach_location", "location_name": "Black-Briar Manor", "note": "Infiltrate **Black-Briar Manor**, Maven's heavily guarded residence, to find definitive proof of her illicit activities."},
                    {"id": "obj_collect_incriminating_evidence", "type": "collect_item", "item_key": "maven_black_briar_ledger", "count": 1, "note": "Retrieve **Maven's personal ledger** or a coded message detailing her crimes."},
                    {"id": "obj_confront_maven_optional", "type": "optional", "objective": {"type": "confront", "npc_id": "maven_black_briar_ID", "note": " (Optional) Directly **confront Maven Black-Briar** with the evidence; her reaction may be... illuminating."}}
                ],
                "on_completion_dialogue": "You have the undeniable proof of Maven Black-Briar's corruption. The fate of Riften, and your own standing, depends on how you use this knowledge. Will you expose her, or use it for your own gain?",
                "branch_options": [
                    {"choice_id": "expose_maven_to_jarl", "text": "Present the evidence to Jarl Laila Law-Giver, seeking justice for Riften. (Path of Justice)", "next_stage_index": 2, "consequences": {"reputation_riften_jarl_laila": 20, "reputation_black_briar": -20}},
                    {"choice_id": "blackmail_maven", "text": "Blackmail Maven Black-Briar, leveraging the evidence for personal gain. (Path of Power/Greed)", "next_stage_index": 3, "consequences": {"gold_gain": 500, "reputation_black_briar": 10, "reputation_riften_citizens": -5}}
                ]
            },
            { # Stage 2: Expose Maven to Jarl
                "stage_name": "Riften's Reckoning",
                "objectives": [
                    {"id": "obj_present_evidence_to_jarl", "type": "talk_to_npc", "npc_id": "jarl_laila_law_giver_ID", "note": "Present the **incriminating evidence to Jarl Laila Law-Giver** in Mistveil Keep."}
                ],
                "on_completion_dialogue": "Jarl Laila is shocked and enraged by the undeniable proof of Maven's treachery. Maven's power in Riften is broken, though her influence may linger. You have brought a new dawn to Riften. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 300, "experience_bonus": 150, "reputation_riften_jarl_laila": 25, "reputation_riften_citizens": 15},
                "final_stage": True
            },
            { # Stage 3: Blackmail Maven
                "stage_name": "A Shadowy Alliance",
                "objectives": [
                    {"id": "obj_blackmail_maven_direct", "type": "talk_to_npc", "npc_id": "maven_black_briar_ID", "note": "Confront **Maven Black-Briar** with the evidence and demand your price."}
                ],
                "on_completion_dialogue": "Maven, seething with silent fury, agrees to your terms. You now have a powerful, dangerous ally in Riften, but the city's corruption remains. You walk a path of shadows and influence. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 750, "experience_bonus": 100, "reputation_black_briar": 15, "reputation_thieves_guild": 10},
                "final_stage": True,
                "failure_state": True # Failure to the original quest giver, but success for this path
            }
        ]
    },
    {
        "id": "riften_lost_prospect_mine",
        "title_template": "The Prospector's Plea: Lost Gold of the Rift",
        "desc_template": "The once-promising **Lost Prospect Mine** in the Rift, rumored to hold rich gold veins, has fallen silent. Its prospector, a hopeful but naive Nord, fears it's overrun by monstrous spiders or bandits. Reclaim the mine, clear its depths of any threats, and perhaps, rediscover its golden promise.",
        "lore_tags": ["the_rift", "mine_gold_abandoned", "spider_infestation_potential", "bandit_lair_potential", "reclamation", "economic_opportunity"],
        "location_tags_required": ["mine_abandoned_gold", "spider_infestation_potential"],
        "level_range": (3, 8),
        "flavor_tags": {"quest": {"type": ["clear", "reclaim", "economic"], "difficulty": ["medium"], "moral": ["ethical", "mercenary"]}},
        "turn_in_role_hint": ["riften_prospector", "riften_jarls_steward"],
        "stages": [
            {
                "stage_name": "A Silent Promise",
                "objectives": [
                    {"id": "obj_talk_to_prospector", "type": "talk_to_npc", "npc_id": "riften_prospector_ID", "note": "Speak with the **anxious prospector** in Riften about the abandoned Lost Prospect Mine."},
                    {"id": "obj_reach_lost_prospect_mine", "type": "reach_location", "location_name": "Lost Prospect Mine", "note": "Travel to the deserted **Lost Prospect Mine** and assess the situation."}
                ],
                "on_completion_dialogue": "The mine's entrance is eerily quiet, save for the faint scuttling sounds from within. It's infested, just as the prospector feared. You must clear it.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Veins",
                "objectives": [
                    {"id": "obj_clear_spiders_or_bandits", "type": "kill", "target_name": "giant frostbite spider", "target_id": "giant_frostbite_spider", "count": 8, "note": "Clear the mine of its **monstrous spider infestation** (or bandits, if they've taken over)."},
                    {"id": "obj_find_gold_vein_optional", "type": "optional", "objective": {"type": "investigate", "object": "hidden_gold_vein", "note": " (Optional) Search for a **hidden, rich gold vein** deep within the mine (requires Mining check DC 14)."}}
                ],
                "on_completion_dialogue": "The mine is clear! The gnawing threat is gone, and the prospector can return. You may have even found a hidden fortune. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 150, "experience_bonus": 75, "reputation_local_bonus": 8},
                "final_stage": True
            }
        ]
    },
    
    # =============================================================================================================
    # HAAFINGAR SPECIFIC QUESTS (Imperial, Solitude, Bards College, Coastal)
    # =============================================================================================================
    {
        "id": "solitude_bards_college_recruitment",
        "title_template": "The Bard's Calling: Solitude's New Voice",
        "desc_template": "The esteemed **Bards College in Solitude**, the heart of Skyrim's musical and historical tradition, is always seeking new talent. They offer a unique opportunity to those with a flair for performance, lore, or even subtle deception. Join their ranks, contribute to their legacy, and perhaps even uncover ancient secrets through song and story.",
        "lore_tags": ["solitude", "bards_college_active", "music_lore", "performance", "recruitment", "cultural_institution", "historic_preservation"],
        "location_tags_required": ["solitude", "bards_college"],
        "level_range": (1, 6),
        "flavor_tags": {"quest": {"type": ["social", "performance", "knowledge"], "difficulty": ["easy", "medium"], "moral": ["ethical", "artistic"]}},
        "turn_in_role_hint": ["viola_giordano", "jorn_bards_college"],
        "stages": [
            {
                "stage_name": "An Audition of Talent",
                "objectives": [
                    {"id": "obj_reach_bards_college", "type": "reach_location", "location_name": "Bards College", "note": "Travel to the grand **Bards College** in Solitude."},
                    {"id": "obj_talk_to_viola", "type": "talk_to_npc", "npc_id": "viola_giordano_ID", "note": "Speak with **Viola Giordano**, one of the College's instructors, about joining."},
                    {"id": "obj_perform_for_audition", "type": "skill_check", "skill": "speech", "dc": 10, "note": "Perform a **short piece or recite a tale** for an audition (requires Speech or Persuasion check DC 10)."}
                ],
                "on_completion_dialogue": "Your performance (or convincing words) has impressed the College. They offer you a chance to prove your dedication by recovering a lost instrument or a forgotten ballad. Your choice: a lute or a song?",
                "branch_options": [
                    {"choice_id": "recover_instrument", "text": "Agree to recover a **lost ancient lute** from a nearby ruin. (Path of Action)", "next_stage_index": 1},
                    {"choice_id": "find_forgotten_ballad", "text": "Agree to find and transcribe a **forgotten ballad** from a reclusive scholar. (Path of Lore)", "next_stage_index": 2}
                ]
            },
            { # Stage 1: Recover Instrument Path
                "stage_name": "The Lost Melody",
                "objectives": [
                    {"id": "obj_reach_instrument_ruin", "type": "reach_location", "location_name": "Lost Instrument Ruin", "note": "Travel to the designated **ruin** where the ancient lute is said to be hidden."},
                    {"id": "obj_collect_instrument", "type": "collect_item", "item_key": "ancient_lute_bards", "count": 1, "note": "Retrieve the **ancient lute** from the ruin's depths."}
                ],
                "on_completion_dialogue": "The lute is recovered, its strings still humming with faint magic. You've proven your dedication. Return to [QUEST_GIVER_NAME] at the Bards College.",
                "reward_modifier": {"reputation_bards_college": 10, "gold_bonus": 75, "experience_bonus": 40, "item_bonus": "bards_college_lute"},
                "final_stage": True
            },
            { # Stage 2: Find Forgotten Ballad Path
                "stage_name": "The Forgotten Verse",
                "objectives": [
                    {"id": "obj_reach_scholar_hermitage", "type": "reach_location", "location_name": "Reclusive Scholar's Hermitage", "note": "Journey to the **hermitage of a reclusive scholar** who might know the forgotten ballad."},
                    {"id": "obj_talk_to_scholar_ballad", "type": "talk_to_npc", "npc_id": "reclusive_scholar_ID", "note": "Persuade the **scholar** to share the forgotten ballad (requires Speech/Persuasion check DC 12)."},
                    {"id": "obj_transcribe_ballad", "type": "event_trigger", "event_type": "transcribe_ballad", "note": "Successfully **transcribe the forgotten ballad** into your journal."}
                ],
                "on_completion_dialogue": "The forgotten ballad is now preserved in your journal, its verses echoing with ancient wisdom. You've proven your dedication to lore. Return to [QUEST_GIVER_NAME] at the Bards College.",
                "reward_modifier": {"reputation_bards_college": 12, "gold_bonus": 50, "experience_bonus": 60, "item_bonus": "rare_songbook"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "solitude_thalmor_interrogation",
        "title_template": "The Thalmor's Reach: A Diplomatic Incident",
        "desc_template": "A **Khajiit traveler** has been apprehended by a zealous **Thalmor patrol** near **[LOCATION_NAME]**, suspected of Talos worship or illicit trade. The situation is tense, threatening to escalate into a diplomatic incident or worse. You are presented with a moral dilemma: intervene on behalf of the Khajiit, or allow the Justiciars to proceed with their grim work, perhaps even aiding them for a price.",
        "lore_tags": ["haafingar", "thalmor_presence_active", "white_gold_concordat_enforcement", "talos_ban", "political_tension", "khajiit_victim", "moral_choice_event", "diplomacy_conflict"],
        "location_tags_required": ["road", "imperial_presence_strong", "thalmor_presence_city"], # Can be triggered by random encounter
        "level_range": (6, 12),
        "flavor_tags": {"quest": {"type": ["rescue", "spy", "diplomacy"], "moral": ["gray", "political_choice"], "urgency": ["urgent", "tense"]}},
        "turn_in_role_hint": ["jarl_torygg", "khajiit_caravan_leader", "thalmor_justiciar"], # Can turn into different quest lines
        "stages": [
            {
                "stage_name": "Witness Interrogation",
                "objectives": [
                    {"id": "obj_witness_interrogation", "type": "talk_to_npc", "npc_id": "thalmor_justiciar_interrogator_ID", "note": "Witness the tense **interrogation between a Thalmor Justiciar and a frightened Khajiit**."},
                    {"id": "obj_observe_situation", "type": "skill_check", "skill": "perception", "dc": 12, "note": "Carefully **observe the situation** for additional details or weaknesses (requires Perception check DC 12)."}
                ],
                "on_completion_dialogue": "The Justiciar's cold eyes meet yours. The fate of the Khajiit hangs in the balance. Will you intervene, or walk away?",
                "branch_options": [
                    {"choice_id": "intervene_speech", "text": "Attempt to **intervene using persuasion**, arguing for the Khajiit's release. (Speech/Persuasion DC 15)", "next_stage_index": 1, "consequences": {"skill_challenge": "speech", "disposition_change_thalmor": -5}},
                    {"choice_id": "intervene_force", "text": "Intervene by **force**, attacking the Thalmor to free the Khajiit. (Direct Confrontation)", "next_stage_index": 2, "consequences": {"faction_hostility": "thalmor"}},
                    {"choice_id": "walk_away", "text": "Simply **walk away**, leaving the Khajiit to their grim fate. (Neutral/Self-Preservation)", "next_stage_index": 3}
                ]
            },
            { # Stage 1: Intervened (Speech)
                "stage_name": "Negotiate Release",
                "objectives": [
                    {"id": "obj_persuade_justiciar", "type": "skill_check", "skill": "speech", "dc": 15, "note": "Successfully **persuade the Justiciar** to release the Khajiit, perhaps with a fabricated story or a clever argument."},
                    {"id": "obj_talk_to_freed_khajiit", "type": "talk_to_npc", "npc_id": "khajiit_traveler_frightened_ID", "note": "Speak to the **freed Khajiit**; they will surely be grateful."}
                ],
                "on_completion_dialogue": "You successfully negotiated the Khajiit's release. He thanks you profusely, promising to speak well of you to his caravan. Your discretion is noted by the Thalmor, though they remain wary. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_khajiit_caravans": 10, "gold_bonus": 100, "experience_bonus": 50},
                "turn_in_dialogue_key": "thalmor_interrogation_success_speech_turn_in", # Custom turn-in dialogue key
                "final_stage": True
            },
            { # Stage 2: Intervened (Force)
                "stage_name": "Combat with Thalmor",
                "objectives": [
                    {"id": "obj_defeat_thalmor_patrol", "type": "kill", "target_name": "thalmor", "target_id": "thalmor_justiciar", "count": 1, "note": "Engage and **defeat the Thalmor patrol** to free the Khajiit."},
                    {"id": "obj_free_khajiit_combat", "type": "talk_to_npc", "npc_id": "khajiit_traveler_frightened_ID", "note": "Ensure the **Khajiit is truly free** after the skirmish."}
                ],
                "on_completion_dialogue": "You have fought off the Thalmor. The Khajiit is free, but you've made powerful enemies in the Aldmeri Dominion. Your name will be known, for better or worse. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_stormcloaks": 15, "reputation_thalmor": -25, "gold_bonus": 150, "experience_bonus": 75},
                "turn_in_dialogue_key": "thalmor_interrogation_success_force_turn_in",
                "final_stage": True
            },
            { # Stage 3: Walked Away
                "stage_name": "Khajiit's Fate Sealed",
                "objectives": [
                    {"id": "obj_observe_aftermath", "type": "reach_location", "location_name": "[LOCATION_NAME]", "note": "Return to the scene later to **observe the aftermath** of the interrogation. The Khajiit is gone."}
                ],
                "on_completion_dialogue": "You find no trace of the Khajiit. Perhaps they were taken to Northwatch Keep, or worse. Your inaction has consequences, and the shadows of the Thalmor grow longer. This path ends here.",
                "reward_modifier": {"reputation_khajiit_caravans": -5}, # Minor reputation loss
                "final_stage": True,
                "failure_state": True # Marks this path as a failure of sorts
            }
        ]
    },
    {
        "id": "solitude_east_empire_company_troubles",
        "title_template": "The East Empire's Woes: A Solitude Investigation",
        "desc_template": "The prestigious **East Empire Company**, a cornerstone of Skyrim's maritime trade, faces mounting troubles at its **Solitude Docks** office. Shipments are delayed, goods vanish, and their agents grow increasingly paranoid. They suspect sabotage or a rival company's schemes. Investigate the disruptions, uncover the source of their woes, and restore the flow of vital commerce.",
        "lore_tags": ["solitude", "east_empire_company", "trade_dispute", "sabotage", "investigation", "economic_intrigue", "maritime_commerce"],
        "location_tags_required": ["solitude", "docks_major_port", "east_empire_company_office"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "economic", "intrigue"], "difficulty": ["medium"], "moral": ["gray", "mercenary"]}},
        "turn_in_role_hint": ["east_empire_company_agent", "solitude_jarls_steward"],
        "stages": [
            {
                "stage_name": "A Tangled Web of Trade",
                "objectives": [
                    {"id": "obj_talk_to_agent", "type": "talk_to_npc", "npc_id": "east_empire_company_agent_ID", "note": "Speak with the **East Empire Company agent** at the Solitude Docks office about their troubles."},
                    {"id": "obj_investigate_docks", "type": "investigate", "location_name": "Solitude Docks", "note": "Investigate the **Solitude Docks**, looking for suspicious activity, hidden caches, or disgruntled workers (requires Perception or Sneak check DC 13)."},
                    {"id": "obj_find_smuggler_note_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "smuggler_coded_note", "count": 1, "note": " (Optional) Find a **coded note** hinting at a smuggling operation or a rival's involvement."}}
                ],
                "on_completion_dialogue": "Your investigation reveals a pattern of subtle sabotage and pilfering, orchestrated by a disgruntled former employee now working with local bandits or a rival trade guild. The trail leads to a hidden cave along the coast, **Brinewater Grotto**.",
                "branch_options": []
            },
            {
                "stage_name": "Unmasking the Saboteurs",
                "objectives": [
                    {"id": "obj_reach_brinewater_grotto", "type": "reach_location", "location_name": "Brinewater Grotto", "note": "Infiltrate **Brinewater Grotto**, the coastal cave hideout of the saboteurs."},
                    {"id": "obj_defeat_saboteurs", "type": "kill", "target_name": "smuggler/bandit", "target_id": "smuggler_bandit", "count": 5, "note": "Neutralize the **smugglers and bandits** responsible for the disruptions."},
                    {"id": "obj_retrieve_stolen_manifest", "type": "collect_item", "item_key": "stolen_shipment_manifest", "count": 1, "note": "Retrieve the **stolen shipment manifest** as proof of their crimes."}
                ],
                "on_completion_dialogue": "The smuggling ring is broken, and the East Empire Company's troubles should cease. You have restored order to the docks. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 200, "experience_bonus": 100, "reputation_east_empire_company": 15, "reputation_merchant_guild": 5},
                "final_stage": True
            }
        ]
    },

    # =============================================================================================================
    # THE RIFT SPECIFIC QUESTS (Thieves Guild, Black-Briar, Autumnal Forests)
    # This section has been moved up for better organization and to ensure all holds are covered.
    # =============================================================================================================
    {
        "id": "riften_thieves_guild_initiation",
        "title_template": "A Chance in the Shadows: Riften's Underbelly",
        "desc_template": "The notorious **Thieves Guild of Riften**, masters of shadow and coin, seeks new blood. Brynjolf, their cunning recruiter, offers a test: prove your worth by framing a local merchant to demonstrate your skills in subterfuge and manipulation. This is your opportunity to join the ranks of Skyrim's most infamous criminal organization.",
        "lore_tags": ["riften", "thieves_guild_active", "criminal_initiation", "subterfuge", "deception", "corruption", "black_briar_influence_indirect"],
        "location_tags_required": ["riften", "thieves_guild_hq_active"],
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["infiltration", "deception", "crime"], "difficulty": ["medium"], "moral": ["unethical", "gray"]}},
        "turn_in_role_hint": ["brynjolf_thieves_guild"],
        "stages": [
            {
                "stage_name": "A Test of Cunning",
                "objectives": [
                    {"id": "obj_talk_to_brynjolf", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** in the Riften marketplace to receive your first task."},
                    {"id": "obj_plant_ring", "type": "use_item", "item_key": "stolen_ring_planted", "location_name": "Madesi's Strongbox", "note": "Discreetly **plant a stolen ring** in Madesi's strongbox in the Riften marketplace (requires Sneak or Pickpocket check DC 15)."},
                    {"id": "obj_create_diversion", "type": "event_trigger", "event_type": "marketplace_diversion", "note": "Create a **diversion** in the marketplace to draw attention away from your actions (e.g., pickpocketing, shouting)."}
                ],
                "on_completion_dialogue": "The ring is planted, and the diversion successful. Brynjolf is impressed by your cunning. 'You've got potential, lad/lass. Meet me down in the Ragged Flagon.' Your initiation into the Guild is at hand.",
                "branch_options": []
            },
            {
                "stage_name": "Joining the Shadows",
                "objectives": [
                    {"id": "obj_reach_ragged_flagon", "type": "reach_location", "location_name": "The Ragged Flagon", "note": "Find your way into the **Ragged Flagon**, the hidden tavern beneath Riften."},
                    {"id": "obj_talk_to_brynjolf_ragged_flagon", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** within the Ragged Flagon to officially join the Thieves Guild."}
                ],
                "on_completion_dialogue": "You are now a member of the Thieves Guild, a new life in the shadows begins. Your first true contract awaits. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_thieves_guild": 20, "gold_bonus": 100, "experience_bonus": 80, "item_bonus": "thieves_guild_armor_set"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "riften_black_briar_corruption",
        "title_template": "The Black-Briar's Grip: Unveiling Riften's Corruption",
        "desc_template": "The city of **Riften** groans under the iron fist of **Maven Black-Briar**, whose influence extends into every corner of the city, from the Jarl's court to the Thieves Guild. A desperate citizen or a disgruntled guard seeks your aid to expose her pervasive corruption and loosen her suffocating grip on the city's economy and politics. This is a dangerous game of shadows and power.",
        "lore_tags": ["riften", "black_briar_family", "corruption_political", "economic_monopoly", "city_intrigue", "investigation", "power_struggle", "justice_difficult"],
        "location_tags_required": ["riften", "black_briar_influence_total"],
        "level_range": (10, 18),
        "flavor_tags": {"quest": {"type": ["investigate", "political", "infiltration"], "difficulty": ["hard", "complex"], "moral": ["gray", "justice_challenging"]}},
        "turn_in_role_hint": ["riften_jarl_laila", "disgruntled_guard_riften", "maven_black_briar_rival"],
        "stages": [
            {
                "stage_name": "Whispers of Influence",
                "objectives": [
                    {"id": "obj_talk_to_disgruntled_guard", "type": "talk_to_npc", "npc_id": "riften_guard_disgruntled_ID", "note": "Speak with a **disgruntled Riften guard** who hints at Maven Black-Briar's pervasive influence."},
                    {"id": "obj_infiltrate_meadery_office", "type": "investigate", "location_name": "Black-Briar Meadery (Riften Office)", "note": "Infiltrate the **Black-Briar Meadery's private office** in Riften to find incriminating ledgers or communications (requires Sneak or Lockpicking check DC 16)."},
                    {"id": "obj_bribe_official_optional", "type": "optional", "objective": {"type": "talk_to_npc", "npc_id": "corrupt_city_official_ID", "note": " (Optional) **Bribe a corrupt city official** for information on Maven's dealings (requires Speech/Bribery check DC 15 and gold)."}}
                ],
                "on_completion_dialogue": "You've gathered initial evidence of Maven's widespread corruption. The trail leads to her manor, and perhaps even to the Jarl's court. This is bigger than you thought.",
                "branch_options": []
            },
            {
                "stage_name": "Exposing the Matriarch",
                "objectives": [
                    {"id": "obj_infiltrate_black_briar_manor", "type": "reach_location", "location_name": "Black-Briar Manor", "note": "Infiltrate **Black-Briar Manor**, Maven's heavily guarded residence, to find definitive proof of her illicit activities."},
                    {"id": "obj_collect_incriminating_evidence", "type": "collect_item", "item_key": "maven_black_briar_ledger", "count": 1, "note": "Retrieve **Maven's personal ledger** or a coded message detailing her crimes."},
                    {"id": "obj_confront_maven_optional", "type": "optional", "objective": {"type": "confront", "npc_id": "maven_black_briar_ID", "note": " (Optional) Directly **confront Maven Black-Briar** with the evidence; her reaction may be... illuminating."}}
                ],
                "on_completion_dialogue": "You have the undeniable proof of Maven Black-Briar's corruption. The fate of Riften, and your own standing, depends on how you use this knowledge. Will you expose her, or use it for your own gain?",
                "branch_options": [
                    {"choice_id": "expose_maven_to_jarl", "text": "Present the evidence to Jarl Laila Law-Giver, seeking justice for Riften. (Path of Justice)", "next_stage_index": 2, "consequences": {"reputation_riften_jarl_laila": 20, "reputation_black_briar": -20}},
                    {"choice_id": "blackmail_maven", "text": "Blackmail Maven Black-Briar, leveraging the evidence for personal gain. (Path of Power/Greed)", "next_stage_index": 3, "consequences": {"gold_gain": 500, "reputation_black_briar": 10, "reputation_riften_citizens": -5}}
                ]
            },
            { # Stage 2: Expose Maven to Jarl
                "stage_name": "Riften's Reckoning",
                "objectives": [
                    {"id": "obj_present_evidence_to_jarl", "type": "talk_to_npc", "npc_id": "jarl_laila_law_giver_ID", "note": "Present the **incriminating evidence to Jarl Laila Law-Giver** in Mistveil Keep."}
                ],
                "on_completion_dialogue": "Jarl Laila is shocked and enraged by the undeniable proof of Maven's treachery. Maven's power in Riften is broken, though her influence may linger. You have brought a new dawn to Riften. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 300, "experience_bonus": 150, "reputation_riften_jarl_laila": 25, "reputation_riften_citizens": 15},
                "final_stage": True
            },
            { # Stage 3: Blackmail Maven
                "stage_name": "A Shadowy Alliance",
                "objectives": [
                    {"id": "obj_blackmail_maven_direct", "type": "talk_to_npc", "npc_id": "maven_black_briar_ID", "note": "Confront **Maven Black-Briar** with the evidence and demand your price."}
                ],
                "on_completion_dialogue": "Maven, seething with silent fury, agrees to your terms. You now have a powerful, dangerous ally in Riften, but the city's corruption remains. You walk a path of shadows and influence. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 750, "experience_bonus": 100, "reputation_black_briar": 15, "reputation_thieves_guild": 10},
                "final_stage": True,
                "failure_state": True # Failure to the original quest giver, but success for this path
            }
        ]
    },
    {
        "id": "riften_lost_prospect_mine",
        "title_template": "The Prospector's Plea: Lost Gold of the Rift",
        "desc_template": "The once-promising **Lost Prospect Mine** in the Rift, rumored to hold rich gold veins, has fallen silent. Its prospector, a hopeful but naive Nord, fears it's overrun by monstrous spiders or bandits. Reclaim the mine, clear its depths of any threats, and perhaps, rediscover its golden promise.",
        "lore_tags": ["the_rift", "mine_gold_abandoned", "spider_infestation_potential", "bandit_lair_potential", "reclamation", "economic_opportunity"],
        "location_tags_required": ["mine_abandoned_gold", "spider_infestation_potential"],
        "level_range": (3, 8),
        "flavor_tags": {"quest": {"type": ["clear", "reclaim", "economic"], "difficulty": ["medium"], "moral": ["ethical", "mercenary"]}},
        "turn_in_role_hint": ["riften_prospector", "riften_jarls_steward"],
        "stages": [
            {
                "stage_name": "A Silent Promise",
                "objectives": [
                    {"id": "obj_talk_to_prospector", "type": "talk_to_npc", "npc_id": "riften_prospector_ID", "note": "Speak with the **anxious prospector** in Riften about the abandoned Lost Prospect Mine."},
                    {"id": "obj_reach_lost_prospect_mine", "type": "reach_location", "location_name": "Lost Prospect Mine", "note": "Travel to the deserted **Lost Prospect Mine** and assess the situation."}
                ],
                "on_completion_dialogue": "The mine's entrance is eerily quiet, save for the faint scuttling sounds from within. It's infested, just as the prospector feared. You must clear it.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Veins",
                "objectives": [
                    {"id": "obj_clear_spiders_or_bandits", "type": "kill", "target_name": "giant frostbite spider", "target_id": "giant_frostbite_spider", "count": 8, "note": "Clear the mine of its **monstrous spider infestation** (or bandits, if they've taken over)."},
                    {"id": "obj_find_gold_vein_optional", "type": "optional", "objective": {"type": "investigate", "object": "hidden_gold_vein", "note": " (Optional) Search for a **hidden, rich gold vein** deep within the mine (requires Mining check DC 14)."}}
                ],
                "on_completion_dialogue": "The mine is clear! The gnawing threat is gone, and the prospector can return. You may have even found a hidden fortune. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 150, "experience_bonus": 75, "reputation_local_bonus": 8},
                "final_stage": True
            }
        ]
    },
    
    # =============================================================================================================
    # HAAFINGAR SPECIFIC QUESTS (Imperial, Solitude, Bards College, Coastal)
    # =============================================================================================================
    {
        "id": "solitude_bards_college_recruitment",
        "title_template": "The Bard's Calling: Solitude's New Voice",
        "desc_template": "The esteemed **Bards College in Solitude**, the heart of Skyrim's musical and historical tradition, is always seeking new talent. They offer a unique opportunity to those with a flair for performance, lore, or even subtle deception. Join their ranks, contribute to their legacy, and perhaps even uncover ancient secrets through song and story.",
        "lore_tags": ["solitude", "bards_college_active", "music_lore", "performance", "recruitment", "cultural_institution", "historic_preservation"],
        "location_tags_required": ["solitude", "bards_college"],
        "level_range": (1, 6),
        "flavor_tags": {"quest": {"type": ["social", "performance", "knowledge"], "difficulty": ["easy", "medium"], "moral": ["ethical", "artistic"]}},
        "turn_in_role_hint": ["viola_giordano", "jorn_bards_college"],
        "stages": [
            {
                "stage_name": "An Audition of Talent",
                "objectives": [
                    {"id": "obj_talk_to_viola", "type": "talk_to_npc", "npc_id": "viola_giordano_ID", "note": "Speak with **Viola Giordano**, one of the College's instructors, about joining."},
                    {"id": "obj_perform_for_audition", "type": "skill_check", "skill": "speech", "dc": 10, "note": "Perform a **short piece or recite a tale** for an audition (requires Speech or Persuasion check DC 10)."}
                ],
                "on_completion_dialogue": "Your performance (or convincing words) has impressed the College. They offer you a chance to prove your dedication by recovering a lost instrument or a forgotten ballad. Your choice: a lute or a song?",
                "branch_options": [
                    {"choice_id": "recover_instrument", "text": "Agree to recover a **lost ancient lute** from a nearby ruin. (Path of Action)", "next_stage_index": 1},
                    {"choice_id": "find_forgotten_ballad", "text": "Agree to find and transcribe a **forgotten ballad** from a reclusive scholar. (Path of Lore)", "next_stage_index": 2}
                ]
            },
            { # Stage 1: Recover Instrument Path
                "stage_name": "The Lost Melody",
                "objectives": [
                    {"id": "obj_reach_instrument_ruin", "type": "reach_location", "location_name": "Lost Instrument Ruin", "note": "Travel to the designated **ruin** where the ancient lute is said to be hidden."},
                    {"id": "obj_collect_instrument", "type": "collect_item", "item_key": "ancient_lute_bards", "count": 1, "note": "Retrieve the **ancient lute** from the ruin's depths."}
                ],
                "on_completion_dialogue": "The lute is recovered, its strings still humming with faint magic. You've proven your dedication. Return to [QUEST_GIVER_NAME] at the Bards College.",
                "reward_modifier": {"reputation_bards_college": 10, "gold_bonus": 75, "experience_bonus": 40, "item_bonus": "bards_college_lute"},
                "final_stage": True
            },
            { # Stage 2: Find Forgotten Ballad Path
                "stage_name": "The Forgotten Verse",
                "objectives": [
                    {"id": "obj_reach_scholar_hermitage", "type": "reach_location", "location_name": "Reclusive Scholar's Hermitage", "note": "Journey to the **hermitage of a reclusive scholar** who might know the forgotten ballad."},
                    {"id": "obj_talk_to_scholar_ballad", "type": "talk_to_npc", "npc_id": "reclusive_scholar_ID", "note": "Persuade the **scholar** to share the forgotten ballad (requires Speech/Persuasion check DC 12)."},
                    {"id": "obj_transcribe_ballad", "type": "event_trigger", "event_type": "transcribe_ballad", "note": "Successfully **transcribe the forgotten ballad** into your journal."}
                ],
                "on_completion_dialogue": "The forgotten ballad is now preserved in your journal, its verses echoing with ancient wisdom. You've proven your dedication to lore. Return to [QUEST_GIVER_NAME] at the Bards College.",
                "reward_modifier": {"reputation_bards_college": 12, "gold_bonus": 50, "experience_bonus": 60, "item_bonus": "rare_songbook"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "solitude_thalmor_interrogation",
        "title_template": "The Thalmor's Reach: A Diplomatic Incident",
        "desc_template": "A **Khajiit traveler** has been apprehended by a zealous **Thalmor patrol** near **[LOCATION_NAME]**, suspected of Talos worship or illicit trade. The situation is tense, threatening to escalate into a diplomatic incident or worse. You are presented with a moral dilemma: intervene on behalf of the Khajiit, or allow the Justiciars to proceed with their grim work, perhaps even aiding them for a price.",
        "lore_tags": ["haafingar", "thalmor_presence_active", "white_gold_concordat_enforcement", "talos_ban", "political_tension", "khajiit_victim", "moral_choice_event", "diplomacy_conflict"],
        "location_tags_required": ["road", "imperial_presence_strong", "thalmor_presence_city"], # Can be triggered by random encounter
        "level_range": (6, 12),
        "flavor_tags": {"quest": {"type": ["rescue", "spy", "diplomacy"], "moral": ["gray", "political_choice"], "urgency": ["urgent", "tense"]}},
        "turn_in_role_hint": ["jarl_torygg", "khajiit_caravan_leader", "thalmor_justiciar"], # Can turn into different quest lines
        "stages": [
            {
                "stage_name": "Witness Interrogation",
                "objectives": [
                    {"id": "obj_witness_interrogation", "type": "talk_to_npc", "npc_id": "thalmor_justiciar_interrogator_ID", "note": "Witness the tense **interrogation between a Thalmor Justiciar and a frightened Khajiit**."},
                    {"id": "obj_observe_situation", "type": "skill_check", "skill": "perception", "dc": 12, "note": "Carefully **observe the situation** for additional details or weaknesses (requires Perception check DC 12)."}
                ],
                "on_completion_dialogue": "The Justiciar's cold eyes meet yours. The fate of the Khajiit hangs in the balance. Will you intervene, or walk away?",
                "branch_options": [
                    {"choice_id": "intervene_speech", "text": "Attempt to **intervene using persuasion**, arguing for the Khajiit's release. (Speech/Persuasion DC 15)", "next_stage_index": 1, "consequences": {"skill_challenge": "speech", "disposition_change_thalmor": -5}},
                    {"choice_id": "intervene_force", "text": "Intervene by **force**, attacking the Thalmor to free the Khajiit. (Direct Confrontation)", "next_stage_index": 2, "consequences": {"faction_hostility": "thalmor"}},
                    {"choice_id": "walk_away", "text": "Simply **walk away**, leaving the Khajiit to their grim fate. (Neutral/Self-Preservation)", "next_stage_index": 3}
                ]
            },
            { # Stage 1: Intervened (Speech)
                "stage_name": "Negotiate Release",
                "objectives": [
                    {"id": "obj_persuade_justiciar", "type": "skill_check", "skill": "speech", "dc": 15, "note": "Successfully **persuade the Justiciar** to release the Khajiit, perhaps with a fabricated story or a clever argument."},
                    {"id": "obj_talk_to_freed_khajiit", "type": "talk_to_npc", "npc_id": "khajiit_traveler_frightened_ID", "note": "Speak to the **freed Khajiit**; they will surely be grateful."}
                ],
                "on_completion_dialogue": "You successfully negotiated the Khajiit's release. He thanks you profusely, promising to speak well of you to his caravan. Your discretion is noted by the Thalmor, though they remain wary. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_khajiit_caravans": 10, "gold_bonus": 100, "experience_bonus": 50},
                "turn_in_dialogue_key": "thalmor_interrogation_success_speech_turn_in", # Custom turn-in dialogue key
                "final_stage": True
            },
            { # Stage 2: Intervened (Force)
                "stage_name": "Combat with Thalmor",
                "objectives": [
                    {"id": "obj_defeat_thalmor_patrol", "type": "kill", "target_name": "thalmor", "target_id": "thalmor_justiciar", "count": 1, "note": "Engage and **defeat the Thalmor patrol** to free the Khajiit."},
                    {"id": "obj_free_khajiit_combat", "type": "talk_to_npc", "npc_id": "khajiit_traveler_frightened_ID", "note": "Ensure the **Khajiit is truly free** after the skirmish."}
                ],
                "on_completion_dialogue": "You have fought off the Thalmor. The Khajiit is free, but you've made powerful enemies in the Aldmeri Dominion. Your name will be known, for better or worse. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_stormcloaks": 15, "reputation_thalmor": -25, "gold_bonus": 150, "experience_bonus": 75},
                "turn_in_dialogue_key": "thalmor_interrogation_success_force_turn_in",
                "final_stage": True
            },
            { # Stage 3: Walked Away
                "stage_name": "Khajiit's Fate Sealed",
                "objectives": [
                    {"id": "obj_observe_aftermath", "type": "reach_location", "location_name": "[LOCATION_NAME]", "note": "Return to the scene later to **observe the aftermath** of the interrogation. The Khajiit is gone."}
                ],
                "on_completion_dialogue": "You find no trace of the Khajiit. Perhaps they were taken to Northwatch Keep, or worse. Your inaction has consequences, and the shadows of the Thalmor grow longer. This path ends here.",
                "reward_modifier": {"reputation_khajiit_caravans": -5}, # Minor reputation loss
                "final_stage": True,
                "failure_state": True # Marks this path as a failure of sorts
            }
        ]
    },
    {
        "id": "solitude_east_empire_company_troubles",
        "title_template": "The East Empire's Woes: A Solitude Investigation",
        "desc_template": "The prestigious **East Empire Company**, a cornerstone of Skyrim's maritime trade, faces mounting troubles at its **Solitude Docks** office. Shipments are delayed, goods vanish, and their agents grow increasingly paranoid. They suspect sabotage or a rival company's schemes. Investigate the disruptions, uncover the source of their woes, and restore the flow of vital commerce.",
        "lore_tags": ["solitude", "east_empire_company", "trade_dispute", "sabotage", "investigation", "economic_intrigue", "maritime_commerce"],
        "location_tags_required": ["solitude", "docks_major_port", "east_empire_company_office"],
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "economic", "intrigue"], "difficulty": ["medium"], "moral": ["gray", "mercenary"]}},
        "turn_in_role_hint": ["east_empire_company_agent", "solitude_jarls_steward"],
        "stages": [
            {
                "stage_name": "A Tangled Web of Trade",
                "objectives": [
                    {"id": "obj_talk_to_agent", "type": "talk_to_npc", "npc_id": "east_empire_company_agent_ID", "note": "Speak with the **East Empire Company agent** at the Solitude Docks office about their troubles."},
                    {"id": "obj_investigate_docks", "type": "investigate", "location_name": "Solitude Docks", "note": "Investigate the **Solitude Docks**, looking for suspicious activity, hidden caches, or disgruntled workers (requires Perception or Sneak check DC 13)."},
                    {"id": "obj_find_smuggler_note_optional", "type": "optional", "objective": {"type": "collect_item", "item_key": "smuggler_coded_note", "count": 1, "note": " (Optional) Find a **coded note** hinting at a smuggling operation or a rival's involvement."}}
                ],
                "on_completion_dialogue": "Your investigation reveals a pattern of subtle sabotage and pilfering, orchestrated by a disgruntled former employee now working with local bandits or a rival trade guild. The trail leads to a hidden cave along the coast, **Brinewater Grotto**.",
                "branch_options": []
            },
            {
                "stage_name": "Unmasking the Saboteurs",
                "objectives": [
                    {"id": "obj_reach_brinewater_grotto", "type": "reach_location", "location_name": "Brinewater Grotto", "note": "Infiltrate **Brinewater Grotto**, the coastal cave hideout of the saboteurs."},
                    {"id": "obj_defeat_saboteurs", "type": "kill", "target_name": "smuggler/bandit", "target_id": "smuggler_bandit", "count": 5, "note": "Neutralize the **smugglers and bandits** responsible for the disruptions."},
                    {"id": "obj_retrieve_stolen_manifest", "type": "collect_item", "item_key": "stolen_shipment_manifest", "count": 1, "note": "Retrieve the **stolen shipment manifest** as proof of their crimes."}
                ],
                "on_completion_dialogue": "The smuggling ring is broken, and the East Empire Company's troubles should cease. You have restored order to the docks. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 200, "experience_bonus": 100, "reputation_east_empire_company": 15, "reputation_merchant_guild": 5},
                "final_stage": True
            }
        ]
    }
]

# Function to generate location-appropriate quest (updated to use stages)
def generate_location_appropriate_quest(player_level: int, current_location_obj: Dict[str, Any], quest_giver_id: str | None = None) -> Quest | None:
    """
    Generates a quest based on player level and current location tags.
    Prioritizes specific quests for the current location, then general ones.
    """
    possible_templates = []
    
    # Extract relevant tags from current_location_obj and its parent hold
    location_tags = set(current_location_obj.get("tags", []))
    # If the current location is a sub-location, add parent hold tags as well
    if "parent_name" in current_location_obj:
        for hold in LOCATIONS:
            if hold["name"] == current_location_obj["parent_name"] or \
               any(sub_loc.get("parent_name") == current_location_obj["parent_name"] for sub_loc in hold.get("sub_locations", [])):
                location_tags.update(hold.get("tags", []))
                break

    # First, prioritize quests specifically designed for this exact location or its direct parent city/town
    for template in QUEST_TEMPLATES:
        template_id_str = str(template["id"])

        # Check level range
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]):
            continue

        # Check for direct location name match in template ID (e.g., "whiterun_investigation_grisly_murders")
        # and ensure at least one required tag matches the current location's tags.
        if template_id_str.startswith(current_location_obj["name"].lower().replace(" ", "_")):
            template_tags_required = template.get("location_tags_required", [])
            if any(tag in location_tags for tag in template_tags_required):
                possible_templates.append(template)
                continue # Prioritize these unique quests

    # If no highly specific quests found, consider all quests that match at least one tag of the current location/hold
    if not possible_templates:
        for template in QUEST_TEMPLATES:
            if not (template["level_range"][0] <= player_level <= template["level_range"][1]):
                continue

            if template["location_tags_required"]:
                if any(tag in location_tags for tag in template["location_tags_required"]):
                    possible_templates.append(template)
            else: # If a template has no required location tags, it's generic and always possible
                possible_templates.append(template)
    
    if not possible_templates:
        UI.print_system_message(f"DEBUG: No specific quest template matched for level {player_level} and tags {list(location_tags)}. Generating generic fallback quest.")
        # Fallback to a generic quest if no templates match
        chosen_location = current_location_obj # Use current location as fallback
        title = f"A Minor Task in {chosen_location.get('name', 'the area')}"
        description = f"A local resident needs a small favor in {chosen_location.get('name', 'this area')}. It might involve a quick delivery or finding a lost item nearby."
        stages = [{"stage_name": "Completion", "objectives": [{"id": "generic_obj_1", "type": "reach_location", "location_name": chosen_location["name"], "note": "Complete the simple errand as requested."}]}]
        reward = generate_reward(player_level, list(location_tags))
        
        quest = Quest(
            title=title,
            description=description,
            reward=reward,
            level_requirement=player_level,
            location=chosen_location,
            stages=stages,
            status="active",
            turn_in_npc_id=quest_giver_id
        )
        quest.add_tag("quest", "type", "generic")
        return quest

    chosen_template = random.choice(possible_templates)

    # Resolve dynamic location names for the quest
    final_quest_location = current_location_obj # Default to current location for the quest object

    # Attempt to find a more specific location if the template requests it and it's not the current one
    if "location_tags_required" in chosen_template:
        specific_loc_candidates = []
        for tag in chosen_template["location_tags_required"]:
            specific_loc_candidates.extend(find_locations_by_tag(tag))
        
        # Filter candidates to prefer locations within the current hold or directly nearby
        filtered_candidates = []
        current_hold_name = current_location_obj.get("parent_name") if "parent_name" in current_location_obj else current_location_obj["name"]
        
        for cand in specific_loc_candidates:
            if cand["name"] == current_location_obj["name"]: # Always prefer the current location if it matches tags
                filtered_candidates.append(cand)
                break # Found the best match
            elif "parent_name" in cand and cand["parent_name"] == current_hold_name:
                filtered_candidates.append(cand)
            # Add logic here for 'nearby' holds if necessary, but keep it constrained
        
        if filtered_candidates:
            final_quest_location = random.choice(filtered_candidates)
        elif specific_loc_candidates: # If no local matches, pick any matching tagged location
            final_quest_location = random.choice(specific_loc_candidates)
        # If still no specific location, fallback to current_location_obj (already set)

    title = chosen_template["title_template"].replace("[LOCATION_NAME]", final_quest_location["name"])
    title = title.replace("[FARM_NAME]", final_quest_location["name"]) 
    title = title.replace("[TRADE_ROUTE_NAME]", final_quest_location["name"])
    title = title.replace("[CITY_NAME]", final_quest_location["name"])
    title = title.replace("[RUIN_NAME]", final_quest_location["name"])
    title = title.replace("[MOUNTAIN_NAME]", final_quest_location["name"])
    title = title.replace("[VILLAGE_NAME]", final_quest_location["name"])
    title = title.replace("[MINE_NAME]", final_quest_location["name"])
    title = title.replace("[ACADEMIC_INSTITUTION]", final_quest_location["name"])

    description = chosen_template["desc_template"].replace("[LOCATION_NAME]", final_quest_location["name"])
    description = description.replace("[FARM_NAME]", final_quest_location["name"])
    description = description.replace("[TRADE_ROUTE_NAME]", final_quest_location["name"])
    description = description.replace("[CITY_NAME]", final_quest_location["name"])
    description = description.replace("[RUIN_NAME]", final_quest_location["name"])
    description = description.replace("[MOUNTAIN_NAME]", final_quest_location["name"])
    description = description.replace("[VILLAGE_NAME]", final_quest_location["name"])
    description = description.replace("[MINE_NAME]", final_quest_location["name"])
    description = description.replace("[ACADEMIC_INSTITUTION]", final_quest_location["name"])

    # Determine dynamic names for NPCs and other elements within descriptions
    if "[ALCHEMIST_NAME]" in description:
        npc_info = get_npc_name_by_role_hint("alchemist")
        description = description.replace("[ALCHEMIST_NAME]", npc_info["name"])
    if "[FARMER1_NAME]" in description:
        farmer1_info = get_npc_name_by_role_hint("farmer")
        description = description.replace("[FARMER1_NAME]", farmer1_info["name"])
    if "[FARMER2_NAME]" in description:
        farmer2_info = get_npc_name_by_role_hint("farmer")
        description = description.replace("[FARMER2_NAME]", farmer2_info["name"])
    if "[DESTINATION_CITY]" in description:
        possible_dest_cities = [loc for loc in LOCATIONS if "city" in loc.get("tags", []) and loc["name"] != final_quest_location["name"]]
        if possible_dest_cities:
            chosen_dest_city = random.choice(possible_dest_cities)
            description = description.replace("[DESTINATION_CITY]", chosen_dest_city["name"])
            for stage_idx, stage in enumerate(chosen_template["stages"]):
                for obj_idx, obj in enumerate(stage.get("objectives", [])):
                    if obj.get("destination") == "[DESTINATION_CITY]":
                        chosen_template["stages"][stage_idx]["objectives"][obj_idx]["destination"] = chosen_dest_city["name"]
                    if obj.get("location_name") == "[DESTINATION_CITY]":
                         chosen_template["stages"][stage_idx]["objectives"][obj_idx]["location_name"] = chosen_dest_city["name"]
        else:
            description = description.replace("[DESTINATION_CITY]", "a distant city")

    # Resolve dynamic names and locations within stages (objectives, dialogue, etc.)
    processed_stages = []
    for stage_template in chosen_template["stages"]:
        processed_stage = stage_template.copy()
        processed_stage_objectives = []

        for obj_template in stage_template.get("objectives", []):
            processed_obj = obj_template.copy()
            if "note" in processed_obj and isinstance(processed_obj["note"], str):
                processed_obj["note"] = processed_obj["note"].replace("[LOCATION_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[FARM_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[TRADE_ROUTE_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[CITY_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[RUIN_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[MOUNTAIN_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[VILLAGE_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[MINE_NAME]", final_quest_location["name"])
                processed_obj["note"] = processed_obj["note"].replace("[ACADEMIC_INSTITUTION]", final_quest_location["name"])
                
                # Dynamic NPC names in notes
                if "[ALCHEMIST_NAME]" in processed_obj["note"]:
                    alchemist_info = get_npc_name_by_role_hint("alchemist")
                    processed_obj["note"] = processed_obj["note"].replace("[ALCHEMIST_NAME]", alchemist_info["name"])
                if "[THIEF_NAME]" in processed_obj["note"]:
                    thief_info = get_npc_name_by_role_hint("thief")
                    processed_obj["note"] = processed_obj["note"].replace("[THIEF_NAME]", thief_info["name"])
                    if processed_obj.get("type") == "confront":
                        processed_obj["npc_id"] = thief_info["id"]
                if "[GHOST_NAME]" in processed_obj["note"]:
                    ghost_info = get_npc_name_by_role_hint("spirit") 
                    processed_obj["note"] = processed_obj["note"].replace("[GHOST_NAME]", ghost_info["name"])
                    if processed_obj.get("type") == "talk_to_npc" and processed_obj.get("npc_id") == "[GHOST_NAME_ID]":
                        processed_obj["npc_id"] = ghost_info["id"]
                
                # Special NPC names for new quests
                if "[ANCIENT_SWORD_NAME]" in processed_obj["note"]:
                    processed_obj["note"] = processed_obj["note"].replace("[ANCIENT_SWORD_NAME]", random.choice(["Dragonbane", "Blade of Woe", "Ghostblade", "Harkon's Sword"])) # Example names
                if "[LUMBERJACK_NAME]" in processed_obj["note"]:
                    processed_obj["note"] = processed_obj["note"].replace("[LUMBERJACK_NAME]", get_npc_name_by_role_hint("lumberjack")["name"])


            if "location_name" in processed_obj and isinstance(processed_obj["location_name"], str):
                processed_obj["location_name"] = processed_obj["location_name"].replace("[LOCATION_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[FARM_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[TRADE_ROUTE_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[CITY_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[RUIN_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[MOUNTAIN_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[VILLAGE_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[MINE_NAME]", final_quest_location["name"])
                processed_obj["location_name"] = processed_obj["location_name"].replace("[ACADEMIC_INSTITUTION]", final_quest_location["name"])
                
                # Specific locations based on context (e.g., ambush site, cave type)
                if "[AMBUSH_SITE_NAME]" in processed_obj["location_name"]:
                    ambush_sites = find_locations_by_tag("road_ambush_site") + find_locations_by_tag("bandit_camp")
                    if ambush_sites:
                        processed_obj["location_name"] = random.choice(ambush_sites)["name"]
                    else:
                        processed_obj["location_name"] = "a desolate roadside"
                if "[CAVE_TYPE]" in processed_obj["location_name"]:
                    cave_types = find_locations_by_tag("cave")
                    if cave_types:
                        processed_obj["location_name"] = random.choice(cave_types)["name"]
                    else:
                        processed_obj["location_name"] = "a shadowy cave"
                if "[WILDERNESS_TYPE]" in processed_obj["location_name"]:
                    wilderness_types = find_locations_by_tag("forest") + find_locations_by_tag("plains") + find_locations_by_tag("mountain")
                    if wilderness_types:
                        processed_obj["location_name"] = random.choice(wilderness_types)["name"]
                    else:
                        processed_obj["location_name"] = "the wilderness"


            # Resolve NPC IDs for "talk_to_npc" objectives
            if "npc_id" in processed_obj and processed_obj["npc_id"].endswith("_ID"):
                role_hint_or_specific_id = processed_obj["npc_id"].replace("_ID", "")
                npc_info = get_npc_name_by_role_hint(role_hint_or_specific_id)
                processed_obj["npc_id"] = npc_info["id"] # The unique_id from NAME_POOLS
                if "npc_name" in processed_obj: # Also update display name if it was a placeholder
                    processed_obj["npc_name"] = npc_info["name"]

            # Resolve target_id for "kill" objectives if it's a placeholder
            if processed_obj.get("type") == "kill" and processed_obj.get("target_id") and processed_obj["target_id"].endswith("_ID"):
                role_hint = processed_obj["target_id"].replace("_ID", "")
                npc_info = get_npc_name_by_role_hint(role_hint)
                processed_obj["target_id"] = npc_info["id"] # Use the generic unique ID for tracking specific enemy types


            processed_stage_objectives.append(processed_obj)
        processed_stage["objectives"] = processed_stage_objectives

        # Process on_completion_dialogue
        if "on_completion_dialogue" in processed_stage and isinstance(processed_stage["on_completion_dialogue"], str):
             processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[QUEST_GIVER_NAME]", quest_giver_id.split('_')[0].capitalize() if quest_giver_id else "your benefactor")
             processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[LOCATION_NAME]", final_quest_location["name"])
             processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[AMBUSH_SITE_NAME]", processed_stage_objectives[0].get("location_name", "the ambush site"))
             
             # Dynamic NPC names in dialogue
             if "[ALCHEMIST_NAME]" in processed_stage["on_completion_dialogue"]:
                 alchemist_info = get_npc_name_by_role_hint("alchemist")
                 processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[ALCHEMIST_NAME]", alchemist_info["name"])
             if "[THIEF_NAME]" in processed_stage["on_completion_dialogue"]:
                 thief_info = get_npc_name_by_role_hint("thief")
                 processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[THIEF_NAME]", thief_info["name"])
             if "[GHOST_NAME]" in processed_stage["on_completion_dialogue"]:
                 ghost_info = get_npc_name_by_role_hint("spirit")
                 processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[GHOST_NAME]", ghost_info["name"])
             if "[GHOST_DESIRE]" in processed_stage["on_completion_dialogue"]:
                 processed_stage["on_completion_dialogue"] = processed_stage["on_completion_dialogue"].replace("[GHOST_DESIRE]", random.choice(["to find its lost love", "to retrieve a buried treasure", "to clear its name", "to seek vengeance on its killer", "to protect a hidden secret"])) 

        # Resolve branching options if they contain placeholders
        if "branch_options" in processed_stage:
            processed_branch_options = []
            for option in processed_stage["branch_options"]:
                processed_option = option.copy()
                processed_option["text"] = processed_option["text"].replace("[LOCATION_NAME]", final_quest_location["name"])
                processed_branch_options.append(processed_option)
            processed_stage["branch_options"] = processed_branch_options

        processed_stages.append(processed_stage)


    reward = generate_reward(player_level, chosen_template.get("reward_tags", []))
    
    quest_tags = chosen_template.get("lore_tags", [])
    initial_flavor_text = ""
    if "flavor_tags" in chosen_template:
        dummy_quest_for_flavor = DummyRumor()
        for category, types_dict in chosen_template["flavor_tags"].items():
            for tag_type, tags_list in types_dict.items():
                dummy_quest_for_flavor.add_tag(category, tag_type, random.choice(tags_list))

        retrieved_flavors = flavor.get_flavor(dummy_quest_for_flavor)
        if retrieved_flavors:
            initial_flavor_text = random.choice(retrieved_flavors)

    quest = Quest(
        quest_id=chosen_template["id"], 
        title=title,
        description=description,
        reward=reward,
        level_requirement=player_level,
        location=final_quest_location,
        stages=processed_stages,
        status="active",
        turn_in_npc_id=quest_giver_id,
        initial_flavor_text=initial_flavor_text
    )

    for lore_tag in quest_tags:
        quest.add_tag("quest", "lore", lore_tag) 

    if "flavor_tags" in chosen_template and "quest" in chosen_template["flavor_tags"] and "type" in chosen_template["flavor_tags"]["quest"]:
        quest.add_tag("quest", "type", random.choice(chosen_template["flavor_tags"]["quest"]["type"]))


    return quest

# Process quest rewards (from your original code)
def process_quest_rewards(player: Any, quest: Quest) -> None:
    UI.print_subheading(f"Quest Completed: {quest.title}!")
    UI.slow_print("You have received your rewards:")

    # Apply base rewards
    for reward_type, reward_value in quest.reward.items():
        if reward_type == "gold":
            player.stats.gold += reward_value
            UI.print_success(f"- {reward_value} Gold.")
        elif reward_type == "experience":
            player.gain_experience(reward_value)
            UI.print_success(f"- {reward_value} Experience.")
        elif reward_type == "item" and isinstance(reward_value, Item):
            if player.add_item(reward_value):
                UI.print_success(f"- {reward_value.name} (Item).")
            else:
                UI.print_warning(f"- You found {reward_value.name}, but your inventory is full!")
        elif reward_type == "reputation":
            UI.print_success(f"- {reward_value} Reputation with local factions.") # Generic, could specify
        elif reward_type == "favor":
            UI.print_success(f"- A favor {reward_value}.")

    # Apply reward modifiers based on quest choices/paths (if any)
    if quest.current_stage and "reward_modifier" in quest.current_stage:
        modifier = quest.current_stage["reward_modifier"]
        if "gold_bonus" in modifier:
            player.stats.gold += modifier["gold_bonus"]
            UI.print_success(f"- {modifier['gold_bonus']} bonus Gold (from your choices!).")
        
        # Specific faction reputation changes (examples, expand as needed)
        if "reputation_merchant_guild_bonus" in modifier:
            player.faction_reputation["merchant_guild"] = player.faction_reputation.get("merchant_guild", 0) + modifier["reputation_merchant_guild_bonus"]
            UI.print_success(f"- {modifier['reputation_merchant_guild_bonus']} Reputation with the Merchant's Guild.")
        if "reputation_thieves_guild" in modifier: # Can be + or -
            player.faction_reputation["thieves_guild"] = player.faction_reputation.get("thieves_guild", 0) + modifier["reputation_thieves_guild"]
            UI.print_success(f"- {modifier['reputation_thieves_guild']} Reputation with the Thieves Guild.")
        if "reputation_jarl_bonus" in modifier:
            player.faction_reputation["jarl"] = player.faction_reputation.get("jarl", 0) + modifier["reputation_jarl_bonus"]
            UI.print_success(f"- {modifier['reputation_jarl_bonus']} Reputation with the Jarl.")
        if "reputation_tribal_bonus" in modifier:
            player.faction_reputation["tribal"] = player.faction_reputation.get("tribal", 0) + modifier["reputation_tribal_bonus"]
            UI.print_success(f"- {modifier['reputation_tribal_bonus']} Reputation with the local tribe.")
        if "reputation_scholar_bonus" in modifier:
            player.faction_reputation["scholar"] = player.faction_reputation.get("scholar", 0) + modifier["reputation_scholar_bonus"]
            UI.print_success(f"- {modifier['reputation_scholar_bonus']} Reputation with Scholars.")
        if "reputation_alchemist_bonus" in modifier:
            player.faction_reputation["alchemist"] = player.faction_reputation.get("alchemist", 0) + modifier["reputation_alchemist_bonus"]
            UI.print_success(f"- {modifier['reputation_alchemist_bonus']} Reputation with Alchemists.")
        if "reputation_spiritual_bonus" in modifier:
            player.faction_reputation["spiritual"] = player.faction_reputation.get("spiritual", 0) + modifier["reputation_spiritual_bonus"]
            UI.print_success(f"- {modifier['reputation_spiritual_bonus']} Reputation with Spiritual Orders.")

        if "experience_bonus" in modifier:
            player.gain_experience(modifier["experience_bonus"])
            UI.print_success(f"- {modifier['experience_bonus']} bonus Experience.")
        if "item_bonus" in modifier:
            bonus_item = generate_item_from_key(modifier["item_bonus"], player.level)
            if bonus_item and player.add_item(bonus_item):
                UI.print_success(f"- Bonus item: {bonus_item.name}!")
            elif bonus_item:
                 UI.print_warning(f"- You found a bonus {bonus_item.name}, but your inventory is full!")
        if "unique_item_sealed_idol" in modifier:
            # Generate the specific unique item. This assumes you have a key for it.
            unique_item = generate_item_from_key(modifier["unique_item_sealed_idol"], player.level)
            if unique_item and player.add_item(unique_item):
                UI.print_success(f"- Unique Item: {unique_item.name} - a symbol of your achievement!")
            elif unique_item:
                UI.print_warning(f"- You earned the {unique_item.name}, but your inventory is full!")
        if "alchemy_skill_gain_bonus" in modifier:
            player.improve_skill("alchemy", modifier["alchemy_skill_gain_bonus"])
            UI.print_success(f"- Your Alchemy skill increased by {modifier['alchemy_skill_gain_bonus']}!")
        
    UI.press_enter()