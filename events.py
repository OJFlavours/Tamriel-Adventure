# events.py
import random
import traceback
from ui import UI
# Assuming Quest, generate_reward, generate_location_appropriate_quest are correctly in quests.py
from quests import Quest, generate_reward, generate_location_appropriate_quest
from items import Item, generate_item_from_key, generate_random_item
from locations import LOCATIONS # For DUNGEON_NAMES
# EXPLORATION_RESULTS would be in exploration_data.py, not directly used here but explore_location uses it
# from npc import generate_npc_from_tags # Conceptual import

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
if not DUNGEON_NAMES: # Fallback
    DUNGEON_NAMES = [
        "Bleak Falls Barrow", "Quicksilver Mine", "Nightcaller Temple", "Iron-Breaker Mine",
        "Saarthal", "Hob's Fall Cave", "Yngol Barrow", "Movarth's Lair", "Ustengrav",
        "Pinewatch", "Halldir's Cairn", "Cidhna Mine", "Druadach Redoubt", "Shroud Hearth Barrow",
        "Wolfskull Cave", "Lost Prospect Mine", "The Ratway", "Labyrinthian", "Dustman's Cairn",
        "Alftand", "Mzinchaleft", "Forelhost", "Silent Moons Camp", "Reachwind Eyrie", "Blind Cliff Cave"
    ]

