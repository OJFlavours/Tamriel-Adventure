# quests_data_eastmarch.py
import random # For random choices in templates

EASTMARCH_QUEST_TEMPLATES = [
    {
        "id": "eastmarch_windhelm_blood_on_the_ice", # Canonical quest ID
        "title_template": "Blood on the Ice: The Butcher of Windhelm",
        "desc_template": "A series of brutal, ritualistic murders has terrified the citizens of **Windhelm**, particularly targeting women in the Gray Quarter. The city guards are stumped. Investigating the chilling crime scenes, uncovering the identity of the 'Butcher,' and bringing the perpetrator to justice is paramount, before another life is lost.",
        "lore_tags": ["eastmarch", "windhelm_city", "murder_mystery_serial", "city_intrigue_dark", "social_tension_gray_quarter", "investigation_forensic", "dark_secrets_windhelm", "justice_vigilante_potential", "necromancy_hints"],
        "location_tags_required": ["windhelm", "murder_investigation_active", "hjerim_house"], # Windhelm and Hjerim are key
        "level_range": (8, 14), # A complex investigation
        "flavor_tags": {"quest": {"type": ["investigate", "mystery", "justice_dark"], "difficulty": ["hard", "dark_themed"], "moral": ["ethical_justice", "vengeance_personal"]}},
        "turn_in_role_hint": ["jorleif_steward_windhelm", "viola_giordano_concerned", "calixto_corrium_suspect"], # Multiple interaction points
        "stages": [
            {
                "stage_name": "The Trail of Blood",
                "objectives": [
                    {"id": "obj_investigate_first_murder_windhelm", "type": "investigate", "location_name": "Windhelm Graveyard (Crime Scene)", "note": "Investigate the **latest murder scene** in Windhelm's graveyard, looking for overlooked clues (requires Perception or Investigation check DC 14)."},
                    {"id": "obj_talk_to_guard_blood_ice", "type": "talk_to_npc", "npc_id": "windhelm_guard_crime_scene_ID", "note": "Speak to the **local guard** at the crime scene; they might be hesitant to share information."},
                    {"id": "obj_visit_hall_of_dead_helgird_windhelm", "type": "talk_to_npc", "npc_id": "helgird_priestess_arkay_ID", "location_name": "Hall of the Dead (Windhelm)", "note": "Visit the **Hall of the Dead** to examine the victims' bodies and speak with Helgird, the priestess."}
                ],
                "on_completion_dialogue": "The clues point to a dark, ritualistic pattern. The victims have been dismembered. You find a strange amulet and disturbing pamphlets ('Beware the Butcher!'). The trail leads you to a grim, abandoned house in the city, **Hjerim**, which can be purchased or entered via lockpicking.",
                "branch_options": []
            },
            {
                "stage_name": "A House of Horrors: Hjerim",
                "objectives": [
                    {"id": "obj_enter_hjerim_windhelm", "type": "reach_location", "location_name": "Hjerim (Windhelm)", "note": "Gain access to and explore **Hjerim**, the abandoned house suspected to be the Butcher's lair."},
                    {"id": "obj_find_butchers_journals_hjerim", "type": "collect_item", "item_key": "butchers_journal_set", "count": 2, "note": "Within Hjerim, find the **Butcher's Journals** detailing the grisly acts and a list of targets."},
                    {"id": "obj_find_strange_amulet_hjerim", "type": "collect_item", "item_key": "strange_amulet_necromancer", "count": 1, "note": "Discover a **Strange Amulet** hidden in Hjerim, hinting at necromantic connections."}
                ],
                "on_completion_dialogue": "The truth is horrifying. The Butcher is performing necromantic rituals. The journals reveal the killer's identity or strong clues. You must decide whether to report to Jorleif, confront Calixto Corrium (a local 'expert'), or investigate Viola Giordano who is also looking into the murders.",
                "branch_options": [
                    {"choice_id": "report_jorleif_blood_ice", "text": "Report your findings to Jorleif, Ulfric's steward.", "next_stage_index": 2},
                    {"choice_id": "confront_calixto_blood_ice", "text": "Confront Calixto Corrium with your suspicions.", "next_stage_index": 3},
                    {"choice_id": "work_with_viola_blood_ice", "text": "Share your findings with Viola Giordano.", "next_stage_index": 4}
                ]
            },
            { # Stage 2: Report to Jorleif (Official Path)
                "stage_name": "The Jarl's Justice",
                "objectives": [
                    {"id": "obj_talk_jorleif_evidence_blood_ice", "type": "talk_to_npc", "npc_id": "jorleif_steward_windhelm_ID", "note": "Present your evidence to Jorleif. He may initially point to Wuunferth the Unliving."},
                    {"id": "obj_investigate_wuunferth_optional_blood_ice", "type": "optional", "objective": {"id": "opt_obj_wuunferth", "type": "talk_to_npc", "npc_id": "wuunferth_the_unliving_ID", "note":" (Optional) Speak to Wuunferth. He reveals Calixto is the likely killer and has the real Necromancer's Amulet."}}
                ],
                "on_completion_dialogue": "If Wuunferth is consulted, he directs you to Calixto. If not, Jorleif might arrest Wuunferth, and the killings continue, forcing you to find the real killer: Calixto. The final confrontation awaits.",
                "next_stage_index": 3 # Leads to confronting Calixto anyway
            },
            { # Stage 3: Confront Calixto (The Butcher)
                "stage_name": "The Final Confrontation",
                "objectives": [
                    {"id": "obj_confront_calixto_final_blood_ice", "type": "confront", "npc_id": "calixto_corrium_butcher_ID", "location_name": "Calixto's House of Curiosities or Hjerim", "note": "Confront the **Windhelm Butcher, Calixto Corrium**, at his shop or Hjerim."},
                    {"id": "obj_defeat_calixto_blood_ice", "type": "kill", "target_name": "Calixto Corrium (The Butcher)", "target_id": "calixto_corrium_butcher_ID", "count": 1, "note": "Bring down the **Windhelm Butcher** to end his reign of terror."}
                ],
                "on_completion_dialogue": "Calixto's dark work is ended. Windhelm can finally breathe a sigh of relief, though the scars of the murders will linger. You have brought justice to the city. Report to Jorleif or Viola.",
                "reward_modifier": {"gold_bonus": 1000, "experience_bonus": 200, "reputation_windhelm_city_bonus": 20, "item_bonus": "necromancer_amulet_true_or_hjerm_key"}, # Player might get Hjerim
                "final_stage": True
            },
            { # Stage 4: Work with Viola (Alternative Investigation)
                "stage_name": "A Citizen's Crusade",
                "objectives": [
                    {"id": "obj_talk_viola_evidence_blood_ice", "type": "talk_to_npc", "npc_id": "viola_giordano_concerned_ID", "note": "Share your evidence with Viola Giordano. She also suspects Calixto."},
                    {"id": "obj_gather_more_proof_viola_blood_ice", "type": "investigate", "location_name": "Calixto's House of Curiosities", "note": "With Viola, find more definitive proof in Calixto's shop."}
                ],
                "on_completion_dialogue": "You and Viola have enough to expose Calixto. Confront him together or report to Jorleif.",
                "next_stage_index": 3 # Leads to confronting Calixto
            }
        ]
    },
    {
        "id": "eastmarch_orc_stronghold_narzulbur_gloom", # Specific ID
        "title_template": "The Ebony Heart of Narzulbur: Gloombound's Affliction",
        "desc_template": "The renowned **Narzulbur**, an Orc stronghold fiercely loyal to Malacath, faces a grave threat: its prized **Gloombound Mine** has been plagued by a strange, aggressive malevolence emanating from its deepest ebony veins. Chief Mauhulakh believes it's a test from Malacath, but the miners fear a growing infestation of Chaurus or worse. You must investigate the mine's depths, quell the threat, and restore the stronghold's honor and prosperity.",
        "lore_tags": ["eastmarch", "orc_stronghold_narzulbur", "malacath_ritual_test", "mine_ebony_rich", "dungeon_danger_chaurus", "tribal_honor_orcish", "resource_threat_mine"],
        "location_tags_required": ["orc_stronghold_isolated", "mine_ebony_major", "narzulbur", "gloombound_mine"], # Narzulbur and Gloombound Mine are key
        "level_range": (10, 16),
        "flavor_tags": {"quest": {"type": ["clear_dungeon", "investigate_supernatural", "honor_tribal"], "difficulty": ["hard"], "moral": ["ethical_aid", "tribal_customs"]}},
        "turn_in_role_hint": ["mauhulakh_orc_chief_narzulbur", "dushnamub_orc_miner_narzulbur"],
        "stages": [
            {
                "stage_name": "The Darkening Veins",
                "objectives": [
                    {"id": "obj_talk_to_chief_mauhulakh_narz", "type": "talk_to_npc", "npc_id": "mauhulakh_orc_chief_narzulbur_ID", "note": "Speak with **Chief Mauhulakh** in Narzulbur about the troubles plaguing Gloombound Mine."},
                    {"id": "obj_investigate_gloombound_mine_narz", "type": "investigate", "location_name": "Gloombound Mine (Ebony Veins)", "note": "Descend into **Gloombound Mine** and investigate the source of the growing malevolence (requires Perception or Mining skill check DC 15 to find clues amidst mining marks)."},
                    {"id": "obj_defeat_chaurus_mine_entrance_narz", "type": "kill", "target_name": "Chaurus Reaper", "target_id": "chaurus_reaper_ID", "count": 3, "note": "Clear the immediate mine entrance of any **Chaurus** that have appeared."}
                ],
                "on_completion_dialogue": "The mine's depths are tainted. You discover signs of an ancient, trapped magic, or perhaps a Chaurus nest drawn to the ebony's essence. The true threat lies deeper, guarded by more formidable foes.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Ebonground",
                "objectives": [
                    {"id": "obj_reach_mine_deep_narz", "type": "reach_location", "location_name": "Gloombound Mine (Deepest Caverns)", "note": "Delve into the **deepest, most dangerous caverns** of Gloombound Mine."},
                    {"id": "obj_defeat_chaurus_queen_or_ancient_dwemer_narz", "type": "kill", "target_name": "Chaurus Queen / Ancient Dwemer Construct", "target_id": random.choice(["chaurus_queen_ID", "ancient_dwemer_centurion_ID"]), "count": 1, "note": "Confront and defeat the **source of the mine's affliction** (e.g., a Chaurus Queen, or a rogue Dwemer construct)."},
                    {"id": "obj_extract_heart_of_ebony_optional_narz", "type": "optional", "objective": {"id": "opt_obj_ebony_heart", "type": "collect_item", "item_key": "heart_of_ebony_pure", "count": 1, "note": " (Optional) Extract a **Heart of Pure Ebony** from the cleansed area, a rare prize for Malacath (requires Smithing/Mining check DC 16)."}}
                ],
                "on_completion_dialogue": "The malevolence is gone, and the rich ebony veins pulse with renewed, clean energy. Narzulbur's prosperity is secured, and your aid has brought great honor to their stronghold. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_orc_strongholds_bonus": 20, "gold_bonus": 1200, "experience_bonus": 180, "item_bonus": "orcish_battleaxe_ebony_infused"}, # Ebony themed reward
                "final_stage": True
            }
        ]
    },
    {
        "id": "eastmarch_witchmist_grove_cleansing", # Specific ID
        "title_template": "The Witches' Weave: Purging Witchmist Grove",
        "desc_template": "The mystical **Witchmist Grove**, a place of natural beauty and potent magical energies in Eastmarch's hot springs region, has been defiled. A coven of malevolent witches, or perhaps a powerful Hagraven, has taken root, twisting its primal energies for dark rituals. Drive out this vile presence, cleanse the grove, and restore its natural tranquility.",
        "lore_tags": ["eastmarch", "witchmist_grove", "grove_magical_hotsprings", "hagraven_lair_powerful", "witch_coven_dark", "dark_ritual_site_nature", "clearance_spiritual", "nature_cleansing_kyne"],
        "location_tags_required": ["grove_magical", "hagraven_lair_potential", "witchmist_grove", "hot_springs_region"], # Witchmist Grove is key
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["clear_area", "hunt_supernatural", "spiritual_cleansing"], "difficulty": ["medium", "hard"], "moral": ["ethical_nature", "divine_intervention_minor"]}},
        "turn_in_role_hint": ["hunter_eastmarch_local", "priestess_kyne_windhelm", "jarls_steward_eastmarch"],
        "stages": [
            {
                "stage_name": "The Twisted Heart of the Grove",
                "objectives": [
                    {"id": "obj_reach_witchmist_grove_east", "type": "reach_location", "location_name": "Witchmist Grove", "note": "Travel to the once-sacred **Witchmist Grove**. Feel the oppressive, twisted magical presence in the air."},
                    {"id": "obj_defeat_hagraven_or_witches_east", "type": "kill", "target_name": "Hagraven Matron / Coven Leader", "target_id": random.choice(["hagraven_matron_ID", "witch_coven_leader_ID"]), "count": 1, "note": "Exterminate the **leader of the malevolent witches or hagravens** defiling the grove."},
                    {"id": "obj_destroy_ritual_altar_optional_east", "type": "optional", "objective": {"id": "opt_obj_altar_destroy", "type": "destroy", "object": "hagraven_ritual_altar", "note": " (Optional) Destroy the **foul altar and ritual components** at the heart of the grove to prevent their return."}}
                ],
                "on_completion_dialogue": "The dark energies have receded from Witchmist Grove. Its natural beauty begins to assert itself once more, cleansed by your actions. The grove is safe. Report to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 600, "experience_bonus": 90, "reputation_eastmarch_locals_bonus": 10, "item_bonus": "rare_alchemy_ingredients_hotsprings_bundle"},
                "final_stage": True
            }
        ]
    }
    # Add more Eastmarch specific quests here
]