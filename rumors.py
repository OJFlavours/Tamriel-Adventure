from locations import Location
import random
from typing import List, Dict, Any
from locations import LocationManager
import tags
import flavor
from items import Item, generate_item_from_key # generate_random_item is now used via rumor_utils
from ui import UI
from quests import Quest, find_locations_by_tag

# Imports from new refactored rumor modules
from rumor_data import QUEST_TEMPLATES, FLAVOR_RUMOR_TEMPLATES
from rumor_utils import (
    generate_reward,
    _get_dynamic_placeholder,
    _replace_placeholders_in_rumor
    # get_npc_name_by_role_hint is used by _get_dynamic_placeholder and _replace_placeholders_in_rumor
    # _get_random_from_list is used by generate_reward
)

# --- Constants ---
PROBABILITY_OF_QUEST_RUMOR = 0.10 # 10% chance an NPC offers a quest

# --- Dummy Class (can stay here or move to utils if more broadly used) ---
class DummyRumor:
    def __init__(self): self.tags = {}
    def add_tag(self, cat: str, type: str, val: str) -> None:
        if cat not in self.tags: self.tags[cat] = {}
        self.tags[cat][type] = val

# --- Core Quest and Rumor Generation Logic ---

def generate_location_appropriate_quest(player_level: int, current_location_obj, quest_giver_id: str | None = None, rumor_text: str | None = None) -> Quest | None:
    possible_templates = []
    current_location_tags = current_location_obj.tags

    for template in QUEST_TEMPLATES:
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]): continue
        if template["location_tags_required"]:
            if not any(tag in current_location_tags for tag in template["location_tags_required"]): continue
        possible_templates.append(template)

    if rumor_text and hasattr(tags, 'filter_entities_by_tags'):
        rumor_obj = DummyRumor()
        rumor_obj.add_tag("rumor", "text", rumor_text)
        rumor_criteria = {"rumor": {"text": rumor_text}}
        # Ensure filter_entities_by_tags can handle list of dicts
        possible_templates = tags.filter_entities_by_tags(list(possible_templates), rumor_criteria)


    if not possible_templates:
        UI.print_system_message(f"DEBUG: No specific quest template matched for level {player_level} and tags {current_location_tags}. Generating generic quest.")
        # Use current_location_data directly for name
        chosen_location_for_generic_quest = current_location_obj
        # Fallback if current_location_data is not suitable or empty
        location_manager = LocationManager()
        if not chosen_location_for_generic_quest or not chosen_location_for_generic_quest.name:
            chosen_location_for_generic_quest = random.choice(location_manager.locations.values())


        title = f"An Errand in {chosen_location_for_generic_quest.name}"
        description = f"Word is that someone in {chosen_location_for_generic_quest.name} could use a hand. Might be a simple delivery, finding a lost trinket, or just lending an ear. Small tasks for small coin, most likely."
        
        objectives_list = [{"id": f"generic_obj_{random.randint(100,999)}", "type": "reach_location", "location_name": chosen_location_for_generic_quest.name, "note": f"Investigate the small task mentioned in {chosen_location_for_generic_quest.name}."}]
        stages_list = [{"stage_name": "Complete Errand", "objectives": objectives_list, "on_completion_dialogue": "You've handled the matter. Well done."}]
        reward = generate_reward(player_level, current_location_tags) # Uses imported generate_reward
        quest = Quest(title=title, description=description, reward=reward, level_requirement=player_level, location=chosen_location_for_generic_quest, stages=stages_list, status="active", turn_in_npc_id=quest_giver_id, quest_id=f"generic_errand_{random.randint(1000,9999)}")
        quest.add_tag("quest", "type", "generic_errand")
        return quest

    if not possible_templates:
        return generate_location_appropriate_quest(player_level, current_location_obj, quest_giver_id, rumor_text)
    chosen_template = random.choice(possible_templates)
    
    location_manager = LocationManager()
    final_quest_location_obj = random.choice(list(location_manager.locations.values())) # Default
    if chosen_template["location_tags_required"]:
        candidate_locations_for_quest_events = []
        for tag_needed_for_event in chosen_template["location_tags_required"]:
            # find_locations_by_tag returns list of location dicts
            candidate_locations_for_quest_events.extend(find_locations_by_tag(tag_needed_for_event))
    if candidate_locations_for_quest_events:
        # Deduplicate based on location 'id'
        candidate_locations_for_quest_events = list({loc["id"]: loc for loc in candidate_locations_for_quest_events}.values())
    if candidate_locations_for_quest_events: # Ensure not empty after deduplication
        final_quest_location_obj = random.choice(candidate_locations_for_quest_events)
    else:
        final_quest_location_obj = random.choice(list(location_manager.locations.values()))
    # Ensure final_quest_location_obj is a dictionary
    if not isinstance(final_quest_location_obj, Location):
        try:
            final_quest_location_obj = final_quest_location_obj.__dict__
        except Exception as e:
            UI.print_system_message(f"ERROR: Could not convert final_quest_location_obj to dict: {e}")
            final_quest_location_obj = {"name": "a mysterious location"} # Provide a default value

    # Add logging
    UI.print_system_message(f"DEBUG: final_quest_location_obj type: {type(final_quest_location_obj)}")
    actual_ruin_name = _get_dynamic_placeholder("[Ruin_Name_Specific]", {"tags": current_location_obj.tags})
    actual_artifact_name = _get_dynamic_placeholder("[Item_Type_Valuable]", {"tags": current_location_obj.tags})
    actual_artifact_key = actual_artifact_name.lower().replace(" ","_") + "_relic"
    
    beast_type = "Cave Bear" # Default
    beast_type_id = "cave_bear" # Default
    forest_or_mountain_name = _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", {"tags": current_location_obj.tags}) # Default
    if "beast_hunt_rumors" == chosen_template["id"]:
        beast_type = random.choice(["Frostbite Spider Broodmother", "Alpha Wolf", "Grizzled Bear", "Ice Wraith Matriarch", "Sabre Cat Packleader"])
        beast_type_id = beast_type.lower().replace(" ", "_")
        # Ensure find_locations_by_tag returns a list of dicts, and handle empty list
        potential_f_m_locs = find_locations_by_tag("forest") + find_locations_by_tag("mountain")
    if potential_f_m_locs:
        forest_or_mountain_name = random.choice(potential_f_m_locs)["name"]
    else:
        forest_or_mountain_name = _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", {"tags": current_location_obj.tags}) # Default

    title = chosen_template["title_template"].replace("[LOCATION_NAME]", final_quest_location_obj.name).replace("[RUIN_NAME]", actual_ruin_name).replace("[ARTIFACT_NAME]", actual_artifact_name).replace("[BEAST_TYPE]", beast_type).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)
    description = chosen_template["desc_template"].replace("[LOCATION_NAME]", final_quest_location_obj.name).replace("[RUIN_NAME]", actual_ruin_name).replace("[ARTIFACT_NAME]", actual_artifact_name).replace("[BEAST_TYPE]", beast_type).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name).replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", {"tags": current_location_obj.tags})).replace("[WILDERNESS_TYPE]", random.choice(["the dark woods","the craggy hills","the misty fens"]))
    
    objectives_list = []
    for i, obj_template in enumerate(chosen_template["objectives_template"]):
        new_obj = obj_template.copy()
        new_obj["id"] = f"obj_{chosen_template['id']}_{i}_{random.randint(100,999)}"
        
        new_obj["note"] = new_obj.get("note", "Complete this objective.")
        new_obj["note"] = new_obj["note"].replace("[LOCATION_NAME]", final_quest_location_obj.name)
        new_obj["note"] = new_obj["note"].replace("[RUIN_NAME]", actual_ruin_name)
        new_obj["note"] = new_obj["note"].replace("[ARTIFACT_NAME]", actual_artifact_name)
        new_obj["note"] = new_obj["note"].replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", {"tags": final_quest_location_obj.tags})).replace("[WILDERNESS_TYPE]", random.choice(["the dark woods","the craggy hills","the misty fens"]))
        new_obj["note"] = new_obj["note"].replace("[BEAST_TYPE]", beast_type)
        new_obj["note"] = new_obj["note"].replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)

        if "##" in new_obj["note"] and "count" in new_obj: new_obj["note"] = new_obj["note"].replace("##", str(new_obj["count"]))
        
        if "location_name" in new_obj: new_obj["location_name"] = new_obj["location_name"].replace("[RUIN_NAME]", actual_ruin_name).replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", {"tags": final_quest_location_obj.tags})).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)
        if "item_key" in new_obj: new_obj["item_key"] = new_obj["item_key"].replace("[ARTIFACT_KEY]", actual_artifact_key)
        if "target_name" in new_obj : new_obj["target_name"] = new_obj["target_name"].replace("[BEAST_TYPE]", beast_type)
        if "target_id" in new_obj : new_obj["target_id"] = new_obj["target_id"].replace("[BEAST_TYPE_ID]", beast_type_id)

        objectives_list.append(new_obj)

    stage_name_template = chosen_template.get("stage_name_template", "Primary Objectives")
    stage_name = stage_name_template.replace("[LOCATION_NAME]", final_quest_location_obj.name).replace("[RUIN_NAME]", actual_ruin_name).replace("[BEAST_TYPE]", beast_type)
    stages_list = [{"stage_name": stage_name, "objectives": objectives_list, "on_completion_dialogue": f"The matter concerning {stage_name} appears to be resolved."}]
    if chosen_template.get("stages"): stages_list = chosen_template["stages"]

    reward_dict = generate_reward(player_level, chosen_template.get("reward_tags", [])) # Uses imported generate_reward
    initial_flavor_text = ""
    if "flavor_tags" in chosen_template:
        dummy_entity = DummyRumor()
        for cat, types_dict in chosen_template["flavor_tags"].items():
            for tag_type, tags_list_val in types_dict.items():
                if tags_list_val: dummy_entity.add_tag(cat, tag_type, random.choice(tags_list_val))
        retrieved_flavors = flavor.get_flavor(dummy_entity) if hasattr(flavor, 'get_flavor') else []
        if retrieved_flavors: initial_flavor_text = random.choice(retrieved_flavors)

    quest = Quest(
        quest_id=chosen_template["id"] + f"_{random.randint(100,999)}",
        title=title, description=description, reward=reward_dict,
        location=final_quest_location_obj, stages=stages_list, status="active",
        turn_in_npc_id=quest_giver_id, initial_flavor_text=initial_flavor_text
    )
    if "lore_tags" in chosen_template:
        for lore_tag in chosen_template["lore_tags"]: quest.add_tag("quest", "lore", lore_tag)
    if "flavor_tags" in chosen_template and "quest" in chosen_template["flavor_tags"] and \
       "type" in chosen_template["flavor_tags"]["quest"] and chosen_template["flavor_tags"]["quest"]["type"]:
       if chosen_template["flavor_tags"]["quest"]["type"]:
           quest.add_tag("quest", "type", random.choice(chosen_template["flavor_tags"]["quest"]["type"]))
       else: quest.add_tag("quest", "type", "general_adventure")
    else: quest.add_tag("quest", "type", "general_adventure")
    return quest

