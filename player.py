# player.py
import random
from typing import Dict, List, Any, Set

# Assuming QuestLog is in quests.py and Item is in items.py
from quests import QuestLog, Quest # Import Quest for type hinting
from items import Item, Torch # Import Item and Torch
from ui import UI # For UI messages
from stats import Stats # Import the Stats class

from spells import Spell, get_spell # Import Spell class and get_spell function

class Player:
    def __init__(self, name: str, race: str, subclass_name: str, stats_instance: Stats, skills: Dict[str, int], starting_spell_keys: List[str] = None):
        self.full_name = name
        self.name = name.split(" ")[0] # First name for simpler references
        self.race = race
        self.subclass = subclass_name # Store the subclass name
        self.stats = stats_instance # This is the Stats object instance
        self.skills = skills
        self.quest_log = QuestLog()
        self.combat = None # Stores Combat instance if player is in combat

        self.slots = {
            "head": None, "chest": None, "hands": None, "feet": None,
            "main_hand": None, "off_hand": None,
            "amulet": None, "ring1": None, "ring2": None
        }

        # Trackers for quest objectives and world state
        self.defeated_enemies_tracker: Dict[str, int] = {}
        self.talked_to_npcs: Set[str] = set()
        self.current_location_obj: Dict[str, Any] | None = None # Current location as a dictionary
        self.known_locations_objects: List[Dict[str, Any]] = [] # List of known location dicts
        self.faction_reputation: Dict[str, int] = {
            "imperial_legion": 0, "stormcloaks": 0, "thieves_guild": 0,
            "college_of_winterhold": 0, "companions": 0, "dark_brotherhood": 0,
            "silver_blood": 0, "thalmor": 0, "khajiit_caravans": 0, "falkreath": 0
        }
        self.known_location_ids: Set[int] = set() # Stores IDs of known locations

        # Combat flags
        self.is_blocking: bool = False
        self.is_dodging: bool = False
        self.is_power_attacking: bool = False # Flag for _calculate_damage

        # Spellcasting
        self.known_spells: List[Spell] = []
        if starting_spell_keys:
            for spell_key in starting_spell_keys:
                spell = get_spell(spell_key)
                if spell:
                    self.known_spells.append(spell)
                else:
                    UI.print_warning(f"Could not find starting spell for key: {spell_key}")
        
        self.followers: List[NPC] = [] # List of NPC objects following the player


        # Integrated from original player.py
        self.inventory = self.stats.inventory # Player's inventory is managed by the Stats object
        self.visibility = 10  # Initial visibility, modified by torches, spells, etc.

    @property
    def location(self) -> Dict[str, Any] | None:
        """Property to access the player's current location object."""
        return self.current_location_obj

    @location.setter
    def location(self, value: Dict[str, Any] | None) -> None:
        """Property to set the player's current location object."""
        self.current_location_obj = value

    @property
    def level(self) -> int:
        return self.stats.level

    @property
    def experience(self) -> int:
        return self.stats.experience

    @property
    def next_level_exp(self) -> int:
        return self.stats.next_level_exp

    @property
    def equipment(self) -> List[Item]:
        equipped_items = []
        for item_obj in self.slots.values():
            if item_obj and item_obj not in equipped_items:
                equipped_items.append(item_obj)
        return equipped_items

    def add_item(self, item_to_add: Item) -> bool:
        """Adds an item to inventory, checking encumbrance via Stats object."""
        added = self.stats.add_to_inventory(item_to_add)
        if added:
            UI.slow_print(f"You obtained {item_to_add.name}.")
        # No message if not added, as stats.add_to_inventory handles encumbrance message
        return added

    def remove_item(self, item_to_remove: Item) -> bool:
        """Removes an item from inventory via Stats object."""
        removed = self.stats.remove_from_inventory(item_to_remove)
        if removed:
            UI.slow_print(f"You lost {item_to_remove.name}.")
        else:
            # This message might be redundant if item is equipped, as unequip handles its own.
            # Or if item simply not found.
            UI.slow_print(f"You do not have {item_to_remove.name} in your carry inventory or it's an error.")
        return removed

    def has_item(self, item_name: str) -> Item | None:
        """Checks inventory (including Stats object's list) and equipped items for an item by name."""
        # Check inventory first (from Stats object)
        for item_obj in self.stats.inventory:
            if item_obj and item_obj.name.lower() == item_name.lower():
                return item_obj
        # Then check equipped items
        for item_obj in self.equipment: # self.equipment is a property listing equipped items
             if item_obj and item_obj.name.lower() == item_name.lower():
                return item_obj
        return None

    def has_lit_torch(self) -> bool:
        """Checks inventory and equipment for a lit torch."""
        # Check inventory (via Stats)
        for item_obj in self.stats.inventory:
            if isinstance(item_obj, Torch) and item_obj.is_lit:
                self.visibility = 30 # Example: Lit torch sets visibility higher
                return True
        # Check equipped items
        for item_obj in self.equipment:
            if isinstance(item_obj, Torch) and item_obj.is_lit:
                self.visibility = 30
                return True
        self.visibility = 10 # Default visibility if no lit torch
        return False

    def move(self, direction: str) -> None:
        """
        Placeholder for player-specific actions upon moving.
        Actual location transition is handled by game.py.
        """
        # This method is largely superseded by game.py's travel system.
        # It can be used for player-specific effects of movement if any.
        # For now, it's a stub.
        UI.print_system_message(f"Player.move({direction}) called. Actual travel logic in game.py.")
        # Example: self.stats.current_fatigue -= 5 # Moving costs fatigue

    def use_item(self, item_name: str, target: Any = None) -> None:
        """Uses an item from inventory or equipment."""
        item_obj = self.has_item(item_name)
        if item_obj:
            if hasattr(item_obj, 'use') and callable(item_obj.use):
                # The item's use method should handle its own effects,
                # including removal from inventory if consumable.
                item_obj.use(self, target_entity=target) # Pass player as the one using the item
            else:
                UI.slow_print(f"You cannot use {item_obj.name} in that way.")
        else:
            UI.slow_print(f"You do not have {item_name} in your inventory.")

    def _unequip_from_slot(self, slot_name: str) -> Item | None:
        """Internal helper to unequip from a slot and return item to inventory."""
        item_in_slot = self.slots.get(slot_name)
        if item_in_slot:
            self.slots[slot_name] = None
            if not self.stats.add_to_inventory(item_in_slot):
                UI.print_warning(f"Could not return {item_in_slot.name} to inventory from {slot_name} (Encumbered?).")
            else:
                UI.slow_print(f"{item_in_slot.name} unequipped from {slot_name}.")
            self.stats.update_encumbrance()
            return item_in_slot
        return None

    def equip_item(self, item_to_equip: Item) -> bool:
        """Equips an item from inventory to an appropriate slot."""
        if item_to_equip not in self.stats.inventory:
            UI.slow_print(f"{item_to_equip.name} is not in your inventory to equip.")
            return False

        if item_to_equip.category not in ["weapon", "armor", "jewelry"]:
            UI.slow_print(f"You cannot equip {item_to_equip.name}; it's not standard equipment.")
            return False

        target_slot_tag = item_to_equip.equipment_tag

        # Handle rings (ring1, ring2)
        if target_slot_tag == "ring":
            slot_to_place_in = "ring1" if not self.slots["ring1"] else "ring2" if not self.slots["ring2"] else None
            if not slot_to_place_in: # Both full, unequip ring1
                UI.slow_print(f"Both ring slots full. Unequipping {self.slots['ring1'].name} to make space.")
                self._unequip_from_slot("ring1")
                slot_to_place_in = "ring1"
            self.slots[slot_to_place_in] = item_to_equip
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} equipped to {slot_to_place_in}.")
            self.stats.update_encumbrance()
            return True

        # Handle two-handed weapons
        if target_slot_tag == "two_handed":
            if self.slots["main_hand"]: self._unequip_from_slot("main_hand")
            if self.slots["off_hand"]: self._unequip_from_slot("off_hand") # Also clear off_hand
            self.slots["main_hand"] = item_to_equip
            # Conceptually, off_hand is also "used" by a two-handed weapon
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} (Two-Handed) equipped.")
            self.stats.update_encumbrance()
            return True

        # Handle other standard slots
        if target_slot_tag in self.slots:
            # If equipping a 1H weapon and a 2H is in main_hand, unequip 2H
            if target_slot_tag == "main_hand" and self.slots["main_hand"] and getattr(self.slots["main_hand"], 'equipment_tag', '') == "two_handed":
                self._unequip_from_slot("main_hand")
            # If equipping to off_hand but main_hand has a two-handed weapon
            if target_slot_tag == "off_hand" and self.slots["main_hand"] and getattr(self.slots["main_hand"], 'equipment_tag', '') == "two_handed":
                UI.slow_print(f"Cannot equip {item_to_equip.name} in off-hand while wielding {self.slots['main_hand'].name}.")
                return False

            if self.slots[target_slot_tag]: # If slot is occupied, unequip current item
                self._unequip_from_slot(target_slot_tag)
            
            self.slots[target_slot_tag] = item_to_equip
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} equipped to {target_slot_tag}.")
            self.stats.update_encumbrance()
            return True
        
        UI.slow_print(f"Cannot equip {item_to_equip.name}: Unknown slot tag '{target_slot_tag}'.")
        return False

    def unequip_item(self, item_to_unequip: Item) -> bool:
        """Unequips an item and returns it to inventory."""
        found_slot_name = None
        for slot_name, equipped_item_in_slot in self.slots.items():
            if equipped_item_in_slot == item_to_unequip:
                found_slot_name = slot_name
                break
        if found_slot_name:
            self._unequip_from_slot(found_slot_name)
            self.stats.update_encumbrance()
            return True
        UI.slow_print(f"{item_to_unequip.name} is not currently equipped.")
        return False

    def examine_item(self, item_name: str) -> None:
        item_obj = self.has_item(item_name)
        if item_obj:
            UI.slow_print(f"You examine {item_obj.name} closely...")
            print(f"\n{item_obj.get_description()}") # Assumes Item has get_description
            UI.press_enter()
        else:
            UI.slow_print(f"You don't have an item called {item_name}.")

    def drop_item(self, item_name: str) -> bool:
        item_to_drop = self.has_item(item_name)
        if not item_to_drop:
            UI.slow_print(f"You don't have {item_name} to drop.")
            return False
        
        if item_to_drop in self.equipment: # Check if it's equipped
            UI.slow_print(f"You must unequip {item_to_drop.name} before dropping it.")
            return False
            
        if self.stats.remove_from_inventory(item_to_drop): # Try removing from Stats's inventory
            UI.slow_print(f"You dropped {item_to_drop.name}.")
            self.stats.update_encumbrance()
            return True
        
        UI.slow_print(f"Could not drop {item_to_drop.name}.") # Fallback
        return False

    def sort_inventory(self, key: str = "name") -> None:
        if hasattr(self.stats, 'inventory') and isinstance(self.stats.inventory, list):
            try:
                self.stats.inventory.sort(key=lambda item_obj: str(getattr(item_obj, key, "")).lower())
                UI.slow_print(f"Inventory sorted by {key.capitalize()}.")
            except AttributeError:
                UI.print_warning(f"Cannot sort by '{key}'.")
        else:
            UI.print_warning("Inventory not available for sorting.")

    def inspect_equipped_items(self) -> None:
        UI.print_subheading("--- Currently Equipped ---")
        found_any = False
        for slot_name, item_obj in self.slots.items():
            if item_obj:
                desc = item_obj.get_description().split('\n')[0] if hasattr(item_obj, 'get_description') else "No description."
                UI.print_info(f"{slot_name.capitalize()}: {item_obj.name} - {desc}")
                found_any = True
        if not found_any:
            UI.slow_print("Nothing equipped.")

    def improve_skill(self, skill_name: str, amount: int = 1) -> None:
        current_val = self.skills.get(skill_name, 0)
        self.skills[skill_name] = current_val + amount
        UI.print_success(f"Your {skill_name.replace('_', ' ')} skill increased to {self.skills[skill_name]}!")

    def is_alive(self) -> bool:
        return self.stats.is_alive()

    def gain_experience(self, amount: int) -> None:
        self.stats.experience += amount
        UI.print_info(f"You gained {amount} XP! (Total: {self.stats.experience}/{self.stats.next_level_exp})")
        leveled_up = False
        while self.stats.experience >= self.stats.next_level_exp:
            xp_for_level = self.stats.next_level_exp
            self.stats.level_up() # Handles level increment, stat/exp recalculation
            self.stats.experience -= xp_for_level # Subtract only XP for that level
            leveled_up = True
        if leveled_up:
            UI.print_info(f"New XP after leveling: {self.stats.experience}/{self.stats.next_level_exp}")


    def update_defeated_enemies_tracker(self, enemy_id: str, count: int = 1) -> None:
        self.defeated_enemies_tracker[enemy_id] = self.defeated_enemies_tracker.get(enemy_id, 0) + count

    def add_talked_to_npc(self, npc_id: str) -> None:
        self.talked_to_npcs.add(npc_id)

    def update_current_location_for_quest(self, location_dict: Dict[str, Any]) -> None:
        self.current_location_obj = location_dict
        is_known = any(known_loc["id"] == location_dict["id"] for known_loc in self.known_locations_objects if "id" in known_loc and "id" in location_dict)
        if not is_known:
            self.known_locations_objects.append(location_dict)

    def perform_skill_check(self, skill_name: str, difficulty_class: int) -> bool:
        player_skill = self.skills.get(skill_name, 5)
        attr_bonus = 0
        # Simplified attribute bonus mapping
        if skill_name in ["one_handed", "two_handed", "block", "heavy_armor", "smithing"]: attr_bonus = self.stats.strength // 10
        elif skill_name in ["destruction", "restoration", "alteration", "conjuration", "illusion", "alchemy"]: attr_bonus = self.stats.intelligence // 10
        elif skill_name in ["archery", "light_armor", "sneak", "pickpocket", "security"]: attr_bonus = self.stats.agility // 10
        elif skill_name in ["speech", "barter"]: attr_bonus = self.stats.personality // 10
        
        luck_bonus = self.stats.luck // 10 
        roll = random.randint(1, 20)
        total_value = player_skill + attr_bonus + luck_bonus + roll

        UI.slow_print(f"Skill Check: {skill_name.replace('_',' ').title()} (DC {difficulty_class})")
        UI.slow_print(f"  Base: {player_skill}, Attr: {attr_bonus}, Luck: {luck_bonus}, Roll: {roll} -> Total: {total_value}")

        if total_value >= difficulty_class:
            UI.print_success("Success!")
            self.improve_skill(skill_name, random.randint(1,2))
            return True
        UI.print_failure("Failure.")
        return False

    def __str__(self) -> str:
        return self.full_name