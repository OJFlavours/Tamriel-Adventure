# events.py
import random
import traceback
from ui import UI
from quests import Quest, generate_reward, generate_location_appropriate_quest # Import Quest and generation functions
from items import Item, generate_item_from_key, generate_random_item
from locations import LOCATIONS # Import LOCATIONS to build DUNGEON_NAMES
from exploration_data import EXPLORATION_RESULTS # Import from the new file
# Assuming npc.py has a function to generate NPCs based on tags, or we do it conceptually here
# from npc import generate_npc_from_tags 

# --- DYNAMICALLY GENERATED DUNGEON_NAMES ---
def get_all_dungeon_style_locations(locations_data):
    dungeon_names = set()
    def find_dungeons_recursive(location_list):
        for loc in location_list:
            loc_tags = loc.get("tags", [])
            is_settlement = "city" in loc_tags or "town" in loc_tags or "village" in loc_tags or "hold" in loc_tags
            is_dungeon_type = "dungeon" in loc_tags or \
                              "dwemer" in loc_tags or \
                              "barrow" in loc_tags or \
                              ("ruin" in loc_tags and not is_settlement) or \
                              ("cave" in loc_tags and not is_settlement) or \
                              (("mine" in loc_tags and not is_settlement) and ("abandoned" in loc_tags or "infested" in loc_tags or "haunted" in loc_tags))

            if is_dungeon_type:
                dungeon_names.add(loc["name"])
            
            if "sub_locations" in loc:
                find_dungeons_recursive(loc["sub_locations"])
    find_dungeons_recursive(locations_data)
    return list(dungeon_names)

DUNGEON_NAMES = get_all_dungeon_style_locations(LOCATIONS)
if not DUNGEON_NAMES: # Fallback
    DUNGEON_NAMES = [
        "Bleak Falls Barrow", "Quicksilver Mine", "Nightcaller Temple", "Iron-Breaker Mine",
        "Saarthal", "Hob's Fall Cave", "Yngol Barrow", "Movarth's Lair", "Ustengrav",
        "Pinewatch", "Halldir's Cairn", "Cidhna Mine", "Druadach Redoubt", "Shroud Hearth Barrow",
        "Wolfskull Cave", "Lost Prospect Mine", "The Ratway", "Labyrinthian", "Dustman's Cairn",
        "Alftand", "Mzinchaleft", "Forelhost", "Silent Moons Camp", "Reachwind Eyrie", "Blind Cliff Cave"
    ]

# --- Define SPECIFIC_LOCATION_TAGS (for prioritizing exploration results) ---
SPECIFIC_LOCATION_TAGS = [
    "tavern", "inn", "market", "mine", "camp", "cave", "ruin", "barrow", "dwemer",
    "keep", "meadhall", "blacksmith", "alchemy_shop", "temple", "college", "palace",
    "meadery", "brewery", "watchtower", "lighthouse", "wreck", "shop", "port",
    "government", "guild", "prison", "graveyard", "sanctuary", "monastery",
    "fort", "fortified", "city", "town", "village", "dragon_lair",
    "enchanted_forest", "cursed_swamp", "volcanic_caldera", "glacial_cave", "ashland_waste"
]

