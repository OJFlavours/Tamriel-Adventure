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
            "description": "You overhear two city guards discussing increased bandit activity on the road to a nearby village (e.g., Riverwood if in Whiterun). They mention the Jarl's steward is o[...]",
            "effect": {"type": "quest_lead", "details": {"quest_title_hint": "Bandit Menace on the [RoadName] Road", "lead_description": "Bandit activity reported by guards on a specific road. A bounty might be offered by the Jarl."}}
        },
        {
            "description": "A street urchin, with eyes too old for their face, offers to show you a 'secret way' into the city's old cistern for 10 septims, hinting it connects to the Thieves Guild.",
            "effect": {"type": "skill_challenge_or_choice", "details": {"choice_text": "Pay the urchin (10 gold) for the cistern entrance, try to intimidate them (Speech DC 13), or pickpocket the gold back (Pickpocket DC 15)."}}
        },
        {
            "description": "You find a crumpled but official-looking notice: 'Mercenaries and able-bodied adventurers needed! The Penitus Oculatus seeks individuals for a discreet operation concerning certain artifacts.'",
            "effect": {"type": "quest_lead", "details": {"quest_title_hint": "A Discreet Operation for the Emperor", "lead_description": "The Penitus Oculatus (Emperor's agents) are recruiting for a secretive mission involving valuable artifacts."}}
        },
        {
            "description": "In a quiet temple garden dedicated to Dibella, Goddess of Beauty and Love, you find a dropped Silver Ruby Ring. It seems to have been left by a forgetful noble.",
            "effect": {"type": "item_find", "details": {"item_key": "silver_ruby_ring"}}
        },
        {
            "description": "While browsing a dusty bookstall, a loose page from 'The Rear Guard' describes legends of a hidden smuggling tunnel beneath the city's docks, used during the Great War.",
            "effect": {"type": "location_discovery_hint", "details": {"location_name_hint": "Great War Smuggling Tunnel - [CityName] Docks", "related_tags": ["smuggling_tunnel", "hidden_history"]}}
        },
        {
            "description": "You notice a member of the local Thieves Guild subtly marking a wealthy merchant's house with a 'Loot' shadowmark. An opportunity for the light-fingered, a chance to warn the merchant, or something else...",
            "effect": {"type": "moral_choice_event", "details": {"choice_text": "Note the 'Loot' shadowmark (Perception DC 12 to understand its meaning & remember house), warn the merchant (Speech DC 14), or do nothing."}}
        },
        {
            "description": "A heated argument erupts at a stall between a Dunmer refugee from Morrowind and a Nord citizen over the price of ash yams. The tension of cultural differences and recent immigration is palpable.",
            "effect": {"type": "flavor", "details": {"atmosphere_effect": "social_tension_cultural_economic", "faction_mention": ["dunmer_refugee_morrowind", "nord_local_citizen", "economic_hardship"]}}
        }
    ],
    "tavern": [
        {
            "description": "The innkeeper, a jovial Redguard named Nazir, mentions a group of treasure hunters who passed through, bragging about a map to 'Redoran's Retreat' but lost a piece of it (perhaps intentionally...)",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_key_to_find": "map_fragment_redorans_retreat", "skill_check_to_find": {"skill":"perception", "dc":15}, "success_desc": "You find a fragment of a map tucked behind a loose stone in the hearth.", "failure_desc": "You search the hearth but find nothing of interest."}}
        },
        {
            "description": "You overhear a group of Companions, their Skyforge steel gleaming, discussing a contract to clear out a den of Ice Wraiths from a cave near [DynamicNearbyLandmark - e.g., Bleak Falls Barrow].",
            "effect": {"type": "quest_lead", "details": {"lead_description": "The Companions are taking a contract on Ice Wraiths. You could offer to join them for a share of the reward.", "related_tags": ["ice_wraiths", "companions", "contract"]}}
        },
        {
            "description": "A notice on the common room wall, stained with mead: 'Dangerous Necromancer, Malyn Varen, defiling graves near [NearbyBarrowName]! Disturbing the ancient dead! Reward offered by the Temple of Arkay!'",
            "effect": {"type": "quest_lead", "details": {"lead_description": "A necromancer is causing trouble in a nearby barrow. The Temple of Arkay is offering a bounty to stop him.", "related_tags": ["necromancer", "barrow", "temple_of_arkay"]}}
        },
        {
            "description": "Tucked under a loose floorboard near the bar, you find a small, worn leather pouch containing a few vials of Sleeping Tree Sap and a coded note about a clandestine meeting.",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_keys": ["sleeping_tree_sap_vial"], "quantity_range_sleeping_tree_sap_vial":(1,2), "lead_description": "The note mentions a meeting at midnight near the city gates. It's signed with a strange symbol.", "related_tags": ["sleeping_tree_sap", "clandestine_meeting"]}}
        },
        {
            "description": "A traveling bard sings a chilling tale of 'The Gauldur Amulet', a powerful artifact split into three fragments, each guarded by one of the Gauldurson brothers in their respective tombs.",
            "effect": {"type": "location_discovery_hint_multiple", "details": {"location_name_hints": ["Folgunthur - Gauldurson Tomb", "Saarthal - Jyrik Gauldurson's Tomb", "Geirmund's Hall - Sigdis Gauldurson's Tomb"], "related_tags": ["gauldur_amulet", "gauldurson_brothers", "ancient_tomb"]}}
        },
        {
            "description": "After a few tankards of Black-Briar Mead, a Nord patron, looking for trouble, challenges you to a brawl. 'Think you're tough enough, eh? Let's see it! Winner gets 100 septims!'",
            "effect": {"type": "skill_challenge_or_combat", "details": {"game_type": "tavern_brawl_nord", "wager_amount": 100, "skill_unarmed_or_onehanded_no_weapon": "strength", "dc": 14, "success_desc": "You win the brawl and collect your winnings!", "failure_desc": "You lose the brawl and have to pay up!"}}
        },
        {
            "description": "You find a 'Lost and Found' notice: 'Lost: One Dwarven Cog, essential for my research! Generous reward for its return. - Calcelmo of Markarth.'",
            "effect": {"type": "quest_lead", "details": {"lead_description": "Calcelmo, the Dwemer scholar in Markarth, has lost a Dwarven Cog. He'll likely pay well for its return.", "related_tags": ["dwarven_cog", "calcelmo", "markarth"]}}
        },
        {
            "description": "The innkeeper quietly warns you that a member of the Dark Brotherhood was seen asking about 'new contracts' in town. 'Best watch your back, traveler. And don't sleep too soundly...'",
            "effect": {"type": "lore_reveal", "details": {"lore_topic": "Dark_Brotherhood_Activity_Rumor", "information": "The Dark Brotherhood is always looking for new recruits or targets. Their presence is rarely a good sign...", "related_tags": ["dark_brotherhood", "contracts"]}}
        }
    ],
    "forest": [
        {
            "description": "You follow a barely visible animal trail to a secluded grotto where a Spriggan Earth Mother is performing a ritual over a bed of glowing mushrooms. She turns her ancient gaze upon you...",
            "effect": {"type": "npc_encounter_choice", "details": {"npc_tags": {"role":"spriggan_earth_mother_powerful", "attitude":"neutral_territorial_ancient"}, "situation": "Spriggan Earth Mother performing a ritual. She may be hostile or helpful depending on your actions.", "choice_text": "Approach cautiously (Speech DC 16), attack immediately, or retreat silently."}}
        },
        {
            "description": "In a sun-dappled clearing, you find a patch of rare Crimson Nirnroot, its glow more intense than its common cousin, alongside some potent Chokeberry vines.",
            "effect": {"type": "item_find", "details": {"item_keys": ["crimson_nirnroot_rare", "chokeberry_vine_poisonous"], "quantity_range_crimson_nirnroot_rare": (1, 2), "quantity_range_chokeberry_vine_poisonous": (2, 4)}}
        },
        {
            "description": "You stumble upon a poacher's trap that has ensnared a young elk. A note nearby details the poacher's plan to sell the prized antlers to a shady merchant in Riften.",
            "effect": {"type": "moral_choice_and_quest_lead", "details": {"choice_text": "Free the elk (Animal Handling DC 13), harvest it yourself, or use the note to track down the poacher/merchant in Riften (Investigation DC 14).", "related_tags": ["poacher", "elk", "riften"]}}
        },
        {
            "description": "An ancient, moss-covered chest is cleverly hidden within a hollow, lightning-struck oak. It's sealed with a complex puzzle lock depicting forest animals.",
            "effect": {"type": "skill_challenge_and_puzzle", "details": {"skill_primary": "lockpicking", "dc_primary": 17, "skill_secondary_puzzle":"lore_nature_or_intelligence", "dc_secondary_puzzle": 15, "puzzle_hint_text":"The lock depicts a bear, a wolf, a hawk, and a snake. Perhaps their order is important?", "success_desc": "You solve the puzzle and unlock the chest!", "failure_desc": "You fail to unlock the chest."}}
        },
        {
            "description": "You discover a small, serene pond where wisps of light dance above the water. The water is impossibly clear. Drinking from it, you feel your magical energies surge and briefly glimpse a vision...",
            "effect": {"type": "interaction_point", "details": {"interaction_name": "Wisp-Mother's Tears Pond", "action_text": "Drink from the pond?", "effect_if_drink": {"type": "minor_buff_debuff", "buff_type": "magicka_regen", "buff_amount": 0.15, "buff_duration": 60, "vision_hint": "A fleeting vision of a distant mountain peak and a hidden shrine."}}}
        }
    ],
    "plains": [
        {
            "description": "You spot a distant, solitary watchtower ruin atop a windswept hill. It looks like an ideal bandit lookout or a forgotten Imperial outpost.",
            "effect": {"type": "location_discovery_hint", "details": {"location_name_hint": "Lone Sentinel Spire", "related_tags": ["ruin_watchtower_isolated", "ancient_imperial_or_bandit_lookout"]}}
        },
        {
            "description": "While crossing a field of tall grass, your foot strikes something hard. Digging, you unearth a small, buried strongbox containing several flawless gems and a silver ingot.",
            "effect": {"type": "item_find", "details": {"item_keys": ["gem_flawless_diamond", "gem_flawless_ruby", "silver_ingot_pure"], "quantity_range_gem_flawless_diamond": (1, 1), "quantity_range_gem_flawless_ruby": (1, 1), "quantity_range_silver_ingot_pure": (1, 2)}}
        },
        {
            "description": "You encounter a travelling Khajiit merchant, Ma'dran, part of a larger caravan. He mentions a rare 'Star-Sung Grass' that only grows on these plains under the light of Jone and Jode.",
            "effect": {"type": "quest_lead", "details": {"lead_description": "A rare visionary herb, Star-Sung Grass, might be found here under specific celestial conditions. Ma'dran would pay handsomely for it.", "related_tags": ["star_sung_grass", "khajiit_caravan", "jone_jode"]}}
        },
        {
            "description": "A sudden gust of wind whips across the plains, revealing an old, discarded Orcish shield with a clan emblem you don't recognize. It's heavy and battle-scarred.",
            "effect": {"type": "item_find", "details": {"item_key": "shield_orcish_clan_unknown"}}
        },
        {
            "description": "You come across a circle of massive Mammoth bones, arranged deliberately around a central, fire-scorched stone altar. A faint drumming seems to echo on the wind. Locals whisper of Giant rituals...",
            "effect": {"type": "lore_reveal_and_interaction", "details": {"lore_topic": "Nordic_Giant_Spirit_Communion_Sites", "information": "These bone circles are sacred to the Giants. Leaving an offering of food or trinkets might appease them (or attract unwanted attention).", "related_tags": ["mammoth_bones", "giant_ritual", "spirit_communion"]}}
        },
        {
            "description": "A pride of sabre cats, their forms sleek and powerful, are stalking a lone elk in the tall grass. You could intervene or observe.",
            "effect": {"type": "dynamic_encounter_choice", "details": {"situation_description":"Sabre cats hunting elk.", "choice_options":["intervene_help_elk", "intervene_help_sabre_cats_for_pet", "observe"]}}
        }
    ],
    "cave": [
        {
            "description": "Deeper in the cave, your pickaxe strikes a rich vein of glowing moonstone ore, alongside some common iron deposits.",
            "effect": {"type": "item_find_multiple_options", "details": {"options": [{"item_key": "moonstone_ore_chunk_glowing", "quantity_range": (2,4), "chance":0.4, "requires_tool":"pickaxe"},{"item_key": "iron_ore_chunk", "quantity_range": (3,6), "chance": 0.7, "requires_tool": "pickaxe"}]}}
        },
        {
            "description": "You find the skeletal remains of an unfortunate mage. A scorched journal beside them speaks of a hidden chamber further in, warded by powerful elemental glyphs and guarded by Atronachs.",
            "effect": {"type": "quest_lead_and_item", "details": {"lead_description": "Mage's journal mentions a warded chamber with Atronach guardians. The glyphs might require specific spells to bypass.", "item_key": "journal_mage_warded_chamber", "related_tags": ["warded_chamber", "atronachs", "elemental_glyphs"]}}
        },
        {
            "description": "A narrow passage is blocked by a massive, perfectly spherical boulder that looks like it could be rolled if enough force is applied or a lever is found nearby.",
            "effect": {"type": "skill_challenge_or_puzzle", "details": {"skill_strength": "strength", "dc_strength": 18, "puzzle_hint_text":"There might be a hidden lever or pressure plate nearby that controls the boulder's release.", "success_desc": "You manage to move the boulder and clear the passage!", "failure_desc": "You fail to move the boulder."}}
        },
        {
            "description": "Bioluminescent fungi illuminate a small grotto where a clear spring bubbles up. The water tastes incredibly pure and invigorating.",
            "effect": {"type": "interaction_point", "details": {"interaction_name": "Grotto Spring of Purity", "action_text": "Drink from the spring?", "effect_if_drink": {"type": "minor_buff_debuff", "buff_type": "health_regen", "buff_amount": 0.2, "buff_duration": 30}}}
        },
        {
            "description": "You find strange, glowing symbols painted on the cave walls. They pulse with a faint energy and seem to react to your presence or perhaps a specific magical attunement...",
            "effect": {"type": "lore_reveal_and_puzzle_hint", "details": {"lore_topic": "Ancient_Cave_Glyphs_Magical", "information": "These symbols might be part of an ancient warding system, a map, or a key to unlocking a hidden chamber. Further investigation is warranted.", "related_tags": ["ancient_glyphs", "magical_warding", "hidden_chamber"]}}
        }
    ],
    "ruin": [
        {
            "description": "Amidst crumbling pillars, you find a faded inscription in the ancient language of the Ayleids. With considerable effort, you might decipher its meaning, hinting at the ruin's original purpose.",
            "effect": {"type": "skill_challenge", "details": {"skill": "lore_ancient_languages_ayleid", "dc": 17, "target_description": "Ayleid inscription", "success_desc": "The inscription speaks of a temple dedicated to a forgotten Ayleid deity.", "failure_desc": "You fail to decipher the inscription."}}
        },
        {
            "description": "A section of the floor has collapsed, revealing a dark, ominous shaft leading to a lower, unexplored level. A sturdy rope might allow descent, or there could be a hidden path...",
            "effect": {"type": "location_feature_and_choice", "details": {"feature_name": "Collapsed Floor to Lower Ruin", "interaction_options": ["use_rope_to_descend_if_has_rope", "search_for_path_down"]}}
        },
        {
            "description": "You find an ancient, tarnished silver locket lying amongst the debris. It feels unnaturally cold to the touch and emanates a faint whisper of sorrow and betrayal. It may be cursed...",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_key": "silver_locket_ancient_cursed_sorrow", "lore_hint": "This locket seems tied to a tragic love story and a vengeful spirit. Someone might want it back...", "related_tags": ["cursed_item", "tragic_love_story", "vengeful_spirit"]}}
        },
        {
            "description": "A ghostly echo of ancient battle cries and clashing steel can be heard, as if the ruin itself relives a pivotal, violent moment from its past. You feel a chill run down your spine...",
            "effect": {"type": "flavor", "details": {"atmosphere_effect": "haunting_battle_echoes", "possible_undead_trigger_chance": 0.2, "enemy_tags_if_triggered":[["undead_ghost_warrior_ancient", "undead_skeleton"]], "trigger_description": "The echoes intensify, and spectral warriors materialize before you!"}}
        },
        {
            "description": "You discover a hidden pressure plate under a loose flagstone. Pressing it causes a nearby bookshelf to slide aside, revealing a secret compartment containing a Scroll of Telekinesis and a journal detailing mage's levitation experiments.",
            "effect": {"type": "item_find_multiple", "details": {"item_keys": ["scroll_telekinesis_standard", "journal_mage_levitation_experiments"], "skill_check_to_find_plate":{"skill":"perception", "dc":15, "success_desc": "You spot the pressure plate!", "failure_desc": "You find nothing of interest."}}}
        }
    ],
    "ashland_waste": [
        {
            "description": "The air is thick with choking ash. You find a half-buried skeleton, its hand clutching a small, heat-resistant pouch containing a few Fire Salts and a charred piece of map.",
            "effect": {"type": "item_find_and_quest_lead", "details": {"item_keys": ["fire_salts_impure", "map_fragment_ashlands_charred"], "quantity_range_fire_salts_impure":(1,2), "lead_description": "The charred map fragment seems to depict a route to a hidden location within the ashlands. It's singed but still legible.", "related_tags": ["fire_salts", "ashlands_map", "hidden_location"]}}
        },
        {
            "description": "A wild Bull Netch, its massive gas-filled body drifting eerily through the ashfall, floats by, its tentacles trailing. They are usually docile unless provoked, but the ash storms make them unpredictable...",
            "effect": {"type": "npc_encounter_hint", "details": {"npc_tags":{"role":"creature_netch_bull_ashlands", "attitude":"neutral_unless_attacked_or_near_calf"}, "situation": "Potential source of leather and alchemical ingredients, but also a dangerous foe if provoked.", "related_tags": ["netch", "ashlands_creature"]}}
        },
        {
            "description": "You discover a small, hidden shrine to the Reclamations (Azura, Boethiah, Mephala), somehow preserved amidst the desolation by faithful Dunmer. Praying here grants you a moment of respite and guidance...",
            "effect": {"type": "flavor_and_buff", "details": {"god_mention": "The Reclamations (Azura, Boethiah, Mephala)", "lore_hint":"The Reclamations guide the Dunmer people. Their hidden shrines offer solace and strength to those who still honor them.", "buff_type": "resistance_fire", "buff_amount": 0.1, "buff_duration": 120}}
        },
        {
            "description": "A sudden tremor shakes the ground, and a fissure opens nearby, venting noxious sulfurous gas and revealing a vein of raw ebony ore, dangerously close to a lava flow.",
            "effect": {"type": "environmental_hazard_and_item_opportunity", "details": {"hazard_type": "ashland_fissure_gas_vent_lava", "effect_desc": "The sulfurous gas stings your eyes and lungs, and the lava poses an immediate threat.", "item_keys": ["ebony_ore_raw"], "quantity_range_ebony_ore_raw":(1,3), "skill_check_to_mine":{"skill":"mining", "dc":16, "success_desc":"Carefully mine the ebony ore, avoiding the lava!", "failure_desc":"The lava is too close and you burn yourself trying to mine the ebony! Take 5 fire damage."}}}
        },
        {
            "description": "A lone Ashlander scout, their face obscured by a traditional Chitin helm and ash goggles, observes you from a high ash dune. They raise a spear in a gesture that could be a greeting or a threat...",
            "effect": {"type": "npc_encounter_hint", "details": {"npc_tags": {"role": "ashlander_scout_watcher_hostile_potential", "attitude": "neutral_wary_territorial"}, "situation": "Being watched by an Ashlander scout. Approaching cautiously or ignoring them are both viable options.", "related_tags": ["ashlander", "scout", "dunmer"]}}
        }
    ]
    # Add more entries for other tags: tundra, desert, river, market, keep, meadhall, blacksmith, alchemy_shop, temple, college, palace, etc.
}