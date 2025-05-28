# events.py
import random
import traceback
from ui import UI
# Assuming Quest, generate_reward, generate_location_appropriate_quest are correctly in quests.py
from quests import Quest, generate_reward, generate_location_appropriate_quest # Import the new Quest class
from items import Item, generate_item_from_key, generate_random_item
from locations import LOCATIONS # For DUNGEON_NAMES
from npc import NPC, HOSTILE_ROLES # To potentially spawn NPCs directly
# EXPLORATION_RESULTS from exploration_data.py
from exploration_data import EXPLORATION_RESULTS
# from npc import generate_npc_from_tags # Conceptual import, depends on implementation


# --- DYNAMICALLY GENERATED DUNGEON_NAMES (from your provided code) ---
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
if not DUNGEON_NAMES: # Fallback (from original)
    DUNGEON_NAMES = [
        "Bleak Falls Barrow", "Quicksilver Mine", "Nightcaller Temple", "Iron-Breaker Mine",
        "Saarthal", "Hob's Fall Cave", "Yngol Barrow", "Movarth's Lair", "Ustengrav",
        "Pinewatch", "Halldir's Cairn", "Cidhna Mine", "Druadach Redoubt", "Shroud Hearth Barrow",
        "Wolfskull Cave", "Lost Prospect Mine", "The Ratway", "Labyrinthian", "Dustman's Cairn",
        "Alftand", "Mzinchaleft", "Forelhost", "Silent Moons Camp", "Reachwind Eyrie", "Blind Cliff Cave"
    ]

# --- Define SPECIFIC_LOCATION_TAGS (from your original code) ---
SPECIFIC_LOCATION_TAGS = [
    "tavern", "inn", "market", "mine", "camp", "cave", "ruin", "barrow", "dwemer",
    "keep", "meadhall", "blacksmith", "alchemy_shop", "temple", "college", "palace",
    "meadery", "brewery", "watchtower", "lighthouse", "wreck", "shop", "port",
    "government", "guild", "prison", "graveyard", "sanctuary", "monastery",
    "fort", "fortified", "city", "town", "village", "dragon_lair_ancient",
    "enchanted_forest", "cursed_swamp", "volcanic_caldera", "glacial_cave", "ashland_waste"
]

