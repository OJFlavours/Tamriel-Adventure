# npc_dialogue_logic.py
import random
from typing import Any, List

# Assuming NPC class and Player class will be passed as arguments
# For type hinting, you might import them if they are in separate files
# from npc import NPC # Or from npc_entities import NPC if moved
# from player import Player

from stats import Stats # Player object will have stats, used for player.full_name
from items import Item # For quest reward type hinting
from ui import UI
from quests import Quest, generate_location_appropriate_quest, QuestLog, process_quest_rewards # process_quest_rewards for turn-in
from locations import RAW_LOCATION_DATA_MAP # For share_rumor and _discuss_place context
from tags import TAGS # For _discuss_place
import flavor # For _discuss_place
from rumors import generate_rumor # For _handle_npc_share_rumor

# Forward declaration for type hinting if NPC methods call these directly (not the case here)
# def _handle_npc_offer_quest(npc: Any, player: Any, quest: Quest, from_rumor: bool = False) -> None:
# pass

def is_quest_related_to_npc(npc: Any, quest: Quest) -> bool:
    """
    Checks if a quest is related to an NPC's work/purpose based on their role and tags.
    """
    try:
        npc_role = npc.role.lower()
        npc_tags = npc.tags.get("npc", {})
        quest_tags = quest.tags.get("quest", {})

        # Check if the quest has any tags related to the NPC's role
        for tag_type, tag_values in npc_tags.items():
            if tag_type in quest_tags:
                return True

        # Check if the quest description mentions the NPC's role
        if npc_role in quest.description.lower():
            return True

        # If no relation is found, return False
        return False
    except Exception as e:
        print(f"Error checking quest relation: {e}")
        return False

def _handle_npc_discuss_place(npc: Any, player: Any, current_location: Any) -> None:
    """Provides a tag/flavor related answer when asked about the location."""
    # current_location is expected to be a dictionary-like structure from RAW_LOCATION_DATA_MAP or similar
    # or an object with .name, .id, and .get('tags')
    try:
        if hasattr(current_location, 'id') and current_location.id in RAW_LOCATION_DATA_MAP:
            loc_data = RAW_LOCATION_DATA_MAP[current_location.id]
        elif isinstance(current_location, dict) and "id" in current_location:
            loc_data = current_location
        else: # Fallback if current_location is not a raw dict or mapped object
            UI.slow_print(UI.capitalize_dialogue(f"“This place... I don't have much to say about it right now.”"))
            return

        loc_name = loc_data.get("name", "this place")
        loc_tags = loc_data.get("tags", [])

        class DummyLocationForFlavor:
            def __init__(self, tags_list):
                self.tags = {"location": {}}
                # Ensure TAGS["LOCATIONS"] is accessed correctly
                if "LOCATIONS" in TAGS:
                    for tag_type, possible_values in TAGS["LOCATIONS"].items():
                        found_tags = [t for t in tags_list if t in possible_values]
                        if found_tags:
                            self.tags["location"][tag_type] = found_tags
                else: # Fallback if TAGS structure is not as expected
                    # This part might need adjustment based on actual TAGS structure
                    # For now, we'll assume it might just be a list of tags if TAGS["LOCATIONS"] isn't there
                    self.tags["location"]["generic_tags"] = tags_list


        dummy_loc_entity = DummyLocationForFlavor(loc_tags)
        flavor_vignettes = flavor.get_flavor(dummy_loc_entity)

        if flavor_vignettes:
            chosen_flavor = random.choice(flavor_vignettes)
            UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {chosen_flavor}”"))
        else:
            comments = []
            if "city" in loc_tags: comments.append("It's a major hub, always something happening, for better or worse.")
            if "town" in loc_tags: comments.append("A decent enough place. Quieter than the big cities, which suits some folk.")
            if "village" in loc_tags: comments.append("A small, tight-knit community. We look out for each other here.")
            if "tavern" in loc_tags or "inn" in loc_tags: comments.append("A good place to rest your feet, share a drink, and hear the latest news... or tall tales.")
            if "mountain" in loc_tags: comments.append("The air here is thin, and the peaks are unforgiving. Beautiful, but dangerous.")
            if "forest" in loc_tags: comments.append("The woods are deep and old here. Many secrets, and many dangers, lie within.")
            if "mine" in loc_tags: comments.append("Many fortunes have been made and lost in these mines. A hard life, but honest work.")

            if comments:
                UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {random.choice(comments)}”"))
            else:
                UI.slow_print(UI.capitalize_dialogue(f"“{loc_name}... It is what it is. Not much else to say about it, really.”"))
    except Exception as e:
        UI.print_failure(f"Error discussing place: {e}")

