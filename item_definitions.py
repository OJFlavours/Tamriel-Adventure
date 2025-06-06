# item_definitions.py
import random
from ui import UI
import tags  # Assuming tags.py exists and is used by Item class
import flavor  # Crucial for item flavor text
from flavor import get_flavor_text
from colorama import Fore, Style  # For colored/styled output in descriptions
from spells import get_spell, Spell  # Import for tome functionality

# Data will be imported from items_data
from items_data import (
    VALUE_MULTIPLIERS,
    BASE_WEIGHTS,
    BASE_VALUES,
    CONSUMABLE_EFFECT_POOLS
)


class Item:
    def __init__(
        self,
        name: str,
        category: str,
        material: str,
        equipment_tag: str = None,
        base_damage: tuple = None,
        armor_rating: int = None,
        enchantment: str = None,
        durability: int = 100,
        properties: dict = None
    ):
        self.name = name
        self.category = category
        self.material = material
        self.equipment_tag = equipment_tag if equipment_tag is not None else category
        self.base_damage = base_damage
        self.armor_rating = armor_rating
        self.enchantment = enchantment
        self.durability = durability
        self.max_durability = durability
        self.is_cursed = properties.get("is_cursed", False) if properties else False
        self.item_level = properties.get("item_level", 1) if properties else 1
        self.properties = properties.copy() if properties else {}
        self.tags = {}
        self.add_tag("item", "type", category)
        self.add_tag("item", "material", material)
        self.weight = self.calculate_weight()
        self.value = self.calculate_value()
        if self.category in ["potion", "ingredient", "food"]:
            self._assign_consumable_effect()

    def add_tag(self, tag_category, tag_type, tag):
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag

    def calculate_weight(self) -> float:
        material_multiplier = VALUE_MULTIPLIERS.get(self.material, 1.0)

        type_w = 1.0
        for type_key, weight_val in BASE_WEIGHTS.items():
            if type_key.lower() in self.name.lower():
                type_w = weight_val
                break

        if self.category == "weapon":
            type_w = max(type_w, 3.0)
        elif self.category == "armor":
            type_w = max(type_w, 2.0)
        elif self.category == "jewelry":
            type_w = max(type_w, 0.1)

        return round(material_multiplier * type_w, 1)

    def calculate_value(self) -> int:
        material_base_value = VALUE_MULTIPLIERS.get(self.material, 5)

        type_v = 5
        for type_key, val in BASE_VALUES.items():
            if type_key.lower() in self.name.lower():
                type_v = val
                break

        if self.category == "weapon":
            type_v = max(type_v, 15)
        elif self.category == "armor":
            type_v = max(type_v, 10)
        elif self.category == "jewelry":
            type_v = max(type_v, 50)

        enchant_bonus_mult = 1.0
        if self.enchantment:
            enchant_bonus_mult = 2.0
            if "Greater" in self.name or "Grand" in self.name or "Superior" in self.name or "Blessed" in self.name or "Enhanced" in self.name:
                enchant_bonus_mult = 3.0
            elif "Minor" in self.name:
                enchant_bonus_mult = 1.5

        if self.properties.get("unique") or self.properties.get("daedric_artifact"):
            enchant_bonus_mult *= 1.5
        if self.properties.get("quest_item"):
            enchant_bonus_mult *= 0.5  # Quest items might be less valuable to general merchants if they can't sell them

        return int((material_base_value + type_v) * enchant_bonus_mult)

    def _assign_consumable_effect(self):
        pool = CONSUMABLE_EFFECT_POOLS.get(self.category, {})
        if not pool:
            return

        if self.name in pool:
            chosen_effect_data = pool[self.name]
        else:
            if pool:  # If item name not in pool, but category matches, pick a random effect from that category's pool
                chosen_name_for_effect = random.choice(list(pool.keys()))
                chosen_effect_data = pool[chosen_name_for_effect]
            else:
                return

        self.properties["effect"] = chosen_effect_data["effect"]
        magnitude_data = chosen_effect_data["magnitude"]
        if isinstance(magnitude_data, tuple):
            min_mag, max_mag = magnitude_data
            self.properties["magnitude"] = random.randint(min_mag, max_mag)
        else:
            self.properties["magnitude"] = magnitude_data

        if "fortify" in self.properties["effect"] or "damage_" in self.properties["effect"] and "duration" not in self.properties:
            self.properties["duration"] = random.randint(30, 60)  # Default duration in seconds

    def use(self, player) -> None:
        if self.category in ["potion", "ingredient", "food"] and "effect" in self.properties:
            try:
                eff = self.properties.get("effect")
                mag = self.properties.get("magnitude", 0)
                dur = self.properties.get("duration")  # Get duration if present

                alchemy_skill = player.skills.get("alchemy", 0) if hasattr(player, 'skills') else 0
                skill_bonus = alchemy_skill / \
                    100.0 if self.category != "food" else 0.0  # Alchemy doesn't boost food
                total_mag = int(mag * (1 + skill_bonus))

                consumed_this_use = True
                if eff == "restore_health":
                    player.stats.heal(total_mag)
                    UI.slow_print(
                        f"You consume the {self.name}, restoring {total_mag} health.")
                elif eff == "restore_magicka":
                    player.stats.restore_magicka(total_mag)
                    UI.slow_print(
                        f"You consume the {self.name}, restoring {total_mag} magicka.")
                elif eff == "restore_fatigue":
                    player.stats.restore_stamina(total_mag)
                    UI.slow_print(
                        f"You consume the {self.name}, restoring {total_mag} stamina.")
                elif eff == "cure_poison":
                    # player.remove_status_effect("poison")
                    UI.slow_print(f"You consume the {self.name}, curing poison.")
                elif eff.startswith("resist_"):
                    # player.add_timed_status_effect(eff, total_mag, duration=dur or 120)
                    UI.slow_print(
                        f"You consume the {self.name}, gaining {total_mag}% {eff.split('_')[1].capitalize()} Resistance for {dur or 120}s.")
                elif eff == "damage_health":
                    player.stats.take_damage(total_mag, "poison")
                    UI.slow_print(
                        f"You consume the {self.name}, taking {total_mag} poison damage!")
                elif eff.startswith("fortify_") or eff.startswith("damage_"):
                    # player.add_timed_status_effect(eff, total_mag, duration=dur or 60)
                    UI.slow_print(
                        f"You consume the {self.name}. Effect: {eff.replace('_',' ').title()} by {total_mag} for {dur or 60}s.")
                elif "spell_on_use" in self.properties:
                    spell_key = self.properties["spell_on_use"]
                    spell = get_spell(spell_key)
                    if spell:
                        UI.slow_print(f"You use the {self.name} and cast {spell.name}!")
                        spell.cast(player, player)  # Cast on self for now
                    else:
                        UI.print_warning(
                            f"The {self.name} tries to cast an unknown spell: {spell_key}!")
                else:
                    UI.slow_print(
                        f"You consume the {self.name}. Its effects are subtle or unknown.")
                    consumed_this_use = False

                if consumed_this_use:
                    if hasattr(player, 'remove_item_from_inventory_by_instance'):
                        player.remove_item_from_inventory_by_instance(self)
                    elif hasattr(player, 'remove_item'):
                        player.remove_item(self)
                    else:
                        UI.print_warning(
                            f"Could not remove {self.name} from inventory after use.")

                if self.category in ["potion", "ingredient"] and hasattr(player, 'improve_skill'):
                    player.improve_skill("alchemy", random.randint(1, 2))

            except Exception as e:
                UI.print_warning(f"Error using {self.name}: {e}")

        elif self.category == "tome" and "spell_key" in self.properties:
            try:
                spell_key_to_learn = self.properties["spell_key"]
                spell_to_learn = get_spell(spell_key_to_learn)
                if spell_to_learn:
                    if any(s.name == spell_to_learn.name for s in player.known_spells):
                        UI.slow_print(
                            f"You already know the spell {spell_to_learn.name}.")
                    else:
                        player.known_spells.append(spell_to_learn)
                        UI.slow_print(
                            f"You study the {self.name} and learn the spell: {Style.BRIGHT}{spell_to_learn.name}{Style.RESET_ALL}!")
                        if hasattr(player, 'remove_item_from_inventory_by_instance'):
                            player.remove_item_from_inventory_by_instance(self)
                        elif hasattr(player, 'remove_item'):
                            player.remove_item(self)
                else:
                    UI.print_warning(
                        f"The {self.name} seems to refer to a forgotten spell ({spell_key_to_learn}).")
            except Exception as e:
                UI.print_warning(f"Error using {self.name}: {e}")

        elif self.category == "scroll":
            UI.slow_print(
                f"You read the {self.name} and a magical effect unfolds! (Scroll effects TODO).")
            if hasattr(player, 'remove_item_from_inventory_by_instance'):
                if hasattr(player, 'remove_item'):
                    player.remove_item(self)

    def get_description(self):
        """Returns a detailed description of the item."""
        description = f"{Fore.GREEN}{self.name}{Style.RESET_ALL}\n"
        description += f"Category: {self.category.title()}\n"
        description += f"Material: {self.material.title()}\n"
        if self.base_damage:
            description += f"Damage: {self.base_damage}\n"
        if self.armor_rating:
            description += f"Armor Rating: {self.armor_rating}\n"
        if self.enchantment:
            description += f"Enchantment: {self.enchantment}\n"
        description += f"Weight: {self.weight} lbs\n"
        description += f"Value: {self.value} gold\n"

        # Add flavor text from flavor.py
        flavor_text = get_flavor_text(self.name)
        if flavor_text:
            description += f"\n{Fore.CYAN}Lore:{Style.RESET_ALL} {flavor_text}\n"

        # Add properties
        if self.properties:
            description += "\nProperties:\n"
            for key, value in self.properties.items():
                description += f"  {key.replace('_', ' ').title()}: {value}\n"

        return description


class Torch(Item):
    def __init__(self, name="Torch", category="misc", material="Wood", properties=None):
        super().__init__(name, category, material, properties=properties)
        self.light_radius = 5  # Example: Torch provides light within 5 units
        self.duration = 60  # Example: Torch lasts for 60 minutes

    def use(self, player):
        UI.slow_print("You light the torch, illuminating your surroundings.")
        # Implement actual lighting effect in the game world here
        # This might involve setting a flag or calling a function
        # that makes the current location brighter for the player.
        pass
# Added by combat module restructuring
# Armor
# falmer_armor_basic