# --- EXPANDED AND REFINED RANDOM_EVENTS (4E 200 LORE APPLIED) ---
RANDOM_EVENTS = {
    "generic_travel": [
        {
            "description": "You spot a weathered Shrine of Akatosh by the roadside, its eternal flame flickering valiantly. You feel a sense of timelessness and renewed purpose upon offering a brief prayer.",
            "type": "flavor_and_buff",
            "details": {
                "god_mention": "Akatosh",
                "minor_buff_debuff": {"stat": "magicka_regen_rate", "amount": 0.1, "duration_turns": 180, "is_buff": True, "buff_name": "Akatosh's Endurance"}
            }
        },
        {
            "description": "A rickety cart has broken an axle. Its merchant owner, a weary Dunmer named Drevis, sighs. 'Azura's curse! My shipment of ash yams for Windhelm's Gray Quarter will spoil if I don't get this fixed!'",
            "type": "npc_interaction_and_quest_lead",
            "details": {
                "npc_spawn_info": {"name": "Drevis", "race": "dunmer", "role": "merchant", "level": 3, "disposition": 60, "unique_id": "drevis_dunmer_merchant"},
                "dialogue_lead": "'Stendarr's Mercy, can anyone assist a humble merchant? I have coin, and perhaps some rare goods from Morrowind for your trouble.'",
                "quest_hint_template_id": "escort_merchant_or_repair_cart", # Point to a quest template
                "related_tags": ["merchant", "dunmer_refugee", "ash_yams", "roadside_assistance"]
            }
        },
        {
            "description": "You find a hastily written, bloodstained note clutched in the hand of a dead Imperial courier. It speaks of rising tensions and a planned attack by 'Nord patriots' on a strategic bridge near [DynamicNearbyLandmark - e.g., Dragon Bridge].",
            "type": "quest_lead_and_item",
            "details": {
                "item_key": "imperial_dispatch_sealed_bloodied",
                "quest_hint_template_id": "imperial_courier_dispatch", # Point to a quest template
                "related_tags": ["political_unrest", "nord_dissidents", "imperial_courier", "ambush_warning"],
                "moral_choice_hint": "Inform Imperials, warn dissidents, or use information for personal gain."
            }
        },
        {
            "description": "A group of stern-faced Vigilants of Stendarr are interrogating a frightened Khajiit traveler on the road. Their leader, a zealous Breton, eyes you suspiciously. 'Unless you bear witness to Daedric corruption, move along. Stendarr's light has no time for idle gawkers!'",
            "type": "npc_interaction_choice",
            "details": {
                "npc_spawn_info": {"name": None, "race": "breton", "role": "vigilant_of_stendarr_leader", "level": 8, "disposition": 40, "unique_id": "vigilant_leader_event_ID"},
                "secondary_npc_spawn_info": {"name": None, "race": "khajiit", "role": "traveler", "level": 4, "disposition": 70, "unique_id": "khajiit_traveler_event_ID"},
                "dialogue_lead": "'State your purpose, or be on your way. We hunt abominations.'",
                "quest_hint_template_id": "thalmor_interrogation", # Link to the specific quest
                "related_tags": ["vigilants_of_stendarr", "khajiit_traveler", "religious_zealots", "daedra_hunting"],
            }
        },
        {
            "description": "A sudden, unnatural tremor shakes the ground violently! Loose rocks tumble from nearby cliffs, and the air fills with dust. You hear a faint, guttural roar from deep within the earth.",
            "type": "environmental_hazard_and_lore_hint",
            "details": {
                "hazard_type": "magical_earthquake_minor",
                "effect_desc": "The world shudders! You must keep your footing (Acrobatics DC 14) or risk minor injury (1d6 bludgeoning) from falling debris.",
                "lore_hint": "Such tremors are sometimes associated with ancient Dwemer machinery reactivating or the stirring of slumbering subterranean beasts.",
                "related_tags": ["earthquake", "dwemer_rumor", "monster_rumor", "skill_challenge_acrobatics"],
                "skill_challenge": {"skill":"agility", "dc":14, "success_desc":"You deftly keep your footing, avoiding the falling rocks.", "failure_desc":"You lose your balance and take 1d6 bludgeoning damage from falling debris."}
            }
        },
        {
            "description": "You encounter a Thalmor patrol on the road. Their Justiciar leader, with a chillingly polite demeanor, questions your travel and adherence to the White-Gold Concordat, specifically inquiring about any Talos worship.",
            "type": "npc_interaction_tense",
            "details": {
                "npc_spawn_info": {"name": None, "race":"altmer", "role":"thalmor_justiciar", "level": 10, "disposition": 30, "unique_id": "thalmor_justiciar_patrol_ID"},
                "secondary_npc_spawn_info": {"name": None, "race":"altmer", "role":"thalmor_soldier", "count": 2, "level": 8, "unique_id": "thalmor_soldier_patrol_ID"},
                "dialogue_lead": "'Citizen. We are ensuring compliance with the terms of the White-Gold Concordat. Have you witnessed any heresy regarding the false god Talos?'",
                "related_tags": ["thalmor_patrol", "white_gold_concordat", "talos_ban", "political_tension", "imperial_law"],
                "quest_hint_template_id": "thalmor_interrogation" # Link to the specific quest
            }
        },
        {
            "description": "A wandering scholar, hunched over a heavy tome, asks if you've seen any unusual ancient carvings or ruins nearby, unrelated to the Dwemer. They seem particularly interested in early Atmoran settlements.",
            "type": "npc_interaction_and_lore_reveal",
            "details": {
                "npc_spawn_info": {"name": "Historian Elmsworth", "race": "imperial", "role": "scholar", "level": 6, "disposition": 70, "unique_id": "historian_elmsworth_ID"},
                "dialogue_lead": "'Pardon me, traveler. My research into pre-Nordic Skyrim leads me to believe this region holds many secrets. Have you encountered any particularly ancient, non-Dwemer stonework?'",
                "lore_hint": "The scholar shares a snippet about the complexity of Atmoran migrations and their early interactions with Skyrim's native creatures and elves.",
                "related_tags": ["scholar", "atmora_lore", "ancient_history", "ruin_research"],
                "quest_lead_potential_simple": {"title": "Atmoran Remains", "description": "Find an ancient Atmoran ruin or artifact.", "turn_in_npc_id": "historian_elmsworth_ID"}
            }
        }
    ],
    "forest": [
        {
            "description": "The air grows cold, and you hear the snap of a twig. A Spriggan Matriarch, its form ancient and wreathed in glowing moss, materializes, its eyes burning with primal fury! It seems to be guarding a rare cluster of glowing mushrooms.",
            "type": "combat_encounter_or_choice",
            "details": {
                "enemy_spawn_info": [{"role": "spriggan_matriarch", "race": "spriggan_creature", "level": 10, "count": 1}],
                "flavor_text": "The Spriggan raises its thorny arms, a low growl emanating from its woody form.",
                "special_ability_hint": "Spriggans are vulnerable to fire but can heal themselves and charm animals.",
                "loot_drop_hint": "Spriggan Sap, Taproot, rare glowing mushrooms",
                "choice_options": ["Attack", "Attempt to sneak past (Sneak DC 16)", "Offer a piece of meat/honey (Nature Lore DC 13 to know this might work)"]
            }
        },
        {
            "description": "You discover a hidden grove with a small, moss-covered shrine to Kyne, Goddess of the Storm and the Hunt. Offerings of hawk feathers and antlers lie before it. Praying here and leaving a small offering (e.g., a feather, a piece of meat) might grant Kyne's favor.",
            "type": "flavor_and_buff_conditional",
            "details": {
                "god_mention": "Kyne",
                "minor_buff_debuff": {"stat": "archery_skill", "amount": 5, "duration_turns": 180, "is_buff": True, "buff_name": "Kyne's Aim"}, # Changed stat to skill
                "condition_for_buff": "Leave a suitable offering (item check or player choice).",
                "failure_condition_text": "You feel nothing, perhaps Kyne requires a token of respect."
            }
        },
        {
            "description": "A reclusive Bosmer alchemist, Elara Meadowlight, has a cleverly hidden treehouse dwelling. She's initially wary but might trade rare forest ingredients or offer a quest to retrieve a lost satchel of herbs from a nearby spider-infested cave.",
            "type": "npc_interaction_and_quest_lead",
            "details": {
                "npc_spawn_info": {"name": "Elara Meadowlight", "race": "bosmer", "role": "alchemist", "level": 7, "disposition": 50, "unique_id": "elara_meadowlight_ID"},
                "dialogue_lead": "'Who disturbs my solitude? Few find this place... unless you seek rare botanicals, or perhaps you can help an old woman?'",
                "quest_hint_template_id": "retrieve_lost_satchel_forest"
            }
        },
        {
            "description": "You find a patch of glowing blue Nirnroot by a moonlit stream, its characteristic chime filling the air, alongside some potent Nightshade and a cluster of Deathbell flowers. This area feels strangely tranquil.",
            "type": "item_and_flavor",
            "details": {
                "item_keys": ["nirnroot", "nightshade", "deathbell"], # Using base keys for simplicity, can make specific
                "quantity_range_nirnroot": (1, 2),
                "quantity_range_nightshade": (1, 1),
                "quantity_range_deathbell": (3, 5),
                "flavor_text": "The gentle chiming of the Nirnroot creates an unexpectedly peaceful atmosphere here."
            }
        },
        {
            "description": "You find a crudely scrawled note pinned to an ancient oak with a hunting knife: 'The Hagravens of [DynamicNearbyLandmark - e.g., Witchmist Grove] have taken my sister for their dark rituals! They demand a sacrifice or she dies! Reward offered by her brother, Jorn, in [NearestVillage].'",
            "type": "quest_lead_and_item",
            "details": {
                "item_key": "hunting_knife_with_note",
                "quest_hint_template_id": "rescue_sister_from_hagravens"
            }
        },
        {
            "description": "Ancient, moss-covered stones are arranged in a circle. Runes glow faintly with elemental energy. In the center, a pedestal has three indentations shaped like the claw of a bear, the feather of a hawk, and the scale of a mudcrab.",
            "type": "puzzle_hint_and_reward_potential",
            "details": {
                "hint_text": "The order of the symbols may be the key to activating the circle. Consider the natural order or dominance of these creatures, or perhaps an elemental affinity.",
                "potential_reward": "Access to a hidden grove with rare ingredients, a temporary elemental resistance blessing, or awakening a minor nature guardian.",
                "puzzle_solution_hint": "Requires specific items (Bear Claw, Hawk Feather, Mudcrab Chitin) placed in the correct sequence.",
                "related_tags": ["ancient_stone_circle", "elemental_puzzle", "nature_ritual"]
            }
        },
        {
            "description": "You stumble upon a poacher's camp, recently abandoned. A few pelts are improperly cured, and a poorly hidden snare trap is still active nearby.",
            "type": "item_and_skill_challenge",
            "details": {
                "item_keys": ["ruined_animal_pelt"], "quantity_range_ruined_animal_pelt": (2,5),
                "skill_challenge_disarm_trap": {"skill":"security", "dc":13, "success_desc":"You carefully disarm the snare, salvaging a usable Spring Wire.", "failure_desc":"You trigger the trap, taking minor (1d4) piercing damage!", "success_item_key":"spring_wire_trap"}
            }
        }
    ],
    "dwemer_ruin": [
        {
            "description": "The air hums with ancient, barely contained power. A massive Dwarven Centurion Master, its aetherium core glowing ominously, activates from its alcove, steam hissing from its joints! Its eyes lock onto you.",
            "type": "combat_encounter_boss",
            "details": {
                "enemy_spawn_info": [{"role": "dwarven_centurion", "race": "dwemer_construct_race", "level": 15, "count": 1}],
                "flavor_text": "The Centurion awakens, its metallic footsteps echoing through the ancient halls!",
                "special_ability_hint": "Its steam attacks are highly damaging, and it's resistant to normal weaponry. Seek its weak points or use powerful magic.",
                "loot_drop_hint": "Grand Soul Gem, Centurion Dynamo Core, several Dwarven Metal Ingots"
            }
        },
        {
            "description": "You find a complex Dwemer Astrolabe on a pedestal. Its interlocking rings are misaligned. Faint glyphs suggest it maps celestial bodies or perhaps controls a nearby mechanism.",
            "type": "puzzle_complex_and_reward_potential",
            "details": {
                "hint_text": "The rings seem to correspond to constellations or perhaps tonal frequencies. Aligning them correctly might require knowledge of Dwemer astronomy or a keen ear for resonance (Lore/Intelligence DC 16).",
                "potential_reward": "Access to a hidden vault with Dwemer artifacts, activates a nearby elevator to a new section, or deactivates local traps.",
                "failure_consequence": "Incorrect alignment might trigger a minor magical backlash (shock damage) or alert nearby constructs.",
                "related_tags": ["dwemer_astrolabe_puzzle", "celestial_mechanics", "tonal_architecture_hint", "hidden_chamber_access"]
            }
        },
        {
            "description": "A hidden pressure plate, almost invisible on the metallic floor, triggers a section of the wall to slide open with a grinding sound. Inside, a small alcove contains several gleaming Dwemer Gyros, a Soul Gem, and a faded schematic diagram.",
            "type": "item_and_trap_awareness",
            "details": {
                "item_keys": ["dwemer_gyro", "lesser_soul_gem", "dwemer_schematic"],
                "quantity_range_dwemer_gyro": (2, 4),
                "trap_awareness_hint": "Finding this might make you more aware of other hidden mechanisms in the ruin.",
                "related_tags": ["dwemer_cache_hidden", "pressure_plate_trap", "valuable_components"]
            }
        },
        {
            "description": "You find the final, rambling journal of a long-dead Mages Guild scholar, Sulla Trebatius. It details their descent into the ruin, their obsession with Dwemer 'tonal architecture,' their growing paranoia, and a chilling account of encountering 'the Silent Ones' (Falmer) before the ink trails off.",
            "type": "lore_reveal_and_warning",
            "details": {
                "information": "Sulla believed Dwemer ruins resonated with magical energies that could be harnessed with sonic manipulation. Their notes warn of the dangers of Falmer and the psychological effects of prolonged exposure to Dwemer machinations.",
                "related_tags": ["mages_guild_expedition_lost", "tonal_architecture_research", "dwemer_lore_scholar", "falmer_warning", "madness_inducing_ruin"],
                "item_key": "sulla_trebatius_journal"
            }
        },
        {
            "description": "A section of the corridor is blocked by a series of pulsing Dwemer pipes emitting scalding steam. A nearby lever seems rusted in place.",
            "type": "environmental_hazard_and_skill_challenge",
            "details": {
                "hazard_type": "dwemer_steam_trap",
                "effect_desc": "The steam is intensely hot. Passing through will cause significant fire damage.",
                "skill_challenge_repair_lever": {"skill":"strength", "dc":15, "success_desc":"With some effort, you manage to force the lever, and the steam subsides, revealing a path.", "failure_desc":"The lever breaks off! The steam continues to vent. You might need to find another way or endure the heat.", "damage_on_fail": {"min":5, "max":10}},
                "alternative_solution_hint": "A well-aimed frost spell might temporarily cool the pipes.",
                "related_tags": ["dwemer_trap_steam", "lever_puzzle_rusted", "elemental_hazard_fire"]
            }
        }
    ],
    "barrow": [
        {
            "description": "A chilling wind sweeps through the burial chamber as you disturb an ancient seal. Draugr Scourges, their eyes burning with cold fire, and Draugr Death Overlords, wielding enchanted ancient Nord weapons, rise from their sarcophagi!",
            "type": "combat_encounter_tough",
            "details": {
                "enemy_spawn_info": [{"role": "draugr_scourge", "race": "undead_nord", "level": 8, "count": 2}, {"role": "draugr_death_overlord", "race": "undead_nord", "level": 12, "count": 1}],
                "flavor_text": "The Draugr awaken, their chilling moans echoing through the tomb, hungry for the warmth of the living!",
                "special_ability_hint": "Draugr are resistant to frost but vulnerable to fire. Death Overlords can use Unrelenting Force shout.",
                "loot_drop_hint": "Enchanted Ancient Nord Weapons, Draugr Dust, valuable grave goods (jewelry, gold)"
            }
        },
        {
            "description": "Behind a loose stone in a sarcophagus of a noble warrior, you find a finely crafted Amulet of Stendarr, surprisingly well-preserved, alongside a handful of potent Bone Meal and a small offering of embalming oils.",
            "type": "item_and_lore_hint",
            "details": {
                "item_keys": ["amulet_of_stendarr", "bone_meal", "embalming_oil"],
                "quantity_range_bone_meal": (3, 5),
                "lore_hint": "The presence of Stendarr's amulet suggests this warrior may have been a protector against abominations in life.",
                "related_tags": ["nordic_burial_offering", "stendarr_amulet", "ancient_warrior_tomb"]
            }
        },
        {
            "description": "A series of Nordic burial urns line a shelf. Most are empty or contain only dust, but one, heavier than the others and sealed with intricate wax depicting a dragon, holds a small hoard of ancient Nord coins and a tarnished silver dragon head ring.",
            "type": "item_valuable_and_puzzle_minor",
            "details": {
                "item_keys": ["nord_coin_ancient", "silver_dragon_ring"],
                "quantity_range_nord_coin_ancient": (25, 50),
                "puzzle_hint_text": "The dragon seal might indicate a connection to the Dragon Cult or a family that revered dragons.",
                "related_tags": ["burial_urn_sealed", "ancient_treasure", "dragon_cult_symbolism_potential"]
            }
        },
        {
            "description": "A Dragon Priest's sarcophagus, intricately carved with draconic motifs and glowing with faint magical wards, dominates the central chamber. Before it is a pedestal with three strange, claw-shaped indentations and a riddle etched in ancient Nordic script.",
            "type": "puzzle_major_and_boss_potential",
            "details": {
                "hint_text": "The riddle speaks of 'three aspects of a dragon's might: breath, scale, and soul.' Finding items representing these and placing them in the correct order on the pedestal might unlock the sarcophagus... and awaken its powerful occupant.",
                "potential_reward": "A unique Dragon Priest mask, a powerful staff, or a scroll of immense power.",
                "boss_encounter_hint": "Awakening the Dragon Priest will result in a formidable battle.",
                "related_tags": ["dragon_priest_sarcophagus_sealed", "nordic_riddle_puzzle", "dragon_cult_artifact", "powerful_undead_guardian"]
            }
        },
        {
            "description": "You enter a chamber filled with draugr seemingly frozen mid-ritual around a central cairn. Disturbing anything might awaken them.",
            "type": "choice_encounter_stealth_or_combat",
            "details": {
                "enemy_spawn_info": [{"role": "draugr_ritualist", "race": "undead_nord", "level": 7, "count": 5}, {"role": "draugr_overseer", "race": "undead_nord", "level": 11, "count":1}],
                "flavor_text": "The air is heavy with ancient magic. The draugr are motionless, but their eyes seem to follow you.",
                "choice_options": ["Attempt to sneak through (Sneak DC 17)", "Loot the cairn directly (triggers combat)", "Try to disrupt the ritual from afar (Archery/Destruction DC 15 - might awaken only some)"],
                "loot_potential_cairn": "Ancient Nord weapon, Soul Gem, Gold.",
                "related_tags": ["draugr_ritual_interrupted", "tomb_puzzle_stealth", "ancient_magic_dormant"]
            }
        }
    ],
    "ashland_waste": [
        {
            "description": "The air is thick with choking ash reminiscent of Morrowind's desolation. You find a half-buried skeleton of a Dunmer traveler, its hand clutching a small, heat-resistant pouch containing a few Fire Salts and a charred map fragment.",
            "type": "item_and_quest_lead",
            "details": {
                "item_key": "fire_salts", "quantity_range_fire_salts": (1, 2),
                "item_key_2": "charred_map_fragment", "quantity_range_charred_map_fragment": (1,1),
                "quest_hint_template_id": "dunmer_ashland_secret",
                "related_tags": ["ashlands_border", "fire_salts_remains", "dunmer_ruin_skyrim_potential", "morrowind_refugee_lore"]
            }
        },
        {
            "description": "A wild Bull Netch, its gas-filled body drifting eerily through the ashfall, floats by, its tentacles trailing. They are usually docile unless provoked, but the ashy conditions make them irritable.",
            "type": "npc_encounter_neutral_or_hostile",
            "details": {
                "npc_spawn_info": {"role": "netch_bull", "race": "netch_creature", "level": 6, "disposition": 50, "unique_id": "bull_netch_event_ID"},
                "situation": "Potential source of Netch Leather and gas sac components if hunted carefully, but will defend itself fiercely.",
                "related_tags": ["netch_skyrim_variant", "ashlands_creature_dangerous", "alchemy_components_netch"],
                "choice_options": ["Attack", "Observe cautiously", "Attempt to sneak past (Sneak DC 14)"]
            }
        },
        {
            "description": "You discover a small, hidden shrine to Azura, built by Dunmer refugees, somehow preserved amidst the desolation. Praying here grants you a brief moment of clarity and magical fortitude against the harsh elements.",
            "type": "flavor_and_buff",
            "details": {
                "god_mention": "Azura",
                "lore_hint": "Azura's influence persists even in the most blighted lands, offering hope to her Dunmer followers who have fled Morrowind.",
                "minor_buff_debuff": {"stat": "fire_resist", "amount": 15, "duration_turns": 240, "is_buff": True, "buff_name": "Azura's Respite"},
                "related_tags": ["dunmer_shrine_azura", "refugee_faith", "environmental_protection_buff"]
            }
        },
        {
            "description": "A sudden tremor shakes the ashen ground, and a fissure opens nearby, venting noxious sulfurous gas and revealing a vein of raw ebony ore, dangerously close to unstable, heated rock.",
            "type": "environmental_hazard_and_item_opportunity",
            "details": {
                "hazard_type": "ashland_fissure_gas_vent_unstable",
                "effect_desc": "The sulfurous gas stings your eyes and lungs (Endurance DC 13 to avoid coughing fit, temporary speech penalty). The ground is treacherous.",
                "item_keys": ["ebony_ore"], "quantity_range_ebony_ore": (1, 2),
                "skill_check_to_mine": {"skill": "mining", "dc": 17, "success_desc": "Carefully, you manage to extract the ebony ore without triggering a further collapse.", "failure_desc": "The ground shifts! You manage to scramble back, but the ore vein is lost, and you take minor (1d4) bludgeoning damage."},
                "related_tags": ["volcanic_hazard_fissure", "ebony_ore_discovery", "mining_challenge_dangerous"]
            }
        }
    ],
    "volcanic_caldera": [
        {
            "description": "You find a rare Obsidian Shard, still warm from the geothermal heat, embedded in a rock. It pulses with a faint, fiery energy, perfect for potent fire enchantments.",
            "type": "item_rare_ingredient",
            "details": {
                "item_key": "obsidian_shard",
                "quantity_range_obsidian_shard": (1, 1),
                "lore_hint": "Obsidian from such active geothermal regions is highly prized by enchanters for its ability to hold powerful fire enchantments. Mages at the College of Winterhold might pay well for it.",
                "related_tags": ["obsidian_rare", "fire_enchanting_material", "geothermal_activity_byproduct"]
            }
        },
        {
            "description": "A mad Argonian pyromancer, his scales stained with ash, believing this caldera to be a gateway to the Deadlands, is attempting a dangerous ritual to summon a powerful Flame Atronach Monarch. He mistakes you for a rival or a sacrifice.",
            "type": "npc_interaction_hostile_boss_potential",
            "details": {
                "npc_spawn_info": {"name": "Ignatius", "race": "argonian", "role": "pyromancer", "level": 12, "disposition": 10, "unique_id": "ignatius_pyromancer_ID"},
                "dialogue_lead": "'More fuel for the Everlasting Flame! You will serve the Lord of Destruction, willingly or not!'",
                "combat_trigger_immediate": True,
                "potential_boss_spawn_info": {"role": "flame_atronach_monarch", "race": "atronach_creature", "level": 18, "count": 1},
                "related_tags": ["argonian_pyromancer_mad", "cultist_mehrunes_dagon", "flame_atronach_summoning", "ritual_interruption_opportunity"]
            }
        },
        {
            "description": "The ground is unstable here. A section of hardened lava crust crumbles beneath your feet, revealing a small lava tube leading downwards. It's incredibly hot, but might lead to valuable minerals or a hidden area.",
            "type": "location_discovery_hazard_and_opportunity",
            "details": {
                "location_name_hint": "Smoldering Lava Tube",
                "related_tags": ["volcanic_cave_lava_tube", "extreme_heat_hazard_constant", "underground_lava_flow", "rare_gem_vein_potential", "fire_elemental_lair_potential"],
                "mark_on_map_chance": 0.6,
                "hazard_continuous_damage_per_turn": {"min": 1, "max": 3}
            }
        },
        {
            "description": "Amidst the scorched rocks and sulfurous vents, you find a perfectly preserved Fire Fern, an extremely rare alchemical ingredient that thrives in intense heat. Its leaves glow with an inner fire.",
            "type": "item_rare_ingredient",
            "details": {
                "item_key": "fire_fern",
                "quantity_range_fire_fern": (1, 1),
                "lore_hint": "Fire Ferns are almost mythical, said to grant unparalleled resistance to flames or imbue potions with explosive power. Highly sought by master alchemists.",
                "related_tags": ["rare_alchemy_ingredient_fire", "volcanic_flora_unique", "master_alchemist_interest"]
            }
        }
    ],
    "thalmor_stronghold_or_embassy_area": [
        {
            "description": "You observe a Thalmor Justiciar berating an Imperial Legionnaire for 'insufficient diligence' in enforcing the White-Gold Concordat. The tension is palpable.",
            "type": "flavor_political_tension",
            "details": {
                "faction_interaction": ["thalmor", "imperial_legion"],
                "lore_hint": "The Thalmor's authority often clashes with local Imperial command, creating resentment.",
                "related_tags": ["thalmor_arrogance", "imperial_subservience_forced", "white_gold_concordat_enforcement", "political_friction"]
            }
        },
        {
            "description": "A nervous informant is seen slipping a note to a Thalmor agent in a secluded corner. Whatever information is changing hands, it likely bodes ill for someone.",
            "type": "lore_reveal_intrigue",
            "details": {
                "situation": "Thalmor intelligence gathering.",
                "potential_consequence": "This could lead to arrests or further Thalmor actions in the area.",
                "related_tags": ["thalmor_spy_network", "informant_betrayal", "secret_intelligence", "oppression_tactics"]
            }
        }
    ]
}


# --- Functions (from your provided code, enhanced to use new quest/NPC structures) ---

def explore_location(player, current_location, random_encounters, npc_registry, all_locations_list, ui): # random_encounters unused still
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

            num_results_to_show = min(random.randint(1, 2), len(unique_results_data))
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
            if not possible_events_for_location:
                ui.slow_print("The area seems quiet, with nothing specific of note occurring right now.")
            else:
                 ui.slow_print("You sense a potential occurrence, but it passes without incident this time.")
        return event
    except Exception as e:
        print(f"Error in trigger_random_event: {e}")
        traceback.print_exc()
        return None