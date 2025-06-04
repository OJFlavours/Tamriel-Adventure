# quests_logic.py
import random
from typing import List, Dict, Any, Optional

from locations import LOCATIONS # Assuming LOCATIONS is fully defined here
import flavor # Used by generate_location_appropriate_quest
from items import Item, generate_item_from_key # Used by process_quest_rewards and generate_location_appropriate_quest (via generate_reward)
from ui import UI # Ensure UI is imported for capitalization

from quest_proxies import LocationProxy, StageProxy # Used by process_quest_rewards
from quest_utils import (find_locations_by_tag, get_npc_name_by_role_hint, 
                         _find_loc_and_parents_recursive, DummyRumor,
                         generate_reward)
from quest_entities import Quest


def create_quest_template_index(quest_templates: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Creates an index that maps location tags to quest templates.
    """
    index = {}
    for template in quest_templates:
        for tag in template.get("location_tags_required", []):
            if tag not in index:
                index[tag] = []
            index[tag].append(template)
    return index

# Function to generate location-appropriate quest
def generate_location_appropriate_quest(
    player_level: int,
    current_location_obj: Dict[str, Any], # This is the raw dictionary of the current location
    all_quest_templates: List[Dict[str, Any]],
    quest_giver_id: str | None = None,
    event_data: Dict[str, Any] | None = None
) -> Quest | None:
    comprehensive_location_tags = set(current_location_obj.get("tags", []))
    effective_hold_name = None

    current_loc_id = current_location_obj.get('id')
    if current_loc_id:
        ancestry_chain_root_to_target = _find_loc_and_parents_recursive(current_loc_id, LOCATIONS, [])
        
        if ancestry_chain_root_to_target:
            for ancestor_dict in ancestry_chain_root_to_target:
                comprehensive_location_tags.update(ancestor_dict.get("tags", []))
            
            for ancestor_dict in ancestry_chain_root_to_target:
                if "hold" in ancestor_dict.get("tags", []):
                    effective_hold_name = ancestor_dict.get("name")
                    break
            if not effective_hold_name and ancestry_chain_root_to_target:
                effective_hold_name = ancestry_chain_root_to_target[0].get("name")
    
    if not effective_hold_name:
        if "hold" in current_location_obj.get("tags", []):
             effective_hold_name = current_location_obj.get("name")

    current_hold_name_processed = effective_hold_name
    location_tags = comprehensive_location_tags

    # Create the quest template index
    quest_template_index = create_quest_template_index(all_quest_templates)

    if event_data:
        # Generate dynamic quest based on event data
        return generate_dynamic_quest(event_data)

    possible_templates = []
    for tag in location_tags:
        if tag in quest_template_index:
            possible_templates.extend(quest_template_index[tag])

    # Remove duplicate templates
    possible_templates = list(set(possible_templates))

    if not possible_templates:
        UI.print_system_message(f"DEBUG: No specific quest template matched for Lvl {player_level}, Loc: {current_location_obj['name']}, Tags: {list(location_tags)}. Generating generic fallback.")
        fallback_location = current_location_obj
        fallback_title = f"Simple Errand in {fallback_location['name']}"
        fallback_desc = f"Someone in {fallback_location['name']} needs a hand with a minor task."
        fallback_stages = [{"stage_name": "Task", "objectives": [{"id": "fb_obj1", "type": "talk_to_npc", "npc_id": quest_giver_id if quest_giver_id else "local_citizen_generic_ID", "note": f"Speak to the person who needs help in {fallback_location['name']}."}]}]
        fallback_reward = generate_reward(max(1, player_level // 2), [])
        quest = Quest(title=fallback_title, description=fallback_desc, reward=fallback_reward, level_requirement=player_level, location=fallback_location, stages=fallback_stages, turn_in_npc_id=quest_giver_id)
        quest.add_tag("quest", "type", "fallback_generic")
        return quest

    chosen_template = random.choice(possible_templates)
    final_quest_location_obj = current_location_obj
    title = chosen_template["title_template"]
    description = chosen_template["desc_template"]
    generic_loc_name_for_fill = final_quest_location_obj["name"]

    def get_specific_location_name_for_placeholder(placeholder_tag: str, base_location: Dict) -> str:
        candidates = find_locations_by_tag(placeholder_tag)
        if candidates:
            return random.choice(candidates)["name"]
        return base_location["name"]

    title = title.replace("[LOCATION_NAME]", generic_loc_name_for_fill)
    description = description.replace("[LOCATION_NAME]", generic_loc_name_for_fill)
    if "[CAVE_TYPE]" in title or "[CAVE_TYPE]" in description:
        cave_name = get_specific_location_name_for_placeholder("cave", final_quest_location_obj)
        title = title.replace("[CAVE_TYPE]", cave_name)
        description = description.replace("[CAVE_TYPE]", cave_name)

    processed_stages = []
    for stage_template in chosen_template["stages"]:
        s_template = stage_template.copy()
        s_template["objectives"] = []
        for obj_template in stage_template.get("objectives", []):
            o_template = obj_template.copy()
            actual_obj_details_template = o_template.get("objective") if o_template.get("type") == "optional" else o_template

            if "note" in actual_obj_details_template:
                actual_obj_details_template["note"] = actual_obj_details_template["note"].replace("[LOCATION_NAME]", generic_loc_name_for_fill)
                if "[CAVE_TYPE]" in actual_obj_details_template["note"]:
                     actual_obj_details_template["note"] = actual_obj_details_template["note"].replace("[CAVE_TYPE]", get_specific_location_name_for_placeholder("cave", final_quest_location_obj))
                if "[WILDERNESS_TYPE]" in actual_obj_details_template["note"]:
                     actual_obj_details_template["note"] = actual_obj_details_template["note"].replace("[WILDERNESS_TYPE]", get_specific_location_name_for_placeholder("wilderness", final_quest_location_obj))

            if "location_name" in actual_obj_details_template and isinstance(actual_obj_details_template["location_name"], str):
                actual_obj_details_template["location_name"] = actual_obj_details_template["location_name"].replace("[LOCATION_NAME]", generic_loc_name_for_fill)
                if "[CAVE_TYPE]" in actual_obj_details_template["location_name"]:
                     actual_obj_details_template["location_name"] = actual_obj_details_template["location_name"].replace("[CAVE_TYPE]", get_specific_location_name_for_placeholder("cave", final_quest_location_obj))
                if "[WILDERNESS_TYPE]" in actual_obj_details_template["location_name"]:
                     actual_obj_details_template["location_name"] = actual_obj_details_template["location_name"].replace("[WILDERNESS_TYPE]", get_specific_location_name_for_placeholder("wilderness", final_quest_location_obj))

            if "npc_id" in actual_obj_details_template and isinstance(actual_obj_details_template["npc_id"], str) and actual_obj_details_template["npc_id"].endswith("_ID"):
                role_hint = actual_obj_details_template["npc_id"].replace("_ID", "")
                npc_info = get_npc_name_by_role_hint(role_hint)
                actual_obj_details_template["npc_id"] = npc_info["id"]
            
            if actual_obj_details_template.get("type") == "kill" and "target_id" in actual_obj_details_template and isinstance(actual_obj_details_template["target_id"], str) and actual_obj_details_template["target_id"].endswith("_ID"):
                role_hint = actual_obj_details_template["target_id"].replace("_ID", "")
                enemy_info = get_npc_name_by_role_hint(role_hint) 
                actual_obj_details_template["target_id"] = enemy_info["id"]

            if o_template.get("type") == "optional":
                o_template["objective"] = actual_obj_details_template
            else:
                 o_template = actual_obj_details_template
            s_template["objectives"].append(o_template)

        if "on_completion_dialogue" in s_template and isinstance(s_template["on_completion_dialogue"], str):
            dialogue = s_template["on_completion_dialogue"]
            dialogue = dialogue.replace("[QUEST_GIVER_NAME]", quest_giver_id.split('_')[0].capitalize() if quest_giver_id else "your contact")
            dialogue = dialogue.replace("[LOCATION_NAME]", generic_loc_name_for_fill)
            s_template["on_completion_dialogue"] = dialogue
        
        if "branch_options" in s_template:
            processed_branches = []
            for branch_opt_template in s_template["branch_options"]:
                b_opt = branch_opt_template.copy()
                b_opt["text"] = b_opt["text"].replace("[QUEST_GIVER_NAME]", quest_giver_id.split('_')[0].capitalize() if quest_giver_id else "your contact")
                b_opt["text"] = b_opt["text"].replace("[LOCATION_NAME]", generic_loc_name_for_fill)
                processed_branches.append(b_opt)
            s_template["branch_options"] = processed_branches
            # This is a branching stage, but the actual branch handling happens elsewhere (e.g., in dialogue logic)
            pass
            
        processed_stages.append(s_template)

    reward_details = generate_reward(player_level, chosen_template.get("reward_tags", []))
    
    initial_flavor = ""
    if "flavor_tags" in chosen_template:
        dummy_for_flavor = DummyRumor()
        for cat, types_d in chosen_template["flavor_tags"].items():
            for tag_t, tags_l in types_d.items():
                dummy_for_flavor.add_tag(cat, tag_t, random.choice(tags_l))
        
        retrieved_flavor_texts = flavor.get_flavor(dummy_for_flavor) if hasattr(flavor, 'get_flavor') else []
        if retrieved_flavor_texts:
            initial_flavor = random.choice(retrieved_flavor_texts)

    final_turn_in_npc_id = quest_giver_id
    if not final_turn_in_npc_id and "turn_in_role_hint" in chosen_template:
        turn_in_role = random.choice(chosen_template["turn_in_role_hint"])
        final_turn_in_npc_id = get_npc_name_by_role_hint(turn_in_role)["id"]

    quest_instance = Quest(
        quest_id=chosen_template["id"], 
        title=title,
        description=description,
        reward=reward_details,
        level_requirement=player_level,
        location=final_quest_location_obj,
        stages=processed_stages,
        status="active",
        turn_in_npc_id=final_turn_in_npc_id,
        initial_flavor_text=initial_flavor
    )

    for lore_tag_val in chosen_template.get("lore_tags", []):
        quest_instance.add_tag("quest", "lore", lore_tag_val) 
    if "flavor_tags" in chosen_template and "quest" in chosen_template["flavor_tags"] and "type" in chosen_template["flavor_tags"]["quest"]:
        quest_instance.add_tag("quest", "type", random.choice(chosen_template["flavor_tags"]["quest"]["type"]))
    
    return quest_instance

def generate_dynamic_quest(event_data: Dict[str, Any]) -> Quest | None:
    """
    Generates a dynamic quest based on the information in the event_data.
    """
    # Placeholder for dynamic quest generation logic
    return None

# Function to handle branching quests
def handle_branching_quest(player: Any, quest: Quest, branch_id: str) -> None:
    """
    Handles the progression of a branching quest based on the player's choice.
    """
    try:
        for stage in quest.stages:
            if "branch_options" in stage:
                for option in stage["branch_options"]:
                    if option["id"] == branch_id:
                        # Apply the effects of the chosen branch
                        if "next_stage" in option:
                            quest.current_stage_index = option["next_stage"]
                        return
    except Exception as e:
        print(f"Error handling branching quest: {e}")


# Process quest rewards
def process_quest_rewards(player: Any, quest: Quest) -> None:
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
                UI.print_success(f"- Item: {reward_value.name}.")
            else:
                UI.print_warning(f"- You found {reward_value.name}, but your inventory is full!")
        elif reward_type == "reputation":
            UI.print_success(f"- {reward_value} Reputation with local factions.")
        elif reward_type == "favor":
            UI.print_success(f"- A favor: {reward_value}.")

    completed_stage_index = quest.current_stage_index
    if 0 <= completed_stage_index < len(quest.stages):
        completed_stage_dict = quest.stages[completed_stage_index]
        completed_stage = StageProxy(completed_stage_dict)

        if completed_stage.reward_modifier:
            modifier = completed_stage.reward_modifier
            UI.slow_print("Additionally, for your choices/actions:")
            if "gold_bonus" in modifier:
                player.stats.gold += modifier["gold_bonus"]
                UI.print_success(f"- {modifier['gold_bonus']} bonus Gold.")
            if "experience_bonus" in modifier:
                player.gain_experience(modifier["experience_bonus"])
            UI.print_success(f"- {modifier['experience_bonus']} bonus Experience.")
            
            if not hasattr(player, 'faction_reputation') or player.faction_reputation is None:
                player.faction_reputation = {}

            rep_keys_in_modifier = [k for k in modifier.keys() if k.startswith("reputation_")]
            for rep_key_mod in rep_keys_in_modifier:
                rep_value = modifier[rep_key_mod]
                faction_id_for_player_rep = rep_key_mod.replace("reputation_", "").replace("_bonus", "")
                if faction_id_for_player_rep == "local":
                    loc_proxy = quest.location if isinstance(quest.location, LocationProxy) else LocationProxy(quest.location if isinstance(quest.location, dict) else None)
                    faction_id_for_player_rep = loc_proxy.get("name", "unknown_local").lower().replace(" ", "_")

                player.faction_reputation[faction_id_for_player_rep] = player.faction_reputation.get(faction_id_for_player_rep, 0) + rep_value
            UI.print_success(f"- {rep_value} Reputation with {faction_id_for_player_rep.replace('_', ' ').title()}.")

            if "item_bonus" in modifier:
                bonus_item_key = modifier["item_bonus"]
                bonus_item = generate_item_from_key(bonus_item_key, player.level)
                if bonus_item and player.add_item(bonus_item):
                    UI.print_success(f"- Bonus item: {bonus_item.name}!")
                elif bonus_item:
                    UI.print_warning(f"- You earned a bonus {bonus_item.name}, but your inventory is full!")
            
            unique_item_keys = [k for k in modifier.keys() if k.startswith("unique_item_")]
            for unique_key in unique_item_keys:
                item_actual_key = modifier[unique_key]
                unique_item_obj = generate_item_from_key(item_actual_key, player.level)
                if unique_item_obj and player.add_item(unique_item_obj):
                    UI.print_success(f"- Unique Item: {unique_item_obj.name} - a symbol of your achievement!")
                elif unique_item_obj:
                    UI.print_warning(f"- You earned the {unique_item_obj.name}, but your inventory is full!")

            if "magicka_gain" in modifier:
                 if hasattr(player.stats, 'max_magicka'):
                     player.stats.max_magicka += modifier["magicka_gain"]
                     player.stats.current_magicka = player.stats.max_magicka
                     UI.print_success(f"- Your maximum Magicka increased by {modifier['magicka_gain']}!")
            
            if "alchemy_skill_gain_bonus" in modifier:
                if hasattr(player, 'improve_skill'):
                    player.improve_skill("alchemy", modifier["alchemy_skill_gain_bonus"])
                else:
                    UI.print_success(f"- Your Alchemy skill has improved by {modifier['alchemy_skill_gain_bonus']} points.")

    if hasattr(player, 'quest_log') and player.quest_log:
        player.quest_log.remove_quest(quest.quest_id)

    UI.press_enter()