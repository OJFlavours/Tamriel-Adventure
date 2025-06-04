# combat_interactions.py
import random
from ui import UI

from combat_logic import Combat
from npc import NPC # NPC class
from npc_roles import HOSTILE_ROLES # HOSTILE_ROLES is now in npc_roles.py
from items import generate_item_from_key
# Assuming determine_npc_culture is in npc_generation or passed if needed
from npc_generation import determine_npc_culture 
# _find_hierarchy will need to be passed as an argument or imported if it's moved to a utility module.
from npc_dialogue_logic import handle_npc_dialogue

def list_npcs_at_location(location_obj, player, npc_registry_param):
    try:
        if not location_obj:
            UI.slow_print("You are nowhere in particular.")
            return

        npcs_here = npc_registry_param.get(location_obj.id, [])
        if not npcs_here:
            UI.slow_print("No souls linger here, save the whispers of the wind.")
            return

        UI.print_heading(f"Souls at {location_obj.name}")
        active_npcs = [npc for npc in npcs_here if npc.stats.is_alive()]

        if not active_npcs:
            UI.slow_print("Only the fallen remain here.")
            return

        for i, npc in enumerate(active_npcs, 1):
            npc_info_tags = npc.tags.get("npc", {})
            attitude_display_val = npc_info_tags.get("attitude", "neutral")
            attitude_display = f"({attitude_display_val.capitalize()})" if attitude_display_val else ""
            role_display = 'Server' if npc.role == 'server' else npc.role.replace('_', ' ').title()
            UI.print_info(f"[{i}] {npc.full_name} — {role_display} ({npc.race.capitalize()}) {attitude_display}")
        UI.print_line()

        sel = UI.print_prompt("With whom do you wish to parley? (0 to pass)").strip()
        if sel.isdigit():
            choice_index = int(sel)
            if 1 <= choice_index <= len(active_npcs):
                selected_npc = active_npcs[choice_index - 1]
                selected_npc_attitude_tags = selected_npc.tags.get("npc", {}).get("attitude", "")
                
                is_hostile = "hostile" in selected_npc_attitude_tags or \
                              selected_npc.role in HOSTILE_ROLES or \
                              any(ht in selected_npc.role.lower() for ht in ["bandit", "draugr", "skeleton", "vampire", "wolf", "bear", "spider", "chaurus", "falmer", "forsworn_hostile_variant"])

                if is_hostile and player.combat is None:
                    UI.slow_print(f"{selected_npc.name} snarls and lunges with clear hostile intent!")
                    combat_instance = Combat(player, [selected_npc], location_obj)
                    player.combat = combat_instance
                    combat_instance.run()
                elif player.combat is not None:
                     UI.slow_print("You are already engaged in combat!")
                else:
                    handle_npc_dialogue(selected_npc, player, location_obj)
            elif choice_index != 0:
                UI.slow_print("No such soul stands before you.")
    except Exception as e:
        UI.print_failure(f"Error in list_npcs_at_location: {e}")