# --- Define SPECIFIC_LOCATION_TAGS (from your provided code) ---
SPECIFIC_LOCATION_TAGS = [
    "tavern", "inn", "market", "mine", "camp", "cave", "ruin", "barrow", "dwemer",
    "keep", "meadhall", "blacksmith", "alchemy_shop", "temple", "college", "palace",
    "meadery", "brewery", "watchtower", "lighthouse", "wreck", "shop", "port",
    "government", "guild", "prison", "graveyard", "sanctuary", "monastery",
    "fort", "fortified", "city", "town", "village", "dragon_lair_ancient", # Adjusted dragon_lair tag
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
                "npc_tags": {"role": "merchant_dunmer_stranded", "name": "Drevis", "attitude": "distressed_resigned", "race": "dunmer"},
                "dialogue_lead": "'Stendarr's Mercy, can anyone assist a humble merchant? I have coin, and perhaps some rare goods from Morrowind for your trouble.'",
                "lead_description": "Dunmer merchant Drevis needs help fixing his cart or escorting him to the nearest settlement. He offers a reward for assistance.",
                "related_tags": ["merchant", "dunmer_refugee", "ash_yams", "roadside_assistance"],
                "quest_template_hint": "escort_merchant_or_repair_cart" # Hint for quest generation
            }
        },
        { # LORE ADJUSTED
            "description": "You find a hastily written, bloodstained note clutched in the hand of a dead Imperial courier. It speaks of rising tensions and a planned attack by 'Nord patriots' on a strategic bridge near [DynamicNearbyLandmark - e.g., Dragon Bridge].",
            "type": "quest_lead_and_item",
            "details": {
                "lead_description": "The courier's note warns of an impending attack by Nord dissidents on a bridge. This could be an opportunity to aid the Empire or warn the dissidents.",
                "related_tags": ["political_unrest", "nord_dissidents", "imperial_courier", "ambush_warning"],
                "item_keys": ["imperial_dispatch_sealed_bloodied"], # More specific item
                "moral_choice_hint": "Inform Imperials, warn dissidents, or use information for personal gain."
            }
        },
        {
            "description": "A group of stern-faced Vigilants of Stendarr are interrogating a frightened Khajiit traveler on the road. Their leader, a zealous Breton, eyes you suspiciously. 'Unless you bear witness to Daedric corruption, move along. Stendarr's light has no time for idle gawkers!'",
            "type": "npc_interaction_choice", # Added choice
            "details": {
                "npc_tags": {"role": "vigilant_of_stendarr_leader_zealous", "attitude": "suspicious_authoritative", "race":"breton"},
                "secondary_npc_tags": {"role": "traveler_khajiit_frightened", "race":"khajiit"},
                "dialogue_lead": "'State your purpose, or be on your way. We hunt abominations.'",
                "related_tags": ["vigilants_of_stendarr", "khajiit_traveler", "religious_zealots", "daedra_hunting"],
                "choice_options": ["Intervene (Speech DC 14)", "Observe quietly", "Offer aid to Vigilants", "Leave"]
            }
        },
        {
            "description": "A sudden, unnatural tremor shakes the ground violently! Loose rocks tumble from nearby cliffs, and the air fills with dust. You hear a faint, guttural roar from deep within the earth.",
            "type": "environmental_hazard_and_lore_hint",
            "details": {
                "hazard_type": "magical_earthquake_minor",
                "effect_desc": "The world shudders! You must keep your footing (Acrobatics DC 14) or risk minor injury (1d6 bludgeoning) from falling debris.",
                "lore_hint": "Such tremors are sometimes associated with ancient Dwemer machinery reactivating or the stirring of slumbering subterranean beasts.",
                "related_tags": ["earthquake", "dwemer_rumor", "monster_rumor", "skill_challenge_acrobatics"]
            }
        },
        { # NEW EVENT
            "description": "You encounter a Thalmor patrol on the road. Their Justiciar leader, with a chillingly polite demeanor, questions your travel and adherence to the White-Gold Concordat, specifically inquiring about any Talos worship.",
            "type": "npc_interaction_tense",
            "details": {
                "npc_tags": {"role":"thalmor_justiciar_interrogator", "attitude":"authoritative_condescending", "race":"altmer"},
                "secondary_npc_tags": {"role":"thalmor_soldier_escort", "count": 2, "race":"altmer"},
                "dialogue_lead": "'Citizen. We are ensuring compliance with the terms of the White-Gold Concordat. Have you witnessed any heresy regarding the false god Talos?'",
                "related_tags": ["thalmor_patrol", "white_gold_concordat", "talos_ban", "political_tension", "imperial_law"],
                "skill_challenge_speech_dc": 15, # DC to talk your way out without trouble
                "consequences_fail_speech": "Increased Thalmor suspicion, possible confiscation of 'heretical' items, or even attack if provoked."
            }
        },
        { # NEW EVENT
            "description": "A wandering scholar, hunched over a heavy tome, asks if you've seen any unusual ancient carvings or ruins nearby, unrelated to the Dwemer. They seem particularly interested in early Atmoran settlements.",
            "type": "npc_interaction_and_lore_reveal",
            "details": {
                "npc_tags": {"role":"scholar_traveling_historian", "name":"Historian Elmsworth", "attitude":"curious_academic", "race":"imperial"},
                "dialogue_lead": "'Pardon me, traveler. My research into pre-Nordic Skyrim leads me to believe this region holds many secrets. Have you encountered any particularly ancient, non-Dwemer stonework?'",
                "lore_hint": "The scholar shares a snippet about the complexity of Atmoran migrations and their early interactions with Skyrim's native creatures and elves.",
                "related_tags": ["scholar", "atmora_lore", "ancient_history", "ruin_research"],
                "quest_lead_potential": "Sharing information about a known ruin might lead to a small reward or further research tasks."
            }
        }
    ],
    "forest": [
        {
            "description": "The air grows cold, and you hear the snap of a twig. A Spriggan Matriarch, its form ancient and wreathed in glowing moss, materializes, its eyes burning with primal fury! It seems to be guarding a rare cluster of glowing mushrooms.",
            "type": "combat_encounter_or_choice", # Added choice
            "details": {
                "enemy_tags": [["spriggan_matriarch_guardian"]], # More specific tag
                "flavor_text": "The Spriggan raises its thorny arms, a low growl emanating from its woody form.",
                "special_ability_hint": "Spriggans are vulnerable to fire but can heal themselves and charm animals.",
                "loot_drop_hint": "Spriggan Sap, Taproot, rare glowing mushrooms",
                "choice_options": ["Attack", "Attempt to sneak past (Sneak DC 16)", "Offer a piece of meat/honey (Nature Lore DC 13 to know this might work)"]
            }
        },
        {
            "description": "You discover a hidden grove with a small, moss-covered shrine to Kyne, Goddess of the Storm and the Hunt. Offerings of hawk feathers and antlers lie before it. Praying here and leaving a small offering (e.g., a feather, a piece of meat) might grant Kyne's favor.",
            "type": "flavor_and_buff_conditional", # Added conditional
            "details": {
                "god_mention": "Kyne",
                "minor_buff_debuff": {"stat": "archery_skill_bonus", "amount": 5, "duration_turns": 180, "is_buff": True, "buff_name": "Kyne's Aim"},
                "condition_for_buff": "Leave a suitable offering (item check or player choice).",
                "failure_condition_text": "You feel nothing, perhaps Kyne requires a token of respect."
            }
        },
        {
            "description": "A reclusive Bosmer alchemist, Elara Meadowlight, has a cleverly hidden treehouse dwelling. She's initially wary but might trade rare forest ingredients or offer a quest to retrieve a lost satchel of herbs from a nearby spider-infested cave.",
            "type": "npc_interaction_and_quest_lead",
            "details": {
                "npc_tags": {"role": "alchemist_bosmer_reclusive_expert", "name": "Elara Meadowlight", "attitude": "wary_curious", "race": "bosmer"},
                "dialogue_lead": "'Who disturbs my solitude? Few find this place... unless you seek rare botanicals, or perhaps you can help an old woman?'",
                "lead_description": "Elara needs someone to retrieve her satchel of rare herbs from a dangerous cave. She offers a valuable potion recipe and some unique ingredients as payment.",
                "related_tags": ["alchemist", "bosmer", "rare_ingredients", "spider_cave", "potion_recipe"],
                "quest_template_hint": "retrieve_lost_satchel_forest"
            }
        },
        {
            "description": "You find a patch of glowing blue Nirnroot by a moonlit stream, its characteristic chime filling the air, alongside some potent Nightshade and a cluster of Deathbell flowers. This area feels strangely tranquil.",
            "type": "item_and_flavor", # Changed type
            "details": {
                "item_keys": ["nirnroot_glowing_prime", "nightshade_potent_cluster", "deathbell_flowers_fresh"], # More specific keys
                "quantity_range_nirnroot_glowing_prime": (1, 2),
                "quantity_range_nightshade_potent_cluster": (1, 1), # One cluster
                "quantity_range_deathbell_flowers_fresh": (3, 5),
                "flavor_text": "The gentle chiming of the Nirnroot creates an unexpectedly peaceful atmosphere here."
            }
        },
        {
            "description": "You find a crudely scrawled note pinned to an ancient oak with a hunting knife: 'The Hagravens of [DynamicNearbyLandmark - e.g., Witchmist Grove] have taken my sister for their dark rituals! They demand a sacrifice or she dies! Reward offered by her brother, Jorn, in [NearestVillage].'",
            "type": "quest_lead_and_item", # Changed type
            "details": {
                "lead_description": "A desperate plea to rescue a sister from Hagravens, or perhaps negotiate her release. Jorn awaits in [NearestVillage].",
                "related_tags": ["hagravens", "rescue_mission_urgent", "dark_rituals", "sacrifice_demand"],
                "item_keys": ["hunting_knife_note_attached"],
                "quest_template_hint": "rescue_sister_from_hagravens"
            }
        },
        {
            "description": "Ancient, moss-covered stones are arranged in a circle. Runes glow faintly with elemental energy. In the center, a pedestal has three indentations shaped like the claw of a bear, the feather of a hawk, and the scale of a mudcrab.",
            "type": "puzzle_hint_and_reward_potential", # Changed type
            "details": {
                "hint_text": "The order of the symbols may be the key to activating the circle. Consider the natural order or dominance of these creatures, or perhaps an elemental affinity.",
                "potential_reward": "Access to a hidden grove with rare ingredients, a temporary elemental resistance blessing, or awakening a minor nature guardian.",
                "puzzle_solution_hint": "Requires specific items (Bear Claw, Hawk Feather, Mudcrab Chitin) placed in the correct sequence.",
                "related_tags": ["ancient_stone_circle", "elemental_puzzle", "nature_ritual"]
            }
        },
        { # NEW EVENT
            "description": "You stumble upon a poacher's camp, recently abandoned. A few pelts are improperly cured, and a poorly hidden snare trap is still active nearby.",
            "type": "item_and_skill_challenge",
            "details": {
                "item_keys": ["ruined_pelt"], "quantity_range_ruined_pelt": (2,5),
                "skill_challenge_disarm_trap": {"skill":"security", "dc":13, "success_desc":"You carefully disarm the snare, salvaging a usable Spring Wire.", "failure_desc":"You trigger the trap, taking minor (1d4) piercing damage!", "success_item_key":"spring_wire_trap"},
                "lore_hint": "These poachers were clearly amateurs or in a hurry.",
                "related_tags": ["poacher_camp_abandoned", "trap_disarming", "survival"]
            }
        }
    ],
    "dwemer_ruin": [ # Events here should emphasize mystery, danger, and ancient technology
        {
            "description": "The air hums with ancient, barely contained power. A massive Dwarven Centurion Master, its aetherium core glowing ominously, activates from its alcove, steam hissing from its joints! Its eyes lock onto you.",
            "type": "combat_encounter_boss",
            "details": {
                "enemy_tags": [["dwarven_centurion_master_ancient"]],
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
                "potential_reward": "Reveals a hidden vault with Dwemer artifacts, activates a nearby elevator to a new section, or deactivates local traps.",
                "failure_consequence": "Incorrect alignment might trigger a minor magical backlash (shock damage) or alert nearby constructs.",
                "related_tags": ["dwemer_astrolabe_puzzle", "celestial_mechanics", "tonal_architecture_hint", "hidden_chamber_access"]
            }
        },
        {
            "description": "A hidden pressure plate, almost invisible on the metallic floor, triggers a section of the wall to slide open with a grinding sound. Inside, a small alcove contains several gleaming Dwemer Gyros, a Soul Gem, and a faded schematic diagram.",
            "type": "item_and_trap_awareness",
            "details": {
                "item_keys": ["dwemer_gyro_pristine", "soul_gem_lesser_filled", "schematic_diagram_dwemer_device"],
                "quantity_range_dwemer_gyro_pristine": (2, 4),
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
                "item_key_journal": "sulla_trebatius_journal_final"
            }
        },
        { # NEW EVENT
            "description": "A section of the corridor is blocked by a series of pulsing Dwemer pipes emitting scalding steam. A nearby lever seems rusted in place.",
            "type": "environmental_hazard_and_skill_challenge",
            "details": {
                "hazard_type": "dwemer_steam_trap",
                "effect_desc": "The steam is intensely hot. Passing through will cause significant fire damage.",
                "skill_challenge_repair_lever": {"skill":"mechanics_or_strength", "dc":15, "success_desc":"With some effort, you manage to force the lever, and the steam subsides, revealing a path.", "failure_desc":"The lever breaks off! The steam continues to vent. You might need to find another way or endure the heat."},
                "alternative_solution_hint": "A well-aimed frost spell might temporarily cool the pipes.",
                "related_tags": ["dwemer_trap_steam", "lever_puzzle_rusted", "elemental_hazard_fire"]
            }
        }
    ],
    "barrow": [ # Events here should focus on undead, ancient Nord traditions, and tomb raiding perils
        {
            "description": "A chilling wind sweeps through the burial chamber as you disturb an ancient seal. Draugr Scourges, their eyes burning with cold fire, and Draugr Death Overlords, wielding enchanted ancient Nord weapons, rise from their sarcophagi!",
            "type": "combat_encounter_tough",
            "details": {
                "enemy_tags": [["draugr_scourge_frost_aura", 2], ["draugr_death_overlord_enchanted_weapon", 1]], # Specific counts and types
                "flavor_text": "The Draugr awaken, their chilling moans echoing through the tomb, hungry for the warmth of the living!",
                "special_ability_hint": "Draugr are resistant to frost but vulnerable to fire. Death Overlords can use Unrelenting Force shout.",
                "loot_drop_hint": "Enchanted Ancient Nord Weapons, Draugr Dust, valuable grave goods (jewelry, gold)"
            }
        },
        {
            "description": "Behind a loose stone in a sarcophagus of a noble warrior, you find a finely crafted Amulet of Stendarr, surprisingly well-preserved, alongside a handful of potent Bone Meal and a small offering of embalming oils.",
            "type": "item_and_lore_hint",
            "details": {
                "item_keys": ["amulet_stendarr_well_preserved", "bone_meal_potent_ritual", "embalming_oil_ancient"],
                "quantity_range_bone_meal_potent_ritual": (3, 5),
                "lore_hint": "The presence of Stendarr's amulet suggests this warrior may have been a protector against abominations in life.",
                "related_tags": ["nordic_burial_offering", "stendarr_amulet", "ancient_warrior_tomb"]
            }
        },
        {
            "description": "A series of Nordic burial urns line a shelf. Most are empty or contain only dust, but one, heavier than the others and sealed with intricate wax depicting a dragon, holds a small hoard of ancient Nord coins and a tarnished silver dragon head ring.",
            "type": "item_valuable_and_puzzle_minor",
            "details": {
                "item_keys": ["nord_coin_ancient_hoard", "silver_dragon_ring_tarnished"],
                "quantity_range_nord_coin_ancient_hoard": (25, 50), # Increased quantity
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
        { # NEW EVENT
            "description": "You enter a chamber filled with draugr seemingly frozen mid-ritual around a central cairn. Disturbing anything might awaken them.",
            "type": "choice_encounter_stealth_or_combat",
            "details": {
                "enemy_tags": [["draugr_ritualist_dormant", 5], ["draugr_overseer_dormant",1]],
                "flavor_text": "The air is heavy with ancient magic. The draugr are motionless, but their eyes seem to follow you.",
                "choice_options": ["Attempt to sneak through (Sneak DC 17)", "Loot the cairn directly (triggers combat)", "Try to disrupt the ritual from afar (Archery/Magic DC 15 - might awaken only some)"],
                "loot_potential_cairn": "Ancient Nord weapon, Soul Gem, Gold.",
                "related_tags": ["draugr_ritual_interrupted", "tomb_puzzle_stealth", "ancient_magic_dormant"]
            }
        }
    ],
    "ashland_waste": [ # Adapted for Skyrim's border regions or unique volcanic areas like parts of Eastmarch
        {
            "description": "The air is thick with choking ash reminiscent of Morrowind's desolation. You find a half-buried skeleton of a Dunmer traveler, its hand clutching a small, heat-resistant pouch containing a few Fire Salts and a charred map fragment.",
            "type": "item_and_quest_lead",
            "details": {
                "item_keys": ["fire_salts_impure", "map_fragment_ashlands_charred_skyrim"],
                "quantity_range_fire_salts_impure": (1, 2),
                "lead_description": "The map fragment seems to point towards a hidden shrine or a forgotten Dunmer outpost within Skyrim's volcanic regions, possibly related to the exodus from Morrowind.",
                "related_tags": ["ashlands_border", "fire_salts_remains", "dunmer_ruin_skyrim_potential", "morrowind_refugee_lore"]
            }
        },
        {
            "description": "A wild Bull Netch, its gas-filled body drifting eerily through the ashfall, floats by, its tentacles trailing. They are usually docile unless provoked, but the ashy conditions make them irritable.",
            "type": "npc_encounter_neutral_or_hostile",
            "details": {
                "npc_tags": {"role": "creature_netch_bull_ash_irritated", "attitude": "neutral_territorial_becomes_hostile_if_close"},
                "situation": "Potential source of Netch Leather and gas sac components if hunted carefully, but will defend itself fiercely.",
                "related_tags": ["netch_skyrim_variant", "ashlands_creature_dangerous", "alchemy_components_netch"]
            }
        },
        {
            "description": "You discover a small, hidden shrine to Azura, built by Dunmer refugees, somehow preserved amidst the desolation. Praying here grants you a brief moment of clarity and magical fortitude against the harsh elements.",
            "type": "flavor_and_buff",
            "details": {
                "god_mention": "Azura",
                "lore_hint": "Azura's influence persists even in the most blighted lands, offering hope to her Dunmer followers who have fled Morrowind.",
                "minor_buff_debuff": {"stat": "resistance_ash_environment", "amount": 0.15, "duration_turns": 240, "is_buff": True, "buff_name": "Azura's Respite"}, # More specific buff
                "related_tags": ["dunmer_shrine_azura", "refugee_faith", "environmental_protection_buff"]
            }
        },
        {
            "description": "A sudden tremor shakes the ashen ground, and a fissure opens nearby, venting noxious sulfurous gas and revealing a vein of raw ebony ore, dangerously close to unstable, heated rock.",
            "type": "environmental_hazard_and_item_opportunity",
            "details": {
                "hazard_type": "ashland_fissure_gas_vent_unstable",
                "effect_desc": "The sulfurous gas stings your eyes and lungs (Endurance DC 13 to avoid coughing fit, temporary speech penalty). The ground is treacherous.",
                "item_keys": ["ebony_ore_raw_volcanic"],
                "quantity_range_ebony_ore_raw_volcanic": (1, 2),
                "skill_check_to_mine": {"skill": "mining_or_survival", "dc": 17, "success_desc": "Carefully, you manage to extract the ebony ore without triggering a further collapse.", "failure_desc": "The ground shifts! You manage to scramble back, but the ore vein is lost, and you take minor (1d4) bludgeoning damage."},
                "related_tags": ["volcanic_hazard_fissure", "ebony_ore_discovery", "mining_challenge_dangerous"]
            }
        }
    ],
    "volcanic_caldera": [ # Specifically for Eastmarch hot springs and volcanic areas
        {
            "description": "You find a rare Obsidian Shard, still warm from the geothermal heat, embedded in a rock. It pulses with a faint, fiery energy, perfect for potent fire enchantments.",
            "type": "item_and_lore_hint",
            "details": {
                "item_key": "obsidian_shard_volcanic_pulsing",
                "lore_hint": "Obsidian from such active geothermal regions is highly prized by enchanters for its ability to hold powerful fire enchantments. Mages at the College of Winterhold might pay well for it.",
                "related_tags": ["obsidian_rare", "fire_enchanting_material", "geothermal_activity_byproduct"]
            }
        },
        {
            "description": "A mad Argonian pyromancer, his scales stained with ash, believing this caldera to be a gateway to the Deadlands, is attempting a dangerous ritual to summon a powerful Flame Atronach Monarch. He mistakes you for a rival or a sacrifice.",
            "type": "npc_interaction_hostile_boss_potential",
            "details": {
                "npc_tags": {"role": "mage_pyromancer_cultist_argonian_deranged", "attitude": "hostile_fanatical_delusional", "race": "argonian"},
                "dialogue_lead": "'More fuel for the Everlasting Flame! You will serve the Lord of Destruction, willingly or not!'",
                "combat_trigger_immediate": True,
                "potential_boss_summon": "flame_atronach_monarch_ritualistic", # If ritual completes
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
                "hazard_continuous_damage": "Minor fire damage per turn while inside unless fire resistance is high."
            }
        },
        {
            "description": "Amidst the scorched rocks and sulfurous vents, you find a perfectly preserved Fire Fern, an extremely rare alchemical ingredient that thrives in intense heat. Its leaves glow with an inner fire.",
            "type": "item_rare_ingredient",
            "details": {
                "item_key": "fire_fern_pristine_glowing",
                "quantity_range": (1, 1),
                "lore_hint": "Fire Ferns are almost mythical, said to grant unparalleled resistance to flames or imbue potions with explosive power. Highly sought by master alchemists.",
                "related_tags": ["rare_alchemy_ingredient_fire", "volcanic_flora_unique", "master_alchemist_interest"]
            }
        }
    ],
    # NEW CATEGORY: THALMOR_ENCOUNTER (can occur in Imperial controlled/influenced areas)
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


# --- Functions (from your provided code, ensure they are compatible with updated RANDOM_EVENTS) ---

def explore_location(player, current_location, random_encounters, npc_registry, all_locations_list, ui): # random_encounters seems unused here
    """Explores the current location and triggers random events based on its tags."""
    try:
        ui.slow_print(f"You carefully explore {current_location['name']}...")

        current_location_tags = current_location.get("tags", [])
        present_specific_tags = [tag for tag in current_location_tags if tag in SPECIFIC_LOCATION_TAGS]
        available_results_data = []

        # Prioritize results from specific tags of the current location
        if present_specific_tags:
            for tag in present_specific_tags:
                if tag in EXPLORATION_RESULTS: # EXPLORATION_RESULTS is in exploration_data.py
                    available_results_data.extend(EXPLORATION_RESULTS[tag])
        
        # Add results from more general tags if present
        general_tags_to_check = [tag for tag in current_location_tags if tag not in present_specific_tags and tag in EXPLORATION_RESULTS]
        if general_tags_to_check:
            for tag in general_tags_to_check:
                 available_results_data.extend(EXPLORATION_RESULTS[tag])

        # Broad fallback if still no specific results
        if not available_results_data:
            broad_fallback_categories = { # Map broad categories to specific tags in EXPLORATION_RESULTS
                "wilderness": ["forest", "plains", "mountain"], # Example mapping
                "urban_area": ["city", "town"],
                "ruin_general": ["ruin", "dwemer_ruin", "barrow"],
                "cave_general": ["cave"],
                "hold_generic": ["hold"] # Generic hold tag, unlikely to have direct exploration results
            }
            for broad_cat, specific_cats in broad_fallback_categories.items():
                if broad_cat in current_location_tags:
                    for specific_fallback_tag in specific_cats:
                        if specific_fallback_tag in EXPLORATION_RESULTS:
                            available_results_data.extend(EXPLORATION_RESULTS[specific_fallback_tag])
                            if available_results_data: break # Found some, move on
                    if available_results_data: break


        selected_exploration_outcomes = []
        if available_results_data:
            unique_descriptions = set()
            unique_results_data = []
            for d in available_results_data: # Deduplicate based on description
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
                    
                    # This section needs robust implementation in your game engine (game.py)
                    # The placeholder comments like "Conceptual: game_engine.initiate_combat"
                    # from your original file highlight this.
                    # For now, I'm keeping the structure as you had it.
                    if effect_type == "item_find":
                        # ... (item finding logic from your file) ...
                        # Example:
                        if "gold_amount_range" in details:
                            gold = random.randint(details["gold_amount_range"][0], details["gold_amount_range"][1])
                            player.stats.gold += gold
                            ui.slow_print(f"You found {gold} septims!")
                        item_keys = details.get("item_keys", [])
                        if "item_key" in details and details["item_key"] not in item_keys: item_keys.append(details["item_key"])
                        for item_k in item_keys:
                            # ... (generate and add item logic) ...
                            pass # Placeholder for brevity

                    elif effect_type == "quest_lead" or effect_type == "quest_lead_and_item":
                        # ... (quest lead logic from your file) ...
                        ui.slow_print(f"[Quest Lead]: {details.get('lead_description', 'Something piques your interest.')}")
                        if hasattr(player, 'quest_log'):
                            # This would ideally use generate_location_appropriate_quest from quests.py
                            # For now, basic object creation
                            new_quest = Quest(
                                title=details.get("quest_title_hint", "Mysterious Find"),
                                description=details.get('lead_description'),
                                reward=generate_reward(player.level, details.get('related_tags', [])),
                                level_requirement=player.level,
                                location=current_location,
                                objectives=[{"type":"investigate", "details":details.get('lead_description')}], # Simplified objective
                                turn_in_npc_id=None # Needs to be determined by game logic
                            )
                            player.quest_log.add_quest(new_quest)
                            ui.slow_print(f"New quest added: {new_quest.title}")


                    elif effect_type == "location_discovery_hint":
                        # ... (location discovery logic from your file) ...
                        pass # Placeholder

                    elif effect_type == "skill_challenge":
                        # ... (skill challenge logic from your file) ...
                        pass # Placeholder
                    
                    # ... (other effect types from your file) ...

        else:
            ui.slow_print("You find nothing particularly noteworthy, though the unique atmosphere of the place certainly leaves an impression.")
        ui.press_enter()
    except Exception as e:
        print(f"Error in explore_location: {e}") # Make sure to use `ui.print_error` or similar if you have it
        traceback.print_exc()


def trigger_random_event(location_tags, player, ui, current_location):
    """Triggers a random event based on location tags, with more comprehensive tag use."""
    event = None
    try:
        possible_events_for_location = []
        
        # Check for events specific to the location's tags
        for tag in location_tags:
            if tag in RANDOM_EVENTS: # RANDOM_EVENTS is defined in this file
                possible_events_for_location.extend(RANDOM_EVENTS[tag])
        
        # Add generic travel events if no specific ones found or with a certain chance
        if not possible_events_for_location or random.random() < 0.25: 
            possible_events_for_location.extend(RANDOM_EVENTS.get("generic_travel", []))

        if possible_events_for_location:
            # Deduplicate events by description
            unique_descriptions = set()
            unique_events = []
            for d_event in possible_events_for_location:
                if d_event["description"] not in unique_descriptions:
                    unique_descriptions.add(d_event["description"])
                    unique_events.append(d_event)
            possible_events_for_location = unique_events

        if possible_events_for_location and random.random() < 0.8: # 80% chance to trigger an event if possibles exist
            event = random.choice(possible_events_for_location)
            ui.slow_print(f"\n{event['description']}") 

            event_type = event.get("type")
            details = event.get("details", {})
            
            # --- Placeholder for Game Engine Calls for Random Event Effects ---
            # This section requires robust implementation in your main game logic (game.py)
            # to handle combat, NPC spawning, item granting, quest starting, etc.
            # The following are conceptual based on your original file's structure.

            if event_type in ["item", "item_and_quest_lead", "quest_lead_and_item", "item_and_skill_challenge"]:
                # ... (your item granting logic here) ...
                # Example:
                item_keys = details.get("item_keys", [])
                if "item_key" in details and details["item_key"] not in item_keys: item_keys.append(details["item_key"])
                for item_k in item_keys:
                    # ... (generate and add item to player inventory) ...
                    pass
                if "lead_description" in details and hasattr(player, 'quest_log'):
                     # ... (logic to create and add a quest to player.quest_log) ...
                     # This should ideally use generate_location_appropriate_quest from quests.py
                     pass

            elif event_type in ["combat_encounter", "combat_encounter_ambush", "npc_interaction_hostile"]:
                ui.slow_print(details.get("flavor_text", "Danger approaches!"))
                # Conceptual: game.initiate_combat(player, details) # Pass details to handle enemy generation
                # For now:
                if "enemy_tags" in details:
                    ui.slow_print(f"Prepare to fight: {details['enemy_tags']}")


            elif event_type in ["npc_interaction", "npc_interaction_and_quest_lead"]:
                # Conceptual: game.spawn_npc_for_event(details) and game.initiate_dialogue(player, spawned_npc)
                ui.slow_print(f"You encounter {details.get('npc_tags', {}).get('name', 'someone interesting')}.")

            elif event_type == "skill_challenge":
                # Conceptual: game.resolve_skill_challenge(player, details)
                ui.slow_print("A challenge of skill presents itself!")

            elif event_type == "environmental_hazard":
                # Conceptual: game.apply_environmental_hazard(player, details)
                ui.slow_print(details.get("effect_desc", "The environment itself seems hostile!"))
            
            # ... (other event types from your file) ...

        else: 
            if not possible_events_for_location: 
                ui.slow_print("The area seems quiet, with nothing specific of note occurring right now.")
            else:
                 ui.slow_print("You sense a potential occurrence, but it passes without incident this time.")
        return event # Return the triggered event object or None
    except Exception as e:
        print(f"Error in trigger_random_event: {e}") # Use ui.print_error if available
        traceback.print_exc()
        return None