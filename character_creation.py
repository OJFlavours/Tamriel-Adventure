# character_creation.py
import random
import traceback
from ui import LINE_WIDTH

from player import Player
from stats import Stats, RACES, CLASSES
from ui import UI
from items import generate_item_from_key
from quests import QuestLog
from npc_names import Race, Gender, generate_npc_name # Import here to avoid circular dependency

def initialize_player():
    try:
        UI.clear_screen() # Changed from clear_screen()
        UI.print_heading("Forge Your Legend")
        wrapped_text = UI.wrap_text("The scrolls have foretold your arrival, yet your path remains unwritten...", width=LINE_WIDTH)
        padding = " " * ((LINE_WIDTH - len(wrapped_text)) // 2)
        UI.slow_print(padding + wrapped_text)

        # --- Quick-Start / Manual Choice ---
        UI.print_line()
        UI.print_menu(["Manual Character Creation", "Quick Start (Random Character)"])
        creation_choice = UI.print_prompt("Choose your path (1 or 2)")

        # --- Character Creation Logic Starts Here ---
        # The following code will be made conditional based on the choice above.

        player_race_str = "nord"
        player_gender = "male"
        player_name = ""
        selected_class_key = "warrior"
        selected_subclass_key_actual = ""

        if creation_choice == "2": # Quick Start
            UI.slow_print("\nForging a legend from the ether...")

            # Randomly select Race
            race_options = list(RACES.keys())
            player_race_str = random.choice(race_options)
            race_display_name = RACES[player_race_str]["display_name"]
            UI.print_success(f"Lineage: {player_race_str.capitalize()}")

            # Randomly select Gender
            player_gender = random.choice(["male", "female"])
            UI.print_success(f"Form: {player_gender.capitalize()}")

            # Randomly select Name Type and Name
            name_types = ["noble", "commoner"] # Exclude custom for quick start
            random_name_type = random.choice(name_types)
            player_name = generate_npc_name(Race(player_race_str), Gender(player_gender), tags={})
            UI.print_success(f"Name: '{player_name}'")

            # Randomly select Class
            class_options_keys = list(CLASSES.keys())
            selected_class_key = random.choice(class_options_keys)
            selected_class_data = CLASSES[selected_class_key]
            UI.print_success(f"Path of Skill: {selected_class_data['name']}")

            # Randomly select Sub-class
            subclass_options_keys = list(selected_class_data["subclasses"].keys())
            selected_subclass_key_actual = random.choice(subclass_options_keys)
            selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
            UI.print_success(f"Specialization: {selected_subclass_final_data['name']}")

        else: # Manual Character Creation (Existing Logic)
            UI.slow_print("\nFrom which lineage do you hail?")
            race_options = list(RACES.keys())
            for i, race_name_key in enumerate(race_options):
                race_bonuses = RACES[race_name_key]
                race_display_name = race_bonuses["display_name"]
                
                bonus_descs = []
                if race_bonuses.get("strength_mod"): bonus_descs.append(f"+{race_bonuses['strength_mod']} STR")
                if race_bonuses.get("intelligence_mod"): bonus_descs.append(f"+{race_bonuses['intelligence_mod']} INT")
                if race_bonuses.get("luck_mod"): bonus_descs.append(f"+{race_bonuses['luck_mod']} LCK")
                if race_bonuses.get("magicka_mod"): bonus_descs.append(f"+{race_bonuses['magicka_mod']} Max Magicka")
                if race_bonuses.get("poison_resist",0) > 0: bonus_descs.append(f"{race_bonuses['poison_resist']}% Poison Resist")
                if race_bonuses.get("fire_resist",0) > 0: bonus_descs.append(f"{race_bonuses['fire_resist']}% Fire Resist")
                for key, value in race_bonuses.items():
                    if key.endswith("_skill") and value > 0:
                        bonus_descs.append(f"+{value} {key.replace('_mod','').replace('_skill','').capitalize()}")
                bonus_str = f" ({', '.join(bonus_descs)})" if bonus_descs else ""
                UI.slow_print(f"[{i+1}] {race_display_name}{bonus_str}", speed=0.005)

            while True:
                race_choice_input = UI.print_prompt("Enter the number of your chosen race")
                try:
                    race_index = int(race_choice_input) - 1
                    if 0 <= race_index < len(race_options):
                        player_race_str = race_options[race_index]
                        break
                    else: UI.slow_print("Invalid choice.")
                except ValueError: UI.slow_print("Invalid input.")
            UI.print_success(f"A {RACES[player_race_str]['display_name'].capitalize()} you are. Your ancestors watch over you.")

            # 2. Choose Gender
            UI.slow_print("\nWhat is your form?")
            UI.print_menu(["Male", "Female"])

            player_gender = ""
            while player_gender not in ["male", "female"]:
                gender_choice_input = UI.print_prompt("Enter your choice (1 or 2)")
                if gender_choice_input == "1":
                    player_gender = "male"
                elif gender_choice_input == "2":
                    player_gender = "female"
                else:
                    UI.slow_print("Invalid choice. Please enter 1 for Male or 2 for Female.")

            UI.print_success(f"You have chosen the form of a {player_gender.capitalize()}.")

            # 3. Choose Social Standing / Name Type
            player_name_type = ""
            while player_name_type not in ["noble", "commoner", "custom"]:
                UI.slow_print("\nName by lineage, common tongue, or your own legend?")
                UI.print_menu(["Noble (names of influence)", "Commoner (everyday names)", "Forge my own name (Custom)"])
                name_type_choice_input = UI.print_prompt("Enter your choice (1, 2, or 3)").strip()
                if name_type_choice_input == "1":
                    player_name_type = "noble"
                elif name_type_choice_input == "2":
                    player_name_type = "commoner"
                elif name_type_choice_input == "3":
                    player_name_type = "custom"
                else:
                    UI.slow_print("Invalid choice. Please select 1, 2, or 3.")

            if player_name_type == "custom":
                while not player_name:
                    player_name = UI.print_prompt("Speak your true name, wanderer")
                    if not player_name:
                        UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
            else:
                player_name = generate_npc_name(Race(player_race_str), Gender(player_gender), tags={})
                UI.print_success(f"Name: '{player_name}'")

            # 4. Choose Class (Path of Skill)
#
#
#
#
#
#
            UI.slow_print("\nWhat path of skill do you tread?")
            class_options_keys = list(CLASSES.keys())
            for i, class_id_key in enumerate(class_options_keys):
                class_data = CLASSES[class_id_key]
                UI.slow_print(f"[{i+1}] {class_data['name']} - {class_data['desc']}", speed=0.005)

            selected_class_key = "warrior"
            selected_class_data = CLASSES[selected_class_key]
            while True:
                class_choice_input = UI.print_prompt("Choice")
                try:
                    class_index = int(class_choice_input) - 1
                    if 0 <= class_index < len(class_options_keys):
                        selected_class_key = class_options_keys[class_index]
                        selected_class_data = CLASSES[selected_class_key]
                        break
                    else: UI.slow_print("Invalid choice.")
                except ValueError: UI.slow_print("Invalid input.")
            UI.print_success(f"The path of the {selected_class_data['name']} chosen.")

            UI.slow_print(f"\nWithin {selected_class_data['name']}, which specialization calls?")
            subclass_options_map = {str(idx+1): sc_key for idx, sc_key in enumerate(selected_class_data["subclasses"].keys())}
            for display_num, sc_id_key in subclass_options_map.items():
                subclass_item_data = selected_class_data["subclasses"][sc_id_key]
                attr_str = ", ".join([f"{k.capitalize()[:3]}: {v}" for k,v in subclass_item_data["attributes"].items()])
                skill_str = ", ".join([f"{k.replace('_',' ').capitalize()}: {v}" for k,v in subclass_item_data["skills"].items()])
                inv_str = ", ".join([name.replace('_', ' ').title() for name in subclass_item_data["inventory"]])
                UI.slow_print(f"[{display_num}] {subclass_item_data['name']}", speed=0.005)
                UI.slow_print(f"    Attrs: {attr_str}", speed=0.005)
                UI.slow_print(f"    Skills: {skill_str}", speed=0.005)
                UI.slow_print(f"    Gear: {inv_str}", speed=0.005)

            selected_subclass_key_actual = list(selected_class_data["subclasses"].keys())[0]
            selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
            while True:
                subclass_choice_input_str = UI.print_prompt("Choice")
                if subclass_choice_input_str in subclass_options_map:
                    selected_subclass_key_actual = subclass_options_map[subclass_choice_input_str]
                    selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
                    break
                else: UI.slow_print("Invalid choice.")
            UI.print_success(f"You are now a {selected_subclass_final_data['name']}.")

        # Create Player instance using selected data
        selected_class_data = CLASSES[selected_class_key] # Ensure this is set correctly after choice
        selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual] # Ensure this is set correctly after choice

        base_stats_params = selected_class_data.get("attributes", {}).copy()
        base_stats_params.update(selected_subclass_final_data["attributes"])

        # Apply racial modifiers
        race_mods = RACES[player_race_str]
        for attr, mod_val in race_mods.items():
            if attr.endswith("_mod") and attr.replace("_mod","") in base_stats_params:
                stat_name = attr.replace("_mod","")
                base_stats_params[stat_name] = base_stats_params.get(stat_name, 40) + mod_val
            elif attr.endswith("_resist"):
                base_stats_params[attr] = mod_val
            elif attr == "magicka_mod":
                base_stats_params["max_magicka_bonus"] = mod_val

        player_stats_instance = Stats(
            strength=base_stats_params.get("strength", 40),
            intelligence=base_stats_params.get("intelligence", 40),
            willpower=base_stats_params.get("willpower", 40),
            agility=base_stats_params.get("agility", 40),
            speed=base_stats_params.get("speed", 40),
            endurance=base_stats_params.get("endurance", 40),
            personality=base_stats_params.get("personality", 40),
            luck=base_stats_params.get("luck", 40),
            poison_resist=base_stats_params.get("poison_resist",0),
            magic_resist=base_stats_params.get("magic_resist",0),
            frost_resist=base_stats_params.get("frost_resist",0),
            shock_resist=base_stats_params.get("shock_resist",0),
            fire_resist=base_stats_params.get("fire_resist",0),
            level=1, gold=50
        )
        if "max_magicka_bonus" in base_stats_params:
            player_stats_instance.max_magicka += base_stats_params["max_magicka_bonus"]
            player_stats_instance.current_magicka = player_stats_instance.max_magicka

        player_skills = selected_subclass_final_data["skills"].copy()
        # Apply racial skill bonuses
        for skill_key, bonus_value in race_mods.items():
            if skill_key.endswith("_skill"):
                actual_skill_name = skill_key.replace("_skill", "")
                player_skills[actual_skill_name] = player_skills.get(actual_skill_name, 5) + bonus_value

        starting_spell_keys_for_subclass = selected_subclass_final_data.get("starting_spells", [])

        player = Player(
            name=player_name,
            race=player_race_str,
            subclass_name=selected_subclass_final_data["name"], # Pass subclass_name
            stats_instance=player_stats_instance,
            skills=player_skills,
            starting_spell_keys=starting_spell_keys_for_subclass # Pass starting spell keys
        )
        player.class_key = selected_class_key # Set the class_key attribute
        player.combat = None

        # Initialize player's known locations (will be populated by initialize_starting_location)
        player.known_location_ids = set()
        player.known_locations_objects = []

        UI.slow_print("Preparing your starting gear...")
        given_items = set()
        for item_key_from_subclass in selected_subclass_final_data["inventory"]:
            if item_key_from_subclass not in given_items:
                item_instance = generate_item_from_key(item_key_from_subclass, player.stats.level)
                if item_instance:
                    if player.add_item(item_instance):
                        if item_instance.category in ["weapon", "armor"]:
                            player.equip_item(item_instance)
                    else:
                        UI.print_warning(f"Could not add starting item {item_instance.name} (inventory full or error).")
                else:
                    UI.print_warning(f"Could not generate starting item for key: {item_key_from_subclass}")
                given_items.add(item_key_from_subclass)

        if player.stats.inventory: UI.slow_print(f"In Your Satchel: {', '.join([item.name.replace('_', ' ').title() for item in player.stats.inventory if item not in player.equipment])}.", speed=0.01)
        if player.equipment: UI.slow_print(f"Equipped: {', '.join([eq.name.replace('_', ' ').title().split(' equipped to ')[0] for eq in player.equipment])}.", speed=0.01)
        else: UI.slow_print("You start with no items equipped.", speed=0.01)

        player.quest_log = QuestLog()
        UI.print_line()
        UI.press_enter()
        return player

    except Exception as e:
        UI.print_failure(f"Error in initialize_player: {e}")
        traceback.print_exc()
        return None