def combat_demo(player, current_location_obj, find_hierarchy_func, npc_registry_param): # Added find_hierarchy_func
    try:
        enemy_level = player.level + random.randint(-1, 1)
        enemy_level = max(1, enemy_level)
        
        # find_hierarchy_func now expects a Location object or ID
        parent_hold_obj, parent_city_obj, _ = find_hierarchy_func(current_location_obj) # Pass object
        
        # Determine demographics source by checking attributes of Location objects
        demographics_source_obj = current_location_obj
        if parent_city_obj and not hasattr(demographics_source_obj, 'demographics'):
            demographics_source_obj = parent_city_obj
        if parent_hold_obj and not hasattr(demographics_source_obj, 'demographics'):
            demographics_source_obj = parent_hold_obj
        
        loc_tags = getattr(current_location_obj, 'tags', []) # Use getattr for safety
        enemy_role = "bandit_raider"
        
        # Ensure loc_tags is a list of strings for 'in' operator
        if not isinstance(loc_tags, list): loc_tags = []
        
        if any(tag in loc_tags for tag in ["undead", "barrow", "graveyard"]):
            enemy_role = random.choice(["draugr_restless", "skeleton_warrior", "ghost_ancient"])
        elif "cave" in loc_tags and "animal_den" in loc_tags:
            enemy_role = random.choice(["cave_bear_young", "wolf_alpha", "giant_spider_cave"])
        elif "dwemer_ruin" in loc_tags:
            enemy_role = random.choice(["dwarven_sphere_guardian", "falmer_warrior", "chaurus_hunter_small"])

        enemy_race = determine_npc_culture(getattr(demographics_source_obj, 'demographics', {"Nord": 50, "Orc": 20, "Dunmer": 15, "Khajiit":15 }))

        if "draugr" in enemy_role: enemy_race = "undead_nord"
        elif "skeleton" in enemy_role: enemy_race = "undead_skeleton"
        elif "ghost" in enemy_role: enemy_race = "spirit"
        elif "falmer" in enemy_role: enemy_race = "falmer"
        elif "dwarven" in enemy_role: enemy_race = "dwemer_construct_race"
        elif "wolf" in enemy_role or "bear" in enemy_role or "spider" in enemy_role or "chaurus" in enemy_role:
             enemy_race = enemy_role.split('_')[0] + "_creature"

        enemy = NPC(
            name=None,
            level=enemy_level,
            race=enemy_race,
            role=enemy_role
        )
        enemy.unique_id = f"{enemy_role}_{random.randint(1000,9999)}" 
        
        if "bandit" in enemy_role or "draugr" in enemy_role or "skeleton" in enemy_role or "falmer" in enemy_role:
            weapon_keys = ["iron_sword", "steel_axe_old", "iron_mace_rusty", "ancient_nord_sword_chipped", "falmer_sword_crude"]
            armor_keys = ["hide_armor_scraps", "iron_armor_dented", "ancient_nord_armor_piece", "falmer_armor_basic"]
            
            if random.random() < 0.8:
                enemy_weapon = generate_item_from_key(random.choice(weapon_keys), enemy.level)
                if enemy_weapon: enemy.stats.inventory.append(enemy_weapon)
            if random.random() < 0.6:
                enemy_armor = generate_item_from_key(random.choice(armor_keys), enemy.level)
                if enemy_armor: enemy.stats.inventory.append(enemy_armor)
        
        enemies_for_combat = [enemy]
        num_additional_enemies = random.randint(0, 2)

        for _ in range(num_additional_enemies):
            additional_enemy_level = max(1, player.level + random.randint(-2, 0))
            additional_enemy_role = random.choice(["bandit_thug", "bandit_scout", "wolf_creature"])
            additional_enemy_race = determine_npc_culture(getattr(demographics_source_obj, 'demographics', {"Nord": 70, "Orc": 15, "Khajiit":15 }))
            if "wolf" in additional_enemy_role: additional_enemy_race = "wolf_creature"

            additional_enemy = NPC(
                name=None,
                level=additional_enemy_level,
                race=additional_enemy_race,
                role=additional_enemy_role
            )
            additional_enemy.unique_id = f"{additional_enemy_role}_{random.randint(1000,9999)}"
            enemies_for_combat.append(additional_enemy)

        enemy_names = ", ".join([e.name for e in enemies_for_combat])
        UI.slow_print(f"Suddenly, hostile figures emerge: {enemy_names}!")

        if player.combat is None:
            combat_instance = Combat(player, enemies_for_combat, current_location_obj)
            player.combat = combat_instance
            combat_instance.run()
            
            for defeated_enemy in enemies_for_combat:
                if not defeated_enemy.stats.is_alive():
                    player.update_defeated_enemies_tracker(defeated_enemy.unique_id)
                    player.gain_experience(defeated_enemy.level * 10)
        else:
            UI.print_warning("Cannot initiate demo combat: Player already in combat.")
        
        return current_location_obj # Return current location, as it might not change
    except Exception as e:
        UI.print_failure(f"Error in combat_demo: {e}")
        return current_location_obj

# --- Complex Interactions ---
class Combo:
    def __init__(self, name, moves, damage_multiplier, stamina_cost):
        self.name = name
        self.moves = moves  # List of move names (e.g., ["attack", "block", "attack"])
        self.damage_multiplier = damage_multiplier
        self.stamina_cost = stamina_cost

    def execute(self, attacker, defender):
        """Executes the combo, applying damage and stamina cost."""
        total_damage = attacker.stats.attack * self.damage_multiplier
        defender.stats.take_damage(total_damage)
        attacker.stats.stamina -= self.stamina_cost
        return f"{attacker.name} executes {self.name} for {total_damage} damage!"

# --- Dynamic Interactions ---
def create_dynamic_interaction(name, condition, effect):
    """Creates a dynamic interaction based on a condition and effect."""
    def dynamic_interaction(attacker, defender):
        if condition(attacker, defender):
            return effect(attacker, defender)
        return None
    dynamic_interaction.__name__ = name  # Set the name of the function
    return dynamic_interaction