def _handle_npc_offer_quest(npc: Any, player: Any, quest: Quest, from_rumor: bool = False) -> None:
    """Handles the process of an NPC offering a quest to the player."""
    try:
        if not from_rumor:
            UI.slow_print(f'"And speaking of such things... I\'ve heard there\'s a need for someone to {quest.description.lower().split(".")[0]}."')
            if quest.initial_flavor_text:
                UI.slow_print(f'"{quest.initial_flavor_text}"')

        UI.print_line('-')
        UI.print_info(f"Quest: {quest.title}")
        UI.print_info(f"Objective: {quest.description}")
        UI.print_info(f"Current Stage Tasks:")
        current_stage_objectives = quest.current_stage.get("objectives", []) if quest.current_stage else []
        for obj in current_stage_objectives:
            UI.print_info(f"  - {obj.get('note', 'A task awaits.')}")

        reward_parts = []
        if isinstance(quest.reward, dict):
            for r_type, r_value in quest.reward.items():
                if isinstance(r_value, Item):
                    reward_parts.append(f"{r_value.name} (Item)")
                else:
                    reward_parts.append(f"{r_value} {r_type.capitalize()}")
        elif quest.reward: # Ensure quest.reward is not None
            reward_parts.append(str(quest.reward))

        reward_display_str = ", ".join(reward_parts) if reward_parts else "a token of my gratitude"
        UI.print_info(f"Reward: {reward_display_str}")
        UI.print_line('-')

        while True:
            quest_action_prompt = UI.print_prompt("Your response? [1] Accept [2] Decline [3] Consider it further").strip()
            if quest_action_prompt == "1":
                if player.quest_log.add_quest(quest):
                    UI.slow_print(UI.capitalize_dialogue(f"“Excellent! I knew I could count on you, {player.full_name}. The details are in your journal.”"))
                    npc.disposition = min(100, npc.disposition + random.randint(3, 7))
                else:
                    UI.slow_print(UI.capitalize_dialogue("“It seems you already have this task, or your journal is full. A pity.”"))
                npc.has_offered_quest = True # Mark that this NPC has gone through the offer process for this quest.
                break
            elif quest_action_prompt == "2":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['A pity. I had hoped for assistance.', 'Very well. The task will fall to another, then.', 'Understandable. Not all are suited for such endeavors.'])}”"))
                npc.disposition = max(0, npc.disposition - random.randint(1, 4))
                npc.has_offered_quest = True # Still mark as offered, even if declined.
                break
            elif quest_action_prompt == "3":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['As you wish. The opportunity may not last indefinitely.', 'Do not tarry too long if you intend to help.', 'Consider it, then. But time is often a factor.'])}”"))
                # Don't set has_offered_quest to True here, allow re-prompt if player talks again.
                # Or, set it to True to prevent re-offering immediately. For now, let's assume "consider" means they might come back.
                # The original logic set has_offered_quest = True for accept/decline.
                # Let's keep it that way: if they consider, they can be re-offered if logic permits.
                # However, the main has_offered_quest flag on NPC is more about "has this NPC made *an* offer",
                # not "is *this specific* quest offer pending".
                # The eligible_for_quest_offer_roll is the one-time check.
                # For simplicity, let's say "consider" doesn't burn the has_offered_quest flag for *this interaction*.\
                break
            else:
                UI.slow_print("A clear answer is expected, traveler.")
    except Exception as e:
        UI.print_failure(f"Error offering quest: {e}")


