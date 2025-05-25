# exploration_data.py

# Structure for each entry:
# {
#     "description": "Flavor text of what the player sees/finds.",
#     "effect": {
#         "type": "effect_category", # e.g., "item_find", "quest_lead", "location_discovery_hint", "skill_challenge", "lore_reveal", "npc_encounter_hint", "minor_buff_debuff", "combat_encounter"
#         "details": { ... specific details for the effect type ... }
#     } (optional, some results might be pure flavor)
# }

EXPLORATION_RESULTS = {
    "city": [
        {
            "description": "Amidst the city's clamor, you spot a discarded coin purse half-hidden under a market stall. It jingles promisingly.",
            "effect": {"type": "item_find", "details": {"gold_amount_range": (25, 75)}}
        },
        {
            "description": "You overhear two city guards discussing increased bandit activity on the road to a nearby village (e.g., Riverwood if in Whiterun). They mention the Jarl's steward is offering a reward for thinning their numbers.",
            "effect": {"type": "quest_lead", "details": {"quest_title_hint": "Bandit Menace on the [RoadName] Road", "lead_description": "Bandit activity reported by guards on a specific road. A bounty might be available from the Jarl's steward in the city.", "related_tags": ["bandit_threat", "road_safety", "government_bounty", "city_steward_contact"], "quest_type_hint": "bounty_clear_bandits", "urgency": "medium", "dynamic_landmark_needed_road": True}}
        },
        {
            "description": "A street urchin, with eyes too old for their face, offers to show you a 'secret way' into the city's old cistern for 10 septims, hinting it connects to the Thieves Guild.",
            "effect": {"type": "skill_challenge_or_choice", "details": {"choice_text": "Pay the urchin (10 gold) for the cistern entrance, try to intimidate them (Speech DC 13), or pickpocket the urchin for any map they might have (Pickpocket DC 15)?", "skill_speech_intimidate": "speech", "dc_speech_intimidate": 13, "skill_pickpocket": "pickpocket", "dc_pickpocket": 15, "cost_if_pay": 10, "success_reward": {"location_discovery_hint": {"location_name_hint": "Old City Cistern - [CityName]", "related_tags":["sewers", "hidden_area", "city_underbelly", "thieves_guild_entrance_hint"], "mark_on_map_chance":0.8}, "lore_reveal": "The city has an extensive, forgotten understructure, often used by those wishing to avoid prying eyes."}, "failure_desc": "The urchin scoffs, 'No coin, no secrets, outlander!' and darts away, or you fail to get anything useful."}}
        },
        {
            "description": "You find a crumpled but official-looking notice: 'Mercenaries and able-bodied adventurers needed! The Penitus Oculatus seeks individuals for a discreet operation concerning a security breach. Inquire with Captain Aldis at Castle Dour (if in Solitude) or the city barracks.'",
            "effect": {"type": "quest_lead", "details": {"quest_title_hint": "A Discreet Operation for the Emperor", "lead_description": "The Penitus Oculatus (Emperor's agents) are recruiting for a secret mission. High risk, high reward, likely involving espionage or eliminating a threat.", "related_tags": ["mercenary_work_secret", "penitus_oculatus", "imperial_intelligence", "espionage_intrigue", "security_breach"], "quest_type_hint": "infiltration_or_assassination_discreet", "urgency": "high", "faction_mention": "Penitus Oculatus"}}
        },
        {
            "description": "In a quiet temple garden dedicated to Dibella, Goddess of Beauty and Love, you find a dropped Silver Ruby Ring. It seems to have been left by a forgetful noble.",
            "effect": {"type": "item_find", "details": {"item_key": "silver_ruby_ring"}}
        },
        {
            "description": "While browsing a dusty bookstall, a loose page from 'The Rear Guard' describes legends of a hidden smuggling tunnel beneath the city's docks, used during the Great War to move supplies.",
            "effect": {"type": "location_discovery_hint", "details": {"location_name_hint": "Great War Smuggling Tunnel - [CityName] Docks", "related_tags": ["smuggling_tunnel", "hidden_history", "city_docks_secret", "great_war_lore"], "mark_on_map_chance": 0.6, "lore_reveal": "The city's docks hide centuries of illicit dealings and secret passages, some with historical significance."}}
        },
        {
            "description": "You notice a member of the local Thieves Guild subtly marking a wealthy merchant's house with a 'Loot' shadowmark. An opportunity for the light-fingered, a chance to warn the occupant, or perhaps a way to set a trap for the thief?",
            "effect": {"type": "moral_choice_event", "details": {"choice_text": "Note the 'Loot' shadowmark (Perception DC 12 to understand its meaning & remember house), warn the merchant (Speech DC 14 to be believed & gain favor), or inform the city guard (risk angering the Guild but gain city rep)?", "lore_topic": "Thieves_Guild_Shadowmarks_Loot", "faction_interaction_lead": {"faction_tags":["Thieves Guild", "city_guard", "wealthy_merchant_target"]}, "success_warn_reward":{"reputation_change":{"faction":"city_guard", "amount":5}}, "success_inform_reward":{"reputation_change":{"faction":"city_guard", "amount":10}, "potential_conflict":"Thieves Guild"}}}
        },
        {
            "description": "A heated argument erupts at a stall between a Dunmer refugee from Morrowind and a Nord citizen over the price of ash yams. The tension of cultural differences and recent hardships is palpable.",
            "effect": {"type": "flavor", "details": {"atmosphere_effect": "social_tension_cultural_economic", "faction_mention": ["dunmer_refugee_morrowind", "nord_local_citizen", "economic_hardship"]}}
        }
    ],
    "tavern": [
        {
            "description": "The innkeeper, a jovial Redguard named Nazir, mentions a group of treasure hunters who passed through, bragging about a map to 'Redoran's Retreat' but lost a piece of it during a brawl. 'Might still be swept in a corner,' he chuckles.",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_key_to_find": "map_fragment_redorans_retreat", "skill_check_to_find": {"skill":"perception", "dc":15}, "success_desc": "Tucked away in a dusty corner, you find a torn piece of a map!", "failure_desc":"Despite searching, the fragment eludes you.", "lead_description": "This map fragment clearly shows part of a dungeon. Finding the other pieces or the treasure hunters could lead to Redoran's Retreat.", "related_tags":["treasure_map_fragment", "dungeon_nordic_ruin", "treasure_hunters_rivals"], "quest_title_hint":"The Lost Map to Redoran's Retreat"}}
        },
        {
            "description": "You overhear a group of Companions, their Skyforge steel gleaming, discussing a contract to clear out a den of Ice Wraiths from a cave near [DynamicNearbyLandmark - e.g., Pilgrim's Trench]. They seem to be looking for an extra hand.",
            "effect": {"type": "quest_lead", "details": {"lead_description": "The Companions are taking a contract on Ice Wraiths. You could offer to join them for a share of the reward.", "related_tags": ["companions_guild_contract", "ice_wraith_hunt", "cave_glacial_danger"], "npc_interaction_hint": "companions_warriors_jorrvaskr", "dynamic_landmark_needed": True, "quest_type_hint":"join_guild_mission_hunt", "potential_reward": "share_of_companions_reward_and_favor"}}
        },
        {
            "description": "A notice on the common room wall, stained with mead: 'Dangerous Necromancer, Malyn Varen, defiling graves near [NearbyBarrowName]! Disturbing the ancient dead! Reward offered by the Temple of Arkay!'",
            "effect": {"type": "quest_lead", "details": {"lead_description": "A necromancer is causing trouble in a nearby barrow. The Temple of Arkay is offering a bounty to stop him.", "related_tags": ["bounty_necromancer_grave_defiling", "barrow_undead_threat", "temple_of_arkay_task"], "quest_type_hint": "hunt_mage_evil_necromancer", "target_barrow_name_dynamic": True, "target_npc_name":"Malyn Varen" }}
        },
        {
            "description": "Tucked under a loose floorboard near the bar, you find a small, worn leather pouch containing a few vials of Sleeping Tree Sap and a coded note about a clandestine meeting of 'devotees'.",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_keys": ["sleeping_tree_sap_vial"], "quantity_range_sleeping_tree_sap_vial":(1,2), "lead_description": "The note mentions a secret meeting of Sleeping Tree Sap users near a giant's camp. This could be dangerous or enlightening.", "related_tags":["sleeping_tree_cult_hint", "drug_use_secret_meeting", "giant_camp_proximity_danger"], "item_found_note_key":"sleeping_tree_cult_note"}}
        },
        {
            "description": "A traveling bard sings a chilling tale of 'The Gauldur Amulet', a powerful artifact split into three fragments, each guarded by one of the Gauldurson brothers in their ancient tombs across Skyrim.",
            "effect": {"type": "location_discovery_hint_multiple", "details": {"location_name_hints": ["Folgunthur - Gauldurson Tomb", "Saarthal - Jyrik Gauldurson's Tomb", "Geirmund's Hall - Sigdis Gauldurson's Tomb"], "related_tags": ["legendary_artifact_gauldur_amulet", "nordic_tomb_brothers_guardian", "multi_part_quest_hint"], "mark_on_map_chance": 0.6, "lore_reveal": "The Gauldur Amulet is a legendary artifact of immense power, but its fragments are well protected by the vengeful spirits of its creators."}}
        },
        {
            "description": "After a few tankards of Black-Briar Mead, a Nord patron, looking for trouble, challenges you to a brawl. 'Think you're tough enough, eh? Let's see it! Winner gets 100 septims!'",
            "effect": {"type": "skill_challenge_or_combat", "details": {"game_type": "tavern_brawl_nord", "wager_amount": 100, "skill_unarmed_or_onehanded_no_weapon": "strength", "dc": 14, "success_desc": "You best the Nord in a fair (or not-so-fair) brawl! You win the wager and some local renown.", "failure_desc": "The Nord's fists are like hammers! You're knocked down, bruised, and lighter in the purse.", "failure_penalty": {"status_effect": {"type":"bruised_and_battered", "potency":-5, "duration_turns":60, "affected_stats":["agility", "strength"]}}, "combat_if_escalated_tags":[["nord_brawler_angry"]]}}
        },
        {
            "description": "You find a 'Lost and Found' notice: 'Lost: One Dwarven Cog, essential for my research! Generous reward for its return. - Calcelmo of Markarth.'",
            "effect": {"type": "quest_lead", "details": {"lead_description": "Calcelmo, the Dwemer scholar in Markarth, has lost a Dwarven Cog. He'll likely pay well for its return.", "related_tags": ["fetch_quest_dwemer_part", "scholar_research_markarth", "calcelmo_npc_contact"], "quest_type_hint": "fetch_item_specific", "item_target": "dwemer_cog_calcelmo"}}
        },
        {
            "description": "The innkeeper quietly warns you that a member of the Dark Brotherhood was seen asking about 'new contracts' in town. 'Best watch your back, traveler. And don't sleep too soundly.'",
            "effect": {"type": "lore_reveal", "details": {"lore_topic": "Dark_Brotherhood_Activity_Rumor", "information": "The Dark Brotherhood is always looking for new recruits or targets. Their presence often means someone is about to have a very bad day.", "faction_mention": "Dark_Brotherhood_Assassins", "atmosphere_effect":"ominous_warning"}}
        }
    ],
    "forest": [
        {
            "description": "You follow a barely visible animal trail to a secluded grotto where a Spriggan Earth Mother is performing a ritual over a bed of glowing mushrooms. She turns her ancient eyes towards you.",
            "effect": {"type": "npc_encounter_choice", "details": {"npc_tags": {"role":"spriggan_earth_mother_powerful", "attitude":"neutral_territorial_ancient"}, "situation": "Spriggan Earth Mother in a ritual. Options: Retreat silently (Sneak DC 15), attempt to communicate (Nature Lore or Speech DC 17), or attack (very dangerous).", "choice_options": ["retreat_silently", "attempt_communication", "attack_spriggan_mother"], "success_communicate_reward":{"lore_reveal":"The Spriggan imparts a cryptic piece of forest wisdom or a blessing of Kynareth."}}}
        },
        {
            "description": "In a sun-dappled clearing, you find a patch of rare Crimson Nirnroot, its glow more intense than its common cousin, alongside some potent Chokeberry vines.",
            "effect": {"type": "item_find", "details": {"item_keys": ["crimson_nirnroot_rare", "chokeberry_vine_poisonous"], "quantity_range_crimson_nirnroot_rare": (1, 2), "quantity_range_chokeberry_vine_poisonous":(1,3), "lore_hint":"Crimson Nirnroot is exceptionally rare and sought after for powerful alchemical concoctions."}}
        },
        {
            "description": "You stumble upon a poacher's trap that has ensnared a young elk. A note nearby details the poacher's plan to sell the prized antlers to a shady merchant in Riften.",
            "effect": {"type": "moral_choice_and_quest_lead", "details": {"choice_text": "Free the elk (Animal Handling DC 13), harvest it yourself, or use the note to track down the poacher/merchant?", "lead_description": "The note provides a lead on poachers and their illicit trade network connected to Riften.", "related_tags": ["poaching_network_riften", "animal_rescue_choice", "forest_crime_evidence"], "quest_type_hint": "confront_poachers_or_expose_merchant", "item_found_note_key": "poachers_elk_antler_deal_note", "success_free_reward":{"minor_buff_debuff":{"stat":"karma_nature_good", "amount":2}}}}
        },
        {
            "description": "An ancient, moss-covered chest is cleverly hidden within a hollow, lightning-struck oak. It's sealed with a complex puzzle lock depicting forest animals.",
            "effect": {"type": "skill_challenge_and_puzzle", "details": {"skill_primary": "lockpicking", "dc_primary": 17, "skill_secondary_puzzle":"lore_nature_or_intelligence", "dc_secondary_puzzle":15, "target_description": "hollow oak puzzle chest", "puzzle_hint_text": "The animals must be pressed in order of their place in the forest's food chain, from smallest prey to largest predator.", "success_reward": {"item_category": "amulet_enchanted_nature_themed", "gold_amount_range": (70,200), "item_key": "potion_of_fortify_sneak_superior"}, "failure_desc": "The lock resists your attempts, and a faint magical ward tingles your fingers."}}
        },
        {
            "description": "You discover a small, serene pond where wisps of light dance above the water. The water is impossibly clear. Drinking from it, you feel your magical energies surge and your mind clear.",
            "effect": {"type": "interaction_point_and_buff", "details": {"interaction_name": "Wisp-Mother's Tears Pond", "action_text": "Drink from the pond?", "effect_if_drink": {"type": "minor_buff_debuff_multiple", "details": [{"stat":"max_magicka", "amount":30, "duration_turns":600, "is_buff":True, "buff_name":"Wisp's Insight"}, {"stat":"magicka_regen_rate", "amount":0.2, "duration_turns":600, "is_buff":True}]}}}
        }
    ],
    "plains": [
        {
            "description": "You spot a distant, solitary watchtower ruin atop a windswept hill. It looks like an ideal bandit lookout or a forgotten Imperial outpost.",
            "effect": {"type": "location_discovery_hint", "details": {"location_name_hint": "Lone Sentinel Spire", "related_tags": ["ruin_watchtower_isolated", "ancient_imperial_or_bandit_lookout", "elevated_view_plains_strategic"], "mark_on_map_chance": 0.7}}
        },
        {
            "description": "While crossing a field of tall grass, your foot strikes something hard. Digging, you unearth a small, buried strongbox containing several flawless gems and a silver ingot.",
            "effect": {"type": "item_find", "details": {"item_keys": ["gem_flawless_diamond", "gem_flawless_ruby", "silver_ingot_pure"], "quantity_range_gem_flawless_diamond": (1, 1), "quantity_range_gem_flawless_ruby": (1,2)}}
        },
        {
            "description": "You encounter a travelling Khajiit merchant, Ma'dran, part of a larger caravan. He mentions a rare 'Star-Sung Grass' that only grows on these plains under the light of both moons, said to grant visions.",
            "effect": {"type": "quest_lead", "details": {"lead_description": "A rare visionary herb, Star-Sung Grass, might be found here under specific celestial conditions. Ma'dran would pay handsomely for samples.", "related_tags": ["alchemy_rare_ingredient_visionary", "celestial_event_plains_moons", "khajiit_lore_herbalism"], "npc_interaction_hint": "khajiit_caravan_merchant_madran", "item_target": "star_sung_grass_sample"}}
        },
        {
            "description": "A sudden gust of wind whips across the plains, revealing an old, discarded Orcish shield with a clan emblem you don't recognize. It's heavy and battle-scarred.",
            "effect": {"type": "item_find", "details": {"item_key": "shield_orcish_clan_unknown"}}
        },
        {
            "description": "You come across a circle of massive Mammoth bones, arranged deliberately around a central, fire-scorched stone altar. A faint drumming seems to echo on the wind. Local Nords and giants consider these powerful spiritual sites.",
            "effect": {"type": "lore_reveal_and_interaction", "details": {"lore_topic": "Nordic_Giant_Spirit_Communion_Sites", "information": "These bone circles are sacred. Leaving an offering of mead or a mammoth tusk might appease the spirits or grant a minor boon.", "interaction_name":"Mammoth Spirit Altar", "offering_options":["mead_honningbrew", "mammoth_tusk_small"], "effect_if_offering":{"type":"minor_buff_debuff", "details":{"stat":"strength", "amount":5, "duration_turns":300, "is_buff":True, "buff_name":"Spirit of the Mammoth" }}}}
        },
        {
            "description": "A pride of sabre cats, their forms sleek and powerful, are stalking a lone elk in the tall grass. You could intervene or observe.",
            "effect": {"type": "dynamic_encounter_choice", "details": {"situation_description":"Sabre cats hunting elk.", "choice_options":["intervene_help_elk", "intervene_help_sabre_cats_for_pelts", "observe_nature"], "combat_if_intervene_tags_sabre_cats":[["sabre_cat_plains_alpha"],["sabre_cat_plains"]], "reward_if_help_elk":"karma_good_nature", "reward_if_help_sabre_cats":{"item_key":"sabre_cat_pelt_prime", "quantity_range":(1,2)}}}
        }
    ],
    "cave": [
        {
            "description": "Deeper in the cave, your pickaxe strikes a rich vein of glowing moonstone ore, alongside some common iron deposits.",
            "effect": {"type": "item_find_multiple_options", "details": {"options": [{"item_key": "moonstone_ore_chunk_glowing", "quantity_range": (2,4), "chance":0.4, "requires_tool":"pickaxe"}, {"item_key":"iron_ore_chunk", "quantity_range":(3,6), "chance":0.6, "requires_tool":"pickaxe"}]}}
        },
        {
            "description": "You find the skeletal remains of an unfortunate mage. A scorched journal beside them speaks of a hidden chamber further in, warded by powerful elemental glyphs and guarded by summoned Atronachs.",
            "effect": {"type": "quest_lead_and_item", "details": {"lead_description": "Mage's journal mentions a warded chamber with Atronach guardians. The glyphs might require specific spells to bypass.", "related_tags": ["hidden_chamber_elemental_wards", "daedra_atronach_guardians", "cave_magic_danger_puzzle"], "item_found_on_skeleton": "journal_mage_elemental_cave", "quest_title_hint": "The Warded Chamber", "potential_reward":"Atronach_Forge_Tome_or_Staff_of_Elements"}}
        },
        {
            "description": "A narrow passage is blocked by a massive, perfectly spherical boulder that looks like it could be rolled if enough force is applied or a lever is found.",
            "effect": {"type": "skill_challenge_or_puzzle", "details": {"skill_strength": "strength", "dc_strength": 18, "puzzle_hint_text":"There might be a hidden lever or pressure plate nearby that controls this boulder.", "target_description": "spherical boulder trap", "success_desc": "With a mighty heave or clever use of a mechanism, the boulder rolls aside, revealing the passage!", "failure_desc": "The boulder is too heavy or the mechanism eludes you.", "related_puzzle_id":"cave_rolling_boulder_passage"}}
        },
        {
            "description": "Bioluminescent fungi illuminate a small grotto where a clear spring bubbles up. The water tastes incredibly pure and invigorating.",
            "effect": {"type": "interaction_point", "details": {"interaction_name": "Grotto Spring of Purity", "action_text": "Drink from the spring?", "effect_if_drink": {"type": "minor_buff_debuff_multiple", "details": [{"stat":"health_current_restore_full", "is_buff":True}, {"stat":"magicka_current_restore_full", "is_buff":True}, {"stat":"fatigue_current_restore_full", "is_buff":True}, {"stat":"disease_cure_all", "is_buff":True, "buff_name":"Spring's Cleansing"}]}}}
        },
        {
            "description": "You find strange, glowing symbols painted on the cave walls. They pulse with a faint energy and seem to react to your presence or perhaps a specific magical attunement.",
            "effect": {"type": "lore_reveal_and_puzzle_hint", "details": {"lore_topic": "Ancient_Cave_Glyphs_Magical", "information": "These symbols might be part of an ancient warding system, a map, or a ritual. They seem to resonate with elemental magic.", "puzzle_hint_text":"Try casting different elemental spells (fire, frost, shock) on the glyphs to see if they react or reveal a pattern.", "related_puzzle_id":"cave_elemental_glyph_sequence"}}
        }
    ],
    "ruin": [
        {
            "description": "Amidst crumbling pillars, you find a faded inscription in the ancient language of the Ayleids. With considerable effort, you might decipher its meaning, hinting at the ruin's original purpose.",
            "effect": {"type": "skill_challenge", "details": {"skill": "lore_ancient_languages_ayleid", "dc": 17, "target_description": "Ayleid inscription", "success_desc": "The inscription speaks of this place as a 'Star-Shrine', dedicated to observing celestial events and channeling magicka from Aetherius!", "success_reward": {"lore_reveal_specific": "Ayleid_StarShrine_Purpose_Aetherius_Conduit", "experience_points":150}, "failure_desc": "The Ayleid script is too complex and fragmented for you to understand fully."}}
        },
        {
            "description": "A section of the floor has collapsed, revealing a dark, ominous shaft leading to a lower, unexplored level. A sturdy rope might allow descent, or there could be a hidden mechanism to lower a platform.",
            "effect": {"type": "location_feature_and_choice", "details": {"feature_name": "Collapsed Floor to Lower Ruin", "interaction_options": ["use_rope_to_descend_if_has_rope", "search_for_platform_mechanism_perception_dc16", "find_alternate_route"], "reveals_sub_area_hint": "Lower Sanctum of [RuinName]"}}
        },
        {
            "description": "You find an ancient, tarnished silver locket lying amongst the debris. It feels unnaturally cold to the touch and emanates a faint whisper of sorrow and betrayal. It might belong to a restless spirit here.",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_key": "silver_locket_ancient_cursed_sorrow", "lore_hint": "This locket seems tied to a tragic love story and a vengeful spirit within these ruins.", "lead_description":"A spirit might be bound to this locket. Finding its resting place or resolving its sorrow could lay it to rest.", "quest_title_hint":"The Locket of Lost Love"}}
        },
        {
            "description": "A ghostly echo of ancient battle cries and clashing steel can be heard, as if the ruin itself relives a pivotal, violent moment from its past. You feel a chill run down your spine.",
            "effect": {"type": "flavor", "details": {"atmosphere_effect": "haunting_battle_echoes", "possible_undead_trigger_chance": 0.2, "enemy_tags_if_triggered":[["undead_ghost_warrior_ancient"]]}}
        },
        {
            "description": "You discover a hidden pressure plate under a loose flagstone. Pressing it causes a nearby bookshelf to slide aside, revealing a secret compartment containing a Scroll of Telekinesis and a journal detailing a mage's experiments with levitation.",
            "effect": {"type": "item_find_multiple", "details": {"item_keys": ["scroll_telekinesis_standard", "journal_mage_levitation_experiments"], "skill_check_to_find_plate":{"skill":"perception", "dc":14}}}
        }
    ],
    "ashland_waste": [
        {
            "description": "The air is thick with choking ash. You find a half-buried skeleton, its hand clutching a small, heat-resistant pouch containing a few Fire Salts and a charred piece of paper with a barely legible map fragment.", 
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_keys": ["fire_salts_impure", "map_fragment_ashlands_charred"], "quantity_range_fire_salts_impure":(1,2), "lead_description": "The map fragment seems to point towards a hidden ancestral tomb or a forgotten Chimeri ruin within these wastes, possibly untouched by the worst of Red Mountain's fury.", "related_tags": ["ashland_exploration_secret", "hidden_dunmer_tomb_map", "survival_challenge_ashlands"], "urgency": "medium", "quest_title_hint":"The Charred Path"}}
        },
        {
            "description": "A wild Bull Netch, its massive gas-filled body drifting eerily through the ashfall, floats by, its tentacles trailing. They are usually docile unless provoked, but their leather and jelly are valuable to Dunmer.", 
            "effect": {"type": "npc_encounter_hint", "details": {"npc_tags":{"role":"creature_netch_bull_ashlands", "attitude":"neutral_unless_attacked_or_near_calf"}, "situation": "Potential source of Netch Leather and Netch Jelly if hunted, but they are tough and might have Betty Netches or calves nearby.", "item_if_killed": ["netch_leather_prime_pelt", "netch_jelly_potent"]}}
        },
        {
            "description": "You discover a small, hidden shrine to the Reclamations (Azura, Boethiah, Mephala), somehow preserved amidst the desolation by faithful Dunmer. Praying here grants you a brief moment of ancestral guidance and resilience.", 
            "effect": {"type": "flavor_and_buff", "details": {"god_mention": "The Reclamations (Azura, Boethiah, Mephala)", "lore_hint":"The Reclamations guide the Dunmer people. Their hidden shrines offer solace and strength in these harsh lands.", "minor_buff_debuff":{"stat":"willpower_and_fire_resist", "amount":10, "duration_turns":600, "is_buff":True, "buff_name":"Ancestral Warding"}}}
        },
        {
            "description": "A sudden tremor shakes the ground, and a fissure opens nearby, venting noxious sulfurous gas and revealing a vein of raw ebony ore, dangerously close to a lava flow.", 
            "effect": {"type": "environmental_hazard_and_item_opportunity", "details": {"hazard_type": "ashland_fissure_gas_vent_lava", "effect_desc": "The sulfurous gas stings your eyes and lungs, and the heat from the lava is intense.", "avoid_skill": "endurance_resist_fire_and_poison", "avoid_dc": 16, "failure_penalty": {"status_effect": {"type":"poison_ash_fumes_severe", "potency":10, "duration_turns":5, "affected_stats":["stamina_regen_rate", "health_current"]}, "damage":5, "damage_type":"fire"}, "item_opportunity_if_hazard_passed":{"item_key":"ebony_ore_chunk_raw_volcanic", "quantity_range":(1,2), "requires_tool":"pickaxe_sturdy"}}}}
        },
        {
            "description": "A lone Ashlander scout, their face obscured by a traditional Chitin helm and ash goggles, observes you from a high ash dune. They raise a spear in a gesture that could be a warning or a challenge before silently disappearing into the grey haze.",
            "effect": {"type": "npc_encounter_hint", "details": {"npc_tags": {"role": "ashlander_scout_watcher_hostile_potential", "attitude": "neutral_wary_territorial"}, "situation": "Being watched by native inhabitants. They are masters of survival and ambush in these lands. Further intrusion into their territory might provoke attack.", "faction_mention":"Ashlander Tribes"}}
        }
    ]
    # Add more entries for other tags: tundra, desert, river, market, keep, meadhall, blacksmith, alchemy_shop, temple, college, palace, etc.
}

