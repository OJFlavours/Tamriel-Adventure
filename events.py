# events.py
import random
import traceback
from ui import UI
# Assuming Quest, generate_reward, generate_location_appropriate_quest are correctly in quests.py
from quests import Quest, generate_reward, generate_location_appropriate_quest # Import the new Quest class
from items import Item, generate_item_from_key, generate_random_item
from npc_entities import NPC # Corrected import for NPC
from npc_roles import HOSTILE_ROLES # Corrected import for HOSTILE_ROLES
# EXPLORATION_RESULTS from exploration_data.py
from exploration_data import EXPLORATION_RESULTS
# from npc import generate_npc_from_tags # Conceptual import, depends on implementation
from event_data import RANDOM_EVENTS, DUNGEON_NAMES, SPECIFIC_LOCATION_TAGS

def trigger_random_event(location_tags, player, ui, current_location_raw_data): # Renamed current_location to current_location_raw_data
    """Triggers a random event based on location tags and context."""
    try:
        current_time = current_location_raw_data.get("time_of_day", "day")  # Default to "day" if not specified
        player_action = player.current_action if hasattr(player, "current_action") else "exploring" # Default to "exploring"
        if not location_tags: # location_tags is from current_location_raw_data.get('tags')
            return None

        current_context_tags = set(current_location_raw_data.get("context_tags", [])) # Expecting context_tags like "interior", "urban"
        if not current_context_tags: # Fallback if not present, derive basic ones
            if any(t in location_tags for t in ["tavern", "inn", "shop", "house", "keep", "temple", "cave", "mine", "barrow", "dungeon"]):
                current_context_tags.add("interior")
            else:
                current_context_tags.add("exterior")
            if any(t in location_tags for t in ["city", "town", "village", "market"]):
                current_context_tags.add("urban")
            elif any(t in location_tags for t in ["forest", "plains", "mountain", "roadside", "wilderness"]):
                current_context_tags.add("wilderness")


        possible_events = []
        # Check all event categories, not just direct tag matches initially
        all_event_categories = RANDOM_EVENTS.keys()

        for category_key in all_event_categories:
            for event_def in RANDOM_EVENTS.get(category_key, []):
                event_location_tags = set(event_def.get("location_tags", []))
                event_context_tags = set(event_def.get("context_tags", [])) # Event defines its suitable contexts

                # Match if:
                # 1. Event has no specific location_tags OR current location has any of the event's required location_tags
                # AND
                # 2. Event has no specific context_tags OR current location's context matches any of the event's required context_tags
                
                location_match = not event_location_tags or event_location_tags.intersection(location_tags)
                context_match = not event_context_tags or event_context_tags.intersection(current_context_tags)

                time_match = True
                if "time_of_day" in event_def:
                    time_match = event_def["time_of_day"] == current_time

                action_match = True
                if "player_action" in event_def:
                    action_match = event_def["player_action"] == player_action

                if location_match and context_match and time_match and action_match:
                    possible_events.append(event_def)
        
        if not possible_events:
             # Fallback to generic_travel if no specific contextual match, but still filter by context
            generic_travel_events = RANDOM_EVENTS.get("generic_travel", [])
            for event_def in generic_travel_events:
                event_context_tags = set(event_def.get("context_tags", []))
                if not event_context_tags or event_context_tags.intersection(current_context_tags):
                    possible_events.append(event_def)

        if not possible_events:
            # UI.print_system_message(f"DEBUG: No suitable random events for tags: {location_tags} and context: {current_context_tags}")
            return None
            
        selected_event = random.choice(possible_events)
        
        # Display the event
        if "short_description" in selected_event:
            ui.slow_print(selected_event["short_description"])
        ui.slow_print(selected_event["description"])
        
        # Process the event based on its type
        event_type = selected_event.get("type", "flavor")
        details = selected_event.get("details", {})
        
        if event_type == "flavor_and_buff":
            # Apply any buffs mentioned in the event
            if "minor_buff_debuff" in details:
                buff_info = details["minor_buff_debuff"]
                ui.slow_print(f"You feel the blessing of {details.get('god_mention', 'the divine')}!")
                
        elif event_type == "item_and_flavor":
            # Give items to the player
            item_keys = details.get("item_keys", [])
            for item_key in item_keys:
                qty_range = details.get(f"quantity_range_{item_key}", (1, 1))
                qty = random.randint(qty_range[0], qty_range[1])
                for _ in range(qty):
                    from items import generate_item_from_key
                    new_item = generate_item_from_key(item_key, player.level)
                    if new_item:
                        if player.add_item(new_item):
                            ui.slow_print(f"You acquired: {new_item.name}!")
                        else:
                            ui.slow_print(f"You found {new_item.name}, but your inventory is full!")
                            
        elif event_type in ["npc_interaction_and_quest_lead", "npc_interaction_choice"]:
            # Spawn an NPC interaction
            if "npc_spawn_info" in details:
                npc_info = details["npc_spawn_info"]
                ui.slow_print(f"You encounter a {npc_info.get('role', 'stranger').replace('_', ' ')}!")
                if details.get("dialogue_lead"):
                    ui.slow_print(f"They say: \"{details['dialogue_lead']}\"")
                    
        elif event_type in ["combat_encounter", "combat_encounter_tough", "combat_encounter_boss"]:
            # Handle combat encounters
            if "enemy_spawn_info" in details:
                ui.slow_print(details.get("flavor_text", "You are attacked!"))
                ui.slow_print("Combat would be initiated here!")
                
        elif event_type == "quest_lead_and_item":
            # Give quest-related items
            item_key = details.get("item_key")
            if item_key:
                from items import generate_item_from_key
                new_item = generate_item_from_key(item_key, player.level)
                if new_item:
                    if player.add_item(new_item):
                        ui.slow_print(f"You discovered: {new_item.name}!")
                    else:
                        ui.slow_print(f"You found {new_item.name}, but your inventory is full!")
                        
        else:
            # Default flavor event
            ui.slow_print("The moment passes, leaving you with a sense of the world's deeper mysteries.")
        
        return selected_event
        
    except Exception as e:
        ui.print_failure(f"Error in trigger_random_event: {e}")
        return None