def process_quest_rewards(player: Any, quest: Quest) -> None:
    UI.print_subheading(f"Quest Completed: {quest.title}!")
    UI.slow_print("You have received your rewards:")
    for reward_type, reward_value in quest.reward.items():
        if reward_type == "gold":
            player.stats.gold += reward_value
            UI.print_success(f"- {reward_value} Gold.")
        elif reward_type == "experience": player.gain_experience(reward_value)
        elif reward_type == "item" and isinstance(reward_value, Item):
            if player.add_item(reward_value): UI.print_success(f"- Acquired: {reward_value.name}!")
            else: UI.print_warning(f"- You found {reward_value.name}, but your inventory is full!")
        elif reward_type == "reputation": UI.print_success(f"- Your reputation with local factions has improved by {reward_value}.")
        elif reward_type == "favor": UI.print_success(f"- You have gained {reward_value}.")
    UI.press_enter()

def generate_rumor(player_level: int, current_location_obj, quest_giver_id: str | None = None, force_no_quest: bool = False) -> Dict[str, Any]:
    quest_data_object = None
    rumor_text = ""

    # Ensure current_location_data is a dictionary for consistency
    # current_location_obj can be an object (e.g. Location class instance) or a dict
    #if hasattr(current_location_obj, 'id') and current_location_obj.id in RAW_LOCATION_DATA_MAP:
    #    location_data_dict = RAW_LOCATION_DATA_MAP[current_location_obj.id]
    #elif isinstance(current_location_obj, dict) and "id" in current_location_obj:
    #     location_data_dict = current_location_obj # Assume it's already the dict we need
    #else: # Fallback if it's an object without a direct map or an unexpected dict
    #    location_data_dict = {"name": getattr(current_location_obj, 'name', "an unknown area"), 
    #                          "tags": getattr(current_location_obj, 'tags', []),
    #                           "parent_name": getattr(current_location_obj, 'parent_name', None),
    #                           "id": getattr(current_location_obj, 'id', None)}
    location_data_dict = {"name": current_location_obj.name, "tags": current_location_obj.tags, "parent_name": current_location_obj.parent_id, "id": current_location_obj.id}


    if not force_no_quest and random.random() < PROBABILITY_OF_QUEST_RUMOR:
        quest_data_object = generate_location_appropriate_quest(player_level, current_location_obj, None)

    if quest_data_object and isinstance(quest_data_object, Quest) and not force_no_quest:
        location_name_for_rumor = quest_data_object.location.name if isinstance(quest_data_object.location, Location) else "a nearby place"

        quest_type_tags_list = quest_data_object.tags.get("quest", {}).get("type", []) if isinstance(quest_data_object.tags, dict) else []
        if not isinstance(quest_type_tags_list, list): quest_type_tags_list = [quest_type_tags_list]

        if any(verb in quest_type_tags_list for verb in ["hunt", "clear"]): action_verb = "dealing with"
        elif any(verb in quest_type_tags_list for verb in ["fetch", "retrieve"]): action_verb = "finding"
        else: action_verb = "looking into" # Default action_verb
        
        short_desc_snippet = quest_data_object.description.split('.')[0]
        if "errand" in quest_data_object.quest_id or "generic_errand" in quest_type_tags_list :
             rumor_text = f"Heard that someone over in {location_name_for_rumor} might have a small task, if you're not too busy for simple work."
        else:
             flavor_snippet = f" {quest_data_object.initial_flavor_text}" if quest_data_object.initial_flavor_text else ""
             rumor_text = f"There's talk of trouble over at {location_name_for_rumor}. {short_desc_snippet}.{flavor_snippet} Sounds like it could use a capable hand."
    else:
        location_tags = location_data_dict.get("tags", []) if isinstance(location_data_dict, dict) else []

        chosen_rumor_category_key = "general_skyrim"  # Default
        tag_precedence = [
            *(tag for tag in ["tavern", "inn", "market", "shop", "blacksmith", "alchemy_shop", "temple", "college", "palace", "keep", "docks"] if tag in location_tags),
            *(tag for tag in ["city", "town", "village"] if tag in location_tags),
            *(tag for tag in ["forest", "mountain", "cave", "ruin", "barrow", "mine", "wilderness", "coastal", "ashland_waste", "volcanic_caldera"] if tag in location_tags),
            location_data_dict.get("parent_name", "impossible_match_for_hold").lower().replace(" ", "_") + "_general",
            "general_skyrim"
        ]

        for tag_key in tag_precedence:
            if tag_key in FLAVOR_RUMOR_TEMPLATES.keys():
                chosen_rumor_category_key = tag_key
                break
        
        rumor_list_for_category = FLAVOR_RUMOR_TEMPLATES.get(chosen_rumor_category_key, FLAVOR_RUMOR_TEMPLATES.get("general_skyrim", []))
        if rumor_list_for_category:
            rumor_template = random.choice(rumor_list_for_category) if isinstance(rumor_list_for_category, list) else ""
        else:
            rumor_template = ""
        rumor_text = _replace_placeholders_in_rumor(rumor_template, location_data_dict) if rumor_template else "I have no news."

    return {"text": UI.capitalize_dialogue(rumor_text.strip()), "quest_data": quest_data_object}
