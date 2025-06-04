# quests_data_winterhold.py

WINTERHOLD_QUEST_TEMPLATES = [
    {
        "id": "winterhold_ancient_relic_retrieval_saarthal", # More specific ID
        "title_template": "The Echoes of Saarthal: The Amulet of Jyrik",
        "desc_template": "An ancient Nordic relic, the Amulet of Jyrik Gauldurson, has been reported deep within Saarthal, guarded by powerful Draugr. Retrieve the Amulet and return it to the College of Winterhold for study.",
        "lore_tags": ["winterhold", "saarthal", "ancient_nords", "magic_powerful", "college_of_winterhold", "dungeon_exploration", "draugr_lords", "gauldur_legend"],
        "location_tags_required": ["saarthal", "barrow_ancient", "dungeon_magic", "undead_powerful", "college_quest_related"], # Saarthal is key
        "level_range": (5, 10), # Suitable for early College quests
        "flavor_tags": {"quest": {"type": ["fetch", "investigate", "dungeon_crawl"], "difficulty": ["medium", "hard"], "urgency": ["important_college"]}},
        "turn_in_role_hint": ["college_mage_archivist", "urag_gro_shub"], # Urag or similar archivist
        "stages": [
            {
                "stage_name": "Venture into Saarthal",
                "objectives": [
                    {"id": "obj_reach_saarthal_winterhold", "type": "reach_location", "location_name": "Saarthal Excavation", "note": "Venture into the ancient ruins of Saarthal. Be wary of the restless dead and magical traps."}
                ],
                "on_completion_dialogue": "You have entered Saarthal. The air here hums with ancient magic, and the shadows seem to move on their own... The College mages are already inside, proceed with caution.",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve the Amulet and Defeat its Guardian",
                "objectives": [
                    {"id": "obj_collect_amulet_jyrik", "type": "collect_item", "item_key": "amulet_of_jyrik_gauldurson", "count": 1, "note": "Find the Amulet of Jyrik Gauldurson within Saarthal's depths."},
                    {"id": "obj_kill_jyrik_gauldurson", "type": "kill", "target_name": "Jyrik Gauldurson (Draugr)", "target_id": "jyrik_gauldurson_draugr_ID", "count": 1, "note": "Defeat the powerful Draugr guardian, Jyrik Gauldurson himself."},
                    {"id": "obj_saarthal_puzzle_optional_winterhold", "type": "optional", "objective": {"id": "opt_obj_saarthal_puzzle", "type": "solve_puzzle", "object": "saarthal_rotating_pillars_puzzle", "note": " (Optional) Decipher and solve the ancient Nordic puzzle to unlock a hidden chamber containing additional lore or treasure."}}
                ],
                "on_completion_dialogue": "The Amulet of Jyrik is now yours, and its guardian defeated. It pulses with a strange, potent energy. Return to [QUEST_GIVER_NAME] at the College of Winterhold.",
                "reward_modifier": {"reputation_college_of_winterhold_bonus": 15, "gold_bonus": 250, "experience_bonus": 150, "item_bonus": "adept_destruction_robe"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "winterhold_college_research_materials_hobs_fall", # More specific ID
        "title_template": "Rare Arcane Reagents from Hob's Fall",
        "desc_template": "A Master Wizard at the College of Winterhold requires rare arcane reagents—specifically, undisturbed Void Salts and potent Deathbell samples—from the treacherous Hob's Fall Cave for a delicate experiment. Retrieve them for a handsome reward.",
        "lore_tags": ["winterhold", "college_of_winterhold", "magic_research", "alchemy_reagents", "necromancy_lair", "cave_dangerous"],
        "location_tags_required": ["college_quest_related", "cave_necromancer", "hobs_fall_cave"], # Hob's Fall Cave is key
        "level_range": (8, 14),
        "flavor_tags": {"quest": {"type": ["fetch", "collection"], "difficulty": ["medium", "hard"], "moral": ["ethical_research", "dangerous_task"]}},
        "turn_in_role_hint": ["college_mage_alchemy_master", "phinis_gestor"], # Phinis or similar alchemy/conjuration expert
        "stages": [
            {
                "stage_name": "Enter Hob's Fall Cave",
                "objectives": [
                    {"id": "obj_reach_hobs_fall_winterhold", "type": "reach_location", "location_name": "Hob's Fall Cave", "note": "Travel to Hob's Fall Cave, a known haunt of necromancers and warlocks."}
                ],
                "on_completion_dialogue": "The cave is dark and reeks of death and decay. You hear unsettling whispers and the crackle of dark magic...",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve Reagents and Deal with Necromancers",
                "objectives": [
                    {"id": "obj_collect_void_salts_hobs", "type": "collect_item", "item_key": "void_salts_pure", "count": 3, "note": "Collect pure Void Salts from the necromancers' ritual sites."},
                    {"id": "obj_collect_deathbell_hobs", "type": "collect_item", "item_key": "deathbell_potent_sample", "count": 5, "note": "Gather potent Deathbell samples from the cave's gloomiest corners."},
                    {"id": "obj_kill_necromancers_hobs", "type": "kill", "target_name": "necromancer adept", "target_id": "necromancer_adept_ID", "count": 3, "note": "Neutralize the necromancers defiling the cave and guarding the reagents."}
                ],
                "on_completion_dialogue": "You have the reagents, and the necromancers are dealt with. Their dark experiments are halted for now. Return to [QUEST_GIVER_NAME] at the College.",
                "reward_modifier": {"reputation_college_of_winterhold_bonus": 12, "gold_bonus": 300, "experience_bonus": 180, "item_bonus": "enchanted_ring_conjuration"},
                "final_stage": True
            }
        ]
    }
    # Add more Winterhold specific quests here
]