def get_recent_events():
    """Returns a list of recent events in the game world."""
    # Replace with actual logic to fetch recent events
    return ["A dragon was spotted near Whiterun!", "A group of bandits attacked a caravan on the road to Riften."]

# --- Functions (from your provided code, enhanced to use new quest/NPC structures) ---

def explore_location(player, current_location, random_encounters, npc_registry, all_locations_list, ui):
    """Explores the current location and triggers random events based on its tags."""
    try:
        ui.slow_print(f"You carefully explore {current_location['name']}...")
        current_time = current_location.get("time_of_day", "day")  # Default to "day" if not specified
        player_action = player.current_action if hasattr(player, "current_action") else "exploring" # Default to "exploring"


        current_location_tags = current_location.get("tags", [])
        present_specific_tags = [tag for tag in current_location_tags if tag in SPECIFIC_LOCATION_TAGS]
        available_results_data = []

        if present_specific_tags:
            for tag in present_specific_tags:
                if tag in EXPLORATION_RESULTS:
                    available_results_data.extend(EXPLORATION_RESULTS[tag])

        general_tags_to_check = [tag for tag in current_location_tags if tag not in present_specific_tags and tag in EXPLORATION_RESULTS]
        if general_tags_to_check:
            for tag in general_tags_to_check:
                 available_results_data.extend(EXPLORATION_RESULTS[tag])

        if not available_results_data:
            broad_fallback_categories = {
                "wilderness": ["forest", "plains", "mountain"],
                "urban_area": ["city", "town"],
                "ruin_general": ["ruin", "dwemer_ruin", "barrow"],
                "cave_general": ["cave"],
                "hold_generic": ["hold"]
            }
            for broad_cat, specific_cats in broad_fallback_categories.items():
                if broad_cat in current_location_tags:
                    for specific_fallback_tag in specific_cats:
                        if specific_fallback_tag in EXPLORATION_RESULTS:
                            available_results_data.extend(EXPLORATION_RESULTS[specific_fallback_tag])
                            if available_results_data: break
                    if available_results_data: break


        selected_exploration_outcomes = []
        if available_results_data:
            unique_descriptions = set()
            unique_results_data = []
            for d in available_results_data:
                if d["description"] not in unique_descriptions:
                    unique_descriptions.add(d["description"])
                    unique_results_data.append(d)

            num_results_to_show = min(1, len(unique_results_data)) # Ensure only one event, or zero if no unique results
            selected_exploration_outcomes = random.sample(unique_results_data, num_results_to_show)

        if selected_exploration_outcomes:
            for outcome in selected_exploration_outcomes:
                ui.slow_print(outcome["description"])
                effect_data = outcome.get("effect")
                if effect_data:
                    effect_type = effect_data.get("type")
                    details = effect_data.get("details", {})

                    if effect_type == "item_find":
                        if "gold_amount_range" in details:
                            gold = random.randint(details["gold_amount_range"][0], details["gold_amount_range"][1])
                            player.stats.gold += gold
                            ui.slow_print(f"You found {gold} septims!")
                        item_keys = details.get("item_keys", [])
                        if "item_key" in details and details["item_key"] not in item_keys: item_keys.append(details["item_key"])
                        for item_k in item_keys:
                            qty_range = details.get(f"quantity_range_{item_k}", (1, 1))
                            qty = random.randint(qty_range[0], qty_range[1])
                            for _ in range(qty):
                                new_item = generate_item_from_key(item_k, player.level)
                                if new_item:
                                    if player.add_item(new_item):
                                        ui.slow_print(f"You acquired: {new_item.name}!")
                                    else:
                                        ui.slow_print(f"You found {new_item.name}, but your inventory is full!")
                                else:
                                    ui.print_warning(f"Could not generate item for key: {item_k}")

                    elif effect_type in ["quest_lead", "quest_lead_and_item", "moral_choice_and_quest_lead"]:
                        # This should now leverage the new quest generation that creates Quest objects
                        quest_template_id = details.get("quest_hint_template_id")
                        if quest_template_id:
                            new_quest = generate_location_appropriate_quest(player.level, current_location.get("tags", []), None) # quest_giver_id is None for general finds
                            if new_quest and player.quest_log.add_quest(new_quest):
                                ui.slow_print(f"A new lead found: '{new_quest.title}' has been added to your journal.")
                            else:
                                ui.slow_print("You sense a potential task, but it doesn't manifest clearly right now.")
                        elif "lead_description" in details:
                             ui.slow_print(f"[Quest Lead]: {details['lead_description']}")
                             # For simple leads not tied to templates, could add a generic quest or just flavour
                    elif effect_type == "location_discovery_hint":
                        # Needs to call game.discover_connected_locations or similar
                        ui.slow_print(f"You gained a hint about: {details.get('location_name_hint', 'a new place')}.")

                    elif effect_type in ["skill_challenge", "skill_challenge_or_choice", "environmental_hazard_and_skill_challenge"]:
                        skill_details = details.get("skill_challenge_disarm_trap") or details.get("skill_challenge_repair_lever")
                        if skill_details:
                            if player.perform_skill_check(skill_details["skill"], skill_details["dc"]):
                                ui.slow_print(skill_details["success_desc"])
                                if skill_details.get("success_item_key"):
                                     success_item = generate_item_from_key(skill_details["success_item_key"], player.level)
                                     if success_item and player.add_item(success_item):
                                         ui.slow_print(f"You recovered: {success_item.name}!")
                            else:
                                ui.slow_print(skill_details["failure_desc"])
                                if "damage_on_fail" in skill_details:
                                    damage_taken = random.randint(skill_details["damage_on_fail"]["min"], skill_details["damage_on_fail"]["max"])
                                    player.stats.take_damage(damage_taken)
                                    ui.print_failure(f"You took {damage_taken} damage!")

                    elif effect_type in ["npc_encounter_hint", "npc_encounter_neutral_or_hostile", "npc_interaction_choice", "npc_interaction_tense", "npc_interaction_and_quest_lead", "npc_interaction_hostile_boss_potential", "npc_interaction_and_lore_reveal"]:
                        # Spawn NPC and potentially trigger interaction/combat
                        if "npc_spawn_info" in details:
                            # Assuming NPC class and creation in npc.py
                            new_npc_info = details["npc_spawn_info"]
                            spawned_npc = NPC(name=new_npc_info.get("name"), race=new_npc_info["race"],
                                              role=new_npc_info["role"], level=new_npc_info["level"],
                                              disposition=new_npc_info.get("disposition", 50),
                                              gold=new_npc_info.get("gold", random.randint(10,50)))
                            spawned_npc.unique_id = new_npc_info.get("unique_id", spawned_npc.unique_id) # Ensure unique ID is used

                            # Add to current location's NPC registry (conceptual, requires game.py to manage)
                            # For now, just print an encounter message
                            ui.slow_print(f"You encounter: {spawned_npc.name} ({spawned_npc.role.replace('_',' ').capitalize()})!")
                            if spawned_npc.role in HOSTILE_ROLES or details.get("combat_trigger_immediate"):
                                ui.slow_print(f"{spawned_npc.name} attacks!")
                                # This would trigger combat, handled by game.py
                            elif details.get("dialogue_lead"):
                                ui.slow_print(f"They say: \"{UI.capitalize_dialogue(details['dialogue_lead'])}\"")
                                # This would lead to dialogue options, handled by game.py's NPC interaction

                            if details.get("quest_hint_template_id"):
                                quest_template_id = details["quest_hint_template_id"]
                                # Generate and offer quest, passing spawned_npc.unique_id as quest_giver_id
                                # This would happen in the NPC's dialogue branch, not immediately here
                                pass # Handled by game.py calling NPC's dialogue

                    elif effect_type in ["combat_encounter", "combat_encounter_tough", "combat_encounter_boss", "choice_encounter_stealth_or_combat"]:
                        ui.print_combat_text(details.get("flavor_text", "You are ambushed!"))
                        # This would trigger combat, handled by game.py
                        if "enemy_spawn_info" in details:
                            enemy_list = []
                            for enemy_spec in details["enemy_spawn_info"]:
                                for _ in range(enemy_spec.get("count", 1)):
                                    enemy_list.append(NPC(name=None, race=enemy_spec["race"], role=enemy_spec["role"], level=enemy_spec["level"]))
                            # Conceptual: game.initiate_combat(player, enemy_list, current_location)
                            ui.slow_print(f"Enemies: {', '.join([e.name for e in enemy_list])}")
                            # For the 'choice_encounter_stealth_or_combat', the choice needs to be presented first by game.py
                            # and then initiate combat if chosen.


        else:
            if not available_results_data:
                ui.slow_print("The area seems quiet, with nothing specific of note occurring right now.")
            else:
                 ui.slow_print("You sense a potential occurrence, but it passes without incident this time.")

        # Trigger random event
        trigger_random_event(current_location_tags, player, ui, current_location)

        return selected_exploration_outcomes
    except Exception as e:
        print(f"Error in explore_location: {e}")
        traceback.print_exc()
        return None