# --- EXPANDED RANDOM_EVENTS (with tangible effects) ---
RANDOM_EVENTS = {
    "generic_travel": [
        {"description": "You spot a Shrine of Akatosh by the roadside, its eternal flame burning brightly. You feel a sense of timelessness and renewed purpose.", 
         "type": "flavor_and_buff", "details": {"god_mention": "Akatosh", "minor_buff_debuff":{"stat":"magicka_regen_rate", "amount":0.1, "duration_turns":180, "is_buff":True, "buff_name":"Akatosh's Blessing"}}},
        {"description": "A rickety cart has broken an axle. Its merchant owner, a weary Dunmer named Drevis, sighs. 'Azura's curse! My shipment of ash yams for Windhelm will spoil!'", 
         "type": "npc_interaction_and_quest_lead", "details": {"npc_tags": {"role": "merchant_ashlander_goods_stranded", "name":"Drevis", "attitude": "distressed_resigned", "race":"dunmer"}, "dialogue_lead": "'Stendarr's Light, can anyone assist a humble merchant?", "lead_description": "Dunmer merchant needs help fixing his cart. He might reward you handsomely for your efforts.", "related_tags": ["merchant", "ashlander", "ash_yams"]}},
        {"description": "You find a scorched note on a dead Imperial courier. It details an imminent Stormcloak ambush on a strategic bridge [DynamicNearbyLandmark - e.g., Dragon Bridge].", 
         "type": "quest_lead_and_item", "details": {"lead_description": "Imperial courier carries warning of Stormcloak ambush at a bridge. A chance to influence the war.", "related_tags": ["civil_war", "stormcloaks", "imperial_army"], "item_keys": ["imperial_orders_sealed"]}},
        {"description": "A group of stern-faced Vigilants of Stendarr are interrogating a frightened Khajiit traveler on the road. Their leader, a zealous Breton, glares at you.", 
         "type": "npc_interaction", "details": {"npc_tags": {"role": "vigilant_of_stendarr_interrogator_zealous", "attitude": "hostile_suspicious"}, "dialogue_lead": "'Stendarr's Light expose the wicked! You there, traveler, keep moving unless you have business with the righteous.'", "related_tags": ["vigilants_of_stendarr", "khajiit", "religious_zealots"]}},
        {"description": "A sudden, unnatural earthquake shakes the ground violently! Loose rocks tumble from nearby cliffs, and the air fills with dust.", 
         "type": "environmental_hazard", "details": {"hazard_type": "magical_earthquake", "effect_desc": "The world shudders! You must keep your footing or risk injury from falling debris.", "skill_to_navigate": "acrobatics", "dc": 14, "damage_if_failed": 8, "damage_type": "bludgeoning", "flavor_text": "The tremors subside after a few terrifying moments."}}
    ],
    "forest": [
        {"description": "The air grows cold, and you hear the snap of a twig. A Spriggan Matriarch, its form ancient and wreathed in glowing moss, materializes, its eyes burning with primal fury!", 
         "type": "combat_encounter", "details": {"enemy_tags": [["spriggan_matriarch"]], "flavor_text": "The Spriggan attacks!", "special_ability_hint": "Spriggans are vulnerable to fire.", "loot_drop_hint": "Spriggan Sap, rare herbs"}},
        {"description": "You discover a hidden grove with a small, moss-covered shrine to Kyne, Goddess of the Storm and the Hunt. Offerings of hawk feathers and antlers lie before it. Praying here grants you a temporary blessing.", 
         "type": "flavor_and_buff", "details": {"god_mention": "Kyne", "minor_buff_debuff": {"stat": "archery_skill_bonus", "amount": 5, "duration_turns": 120, "is_buff": True, "buff_name": "Kyne's Blessing"}}},
        {"description": "A reclusive Bosmer alchemist, Elara Meadowlight, has a cleverly hidden treehouse dwelling. She's initially wary but might trade rare forest ingredients or offer a quest to retrieve a lost artifact.", 
         "type": "npc_interaction_and_quest_lead", "details": {"npc_tags": {"role": "alchemist_bosmer_reclusive", "name": "Elara Meadowlight", "attitude": "wary_curious", "race": "bosmer"}, "dialogue_lead": "'Who goes there? I don't get many visitors... unless you're here for something.'", "lead_description": "Elara needs someone to retrieve a rare flower from a dangerous cave. She offers a valuable potion as payment.", "related_tags": ["alchemist", "bosmer", "rare_ingredients"]}},
        {"description": "You find a patch of glowing blue Nirnroot by a moonlit stream, its characteristic chime filling the air, alongside some potent Nightshade and a cluster of Deathbell flowers.", 
         "type": "item", "details": {"item_keys": ["nirnroot_glowing", "nightshade_potent", "deathbell_flowers"], "quantity_range_nirnroot_glowing": (1, 2), "quantity_range_nightshade_potent": (2, 3), "quantity_range_deathbell_flowers": (3, 5)}},
        {"description": "You find a crudely scrawled note pinned to an ancient oak: 'The Hagravens of [DynamicNearbyLandmark - e.g., Witchmist Grove] have taken my sister for their dark rituals! Reward offered for her safe return!'", 
         "type": "quest_lead", "details": {"lead_description": "A desperate plea to rescue a sister from Hagravens. A dangerous but potentially rewarding quest.", "related_tags": ["hagravens", "rescue_mission", "dark_rituals"]}},
        {"description": "Ancient, moss-covered stones are arranged in a circle. Runes glow faintly. In the center, a pedestal has three indentations shaped like the claw of a bear, the feather of a hawk, and the scale of a snake.", 
         "type": "puzzle_hint", "details": {"hint_text": "The order of the symbols may be the key to activating the circle. Consider the natural order or dominance of these creatures.", "potential_reward": "Access to a hidden grove or a powerful blessing."}}
    ],
    "dwemer_ruin": [
        {"description": "The air hums with ancient, barely contained power. A massive Dwarven Centurion Master, its aetherium core glowing ominously, activates from its alcove, steam hissing from its joints!", 
         "type": "combat_encounter", "details": {"enemy_tags": [["dwarven_centurion_master"]], "flavor_text": "The Centurion awakens!", "special_ability_hint": "Its steam attacks are highly damaging, but it's slow to maneuver.", "loot_drop_hint": "Dwarven Metal Ingots, Centurion Dynamo Core"}},
        {"description": "You find a complex Dwemer Astrolabe on a pedestal. Its interlocking rings are misaligned. Solving this celestial puzzle might reveal a hidden chamber or activate a nearby mechanism.", 
         "type": "puzzle_hint", "details": {"hint_text": "The rings seem to correspond to constellations. Aligning them correctly might require knowledge of Dwemer astronomy.", "potential_reward": "Access to a hidden vault or control over a defensive system."}},
        {"description": "A hidden pressure plate, almost invisible on the metallic floor, triggers a section of the wall to slide open with a grinding sound. Inside, a small alcove contains several gleaming Dwemer Gyros and a schematic diagram.", 
         "type": "item", "details": {"item_keys": ["dwemer_gyro", "schematic_diagram_advanced"], "quantity_range_dwemer_gyro": (2, 4)}},
        {"description": "You find the final, rambling journal of a long-dead Mages Guild scholar, Sulla Trebatius. It details their descent into the ruin, their obsession with Dwemer 'tonal architecture,' and their descent into madness.", 
         "type": "lore_reveal", "details": {"information": "Sulla believed Dwemer ruins resonated with magical energies that could be harnessed with sonic manipulation. Their experiments may have unleashed something dangerous.", "related_tags": ["mages_guild", "tonal_architecture", "dwemer_lore"]}}
    ],
    "barrow": [
        {"description": "A chilling wind sweeps through the burial chamber as you disturb an ancient seal. Draugr Scourges, their eyes burning with cold fire, and Draugr Death Overlords, wielding ancient Nord weapons, rise from their tombs!", 
         "type": "combat_encounter", "details": {"enemy_tags": [["draugr_scourge"], ["draugr_death_overlord"]], "count_range": (2, 4), "flavor_text": "The Draugr awaken, hungry for the warmth of the living!", "special_ability_hint": "Draugr are resistant to frost but vulnerable to fire.", "loot_drop_hint": "Ancient Nord Weapons, Draugr Dust"}},
        {"description": "Behind a loose stone in a sarcophagus of a noble warrior, you find a finely crafted Amulet of Stendarr, surprisingly well-preserved, alongside a handful of potent Bone Meal.", 
         "type": "item", "details": {"item_keys": ["amulet_stendarr_finely_crafted", "bone_meal_potent"], "quantity_range_bone_meal_potent": (3, 5)}},
        {"description": "A series of Nordic burial urns line a shelf. Most are empty or contain only dust, but one, heavier than the others and sealed with wax, holds a small hoard of ancient Nord coins and a tarnished silver ring.", 
         "type": "item", "details": {"item_keys": ["nord_coin_ancient", "silver_ring_tarnished"], "quantity_range_nord_coin_ancient": (15, 30)}},
        {"description": "A Dragon Priest's sarcophagus, intricately carved with draconic motifs and glowing with faint magical wards, dominates the central chamber. Before it is a pedestal with three strange claw-shaped indentations...", 
         "type": "puzzle_hint", "details": {"hint_text": "The claws are likely keys. Finding them and placing them in the correct order might unlock the sarcophagus... and unleash its occupant.", "potential_reward": "A powerful Dragon Priest mask or a scroll of immense power."}}
    ],
    "ashland_waste": [
        {"description": "The air is thick with choking ash. You find a half-buried skeleton, its hand clutching a small, heat-resistant pouch containing a few Fire Salts and a charred piece of paper.", 
         "type": "item_and_quest_lead", "details": {"item_keys": ["fire_salts_impure", "map_fragment_ashlands_charred"], "quantity_range_fire_salts_impure":(1,2), "lead_description": "The map fragment seems to point towards a hidden ruin or a forgotten Dunmer shrine somewhere in the ashlands.", "related_tags": ["ashlands", "fire_salts", "dunmer_ruin"]}},
        {"description": "A wild Netch, its gas-filled body drifting eerily through the ashfall, floats by. They are usually docile unless provoked, but their leather is valuable.", 
         "type": "npc_encounter_hint", "details": {"npc_tags":{"role":"creature_netch_bull_or_betty", "attitude":"neutral_unless_attacked"}, "situation": "Potential source of Netch Leather if hunted carefully.", "related_tags": ["netch", "ashlands_creature"]}},
        {"description": "You discover a small, hidden shrine to Azura, somehow preserved amidst the desolation. Praying here grants you a brief moment of clarity and magical fortitude.", 
         "type": "flavor_and_buff", "details": {"god_mention": "Azura", "lore_hint":"Azura's influence persists even in the most blighted lands, offering hope to her Dunmer followers.", "minor_buff_debuff": {"stat": "resistance_fire", "amount": 0.1, "duration_turns": 120, "is_buff": True, "buff_name": "Azura's Grace"}}},
        {"description": "A sudden tremor shakes the ground, and a fissure opens nearby, venting noxious sulfurous gas. You must move quickly to avoid being overcome.", 
         "type": "environmental_hazard", "details": {"hazard_type": "ashland_fissure_gas_vent", "effect_desc": "The sulfurous gas stings your eyes and lungs, making it hard to breathe.", "avoid_skill": "endurance", "avoid_dc": 13, "damage_if_failed": 6, "damage_type": "poison", "flavor_text": "The gas dissipates after a few moments, leaving a lingering stench."}}
    ],
    "volcanic_caldera": [
        {"description": "You find a rare Obsidian Shard, still warm from the geothermal heat, embedded in a rock. It pulses with a faint, fiery energy.", 
         "type": "item", "details": {"item_key": "obsidian_shard_volcanic", "lore_hint":"Obsidian from such active regions is prized for fire enchantments."}},
        {"description": "A mad Argonian pyromancer, believing this caldera to be a gateway to the Deadlands, is attempting a dangerous ritual to summon a Flame Atronach Monarch. He mistakes you for a fellow cultist...", 
         "type": "npc_interaction_hostile", "details": {"npc_tags": {"role": "mage_pyromancer_cultist_argonian_mad", "attitude": "hostile_fanatical", "race":"argonian"}, "dialogue_lead": "'More followers for the Great Conflagration! Join me, brother, and we shall unleash the fury of Oblivion!'", "related_tags": ["argonian", "pyromancer", "cultist"]}},
        {"description": "The ground is unstable here. A section of hardened lava crust crumbles beneath your feet, revealing a small lava tube leading downwards. It's incredibly hot.", 
         "type": "location_discovery_hint", "details": {"location_name_hint": "Caldera Lava Tube", "related_tags": ["volcanic_cave", "extreme_heat_hazard", "underground_lava_flow"], "mark_on_map_chance": 0.4}},
        {"description": "Amidst the scorched rocks, you find a perfectly preserved Fire Fern, an extremely rare alchemical ingredient that thrives in intense heat.", 
         "type": "item", "details": {"item_key": "fire_fern_pristine", "quantity_range": (1,1), "lore_hint":"Fire Ferns are almost mythical, said to grant unparalleled resistance to flames."}}
    ]
    # ... (Ensure all other RANDOM_EVENTS categories are similarly detailed)
}


