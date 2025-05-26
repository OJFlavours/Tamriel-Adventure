# rumors.py
import random
from typing import List, Dict, Any
from locations import LOCATIONS
import tags
import flavor
from items import Item, generate_random_item as gr_item_func, generate_item_from_key

# Constant defined for quest rewards
QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item_quality_levels": {
        (1, 5): ["common", "uncommon"],
        (6, 10): ["uncommon", "rare"],
        (11, 20): ["rare", "epic"],
        (21, 99): ["epic", "legendary"]
    },
    "reputation": {"min": 5, "max": 15},
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold"]
}

# Quest templates for diverse, lore-friendly quests
QUEST_TEMPLATES = [
    {
        "id": "clear_bandit_camp",
        "title_template": "Bandit Menace at [LOCATION_NAME]",
        "desc_template": "A group of ruthless bandits has set up a camp near [LOCATION_NAME], preying on travelers and merchants. Eliminate the bandit leader and his thugs to restore safety.",
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
    {
        "id": "ancient_relic_retrieval",
        "title_template": "The Echoes of Saarthal",
        "desc_template": "An ancient Nordic relic has been reported deep within Saarthal. Retrieve the Glyph and return it to the College of Winterhold.",
        "objectives_template": [
            {"type": "reach_location", "location_name": "Saarthal"},
            {"type": "collect_item", "item_key": "glyph_of_unraveling", "count": 1},
            {"type": "kill", "target_name": "draugr death overlord", "target_id": "draugr_death_overlord", "count": 1}
        ],
        "reward_tags": ["gold", "experience", "unique_spell_tome"],
        "lore_tags": ["saarthal", "ancient_nords", "magic", "mages_guild"],
        "location_tags_required": ["barrow", "dungeon", "undead"],
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["fetch", "investigate"]}},
        "turn_in_role_hint": ["scholar", "court_mage", "priest"]
    },
]

# Helper function
def _get_random_from_list(lst: List[Any]) -> Any:
    return random.choice(lst) if lst else None

def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    from npc import NAME_POOLS
    random_race = random.choice(list(NAME_POOLS.keys()))
    random_gender = random.choice(["male", "female"])
    
    name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, None)
    if not name_pool_entry:
        name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"]
    
    chosen_name_with_id = random.choice(name_pool_entry)
    name_display = chosen_name_with_id.split('_')[0].capitalize()

    return {"name": name_display, "id": chosen_name_with_id}

# Generate reward
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

    if random.random() < 0.4:
        reward_item = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level)
        reward["item"] = reward_item

    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3:
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list):
            reward[chosen_type] = _get_random_from_list(value_source)
        else:
            reward[chosen_type] = random.randint(value_source["min"], value_source["max"])

    return reward

# Quest class
class Quest:
    def __init__(self, title: str, description: str, reward: Dict[str, Any], level_requirement: int, location: Dict[str, Any],
                 objectives: List[Dict[str, Any]],
                 quest_id: int | None = None, status: str = "active", turn_in_npc_id: str | None = None):
        self.quest_id = quest_id or random.randint(1000, 9999)
        self.title = title
        self.description = description
        self.reward = reward
        self.level_requirement = level_requirement
        self.location = location
        self.objectives = objectives
        self.status = status
        self.turn_in_npc_id = turn_in_npc_id
        self.tags: Dict[str, Any] = {}
        self.add_tag("quest", "type", "generic")

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

    def is_objective_met(self, objective: Dict[str, Any], player: Any) -> bool:
        obj_type = objective["type"]
        
        if obj_type == "kill":
            target_id = objective["target_id"]
            required_count = objective["count"]
            current_count = player.defeated_enemies_tracker.get(target_id, 0)
            objective['current'] = current_count
            return current_count >= required_count
        
        elif obj_type == "collect_item":
            item_key = objective["item_key"]
            required_count = objective["count"]
            current_count = sum(1 for item in player.stats.inventory if item.name.lower().replace(' ', '_') == item_key.lower().replace(' ', '_'))
            objective['current'] = current_count
            return current_count >= required_count
        
        elif obj_type == "reach_location":
            location_name = objective["location_name"]
            return (player.current_location_obj and player.current_location_obj["name"].lower() == location_name.lower()) or \
                   any(loc_obj["name"].lower() == location_name.lower() for loc_obj in player.known_locations_objects)
        
        elif obj_type == "talk_to_npc":
            npc_id = objective["npc_id"]
            return npc_id in player.talked_to_npcs
        
        return False

    def check_all_objectives_met(self, player: Any) -> bool:
        if self.status == "completed":
            return True
            
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
        reward_str_parts = []
        for key, value in self.reward.items():
            if isinstance(value, Item):
                reward_str_parts.append(f"{value.name} (Item)")
            else:
                reward_str_parts.append(f"{value} {key.capitalize()}")
        reward_display = ", ".join(reward_str_parts)

        objectives_display = []
        for obj in self.objectives:
            current_progress_str = f" ({obj.get('current', 0)}/{obj['count']})" if "count" in obj else ""
            if obj["type"] == "kill":
                objectives_display.append(f"Defeat {obj['count']} {obj['target_name']}s{current_progress_str}")
            elif obj["type"] == "collect_item":
                objectives_display.append(f"Collect {obj['count']} {obj['item_key'].replace('_', ' ').title()}{current_progress_str}")
            elif obj["type"] == "reach_location":
                objectives_display.append(f"Reach {obj['location_name']}")
            elif obj["type"] == "talk_to_npc":
                objectives_display.append(f"Talk to {obj['npc_name']}")
        
        flavor_texts = flavor.get_flavor(self)
        description_prefix = f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at {self.location.get('name', 'Unknown')} [Status: {self.status.capitalize()}]:"
        
        full_description = f"{description_prefix}\n  Objective: {self.description}\n"
        if objectives_display:
            full_description += "  Tasks:\n" + "\n".join([f"    - {task}" for task in objectives_display])
        full_description += f"\n  Reward: {reward_display}"
        
        if flavor_texts:
            full_description += f"\n  Lore: {' '.join(flavor_texts)}"
            
        return full_description

