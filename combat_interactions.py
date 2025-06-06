# combat_interactions.py
import random
from ui import UI
from combat import Combat  # CORRECTED IMPORT
from npc_entities import NPC
from npc_roles import HOSTILE_ROLES
from items import generate_item_from_key
from npc_generation import determine_npc_culture 
from npc_dialogue_logic import handle_npc_dialogue

def list_npcs_at_location(location_obj, player, npc_registry_param):
    try:
        if not location_obj:
            UI.slow_print("You are nowhere in particular.")
            return

        npcs_here = npc_registry_param.get(location_obj.id if hasattr(location_obj, 'id') else None, [])
        if not npcs_here:
            UI.slow_print("No souls linger here, save the whispers of the wind.")
            return

        UI.print_heading(f"Souls at {location_obj.name if hasattr(location_obj, 'name') else 'this location'}")
        active_npcs = [npc for npc in npcs_here if npc.stats.is_alive()]

        if not active_npcs:
            UI.slow_print("Only the fallen remain here.")
            return

        for i, npc in enumerate(active_npcs, 1):
            npc_info_tags = npc.tags.get("npc", {})
            attitude_display_val = npc_info_tags.get("attitude", "neutral")
            attitude_display = f"({attitude_display_val.capitalize()})" if attitude_display_val else ""
            role_display = format_npc_role(npc.role)
            UI.slow_print(f"[{i}] {npc.full_name} — {role_display} ({npc.race.capitalize()}) {attitude_display}")
        
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
                    combat_instance = Combat(player, [selected_npc], location_obj.__dict__ if not isinstance(location_obj, dict) else location_obj)
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

def combat_demo(player, current_location_obj, find_hierarchy_func, npc_registry_param):
    try:
        enemy_level = player.level + random.randint(-1, 1)
        enemy_level = max(1, enemy_level)
        
        parent_hold_obj, parent_city_obj, _ = find_hierarchy_func(current_location_obj.id)
        
        demographics_source_obj = current_location_obj
        if parent_city_obj and not hasattr(demographics_source_obj, 'demographics'):
            demographics_source_obj = parent_city_obj
        if parent_hold_obj and not hasattr(demographics_source_obj, 'demographics'):
            demographics_source_obj = parent_hold_obj
        
        loc_tags = getattr(current_location_obj, 'tags', [])
        enemy_role = "bandit_raider"
        
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
        
        enemies_for_combat = [enemy]
        num_additional_enemies = random.randint(0, 2)

        for _ in range(num_additional_enemies):
            additional_enemy = NPC(name=None, level=max(1, player.level + random.randint(-2, 0)), race=determine_npc_culture(getattr(demographics_source_obj, 'demographics', {"Nord": 70})), role=random.choice(["bandit_thug", "wolf_creature"]))
            additional_enemy.unique_id = f"{additional_enemy.role}_{random.randint(1000,9999)}"
            enemies_for_combat.append(additional_enemy)

        enemy_names = ", ".join([e.name for e in enemies_for_combat])
        UI.slow_print(f"Suddenly, hostile figures emerge: {enemy_names}!")

        if player.combat is None:
            combat_instance = Combat(player, enemies_for_combat, current_location_obj.__dict__ if not isinstance(current_location_obj, dict) else current_location_obj)
            player.combat = combat_instance
            combat_instance.run()
            
            for defeated_enemy in enemies_for_combat:
                if not defeated_enemy.stats.is_alive():
                    player.update_defeated_enemies_tracker(defeated_enemy.unique_id)
                    player.gain_experience(defeated_enemy.level * 10)
        else:
            UI.print_warning("Cannot initiate demo combat: Player already in combat.")
        
        return current_location_obj
    except Exception as e:
        UI.print_failure(f"Error in combat_demo: {e}")
        return current_location_obj
def format_npc_role(role_str: str) -> str:
    """Intelligently formats complex NPC role strings for display."""
    from npc_roles import NOBLE_ROLES, COMMONER_ROLES
    parts = role_str.split('_')
    base_roles = NOBLE_ROLES.union(COMMONER_ROLES)
    
    base_role_part = ""
    clarifiers = []

    for part in parts:
        if part in base_roles and not base_role_part:
            base_role_part = part
        else:
            clarifiers.append(part)
    
    if not base_role_part and parts:
        base_role_part = parts[-1]
        clarifiers = parts[:-1]

    clarifier_str = " ".join(c.capitalize() for c in clarifiers)
    base_role_str = base_role_part.capitalize()

    return f"{clarifier_str} {base_role_str}".strip()