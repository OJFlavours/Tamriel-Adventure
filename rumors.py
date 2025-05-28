import random
from typing import List, Dict, Any
from locations import LOCATIONS
import tags
import flavor
from items import Item, generate_random_item as gr_item_func, generate_item_from_key
from ui import UI # Ensure UI is imported for capitalization
from quests import Quest # Import the Quest class here

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

class DummyRumor:
    def __init__(self):
        self.tags = {}

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag_value

def generate_location_appropriate_quest(player_level: int, location_tags: List[str], quest_giver_id: str | None = None, rumor_text: str | None = None) -> Any:
    possible_templates = []

    for template in QUEST_TEMPLATES:
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]):
            continue

        if template["location_tags_required"]:
            if not all(tag in location_tags for tag in template["location_tags_required"]):
                continue

        possible_templates.append(template)

    if rumor_text:
        rumor = DummyRumor()
        rumor.add_tag("rumor", "text", rumor_text)
        rumor_tags = tags.get_tags(rumor)
        possible_templates = tags.filter_entities_by_tags(possible_templates, rumor_tags)

    if not possible_templates:
        # Re-enabled DEBUG message
        UI.print_system_message(f"DEBUG: No specific quest template matched for level {player_level} and tags {location_tags}. Generating generic quest.")

        chosen_location = random.choice(LOCATIONS)

        title = "A Simple Request"
        description = f"A local resident needs help in {chosen_location.get('name', 'the area')} with a minor issue."
        objectives = [{"type": "reach_location", "location_name": chosen_location["name"]}]
        reward = generate_reward(player_level, location_tags)

        quest = Quest( # Directly instantiate Quest object
            title=title,
            description=description,
            reward=reward,
            level_requirement=player_level,
            location=chosen_location,
            objectives=objectives,
            status="active",
            turn_in_npc_id=quest_giver_id
        )

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

    quest = Quest( # Directly instantiate Quest object
        title=title,
        description=description,
        reward=reward,
        level_requirement=player_level,
        location=final_quest_location,
        objectives=objectives,
        status="active",
        turn_in_npc_id=quest_giver_id
    )

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

def generate_rumor(player_level: int, current_location: Dict[str, Any], quest_giver_id: str | None = None) -> Dict[str, Any]:
    """
    Generates a rumor text, potentially linking to a new quest.
    It uses the generate_location_appropriate_quest function also within this file.
    """
    # Generate a potential quest using the function already in rumors.py

    class DummyRumor:
        def __init__(self):
            self.tags = {}

        def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
            if tag_category not in self.tags:
                self.tags[tag_category] = {}
            self.tags[tag_category][tag_type] = tag_value

    quest_data = generate_location_appropriate_quest(player_level, current_location.get("tags", []), quest_giver_id)
    rumor_text = ""

    # Attempt to get generic rumor starting phrases from flavor.py
    generic_rumor_starts = []
    if hasattr(flavor, 'DIALOGUE_FLAVORS') and \
       "topic" in flavor.DIALOGUE_FLAVORS and \
       "rumor" in flavor.DIALOGUE_FLAVORS["topic"]:
        generic_rumor_starts = flavor.DIALOGUE_FLAVORS["topic"]["rumor"]

    if quest_data:
        # Craft a rumor based on the generated quest
        if quest_data["location"] and quest_data["location"].get('name'):
            rumor_text_base = f"I've heard whispers concerning {quest_data['location'].get('name', 'a nearby place')}."
        else:
            rumor_text_base = f"Word is there's something stirring in the region."

        # Extract quest type for more specific rumor details
        quest_type_tag = ""
        if quest_data and "tags" in quest_data and "quest" in quest_data["tags"] and "type" in quest_data["tags"]["quest"]: # Check `quest_data.tags` first
             quest_type_tag = quest_data["tags"]["quest"]["type"]
        elif quest_data and "type" in quest_data: # Fallback to a direct 'type' if tags structure is different
            quest_type_tag = quest_data["type"]


        if "bandits" in quest_type_tag or "clear_bandit_camp" in quest_type_tag:
            rumor_text_detail = "Bandits are causing trouble, preying on the weak. Someone ought to do something about it."
        elif "fetch" in quest_type_tag or "ancient_relic_retrieval" in quest_type_tag:
            item_name_objective = "an ancient relic"
            for obj in quest_data["objectives"]:
                if obj["type"] == "collect_item":
                    item_name_objective = obj.get("item_key", "an important item").replace("_", " ")
                    break
            rumor_text_detail = f"There's talk of {item_name_objective} hidden away, waiting to be found by a worthy adventurer."
        else:
            rumor_text_detail = "It sounds like a task fitting for someone of your skills."

        if generic_rumor_starts:
            rumor_text = f"{random.choice(generic_rumor_starts)} {rumor_text_detail}"
        else:
            rumor_text = f"{rumor_text_base} {rumor_text_detail}"

        # Add tags to quest_data
        # This part of the original code was trying to set quest_data["tags"] directly.
        # Since `quest_data` is now a `Quest` object, you should use its `add_tag` method.
        # However, `generate_location_appropriate_quest` already adds tags to the `Quest` object it returns.
        # So, this block is likely redundant or should be re-evaluated based on the desired tag propagation.
        # For now, I'm commenting it out as it's not strictly necessary for the immediate fix.
        # dummy_rumor = DummyRumor()
        # dummy_rumor.add_tag("rumor", "text", rumor_text)
        # rumor_tags = tags.get_tags(dummy_rumor)
        # quest_data["tags"] = rumor_tags


    else:
        # Generate a generic rumor if no quest is created
        loc_name = current_location.get("name", "these parts")

        generic_rumors_list = [
            f"The winds whisper strange tales around {loc_name} lately.",
            f"Keep an eye out if you're traveling near {loc_name}. You never know what you'll encounter.",
            "Just the usual tavern chatter, mostly nonsense, but sometimes there's a kernel of truth.",
            f"Some say the Jarl over in {current_location.get('parent_name', 'the capital city')} is in a foul mood these days.",
            "The local merchants have been complaining about the price of mead again."
        ]
        if generic_rumor_starts:
            chosen_start = random.choice(generic_rumor_starts)
            detail_fallback = [
                "The caravans seem to be running late again.",
                "Strange lights were seen over the mountains last night.",
                "Never a dull moment in Skyrim, is there?"
            ]
            current_tags = current_location.get("tags", [])
            if "trade" in current_tags or "market" in current_tags:
                detail = "There's talk of a new shipment arriving soon, or perhaps being delayed."
            elif "magic" in current_tags or "college" in current_tags:
                detail = "The mages are probably up to something, as usual."
            else:
                detail = random.choice(detail_fallback)
            rumor_text = f"{chosen_start} {detail}"
        else: # Absolute fallback
            rumor_text = random.choice(generic_rumors_list)

    # Ensure the text is properly capitalized for dialogue
    return {"text": UI.capitalize_dialogue(rumor_text), "quest_data": quest_data}