# QuestLog class
class QuestLog:
    def __init__(self):
        self.active_quests: List[Quest] = []
        self.completed_quests: List[Quest] = []

    def add_quest(self, quest: Quest) -> bool:
        if quest.quest_id not in [q.quest_id for q in self.active_quests] and \
           quest.quest_id not in [q.quest_id for q in self.completed_quests]:
            self.active_quests.append(quest)
            return True
        return False

    def remove_quest(self, quest_id: int) -> bool:
        quest_to_remove = next((q for q in self.active_quests if q.quest_id == quest_id), None)
        if quest_to_remove:
            self.active_quests.remove(quest_to_remove)
            if quest_to_remove.status == "completed":
                self.completed_quests.append(quest_to_remove)
            return True
        return False

    def get_quest_by_id(self, quest_id: int) -> Quest | None:
        for q in self.active_quests:
            if q.quest_id == quest_id:
                return q
        for q in self.completed_quests:
            if q.quest_id == quest_id:
                return q
        return None

    def list_quests(self) -> List[Quest]:
        return self.active_quests + self.completed_quests

    def get_quests_for_turn_in(self, npc_id: str) -> List[Quest]:
        return [q for q in self.active_quests if q.status == "completed" and q.turn_in_npc_id == npc_id]

# Utility function
def list_player_quests_for_display(player: Any) -> List[Quest]:
    if hasattr(player, 'quest_log') and player.quest_log:
        return player.quest_log.list_quests()
    return []

# Helper function
def find_locations_by_tag(tag: str) -> List[Dict]:
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

