# stats.py
import random
from typing import Dict, List, Any, Set # Import Set for type hinting

# Assuming QuestLog is in quests.py and Item is in items.py
# We import them here to avoid circular dependencies where possible
# and for type hinting clarity.
from quests import QuestLog, Quest # Import Quest for type hinting in QuestLog and Player
from items import Item # Import Item for type hinting in inventory and equipment
from ui import UI # For UI messages within Player/Stats methods

class Stats:
    """
    Encapsulates player or NPC stats, attributes, and derived combat values for Skyrim Adventure.
    """
    def __init__(self,
                 strength: int = 40, intelligence: int = 40, willpower: int = 40, agility: int = 40, speed: int = 40,
                 endurance: int = 40, personality: int = 40, luck: int = 40,
                 max_health: int | None = None, max_magicka: int | None = None, max_fatigue: int | None = None,
                 current_health: int | None = None, current_magicka: int | None = None, current_fatigue: int | None = None,
                 poison_resist: int = 0, magic_resist: int = 0, frost_resist: int = 0,
                 shock_resist: int = 0, fire_resist: int = 0,
                 inventory: List[Item] | None = None, # Should be list of Item objects
                 gold: int = 0, level: int = 1):
        # Attributes
        self.strength = strength
        self.intelligence = intelligence
        self.willpower = willpower
        self.agility = agility
        self.speed = speed
        self.endurance = endurance
        self.personality = personality
        self.luck = luck

        self.level = level
        self.gold = gold

        # Experience for leveling
        self.experience = 0
        self.next_level_exp = self._calculate_next_level_exp(self.level)

        # Resistances
        self.poison_resist = poison_resist
        self.magic_resist = magic_resist
        self.frost_resist = frost_resist
        self.shock_resist = shock_resist
        self.fire_resist = fire_resist

        # Core stats (set after attributes)
        # If not provided, calculate based on level and endurance/intelligence
        self.max_health = int(max_health if max_health is not None else 100 + (self.endurance * 2) + (self.level * 5))
        self.max_magicka = int(max_magicka if max_magicka is not None else 50 + (self.intelligence * 1.5) + (self.level * 3))
        self.max_fatigue = int(max_fatigue if max_fatigue is not None else 100 + (self.endurance * 1.5) + (self.level * 4))

        # Current stats default to max if not specified
        self.current_health = int(current_health if current_health is not None else self.max_health)
        self.current_magicka = int(current_magicka if current_magicka is not None else self.max_magicka)
        self.current_fatigue = int(current_fatigue if current_fatigue is not None else self.max_fatigue)

        self.inventory = inventory if inventory is not None else []
        self.encumbrance_limit = 100 + (self.strength * 2)
        self.current_encumbrance = self.calculate_current_encumbrance()

    def _calculate_next_level_exp(self, current_level: int) -> int:
        """Calculates the experience needed for the next level based on current level."""
        return int(100 * (current_level ** 1.5)) # Simple exponential scaling

    def calculate_current_encumbrance(self) -> float:
        """Calculates the total weight of items in the inventory."""
        return sum(item.weight for item in self.inventory if hasattr(item, 'weight'))

    def add_to_inventory(self, item: Item) -> bool:
        """Adds an item to the inventory if there's enough encumbrance capacity."""
        if not hasattr(item, 'weight'):
            UI.print_warning(f"Item {getattr(item, 'name', 'Unknown item')} has no weight attribute, cannot add to inventory.")
            return False
        if self.current_encumbrance + item.weight <= self.encumbrance_limit:
            self.inventory.append(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        else:
            UI.slow_print(f"Cannot carry {item.name}, you are too encumbered!")
            return False

    def remove_from_inventory(self, item: Item) -> bool:
        """Removes an item from the inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        return False

    def is_alive(self) -> bool:
        """Checks if the character is alive."""
        return self.current_health > 0

    def take_damage(self, amount: int) -> bool:
        """Applies damage to the character's health."""
        self.current_health = max(0, self.current_health - amount)
        return self.current_health == 0 # Returns True if dead

    def heal(self, amount: int) -> None:
        """Restores health to the character."""
        self.current_health = min(self.max_health, self.current_health + amount)

    def restore_magicka(self, amount: int) -> None:
        """Restores magicka to the character."""
        self.current_magicka = min(self.max_magicka, self.current_magicka + amount)

    def restore_fatigue(self, amount: int) -> None:
        """Restores fatigue (stamina) to the character."""
        self.current_fatigue = min(self.max_fatigue, self.current_fatigue + amount)

    def update_encumbrance(self) -> None:
        """Recalculates current encumbrance."""
        self.current_encumbrance = self.calculate_current_encumbrance()

    def level_up(self) -> None:
        """Increases character's level and recalculates derived stats."""
        self.level += 1
        UI.print_system_message(f"CONGRATULATIONS! You have reached LEVEL {self.level}!")

        attribute_increase = random.randint(3, 5)
        self.strength += attribute_increase
        self.intelligence += attribute_increase
        self.willpower += attribute_increase
        self.agility += attribute_increase
        self.speed += attribute_increase
        self.endurance += attribute_increase
        self.personality += attribute_increase
        self.luck += attribute_increase

        self.max_health = int(100 + (self.endurance * 2) + (self.level * 5))
        self.max_magicka = int(50 + (self.intelligence * 1.5) + (self.level * 3))
        self.max_fatigue = int(100 + (self.endurance * 1.5) + (self.level * 4))

        self.current_health = self.max_health
        self.current_magicka = self.max_magicka
        self.current_fatigue = self.max_fatigue

        self.next_level_exp = self._calculate_next_level_exp(self.level)
        self.experience = 0
        UI.slow_print("Your attributes and skills have grown stronger!")
        UI.press_enter()

# --- Racial Modifiers --- (from original - unchanged)
RACES = {
    "nord": {"strength_mod": 10, "endurance_mod": 10, "frost_resist": 50, "two_handed_skill": 5, "block_skill": 5},
    "imperial": {"personality_mod": 10, "luck_mod": 5, "restoration_skill": 5, "heavy_armor_skill": 5},
    "breton": {"intelligence_mod": 10, "willpower_mod": 5, "magic_resist": 25, "conjuration_skill": 10},
    "redguard": {"agility_mod": 10, "speed_mod": 10, "one_handed_skill": 10, "archery_skill": 5},
    "dunmer": {"intelligence_mod": 5, "agility_mod": 5, "fire_resist": 50, "destruction_skill": 10, "sneak_skill": 5},
    "altmer": {"intelligence_mod": 15, "magicka_mod": 50, "illusion_skill": 10, "alteration_skill": 5},
    "bosmer": {"agility_mod": 15, "archery_skill": 10, "sneak_skill": 5, "light_armor_skill": 5},
    "orc": {"strength_mod": 15, "endurance_mod": 5, "heavy_armor_skill": 10, "smithing_skill": 5},
    "argonian": {"speed_mod": 10, "poison_resist": 75, "disease_resist": 50, "alteration_skill": 5, "light_armor_skill": 5},
    "khajiit": {"agility_mod": 10, "luck_mod": 10, "sneak_skill": 10, "pickpocket_skill": 5},
}

# --- Class Definitions --- (from original - unchanged)
CLASSES = {
    "warrior": {
        "name": "Warrior",
        "desc": "A master of arms, favoring strength and direct combat.",
        "subclasses": {
            "1": {"name": "Blademaster", "attributes": {"strength": 50, "endurance": 50}, "skills": {"one_handed": 20, "heavy_armor": 20}, "inventory": ["iron_sword", "hide_shield"]},
            "2": {"name": "Berserker", "attributes": {"strength": 60, "speed": 40}, "skills": {"two_handed": 20, "light_armor": 15}, "inventory": ["iron_battleaxe", "hide_armor"]},
            "3": {"name": "Spellblade", "attributes": {"strength": 45, "intelligence": 45}, "skills": {"one_handed": 15, "destruction": 15}, "inventory": ["steel_sword", "apprentice_tome_flames"]},
            "4": {"name": "Knight", "attributes": {"endurance": 55, "personality": 40}, "skills": {"heavy_armor": 20, "block": 15}, "inventory": ["steel_plate_armor", "steel_shield"]},
            "5": {"name": "Dragonslayer", "attributes": {"strength": 55, "willpower": 45}, "skills": {"two_handed": 25, "restoration": 10}, "inventory": ["dragonbone_greatsword", "amulet_of_mara"]}
        }, "inventory": ["iron_sword", "hide_shield"]
    },
    "mage": {
        "name": "Mage", "desc": "A scholar of the arcane arts, wielding powerful spells.",
        "subclasses": {
            "1": {"name": "Sorcerer", "attributes": {"intelligence": 50, "willpower": 50}, "skills": {"destruction": 20, "alteration": 15}, "inventory": ["novice_robes", "apprentice_tome_firebolt"]},
            "2": {"name": "Cleric", "attributes": {"willpower": 50, "personality": 50}, "skills": {"restoration": 20, "heavy_armor": 15}, "inventory": ["priest_robes", "apprentice_tome_healing"]},
            "3": {"name": "Conjurer", "attributes": {"intelligence": 45, "willpower": 45}, "skills": {"conjuration": 20, "alteration": 10}, "inventory": ["apprentice_robes", "apprentice_tome_conjure_familiar"]},
            "4": {"name": "Illusionist", "attributes": {"intelligence": 40, "personality": 55}, "skills": {"illusion": 20, "sneak": 10}, "inventory": ["fine_clothes", "apprentice_tome_courage"]},
            "5": {"name": "Mystic", "attributes": {"intelligence": 55, "luck": 40}, "skills": {"mysticism": 20, "alchemy": 15}, "inventory": ["alchemist_robes", "scroll_of_soul_trap"]}
        }, "inventory": ["novice_robes", "apprentice_tome_firebolt"]
    },
    "thief": {
        "name": "Thief", "desc": "A master of stealth and subterfuge, relying on cunning.",
        "subclasses": {
            "1": {"name": "Assassin", "attributes": {"agility": 50, "speed": 50}, "skills": {"sneak": 20, "one_handed": 15}, "inventory": ["leather_armor", "iron_dagger"]},
            "2": {"name": "Nightblade", "attributes": {"agility": 40, "intelligence": 40}, "skills": {"sneak": 15, "illusion": 20}, "inventory": ["dark_brotherhood_robes", "iron_dagger"]},
            "3": {"name": "Rogue", "attributes": {"agility": 45, "personality": 45}, "skills": {"pickpocket": 20, "speech": 15}, "inventory": ["fine_clothes", "lockpick"]},
            "4": {"name": "Scout", "attributes": {"speed": 55, "endurance": 40}, "skills": {"light_armor": 20, "archery": 15}, "inventory": ["hide_armor", "hunting_bow"]},
            "5": {"name": "Trickster", "attributes": {"luck": 50, "agility": 40}, "skills": {"alteration": 15, "speech": 20}, "inventory": ["jester_outfit", "scroll_of_calm"]}
        }, "inventory": ["leather_armor", "iron_dagger"]
    },
    "adventurer": {
        "name": "Adventurer", "desc": "A versatile explorer, comfortable in many situations.",
        "subclasses": {
            "1": {"name": "Explorer", "attributes": {"endurance": 50, "luck": 50}, "skills": {"light_armor": 15, "speech": 15}, "inventory": ["leather_armor", "hunting_bow"]},
            "2": {"name": "Bard", "attributes": {"personality": 50, "intelligence": 40}, "skills": {"speech": 20, "illusion": 15}, "inventory": ["fine_clothes", "lute"]},
            "3": {"name": "Survivalist", "attributes": {"endurance": 55, "strength": 40}, "skills": {"block": 15, "one_handed": 15}, "inventory": ["fur_armor", "iron_axe", "venison_steak"]}
        }, "inventory": ["leather_armor", "hunting_bow"]
    }
}

class Player:
    """
    Represents the player character, inheriting core stats from Stats and
    managing inventory, equipment, quest log, and various quest-related trackers.
    """
    def __init__(self, name: str, race: str, subclass: str, stats: Stats, skills: Dict[str, int]):
        self.name = name
        self.race = race
        self.subclass = subclass
        self.stats = stats      # The actual Stats object instance
        self.skills = skills    # Dictionary of skill_name: value
        self.quest_log = QuestLog() # Manages active and completed quests
        self.combat = None      # To store a Combat instance if player is in combat

        self.slots = { # Equipment slots
            "head": None, "chest": None, "hands": None, "feet": None,
            "main_hand": None, "off_hand": None,
            "amulet": None, "ring1": None, "ring2": None
        }

        # Trackers for quest objectives and world state
        self.defeated_enemies_tracker: Dict[str, int] = {} # e.g., {"bandit_raider_unique_id": 3, "draugr_restless_unique_id": 1}
        self.talked_to_npcs: Set[str] = set() # Stores unique NPC IDs after talking to them
        self.current_location_obj: Dict[str, Any] | None = None # Set by the game loop during travel
        self.known_locations_objects: List[Dict[str, Any]] = [] # List of known location dicts, updated during travel
        self.faction_reputation: Dict[str, int] = { # Initial faction reputations
            "imperial_legion": 0,
            "stormcloaks": 0,
            "thieves_guild": 0,
            "college_of_winterhold": 0,
            "companions": 0,
            "dark_brotherhood": 0,
            "silver_blood": 0,
            "thalmor": 0,
            "khajiit_caravans": 0,
            "falkreath": 0 # Example for a hold-level reputation
        }


    @property
    def level(self) -> int:
        """Convenience property to access player's level from their Stats object."""
        return self.stats.level

    @property
    def experience(self) -> int:
        """Convenience property to access player's current experience from their Stats object."""
        return self.stats.experience

    @property
    def next_level_exp(self) -> int:
        """Convenience property to access XP needed for next level from Stats object."""
        return self.stats.next_level_exp

    @property
    def equipment(self) -> List[Item]:
        """Returns a list of all items currently equipped in slots."""
        equipped_items = []
        for item in self.slots.values():
            if item and item not in equipped_items: # Check for item and avoid duplicates if any item could fill multiple conceptual slots
                equipped_items.append(item)
        return equipped_items

    def add_item(self, item_to_add: Item) -> bool:
        """Adds an item to the player's main inventory (managed by Stats object)."""
        return self.stats.add_to_inventory(item_to_add)

    def remove_item(self, item_to_remove: Item) -> bool:
        """Removes an item from the player's main inventory (managed by Stats object)."""
        return self.stats.remove_from_inventory(item_to_remove)

    def _unequip_from_slot(self, slot_name: str) -> Item | None:
        """Internal helper to unequip an item from a specific slot and add it back to inventory."""
        item_in_slot = self.slots.get(slot_name)
        if item_in_slot:
            self.slots[slot_name] = None
            if not self.stats.add_to_inventory(item_in_slot):
                UI.print_warning(f"Could not return {item_in_slot.name} to inventory after unequipping from {slot_name}! It may be lost if encumbered.")
            UI.slow_print(f"{item_in_slot.name} unequipped from {slot_name}.")
            return item_in_slot
        return None

    def equip_item(self, item_to_equip: Item) -> bool:
        """Equips an item from the main inventory into an appropriate slot."""
        if item_to_equip not in self.stats.inventory:
            UI.slow_print(f"{item_to_equip.name} is not in your inventory to equip.")
            return False

        equippable_categories = ["weapon", "armor", "jewelry"]
        if item_to_equip.category not in equippable_categories:
            UI.slow_print(f"You cannot equip {item_to_equip.name}; it's not standard equipment.")
            return False

        target_slot_tag = item_to_equip.equipment_tag

        if target_slot_tag == "ring":
            slot_to_place_in = None
            if not self.slots["ring1"]: slot_to_place_in = "ring1"
            elif not self.slots["ring2"]: slot_to_place_in = "ring2"
            else:
                UI.slow_print(f"Both ring slots are full. Unequipping {self.slots['ring1'].name} to make space for {item_to_equip.name}.")
                self._unequip_from_slot("ring1")
                slot_to_place_in = "ring1"

            self.slots[slot_to_place_in] = item_to_equip
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} has been equipped to {slot_to_place_in}.")
            return True

        if target_slot_tag == "two_handed":
            if self.slots["main_hand"]: self._unequip_from_slot("main_hand")
            if self.slots["off_hand"]: self._unequip_from_slot("off_hand")

            self.slots["main_hand"] = item_to_equip;
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} (Two-Handed) has been equipped.")
            return True

        if target_slot_tag in self.slots:
            if target_slot_tag == "main_hand" and self.slots["main_hand"] and getattr(self.slots["main_hand"], 'equipment_tag', '') == "two_handed":
                self._unequip_from_slot("main_hand")

            if target_slot_tag == "off_hand" and self.slots["main_hand"] and \
               getattr(self.slots["main_hand"], 'equipment_tag', '') == "two_handed":
                UI.slow_print(f"Cannot equip {item_to_equip.name} in off-hand while wielding {self.slots['main_hand'].name}. Unequip it first.")
                return False

            if self.slots[target_slot_tag]:
                self._unequip_from_slot(target_slot_tag)

            self.slots[target_slot_tag] = item_to_equip
            self.stats.remove_from_inventory(item_to_equip)
            UI.slow_print(f"{item_to_equip.name} has been equipped to {target_slot_tag}.")
            return True
        else:
            UI.slow_print(f"Cannot equip {item_to_equip.name}: Unknown or inappropriate equipment slot tag '{target_slot_tag}'.")
            return False

    def unequip_item(self, item_to_unequip: Item) -> bool:
        """Unequips an item from its slot and returns it to the main inventory."""
        found_slot_name = None
        for slot_name, equipped_item_in_slot in self.slots.items():
            if equipped_item_in_slot == item_to_unequip:
                found_slot_name = slot_name
                break

        if found_slot_name:
            self._unequip_from_slot(found_slot_name)
            return True
        else:
            UI.slow_print(f"{item_to_unequip.name} is not currently equipped or not found in slots.")
            return False

    def examine_item(self, item: Item) -> None:
        """Displays detailed information about an item."""
        UI.slow_print(f"You examine {item.name} more closely...")
        print("\n" + item.get_description())

    def use_item(self, item: Item) -> None:
        """Attempts to use an item (e.g., consumable, scroll)."""
        if hasattr(item, 'use') and callable(item.use):
            item.use(self)
        else:
            UI.slow_print(f"You cannot use {item.name} in that way.")

    def drop_item(self, item_to_drop: Item) -> bool:
        """Drops an item from inventory or unequipped from equipment."""
        for slot_name, equipped_item in self.slots.items():
            if equipped_item == item_to_drop:
                UI.slow_print(f"You must unequip {item_to_drop.name} from your {slot_name} slot before dropping it.")
                return False

        if item_to_drop in self.stats.inventory:
            if self.stats.remove_from_inventory(item_to_drop):
                UI.slow_print(f"You dropped {item_to_drop.name} on the ground.")
                return True
            else:
                UI.slow_print(f"Could not drop {item_to_drop.name} for an unknown reason.")
                return False
        else:
            UI.slow_print(f"{item_to_drop.name} is not in your possession to drop.")
            return False

    def sort_inventory(self, key: str = "name") -> None:
        """Sorts the player's main inventory (self.stats.inventory)."""
        if hasattr(self.stats, 'inventory') and isinstance(self.stats.inventory, list):
            try:
                self.stats.inventory.sort(key=lambda item_obj: str(getattr(item_obj, key, "")).lower())
                UI.slow_print(f"Inventory sorted by {key.capitalize()}.")
            except AttributeError:
                UI.print_warning(f"Cannot sort inventory by '{key}', items may lack this attribute.")
        else:
            UI.print_warning("Inventory could not be sorted (data missing or not a list).")

    def inspect_equipped_items(self) -> None:
        """Displays currently equipped items and their slots."""
        UI.print_subheading("--- Currently Equipped ---")
        found_any = False
        for slot_name, item in self.slots.items():
            if item:
                UI.print_info(f"{slot_name.capitalize()}: {item.name} - {item.get_description().splitlines()[0]}")
                found_any = True
        if not found_any:
            UI.slow_print("You have nothing equipped.")

    def improve_skill(self, skill_name: str, amount: int = 1) -> None:
        """Improves a player skill by a certain amount."""
        if skill_name in self.skills:
            self.skills[skill_name] = self.skills.get(skill_name, 0) + amount
        else:
            self.skills[skill_name] = amount

    def is_alive(self) -> bool:
        """Checks if the player is alive."""
        return self.stats.is_alive()

    def gain_experience(self, amount: int) -> None:
        """Awards experience points to the player and checks for level up."""
        self.stats.experience += amount
        UI.print_info(f"You gained {amount} experience points!")
        UI.print_info(f"Total XP: {self.stats.experience} / {self.stats.next_level_exp}")
        while self.stats.experience >= self.stats.next_level_exp:
            self.stats.level_up()
            self.stats.experience -= self.stats.next_level_exp
            self.stats.next_level_exp = self.stats._calculate_next_level_exp(self.stats.level)

    def update_defeated_enemies_tracker(self, enemy_id: str, count: int = 1) -> None:
        """Updates the count of defeated enemies for quest tracking."""
        self.defeated_enemies_tracker[enemy_id] = self.defeated_enemies_tracker.get(enemy_id, 0) + count

    def add_talked_to_npc(self, npc_id: str) -> None:
        """Adds an NPC's ID to the set of talked-to NPCs for quest tracking."""
        self.talked_to_npcs.add(npc_id)

    def update_current_location_for_quest(self, location_obj: Dict[str, Any]) -> None:
        """Updates the player's current location for quest tracking."""
        self.current_location_obj = location_obj
        if location_obj not in self.known_locations_objects:
             self.known_locations_objects.append(location_obj)

    def perform_skill_check(self, skill_name: str, difficulty_class: int) -> bool:
        """
        Performs a skill check against a difficulty class.
        Returns True for success, False for failure.
        """
        player_skill_value = self.skills.get(skill_name, 5) # Default to 5 if skill not present
        
        # Determine relevant attribute for the skill if needed (example mapping)
        if skill_name in ["one_handed", "two_handed", "block", "heavy_armor", "smithing"]:
            attribute_bonus = self.stats.strength // 10
        elif skill_name in ["destruction", "restoration", "alteration", "conjuration", "illusion", "mysticism", "alchemy"]:
            attribute_bonus = self.stats.intelligence // 10
        elif skill_name in ["archery", "light_armor", "sneak", "pickpocket", "security"]:
            attribute_bonus = self.stats.agility // 10
        elif skill_name in ["speech", "persuasion", "intimidation"]:
            attribute_bonus = self.stats.personality // 10
        else:
            attribute_bonus = 0 # No specific attribute bonus for other skills

        roll = random.randint(1, 20) # A D20 roll
        total_skill_value = player_skill_value + attribute_bonus + (self.stats.luck // 5) # Luck provides a minor bonus

        UI.slow_print(f"Performing a {skill_name.replace('_', ' ').capitalize()} check (DC: {difficulty_class})...")
        UI.slow_print(f"Your skill: {player_skill_value} + Attribute Bonus: {attribute_bonus} + Luck Bonus: {self.stats.luck // 5} (Total: {total_skill_value}) + Roll: {roll}")

        if roll + total_skill_value >= difficulty_class:
            UI.print_success(f"SUCCESS! You pass the {skill_name.replace('_', ' ').capitalize()} check.")
            self.improve_skill(skill_name, random.randint(1,2)) # Minor skill improvement on success
            return True
        else:
            UI.print_failure(f"FAILURE! You fail the {skill_name.replace('_', ' ').capitalize()} check.")
            return False