def explore_location(player, current_location, random_encounters, npc_registry, all_locations_list, ui):
    """Explores the current location and triggers random events based on its tags."""
    try:
        ui.slow_print(f"You carefully explore {current_location['name']}...")

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
            broad_fallback_tags = ["wilderness", "urban_area", "ruin_general", "cave_general", "hold_generic"] 
            for broad_tag_category_key in broad_fallback_tags:
                for specific_fallback_tag in ["forest", "city", "ruin", "cave", "hold"]: 
                    if specific_fallback_tag in current_location_tags and specific_fallback_tag in EXPLORATION_RESULTS:
                        available_results_data.extend(EXPLORATION_RESULTS[specific_fallback_tag])
                        if available_results_data: break
                if available_results_data: break

        selected_exploration_outcomes = []
        if available_results_data:
            # Remove duplicates based on "description"
            unique_descriptions = set()
            unique_results_data = []
            for d in available_results_data:
                if d["description"] not in unique_descriptions:
                    unique_descriptions.add(d["description"])
                    unique_results_data.append(d)

            num_results_to_show = min(random.randint(1, 2), len(unique_results_data)) 
            selected_exploration_outcomes = random.sample(unique_results_data, num_results_to_show)

        if selected_exploration_outcomes:
            for outcome in selected_exploration_outcomes:
                ui.slow_print(outcome["description"])
                effect_data = outcome.get("effect")
                if effect_data:
                    effect_type = effect_data.get("type")
                    details = effect_data.get("details", {})
                    
                    # --- Implemented Game Engine Calls for Exploration Effects ---
                    if effect_type == "item_find":
                        if "gold_amount_range" in details:
                            gold = random.randint(details["gold_amount_range"][0], details["gold_amount_range"][1])
                            player.stats.gold += gold 
                            ui.slow_print(f"You found {gold} septims!")
                        item_keys_to_find = details.get("item_keys", [])
                        if "item_key" in details and details["item_key"] not in item_keys_to_find:
                            item_keys_to_find.append(details["item_key"])
                        
                        for item_k in item_keys_to_find:
                            item_template = generate_item_from_key(item_k, player.level)
                            if item_template:
                                q_key_specific = f"quantity_range_{item_k}"
                                q_range = details.get(q_key_specific, details.get("quantity_range", (1,1)))
                                quantity = random.randint(q_range[0], q_range[1])
                                added_count = 0
                                for _ in range(quantity):
                                    item_instance = generate_item_from_key(item_k, player.level)
                                    if player.add_item(item_instance): 
                                        added_count +=1
                                    else:
                                        ui.slow_print(f"Your inventory is full, couldn't pick up {item_instance.name}.")
                                        break
                                if added_count > 0: ui.slow_print(f"You obtained: {item_template.name}" + (f" (x{added_count})" if added_count > 1 else "") + "!")
                            else:
                                ui.slow_print(f"(Could not find item definition for key: {item_k})")

                        if "item_category" in details: 
                            item = generate_random_item(details["item_category"], player.level)
                            if player.add_item(item): ui.slow_print(f"You managed to find a {item.name}.")
                            else: ui.slow_print(f"You found a {item.name}, but your inventory is full.")
                        
                        if "item_find_multiple_options" in details: 
                            for option in details.get("options", []):
                                if random.random() < option.get("chance", 1.0):
                                    item_template = generate_item_from_key(option["item_key"], player.level)
                                    if item_template:
                                        q_range = option.get("quantity_range", (1,1))
                                        quantity = random.randint(q_range[0], q_range[1])
                                        # (Add item logic similar to above)
                                        ui.slow_print(f"You found some {item_template.name} (x{quantity})!")
                                    break 

                    elif effect_type == "quest_lead" or effect_type == "quest_lead_and_item":
                        ui.slow_print(f"[Quest Lead Discovered]: {details.get('lead_description', 'You feel this could lead to something more.')}")
                        # Generate a quest object based on the lead
                        # This is a simplified quest generation; your game.py might have a more complex system
                        if hasattr(player, 'quest_log'):
                            # Try to use generate_location_appropriate_quest if suitable
                            # For now, create a basic quest from the lead
                            quest_title = details.get("quest_title_hint", f"Investigate {details.get('related_tags',[current_location['name']])[0].title()}")
                            quest_reward = generate_reward(player.level, details.get('related_tags', []))
                            new_quest = Quest(
                                title=quest_title,
                                description=details.get('lead_description'),
                                reward=quest_reward,
                                level_requirement=player.level,
                                location=current_location, # Or a hinted location
                                completion_condition=f"resolved_{quest_title.replace(' ','_').lower()}"
                            )
                            player.quest_log.add_quest(new_quest)
                            ui.slow_print(f"New quest added to your log: {new_quest.title}")
                        if "item_found_on_skeleton" in details: # Example for quest_lead_and_item
                             item_skel = generate_item_from_key(details["item_found_on_skeleton"], player.level)
                             if item_skel and player.add_item(item_skel): ui.slow_print(f"You also find {item_skel.name} nearby.")


                    elif effect_type == "location_discovery_hint":
                        hinted_loc_name = details.get("location_name_hint", "a mysterious place")
                        ui.slow_print(f"You learn of a place called '{hinted_loc_name}'. It seems related to {', '.join(details.get('related_tags', ['local legends']))}.")
                        if random.random() < details.get("mark_on_map_chance", 0.3):
                            target_loc = next((loc for loc in all_locations_list if loc["name"] == hinted_loc_name), None)
                            if target_loc:
                                try:
                                    from game import known_locations 
                                    if target_loc["id"] not in known_locations:
                                        known_locations.add(target_loc["id"])
                                        ui.slow_print(f"'{hinted_loc_name}' has been marked on your map!")
                                except ImportError: pass # Game module not available here
                            else:
                                ui.slow_print(f"(Though you hear of '{hinted_loc_name}', its exact location isn't clear enough to mark.)")
                    
                    elif effect_type == "skill_challenge" or effect_type == "skill_challenge_or_choice":
                        skill_to_test = details.get("skill", details.get("skill_persuade", details.get("skill_stealth", "perception")))
                        dc = details.get("dc", details.get("dc_persuade", details.get("dc_stealth", 12)))
                        player_skill_level = player.skills.get(skill_to_test, 5) # Default to 5 if skill not present
                        skill_modifier = player_skill_level // 4 # Example modifier
                        roll = random.randint(1,20)
                        total_roll = roll + skill_modifier
                        ui.slow_print(f"You attempt to use your {skill_to_test.replace('_',' ')}... (Rolled {roll} + Mod {skill_modifier} = {total_roll} vs DC {dc})")

                        if total_roll >= dc:
                            ui.slow_print(details.get("success_desc", "You succeed!"))
                            if "success_reward" in details:
                                reward = details["success_reward"]
                                if "gold_amount_range" in reward:
                                    player.stats.gold += random.randint(reward["gold_amount_range"][0], reward["gold_amount_range"][1])
                                    ui.slow_print("You gain some gold.")
                                if "item_category" in reward:
                                    item = generate_random_item(reward["item_category"], player.level)
                                    if player.add_item(item): ui.slow_print(f"You find a {item.name}.")
                                if "location_access_hint" in reward:
                                     ui.slow_print(f"This grants access to: {reward['location_access_hint']}")
                        else:
                            ui.slow_print(details.get("failure_desc", "You fail."))
                            if "failure_penalty" in details:
                                penalty = details["failure_penalty"]
                                if "damage" in penalty: 
                                    player.stats.take_damage(penalty["damage"])
                                    ui.slow_print(f"You take {penalty['damage']} damage!")
                                if "status_effect" in penalty:
                                    # Conceptual: player.apply_status_effect(penalty["status_effect"])
                                    ui.slow_print(f"You feel {penalty['status_effect']['type']}.")


                    elif effect_type == "lore_reveal":
                        ui.slow_print(f"[Lore]: {details.get('information', 'You recall an old tale related to this place.')}")
                        if "minor_buff_debuff" in details:
                            buff = details["minor_buff_debuff"]
                            # Conceptual: player.apply_temporary_effect(buff)
                            ui.slow_print(f"Recalling this lore makes you feel a surge of {buff.get('stat')} ({'+' if buff.get('is_buff') else '-'}{buff.get('amount')})!")
                    
                    elif effect_type == "npc_encounter_hint":
                        ui.slow_print(f"You get the feeling you might encounter a {details.get('npc_tags',{}).get('role','certain individual')} here: {details.get('situation','They might be nearby...')}")

                    elif effect_type == "item_purchase_opportunity":
                        item_key_offered = details.get('item_key')
                        cost = details.get('cost', 50)
                        ui.slow_print(f"The {details.get('dialogue_npc_role', 'person')} offers to sell you a {item_key_offered} for {cost} gold.")
                        # Conceptual: if ui.ask_yes_no(f"Purchase {item_key_offered} for {cost} gold?"):
                        #    if player.stats.gold >= cost:
                        #        player.stats.gold -= cost
                        #        item = generate_item_from_key(item_key_offered, player.level)
                        #        if player.add_item(item): ui.slow_print(f"You purchased {item.name}.")
                        #        else: player.stats.gold += cost; ui.slow_print("Inventory full.")
                        #    else: ui.slow_print("Not enough gold.")

                    elif effect_type == "moral_choice_event":
                        ui.slow_print(f"[Choice]: {details.get('choice_text')}")
                        # Conceptual: user_choice = ui.get_player_choice(["Option1", "Option2"])
                        # if user_choice == "Option1": game_engine.apply_effect(player, details.get('option1_reward_or_penalty'))

                    elif effect_type == "interaction_point":
                        ui.slow_print(f"You notice a {details.get('interaction_name')}. {details.get('action_text', 'Interact?')}")
                        # Conceptual: if ui.ask_yes_no(f"Interact with {details.get('interaction_name')}"):
                        #    if "requires_item_key" in details and not player.inventory_has_item(details["requires_item_key"]):
                        #        ui.slow_print("You lack the required item.")
                        #    else:
                        #        game_engine.apply_interaction_effect(player, details.get('success_effect'))

                    # Check for dungeon name in description for direct discovery
                    for dn_name in DUNGEON_NAMES:
                        if dn_name.lower() in outcome["description"].lower():
                            dungeon_loc_obj = next((loc for loc in all_locations_list if loc["name"] == dn_name), None)
                            if dungeon_loc_obj:
                                try:
                                    from game import known_locations 
                                    if dungeon_loc_obj["id"] not in known_locations:
                                        known_locations.add(dungeon_loc_obj["id"])
                                        ui.slow_print(f"You've pinpointed the location of {dn_name} on your map!")
                                except ImportError: pass 
                            break 
        else:
            ui.slow_print("You find nothing particularly noteworthy, though the unique atmosphere of the place certainly leaves an impression.")
        ui.press_enter()
    except Exception as e:
        print(f"Error in explore_location: {e}")
        traceback.print_exc()