def generate_location_appropriate_quest(player_level: int, location_tags: List[str], quest_giver_id: str | None = None) -> Quest | None:
    possible_templates = []
    
    for template in QUEST_TEMPLATES:
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]):
            continue

        if template["location_tags_required"]:
            if not all(tag in location_tags for tag in template["location_tags_required"]]):
                continue
        
        possible_templates.append(template)

    if not possible_templates:
        print(f"DEBUG: No specific quest template matched for level {player_level} and tags {location_tags}. Generating generic quest.")
        
        chosen_location = random.choice(LOCATIONS)
        
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

    chosen_template = random.choice(possible_templates)
    
    relevant_locations = []
    for tag in chosen_template["location_tags_required"]:
        relevant_locations.extend(find_locations_by_tag(tag))
    relevant_locations = list({loc["name"]: loc for loc in relevant_locations}.values())
    
    if not relevant_locations:
        final_quest_location = random.choice(LOCATIONS)
    else:
        final_quest_location = random.choice(relevant_locations)

    title = chosen_template["title_template"].replace("[LOCATION_NAME]", final_quest_location["name"])
    description = chosen_template["desc_template"].replace("[LOCATION_NAME]", final_quest_location["name"])

    if "[ALCHEMIST_NAME]" in description:
        npc_info = get_npc_name_by_role_hint("alchemist")
        description = description.replace("[ALCHEMIST_NAME]", npc_info["name"])
    if "[FARMER1_NAME]" in description:
        farmer1_info = get_npc_name_by_role_hint("farmer")
        farmer2_info = get_npc_name_by_role_hint("farmer")
        description = description.replace("[FARMER1_NAME]", farmer1_info["name"])
        description = description.replace("[FARMER2_NAME]", farmer2_info["name"])
        for obj in chosen_template["objectives_template"]:
            if obj["type"] == "talk_to_npc":
                if obj["npc_name"] == "[FARMER1_NAME]": obj["npc_id"] = farmer1_info["id"]
                if obj["npc_name"] == "[FARMER2_NAME]": obj["npc_id"] = farmer2_info["id"]
    if "[SPECIFIC_SITE]" in chosen_template["objectives_template"][0].get("location_name", ""):
        possible_sites = find_locations_by_tag("cave") + find_locations_by_tag("ruin") + find_locations_by_tag("barrow")
        possible_sites = [s for s in possible_sites if s.get("name") not in [final_quest_location["name"]]]
        if possible_sites:
            specific_site = random.choice(possible_sites)
            for obj in chosen_template["objectives_template"]:
                if obj["type"] == "reach_location" and obj["location_name"] == "[SPECIFIC_SITE]":
                    obj["location_name"] = specific_site["name"]
        else:
            for obj in chosen_template["objectives_template"]:
                if obj["type"] == "reach_location" and obj["location_name"] == "[SPECIFIC_SITE]":
                    obj["location_name"] = f"a mysterious site in {final_quest_location['name']}"

    objectives = []
    for obj_template in chosen_template["objectives_template"]:
        new_obj = obj_template.copy()
        if new_obj["type"] == "kill" and new_obj["target_name"] == "bandit":
            new_obj["target_id"] = "bandit_raider_generic"
        elif new_obj["type"] == "kill" and new_obj["target_name"] == "draugr death overlord":
             new_obj["target_id"] = "draugr_death_overlord"

        objectives.append(new_obj)

    reward = generate_reward(player_level, chosen_template.get("reward_tags", []))

    quest = Quest(
        title=title,
        description=description,
        reward=reward,
        level_requirement=player_level,
        location=final_quest_location,
        objectives=objectives,
        status="active",
        turn_in_npc_id=quest_giver_id
    )
    quest.add_tag("quest", "type", chosen_template["id"])
    
    if "flavor_tags" in chosen_template:
        for cat, types_dict in chosen_template["flavor_tags"].items():
            for t_type, t_value in types_dict.items():
                if isinstance(t_value, list):
                    for val in t_value:
                        quest.add_tag(cat, t_type, val)
                else:
                    quest.add_tag(cat, t_type, t_value)

    if not quest.objectives:
        print(f"Warning: Quest '{quest.title}' generated without objectives. Adding default.")
        quest.objectives.append({"type": "reach_location", "location_name": final_quest_location["name"]})

    return quest

def process_quest_rewards(player: Any, quest: Quest) -> None:
    from ui import UI 
    
    UI.print_subheading(f"Quest Completed: {quest.title}!")
    UI.slow_print("You have received your rewards:")

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
            UI.print_success(f"- {reward_value} Reputation with local factions.")
        elif reward_type == "favor":
            UI.print_success(f"- A favor {reward_value}.")
    
    UI.press_enter()

