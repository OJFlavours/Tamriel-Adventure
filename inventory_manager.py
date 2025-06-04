# inventory_manager.py
from player import Player # Assuming Player class is in player.py
from ui import UI # Assuming UI class is in ui.py
# from items import Item # Not strictly needed if only interacting via Player methods

def clear_screen(): # Helper, if not directly using UI.clear_screen()
    UI.clear_screen()

def display_inventory_with_equipped(player: Player):
    UI.print_subheading("Inventory")
    if not player.stats.inventory and not player.equipment:
        UI.slow_print("Your satchel is empty, and you wear nothing but your conviction.")
        return []

    display_list_for_selection = []
    current_selection_idx = 1

    UI.print_info("--- Equipped ---")
    if not player.equipment:
        UI.print_info("Nothing equipped.")
    else:
        for item_obj in player.equipment:
            desc_preview = item_obj.get_description().split('\n')[0]
            for slot, Gitem in player.slots.items():
                if Gitem == item_obj:
                     desc_preview += f" (Slot: {slot.capitalize()})"
                     break
            UI.print_info(f"[{current_selection_idx}] {item_obj.name} (Equipped) - {desc_preview}")
            display_list_for_selection.append({"item": item_obj, "equipped": True, "original_index": -1}) # original_index might not be needed here
            current_selection_idx +=1
    
    UI.print_info("\n--- Carried in Satchel ---")
    carried_items_display = []
    for item_obj in player.stats.inventory:
        is_also_equipped = any(equipped_item == item_obj for equipped_item in player.equipment)
        if not is_also_equipped:
            carried_items_display.append(item_obj)

    if not carried_items_display:
        UI.print_info("Carrying nothing else in your satchel.")
    else:
        for item_obj in carried_items_display:
            desc_preview = item_obj.get_description().split('\n')[0]
            UI.print_info(f"[{current_selection_idx}] {item_obj.name} - {desc_preview}")
            display_list_for_selection.append({"item": item_obj, "equipped": False, "original_index": -1})
            current_selection_idx += 1
        
    return display_list_for_selection


def handle_inventory_menu(player: Player):
    while True:
        clear_screen()
        UI.print_heading("Possessions")
        
        display_entries = display_inventory_with_equipped(player)

        if not display_entries:
            UI.press_enter()
            break
        
        UI.print_line()
        item_choice_input = UI.print_prompt("Select an item to interact with (Number or 0 to go back):")
        
        if not item_choice_input.isdigit():
            UI.slow_print("Invalid input. Please enter a number.")
            UI.press_enter()
            continue

        item_choice_idx_user = int(item_choice_input)
        if item_choice_idx_user == 0:
            break
        
        actual_item_idx_list = item_choice_idx_user - 1

        if 0 <= actual_item_idx_list < len(display_entries):
            selected_entry = display_entries[actual_item_idx_list]
            selected_item_obj = selected_entry["item"]
            is_equipped_flag = selected_entry["equipped"]

            clear_screen()
            UI.print_heading(f"Item Details: {selected_item_obj.name} {'(Equipped)' if is_equipped_flag else ''}")
            print(selected_item_obj.get_description()) # Direct print for potentially multi-line description
            UI.print_line()

            options = []
            if is_equipped_flag:
                options.append("Unequip")
            else:
                options.append("Equip")
                if selected_item_obj.category in ["potion", "food", "scroll", "ingredient"]:
                    options.append("Use")
            
            if not is_equipped_flag: # Can only drop unequipped items from this menu path
                options.append("Drop")

            options.append("Back to Inventory List")
            
            UI.print_menu(options)
            action_choice_str = UI.print_prompt("Your choice?")

            chosen_action_text = None
            if action_choice_str.isdigit():
                action_num = int(action_choice_str)
                if 1 <= action_num <= len(options):
                    chosen_action_text = options[action_num-1]
            
            action_performed_this_loop = False
            if chosen_action_text == "Unequip":
                player.unequip_item(selected_item_obj)
                action_performed_this_loop = True
            elif chosen_action_text == "Equip":
                player.equip_item(selected_item_obj) # Assumes Player.equip_item handles logic
                action_performed_this_loop = True
            elif chosen_action_text == "Use":
                if selected_item_obj.category in ["potion", "food", "scroll", "ingredient"]:
                    player.use_item(selected_item_obj) # Assumes Player.use_item handles logic
                else:
                    UI.slow_print(f"{selected_item_obj.name} cannot be 'used' in this way now.")
                action_performed_this_loop = True
            elif chosen_action_text == "Drop":
                if not is_equipped_flag: # Redundant check, but safe
                    player.drop_item(selected_item_obj) # Assumes Player.drop_item handles logic
                else: # Should not be reachable if "Drop" is only shown for unequipped
                    UI.slow_print(f"You must unequip {selected_item_obj.name} first.")
                action_performed_this_loop = True
            elif chosen_action_text == "Back to Inventory List":
                continue 
            else:
                UI.slow_print("Invalid action or choice.")
                action_performed_this_loop = True # To trigger press_enter
            
            if action_performed_this_loop:
                UI.press_enter() # Pause after action before re-listing inventory
        else:
            UI.slow_print("Invalid selection number.")
            UI.press_enter()

def sort_inventory_menu(player: Player): # This function is not called in game.py from what I can see
    UI.print_subheading("Sort Inventory")
    sort_choice = UI.print_prompt("Sort inventory by [1] Name [2] Category")
    if sort_choice == "1":
        player.stats.inventory.sort(key=lambda item: item.name.lower())
        UI.slow_print("Inventory sorted by name.")
    elif sort_choice == "2":
        player.stats.inventory.sort(key=lambda item: item.category.lower())
        UI.slow_print("Inventory sorted by category.")
    else:
        UI.slow_print("Invalid choice.")
    UI.press_enter()


def handle_item_use(player: Player):
    UI.print_subheading("Use Item from Inventory")
    if not player.stats.inventory:
        UI.slow_print("Your inventory is empty.")
        UI.press_enter()
        return

    usable_items = [item for item in player.stats.inventory if item.category in ["potion", "food", "scroll", "ingredient"]]
    
    if not usable_items:
        UI.slow_print("You have no items that can be readily used in this way.")
        UI.press_enter()
        return

    UI.slow_print("Usable items in your inventory:")
    for i, item in enumerate(usable_items, 1):
        UI.print_info(f"[{i}] {item.name} - Desc: {item.get_description()}")

    try:
        item_choice_input = UI.print_prompt(
            "Which item do you wish to use? (Enter number, 0 to cancel)"
        )
        if not item_choice_input.isdigit():
            UI.slow_print("Invalid input.")
            UI.press_enter()
            return

        item_choice_idx = int(item_choice_input)
        if item_choice_idx == 0:
            UI.slow_print("No item used.")
            UI.press_enter()
            return
        
        if 1 <= item_choice_idx <= len(usable_items):
            selected_item = usable_items[item_choice_idx - 1]
            UI.slow_print(f"You use {selected_item.name}...")
            selected_item.use(player) # Assumes item.use() handles its effects and removal if consumable
        else:
            UI.slow_print("Invalid item number.")
    except ValueError:
        UI.slow_print("Invalid input. Please enter a number.")
    except Exception as e:
        # It's good practice to log the full error for debugging
        # print(f"DEBUG: Error in handle_item_use: {e}")
        # traceback.print_exc() # For more detailed logs during development
        UI.print_failure(f"An error occurred while using item: {e}")
    UI.press_enter()