def trigger_random_event(location_tags, player, ui, current_location):
    """Triggers a random event based on location tags, with more comprehensive tag use."""
    event = None
    try:
        possible_events_for_location = []
        
        for tag in location_tags:
            if tag in RANDOM_EVENTS:
                possible_events_for_location.extend(RANDOM_EVENTS[tag])
        
        if not possible_events_for_location or random.random() < 0.25: 
            possible_events_for_location.extend(RANDOM_EVENTS.get("generic_travel", []))

        if possible_events_for_location:
            # Remove duplicates based on "description"
            unique_descriptions = set()
            unique_events = []
            for d in possible_events_for_location:
                if d["description"] not in unique_descriptions:
                    unique_descriptions.add(d["description"])
                    unique_events.append(d)
            possible_events_for_location = unique_events

        if possible_events_for_location and random.random() < 0.8: 
            event = random.choice(possible_events_for_location)
            ui.slow_print(f"\n{event['description']}") 

            event_type = event.get("type")
            details = event.get("details", {})
            
            # --- Implemented Game Engine Calls for Random Event Effects ---
            if event_type == "item" or event_type == "item_and_quest_lead" or event_type == "item_and_skill_challenge" or event_type == "quest_lead_and_item":
                if "gold_amount_range" in details:
                    gold = random.randint(details["gold_amount_range"][0], details["gold_amount_range"][1])
                    player.stats.gold += gold
                    ui.slow_print(f"You gain {gold} gold!")
                if "gold_loss_range" in details:
                    gold_loss = random.randint(details["gold_loss_range"][0], details["gold_loss_range"][1])
                    actual_loss = min(gold_loss, player.stats.gold)
                    player.stats.gold -= actual_loss
                    ui.slow_print(f"You lose {actual_loss} gold! {details.get('flavor_text', '')}")
                
                item_keys_to_grant = details.get("item_keys", [])
                if "item_key" in details and details["item_key"] not in item_keys_to_grant: 
                    item_keys_to_grant.append(details["item_key"])
                for key_type in ["item_found_on_body", "item_found_at_camp"]: # Adding more specific keys
                    if key_type in details and details[key_type] not in item_keys_to_grant:
                        item_keys_to_grant.append(details[key_type])

                for item_k in item_keys_to_grant:
                    if not isinstance(item_k, str): continue
                    item_template = generate_item_from_key(item_k, player.level)
                    if item_template:
                        quantity = 1
                        specific_q_key = f"quantity_range_{item_k}" # e.g. quantity_range_lockpick
                        if specific_q_key in details and isinstance(details[specific_q_key], tuple):
                            quantity = random.randint(details[specific_q_key][0], details[specific_q_key][1])
                        elif "quantity_range" in details and isinstance(details["quantity_range"], tuple): # General quantity
                             quantity = random.randint(details["quantity_range"][0], details["quantity_range"][1])

                        added_count = 0
                        for _ in range(quantity):
                            item_instance = generate_item_from_key(item_k, player.level) 
                            if player.add_item(item_instance): added_count +=1
                            else:
                                ui.slow_print(f"Your inventory is full, couldn't pick up {item_instance.name}.")
                                break
                        if added_count > 0: ui.slow_print(f"You found: {item_template.name}" + (f" (x{added_count})" if added_count > 1 else "") + "!")
                    else: ui.slow_print(f"(Could not define item for key: {item_k})")

                if "item_category" in details: 
                    item = generate_random_item(details["item_category"], player.level)
                    if "item_name" in details: item.name = details["item_name"] 
                    if player.add_item(item): ui.slow_print(f"You acquire: {item.name}!")
                    else: ui.slow_print(f"You spot {item.name}, but your inventory is full!")
                
                if (event_type == "item_and_quest_lead" or event_type == "quest_lead_and_item") and "lead_description" in details:
                     ui.slow_print(f"Additionally: {details['lead_description']}")
                     if hasattr(player, 'quest_log'):
                        quest_title = details.get("quest_title_hint", f"Investigate Clue from {current_location['name']}")
                        quest_reward = generate_reward(player.level, details.get('related_tags', []))
                        new_quest = Quest(title=quest_title, description=details.get('lead_description'), reward=quest_reward, level_requirement=player.level, location=current_location, completion_condition="unresolved")
                        player.quest_log.add_quest(new_quest)
                        ui.slow_print(f"A new lead has been noted in your journal: {new_quest.title}")


            elif event_type == "combat_encounter" or event_type == "combat_encounter_ambush":
                ui.slow_print(details.get("flavor_text", f"Suddenly, you are attacked!"))
                # Conceptual: game_engine.initiate_combat(player, details.get("enemy_tags", [["mysterious_foe"]]), details.get("count_range",(1,1)), details.get("ambush", False), current_location)
                # For now, just print the hint if it exists
                if "special_ability_hint" in details: ui.slow_print(f"(Hint: {details['special_ability_hint']})")
                if "loot_drop_hint" in details: ui.slow_print(f"(They might drop: {details['loot_drop_hint']})")


            elif event_type == "npc_interaction" or event_type == "npc_interaction_and_quest_lead" or event_type == "npc_interaction_hostile":
                npc_role = details.get("npc_tags", {}).get("role", "stranger").replace('_', ' ')
                npc_name_from_details = details.get("npc_tags", {}).get("name", f"a {npc_role}")
                ui.slow_print(f"You encounter {npc_name_from_details}. They say, \"{details.get('dialogue_lead', 'Well met.')}\"")
                # Conceptual: game_engine.initiate_dialogue_or_interaction(player, details, current_location)
                if details.get("combat_trigger_immediate"):
                    # Conceptual: game_engine.initiate_combat(player, [details.get("npc_tags", {"role":"hostile_attacker"})], (1,1), True, current_location)
                    ui.slow_print(f"{npc_name_from_details} attacks!")


            elif event_type == "skill_challenge" or event_type == "item_and_skill_challenge":
                skill_to_test = details.get("skill", "perception")
                dc = details.get("dc", 12)
                player_skill_level = player.skills.get(skill_to_test, 5) 
                skill_modifier = player_skill_level // 4 
                roll = random.randint(1,20) + skill_modifier
                target_desc = details.get('target_description', 'a task')
                ui.slow_print(f"You attempt {target_desc} using your {skill_to_test.replace('_',' ')} (Roll: {roll} + Mod: {skill_modifier} = {total_roll} vs DC: {dc})...")

                if total_roll >= dc: 
                    ui.slow_print(details.get("success_desc", "You succeed!"))
                    if "success_reward" in details:
                        reward = details["success_reward"]
                        if "gold_amount_range" in reward:
                            gained_gold = random.randint(reward["gold_amount_range"][0], reward["gold_amount_range"][1])
                            player.stats.gold += gained_gold
                            ui.slow_print(f"You gain {gained_gold} gold.")
                        if "item_key" in reward: # Can also be item_keys for multiple
                            keys = reward.get("item_keys", [reward.get("item_key")])
                            for r_item_k in keys:
                                if r_item_k:
                                    r_item = generate_item_from_key(r_item_k, player.level)
                                    if r_item and player.add_item(r_item): ui.slow_print(f"You obtained: {r_item.name}.")
                                    elif r_item: ui.slow_print(f"You found {r_item.name} but are too encumbered.")
                        if "temp_buff" in reward:
                            # Conceptual: player.apply_temporary_effect(reward['temp_buff'])
                            ui.slow_print(f"You feel a temporary boon: {reward['temp_buff'].get('stat')} +{reward['temp_buff'].get('amount')}.")
                        if "lore_reveal_specific" in reward: ui.slow_print(f"[Lore Uncovered!]: {reward['lore_reveal_specific']}")
                        if "quest_lead_info" in reward:
                            ui.slow_print(f"[Quest Clue!]: {reward['quest_lead_info']}")
                            # Conceptual: player.journal.add_lead_from_string(reward['quest_lead_info'])

                else: # Failure
                    ui.slow_print(details.get("failure_desc", "You fail."))
                    if "failure_penalty" in details:
                        penalty = details["failure_penalty"]
                        if "damage" in penalty: 
                            player.stats.take_damage(penalty["damage"])
                            ui.slow_print(f"You take {penalty['damage']} {penalty.get('damage_type','')} damage!")
                        if "status_effect" in penalty:
                            # Conceptual: player.apply_status_effect(penalty["status_effect"])
                            eff = penalty["status_effect"]
                            ui.slow_print(f"You are afflicted with {eff.get('type')} (Potency: {eff.get('potency',0)}, Duration: {eff.get('duration_turns',0)} turns)!")
                        if "item_loss" in penalty and penalty["item_loss"]:
                            # Conceptual: player.inventory.remove_item_by_name_or_key(penalty['item_loss'])
                            ui.slow_print(f"In your fumbling, you lose your {penalty['item_loss']}!")
                
                if event_type == "item_and_skill_challenge" and "item_key" in details: 
                    item_obj = generate_item_from_key(details["item_key"], player.level)
                    if item_obj: ui.slow_print(f"The challenge was related to a {item_obj.name}.")


            elif event_type == "quest_lead":
                ui.slow_print(f"Clue: {details.get('lead_description', 'Something here seems important...')}")
                if hasattr(player, 'quest_log'):
                    quest_title = details.get("quest_title_hint", f"Investigate Rumor in {current_location['name']}")
                    quest_reward = generate_reward(player.level, details.get('related_tags', []))
                    new_quest = Quest(title=quest_title, description=details.get('lead_description'), reward=quest_reward, level_requirement=player.level, location=current_location, completion_condition="unresolved")
                    player.quest_log.add_quest(new_quest)
                    ui.slow_print(f"A new entry has been added to your journal: {new_quest.title}")
                if "related_tags" in details: ui.slow_print(f"(Related to: {', '.join(details['related_tags'])})")

            elif event_type == "environmental_hazard":
                ui.slow_print(details.get("effect_desc", "The environment poses a sudden threat!"))
                if "skill_to_navigate" in details or "avoid_skill" in details:
                    skill_to_test = details.get("skill_to_navigate", details.get("avoid_skill"))
                    dc = details.get("dc", details.get("avoid_dc", 13))
                    player_skill_level = player.skills.get(skill_to_test, 5)
                    roll = random.randint(1,20) + (player_skill_level // 4)
                    ui.slow_print(f"You try to navigate the hazard (Roll: {roll} vs DC: {dc})...")
                    if roll < dc and "damage_if_failed" in details:
                        player.stats.take_damage(details["damage_if_failed"])
                        ui.slow_print(f"You couldn't avoid it and take {details['damage_if_failed']} {details.get('damage_type','')} damage!")
                    elif roll >= dc:
                        ui.slow_print("You manage to avoid the worst of it!")
                elif "damage_if_failed" in details: # Immediate damage if no avoidance skill
                    player.stats.take_damage(details["damage_if_failed"])
                    ui.slow_print(f"You take {details['damage_if_failed']} {details.get('damage_type','')} damage from the hazard!")
                if "continuous_debuff_while_in_area" in details:
                    # Conceptual: player.apply_area_effect_debuff(details["continuous_debuff_while_in_area"])
                    debuff = details["continuous_debuff_while_in_area"]
                    ui.slow_print(f"The {debuff.get('buff_name', 'hazard')} affects your {debuff.get('stat')} while you remain here.")


            elif event_type == "puzzle_hint":
                ui.slow_print(f"Hint: {details.get('hint_text', 'A strange mechanism or inscription catches your eye...')}")
                # Conceptual: player.journal.add_puzzle_hint(details, current_location['name'])
                if "potential_reward" in details: ui.slow_print(f"(Solving it might yield: {details['potential_reward']})")

            elif event_type == "faction_interaction_lead":
                ui.slow_print(f"Faction event: {details.get('situation', 'Activity is afoot.')}")
                ui.slow_print(f"(Involving factions: {', '.join(details.get('faction_tags',[]))})")
                # Conceptual: game_engine.process_faction_lead(player, details, current_location)

            elif event_type == "flavor" or event_type == "flavor_and_buff":
                if "temporary_buff" in details:
                    buff = details['temporary_buff']
                    # Conceptual: player.apply_temporary_effect(buff) # This method needs to exist on Player or Stats
                    # Example direct stat modification (needs a system for duration)
                    target_stat = buff.get('stat')
                    if target_stat == "personality": player.stats.personality += buff.get('amount',0)
                    elif target_stat == "alchemy_skill_bonus": player.skills['alchemy'] = player.skills.get('alchemy', 15) + buff.get('amount',0)
                    # Add more direct stat/skill modifications or implement a proper buff system
                    ui.slow_print(f"You feel a brief surge of {buff.get('stat')} ({'+' if buff.get('is_buff', True) else '-'}{buff.get('amount')})!")
                if "weather_change" in details:
                    # Conceptual: game_engine.world_state.set_weather(details['weather_change'], current_location.get('region_tag'))
                    ui.slow_print(f"The weather noticeably shifts towards {details['weather_change']}.")
                pass
        else: 
            if not possible_events_for_location: 
                ui.slow_print("The area seems quiet, with nothing specific of note occurring right now.")
            else:
                 ui.slow_print("You sense a potential occurrence, but it passes without incident this time.")
        return event
    except Exception as e:
        print(f"Error in trigger_random_event: {e}")
        traceback.print_exc()
        return None