def generate_rumor(player_level: int, current_location: Dict[str, Any], quest_giver_id: str = None) -> Dict[str, Any]:
    """
    Generate a contextual rumor based on player level and current location.
    Can optionally include quest data.
    Returns:
        Dict with 'text' key containing rumor text, and optional 'quest_data' key with Quest object
    """
    rumors_general = [
        "I heard strange sounds coming from the old ruins to the north.",
        "Merchants have been avoiding the main roads lately. Bandits, they say.",
        "The local mine has been quiet for days. Might be trouble down there.",
        "Travelers speak of unnatural cold in the mountains, even in summer.",
        "The guards whisper of missing livestock near the old burial grounds.",
        "Psst, I hear the skooma trade is picking up again. Keep an eye out.",
        "They say the dragons are gone, but I swear I saw one flying near the Throat of the World.",
        "The Greybeards have been unusually active lately. Something big is coming, I feel it.",
        "Word is the Thalmor are sniffing around again. They're always looking for something.",
        "Heard a tale of a hidden Dwemer ruin, untouched for centuries, filled with treasures and dangers.",
        "Some say the Sea of Ghosts is haunted by the ghosts of ancient shipwrecks.",
        "A Khajiit caravan passed through, muttering about a rising darkness in Elsweyr."
    ]
    
    rumors_by_location_tag = {
        "whiterun": [
            "The Companions are looking for new recruits. Maybe you have what it takes?",
            "Heard that Nazeem is still as annoying as ever. Someone ought to teach him a lesson.",
            "The Gildergreen is looking a little worse for wear. I hope it's not dying.",
            "The Jarl is worried about the dragons, but he's doing his best to protect us.",
            "The market is bustling as usual. Always something to buy or sell."
        ],
        "riften": [
            "The Thieves Guild is always looking for new members. Are you light-fingered enough?",
            "Maven Black-Briar controls everything in this town. Don't cross her.",
            "The fishing is good in Lake Honrich, but be careful of Slaughterfish.",
            "The orphanage is always in need of donations. Think of the children.",
            "The mead is flowing freely at the Bee and Barb. Maybe too freely..."
        ],
        "windhelm": [
            "The Gray Quarter is getting restless. Tensions are rising between the Nords and Dunmer.",
            "Ulfric Stormcloak is preparing for war. Skyrim will soon be free!",
            "The Palace of the Kings is always bustling with activity. Something big is brewing.",
            "The docks are busy with ships coming and going. Trade is booming, despite the war.",
            "Be careful walking around at night. The streets can be dangerous."
        ],
        "solitude": [
            "The Blue Palace is always a sight to behold. The Empire's wealth is on full display.",
            "The Bards College is hosting a performance tonight. It's sure to be a spectacle.",
            "The East Empire Company has a strong presence here. They control much of the trade.",
            "The executioner is sharpening his blade. Justice will be served.",
            "The views from the city walls are breathtaking. You can see for miles."
        ],
        "markarth": [
            "The Silver-Bloods control everything in this city. Don't cross them.",
            "The Forsworn are a constant threat in the Reach. Be careful traveling outside the city walls.",
            "The Dwemer ruins are fascinating, but also dangerous. Explore at your own risk.",
            "The guards are always on the lookout for trouble. Crime is rampant in this city.",
            "The views from the top of the city are incredible. You can see the entire Reach."
        ],
        "falkreath": [
            "The graveyard is always expanding. Death is a constant presence in this town.",
            "The Jarl is a somber man. He carries the weight of the past on his shoulders.",
            "Hunters are frequently seen bringing in kills from the surrounding forest. It's a dangerous place.",
            "The local inn is always filled with travelers. It's a good place to hear the latest news.",
            "There's an unsettling quiet about this town. It's as if something is always watching."
        ],
        "dawnstar": [
            "The nightmares are getting worse. People are afraid to go to sleep.",
            "Miners are unearthing strange artifacts from the nearby mines. What secrets do they hold?",
            "The sea is rough these days. Shipwrecks are becoming more common.",
            "Fishermen are reporting strange creatures in the water. Stay away from the shore at night.",
            "There's a chill in the air that has nothing to do with the snow. Something is amiss."
        ],
        "winterhold": [
            "The College of Winterhold attracts mages from all over Tamriel. It's a hub of magical knowledge.",
            "The ruins of the old city are a constant reminder of the Great Collapse. A tragic event.",
            "Locals whisper of strange energies emanating from the College. What are they up to?",
            "The Frozen Hearth is the only inn left in town. It's a quiet place, but the ale is good.",
            "The sea is encroaching on the town. Winterhold is slowly being swallowed by the waves."
        ],
        "morthal": [
            "The Jarl seems preoccupied these days. What troubles weigh on her mind?",
            "The swamp is a dangerous place. Strange creatures lurk in the murky waters.",
            "People whisper of dark magic being practiced in the shadows. Be wary of strangers.",
            "The old barrows are said to be haunted by restless spirits. Don't disturb the dead.",
            "The fog is always thick in Morthal. It's easy to get lost in the gloom."
        ]
    }
    
    location_tags = current_location.get("tags", [])
    possible_rumors = rumors_general.copy()
    
    for tag in location_tags:
        if tag in rumors_by_location_tag:
            possible_rumors.extend(rumors_by_location_tag[tag])
    
    chosen_rumor = random.choice(possible_rumors)
    
    result = {"text": chosen_rumor}
    
    if random.random() < 0.3 and quest_giver_id:
        quest = generate_location_appropriate_quest(player_level, location_tags, quest_giver_id)
        if quest:
            result["quest_data"] = quest
    
    return result