def _handle_npc_share_rumor(npc: Any, player: Any, current_location_obj: Any) -> None:
    """Handles NPC sharing a rumor and potentially offering a quest."""
    try:
        if npc.disposition < 35:
            UI.slow_print(UI.capitalize_dialogue(f'"{random.choice(["I have no time for idle gossip.", "Find someone else to bother with your trivial questions."])}"'))
            return

        # current_location_obj is expected to be a Location OBJECT or a dict with 'id', 'name', 'tags'
        if hasattr(current_location_obj, 'id') and current_location_obj.id in RAW_LOCATION_DATA_MAP:
            location_data_dict = RAW_LOCATION_DATA_MAP[current_location_obj.id]
        elif isinstance(current_location_obj, dict) and "id" in current_location_obj:
             location_data_dict = current_location_obj # Assume it's already the data dict
        else: # Fallback if current_location_obj is not a known type
            UI.print_system_message(f"DEBUG: share_rumor - Unexpected current_location_obj type: {type(current_location_obj)}")
            location_data_dict = {"name": "this area", "tags": [], "id": "unknown_loc_id"}


        if not npc.rumor_pool:
            for _ in range(3):
                rumor_output = generate_rumor(player.stats.level, location_data_dict, npc.unique_id, force_no_quest=True)
                if rumor_output["text"] not in npc.rumor_pool:
                    npc.rumor_pool.append(rumor_output["text"])
            if not npc.rumor_pool:
                npc.rumor_pool.append("I've heard nothing new lately. The wind carries few secrets today.")

        rumor_text_to_share = npc.rumor_pool[npc.current_rumor_index]
        
        # Add recent events to the rumor pool
        from events import get_recent_events
        recent_events = get_recent_events()
        if recent_events:
            num_events_to_add = random.randint(1, min(2, len(recent_events)))
            selected_events = random.sample(recent_events, num_events_to_add)
            
            # Add recent events to the rumor pool, ensuring no duplicates
            for event in selected_events:
                if event not in npc.rumor_pool:
                    npc.rumor_pool.append(event)

            # Limit the number of recent events in the pool to 1-2
            npc.rumor_pool = npc.rumor_pool[-2:]
        UI.slow_print(f'"{rumor_text_to_share}"')
        npc.current_rumor_index = (npc.current_rumor_index + 1) % len(npc.rumor_pool)

        if npc.eligible_for_quest_offer_roll and not npc.has_offered_quest:
            npc.eligible_for_quest_offer_roll = False # This NPC gets only one roll, ever.
            if random.random() < 0.20: # 20% chance for this NPC to decide to offer a quest
                quest_to_offer = generate_location_appropriate_quest(player.stats.level, location_data_dict, npc.unique_id)
                if quest_to_offer:
                    if not player.quest_log.get_quest_by_id(quest_to_offer.quest_id):
                        _handle_npc_offer_quest(npc, player, quest_to_offer, from_rumor=True)
                # else: No quest generated, or NPC decided not to offer.
    except Exception as e:
        UI.print_failure(f"Error sharing rumor: {e}")

def _handle_npc_hire_mercenary(npc: Any, player: Any) -> None:
    """Handles the process of hiring a mercenary NPC."""
    try:
        if player.stats.gold >= npc.mercenary_hire_cost:
            player.stats.gold -= npc.mercenary_hire_cost
            player.followers.append(npc)
            npc.is_follower = True
            npc.disposition = min(100, npc.disposition + 15)
            UI.slow_print(UI.capitalize_dialogue(f"\"{npc.name} takes your coin. 'For this price, my blade is yours.'\""))
            # options_texts.remove(chosen_option_text) # Menu will rebuild
        else:
            UI.slow_print(UI.capitalize_dialogue(f"\"{npc.name} scoffs. 'Come back when you have {npc.mercenary_hire_cost} septims.'\""))
    except Exception as e:
        UI.print_failure(f"Error hiring mercenary: {e}")

def _handle_npc_recruit_follower(npc: Any, player: Any) -> None:
    """Handles the process of recruiting an NPC to join the player's travels."""
    try:
        recruit_chance = 0.3 + (player.stats.personality / 200) + ((npc.disposition - 50) / 100)
        if random.random() < recruit_chance:
            player.followers.append(npc)
            npc.is_follower = True
            npc.disposition = min(100, npc.disposition + 20)
            UI.slow_print(UI.capitalize_dialogue(f"\"{npc.name} considers your offer. 'Aye, the road is better with company. I'll join you!'\""))
        else:
            npc.disposition = max(0, npc.disposition - 5)
            UI.slow_print(UI.capitalize_dialogue(f"\"{npc.name} shakes their head. 'Perhaps another time, traveler. My path lies elsewhere for now.'\""))
    except Exception as e:
        UI.print_failure(f"Error recruiting follower: {e}")

def _handle_npc_dismiss_follower(npc: Any, player: Any) -> None:
    """Handles the process of dismissing an NPC from the player's service."""
    try:
        if npc in player.followers:
            player.followers.remove(npc)
            npc.is_follower = False
            npc.disposition = max(0, npc.disposition - 10)
            UI.slow_print(UI.capitalize_dialogue(f"\"{npc.name} nods. 'As you wish. May our paths cross again.'\""))
        else:
            UI.slow_print("This person is not in your service.") # Should not happen
    except Exception as e:
        UI.print_failure(f"Error dismissing follower: {e}")

def handle_npc_dialogue(npc: Any, player: Any, current_location: Any) -> None:
    """Main handler for NPC dialogue interactions."""
    try:
        UI.clear_screen()
        player.add_talked_to_npc(npc.unique_id)

        UI.slow_print(f"You approach {npc.name} ({npc.role.replace('_',' ').capitalize()}). Disposition: {npc.disposition}")
        UI.slow_print(f'"{npc.greeting}"')
        previous_dialogue_purpose = ""  # To track if purpose was already stated

        while True:
            options_texts = []
            quests_to_turn_in = player.quest_log.get_quests_for_turn_in(npc.unique_id)

            if quests_to_turn_in:
                options_texts.append("Turn in a completed quest")

            options_texts.append("Ask for rumors or work")
            options_texts.append("Ask about your work/purpose")
            options_texts.append("Discuss this place")

            if not npc.is_follower and npc not in player.followers:
                if "mercenary" in npc.role.lower() and npc.mercenary_hire_cost > 0:
                    options_texts.append(f"Offer to hire for {npc.mercenary_hire_cost} gold")
                elif npc.role.lower() in ["adventurer", "companion_warrior", "explorer"] and npc.disposition >= 65:
                    options_texts.append("Ask to join your travels")
            elif npc.is_follower and npc in player.followers:
                options_texts.append("Dismiss from service")

            options_texts.append("Farewell")

            UI.print_menu(options_texts)
            choice_input = UI.print_prompt("Your response? (Enter number)").strip()

            if not choice_input.isdigit():
                UI.slow_print("Please enter a valid number for your choice.")
                UI.press_enter()
                continue

            choice_idx = int(choice_input)
            action_taken = False
            chosen_option_text = None

            if 1 <= choice_idx <= len(options_texts):
                chosen_option_text = options_texts[choice_idx - 1]

            if chosen_option_text == "Turn in a completed quest":
                if quests_to_turn_in:
                    # Let player choose which quest if multiple
                    UI.slow_print("Which quest would you like to turn in?")
                    for i, q_to_turn_in in enumerate(quests_to_turn_in):
                        UI.print_info(f"[{i+1}] {q_to_turn_in.title}")

                    quest_choice_input = UI.print_prompt("Enter quest number:").strip()
                    if quest_choice_input.isdigit():
                        quest_choice_idx = int(quest_choice_input) - 1
                        if 0 <= quest_choice_idx < len(quests_to_turn_in):
                            selected_quest = quests_to_turn_in[quest_choice_idx]
                            UI.slow_print(f"You discuss completing '{selected_quest.title}' with {npc.name}.")
                            # Assuming process_quest_rewards handles dialogue and rewards
                            process_quest_rewards(player, selected_quest, npc)
                            # Disposition change might be handled in process_quest_rewards or here
                            npc.disposition = min(100, npc.disposition + random.randint(5, 15))
                            # Remove the quest from turn-in options for this dialogue session
                            quests_to_turn_in.pop(quest_choice_idx)
                            if not quests_to_turn_in and "Turn in a completed quest" in options_texts:
                                options_texts.remove("Turn in a completed quest")

                        else:
                            UI.slow_print("Invalid quest selection.")
                    else:
                        UI.slow_print("Invalid input for quest selection.")
                else:
                    UI.slow_print("You have no quests to turn in to this person right now.")  # Should not happen if menu is correct
                action_taken = True

            elif chosen_option_text == "Ask for rumors or work":
                _handle_npc_share_rumor(npc, player, current_location)
                action_taken = True

            elif chosen_option_text == "Ask about your work/purpose":
                current_dialogue = npc.purpose
                spoken_purpose = current_dialogue.strip()
                first_word = spoken_purpose.split(' ')[0].lower() if spoken_purpose else ""
                if not first_word in ("i", "my", "i'm", "i've", "to"):
                    # Check if the second word starts with a capital letter
                    words = spoken_purpose.split()
                    if len(words) > 1 and words[1][0].isupper():
                        pass  # Do not add "I "
                    else:
                        spoken_purpose = "I " + spoken_purpose
                if spoken_purpose.startswith("I ") and len(spoken_purpose) > 2 and spoken_purpose[2].islower():
                    spoken_purpose = "I " + spoken_purpose[2].upper() + spoken_purpose[3:]
                elif spoken_purpose and spoken_purpose[0].islower():
                    spoken_purpose = spoken_purpose[0].upper() + spoken_purpose[1:]

                if current_dialogue == previous_dialogue_purpose:
                    UI.slow_print(UI.capitalize_dialogue(f'"As I said, {spoken_purpose}"'))
                else:
                    UI.slow_print(UI.capitalize_dialogue(f'"{spoken_purpose}"'))
                previous_dialogue_purpose = current_dialogue

                if npc.disposition > 60 and "merchant" in npc.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f'"Perhaps you\'re looking to buy or sell, {player.full_name}? I have a few things that might interest you, or I might be interested in what you have to offer."'))
                elif npc.disposition > 55 and "guard" in npc.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f'"Just try to stay out of trouble. That makes my job easier."'))

                if not npc.has_offered_quest and random.random() < 0.1:  # 10% chance from purpose
                    UI.slow_print(UI.capitalize_dialogue(f'"Actually, since you\'re asking, there is something that\'s been bothering me about my work..."'))
                    # Determine location_data_dict for quest generation
                    if hasattr(current_location, 'id') and current_location.id in RAW_LOCATION_DATA_MAP:
                        location_data_dict_for_quest = RAW_LOCATION_DATA_MAP[current_location.id]
                    elif isinstance(current_location, dict) and "id" in current_location:
                        location_data_dict_for_quest = current_location
                    else:
                        location_data_dict_for_quest = {"name": "this area", "tags": [], "id": "unknown_loc_id_purpose_quest"}

                    quest_to_offer = generate_location_appropriate_quest(player.stats.level, location_data_dict_for_quest, npc.unique_id)
                    if quest_to_offer:
                        if is_quest_related_to_npc(npc, quest_to_offer) and not player.quest_log.get_quest_by_id(quest_to_offer.quest_id):
                            _handle_npc_offer_quest(npc, player, quest_to_offer)
                        else:
                            UI.slow_print(UI.capitalize_dialogue(random.choice(['"But perhaps it\'s best not to burden you with my troubles."', '"Nevermind, I\'ll handle it myself."'])))
                    else:
                        UI.slow_print(UI.capitalize_dialogue(random.choice(['"But perhaps it\'s best not to burden you with my troubles."', '"Nevermind, I\'ll handle it myself."'])))
                action_taken = True

            elif chosen_option_text == "Discuss this place":
                _handle_npc_discuss_place(npc, player, current_location)  # Pass player if needed by discuss_place, currently not.
                action_taken = True

            elif chosen_option_text == "Farewell":
                farewell_messages = ['Farewell, traveler.', 'May your path be clear.', 'Until next time.']
                UI.slow_print(UI.capitalize_dialogue(f'"{random.choice(farewell_messages)}"'))
                return

            elif chosen_option_text and "Offer to hire for" in chosen_option_text:
                _handle_npc_hire_mercenary(npc, player)
                action_taken = True

            elif chosen_option_text == "Ask to join your travels":
                _handle_npc_recruit_follower(npc, player)
                action_taken = True

            elif chosen_option_text == "Dismiss from service":
                _handle_npc_dismiss_follower(npc, player)
                action_taken = True

            else:  # No valid option chosen from menu
                UI.slow_print("A clear answer is expected, traveler.")
                # No action_taken = True, so it will loop back to menu prompt after enter.

            if action_taken:
                UI.press_enter()
                UI.clear_screen()
                UI.slow_print(f"You are speaking with {npc.name}. Disposition: {npc.disposition}")
                # Greeting is not repeated, purpose is handled via its option.
    except Exception as e:
        UI.print_failure(f"Error in handle_npc_dialogue: {e}")