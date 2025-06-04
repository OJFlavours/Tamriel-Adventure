# quests_data_the_rift.py

THE_RIFT_QUEST_TEMPLATES = [
    {
        "id": "riften_thieves_guild_initiation_brynjolf", # Specific ID
        "title_template": "A Chance Arrangement: Joining Riften's Thieves Guild",
        "desc_template": "The notorious **Thieves Guild of Riften**, masters of shadow and coin, seeks new blood. Brynjolf, their cunning recruiter, offers a test in the Riften marketplace: prove your worth by framing Brand-Shei to demonstrate your skills in subterfuge and manipulation. This is your opportunity to join the ranks of Skyrim's most infamous criminal organization.",
        "lore_tags": ["the_rift", "riften_city", "thieves_guild_active_recruitment", "criminal_initiation_test", "subterfuge_deception", "corruption_citywide", "black_briar_influence_guild"],
        "location_tags_required": ["riften", "thieves_guild_hq_ragged_flagon", "marketplace_riften"], # Riften marketplace and Ragged Flagon are key
        "level_range": (3, 8), # Early access to Thieves Guild
        "flavor_tags": {"quest": {"type": ["infiltration", "deception_skill", "crime_faction_join"], "difficulty": ["medium"], "moral": ["unethical_choice_faction", "gray_survival"]}},
        "turn_in_role_hint": ["brynjolf_thieves_guild_recruiter"], # Brynjolf is the main contact
        "stages": [
            {
                "stage_name": "A Test of Cunning",
                "objectives": [
                    {"id": "obj_talk_to_brynjolf_riften_market", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** in the Riften marketplace to receive your first task."},
                    {"id": "obj_steal_madesis_ring_riften", "type": "collect_item", "item_key": "madesis_silver_ring_stolen", "location_name": "Madesi's Stall (Strongbox)", "count": 1, "note": "Steal **Madesi's silver ring** from his strongbox (requires Sneak or Pickpocket check DC 12)."},
                    {"id": "obj_plant_ring_brand_shei_riften", "type": "use_item", "item_key": "madesis_silver_ring_stolen", "npc_id": "brand_shei_dunmer_merchant_ID", "note": "Discreetly **plant Madesi's ring** on Brand-Shei (requires Sneak or Pickpocket check DC 15)."},
                    {"id": "obj_report_to_brynjolf_after_plant_riften", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Report back to Brynjolf once the ring is planted."}
                ],
                "on_completion_dialogue": "The ring is planted, and Brand-Shei is framed. Brynjolf is impressed by your cunning. 'You've got potential, lad/lass. Meet me down in the Ragged Flagon, in the Ratway.' Your initiation into the Guild is at hand.",
                "branch_options": []
            },
            {
                "stage_name": "Joining the Shadows",
                "objectives": [
                    {"id": "obj_reach_ragged_flagon_riften_guild", "type": "reach_location", "location_name": "The Ragged Flagon (Ratway)", "note": "Find your way into the **Ragged Flagon**, the hidden tavern beneath Riften via the Ratway."},
                    {"id": "obj_talk_to_brynjolf_ragged_flagon_join", "type": "talk_to_npc", "npc_id": "brynjolf_thieves_guild_ID", "note": "Speak with **Brynjolf** within the Ragged Flagon to officially join the Thieves Guild and receive your first real assignment."}
                ],
                "on_completion_dialogue": "You are now a member of the Thieves Guild, a new life in the shadows begins. Your first true contract awaits from Mercer Frey or another senior member. Return to [QUEST_GIVER_NAME] (Brynjolf).",
                "reward_modifier": {"reputation_thieves_guild_member_bonus": 20, "gold_bonus": 100, "experience_bonus": 80, "item_bonus": "thieves_guild_armor_set_basic"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "riften_black_briar_meadery_sabotage", # Specific ID
        "title_template": "The Black-Briar's Bite: A Rival's Revenge",
        "desc_template": "The city of **Riften** groans under the iron fist of **Maven Black-Briar**. A rival meadery owner, or perhaps a disgruntled former employee, seeks your aid to subtly sabotage the Black-Briar Meadery's operations—poisoning a batch of mead or stealing their secret recipe. This is a dangerous game against Riften's most powerful family.",
        "lore_tags": ["the_rift", "riften_city", "black_briar_family_maven", "corruption_economic_maven", "economic_sabotage_rivalry", "meadery_intrigue", "thieves_guild_potential_link"],
        "location_tags_required": ["riften", "black_briar_meadery", "black_briar_influence_total"], # Black-Briar Meadery is key
        "level_range": (6, 12),
        "flavor_tags": {"quest": {"type": ["sabotage", "infiltration_stealth", "corporate_espionage_fantasy"], "difficulty": ["medium", "hard_stealth"], "moral": ["unethical_choice_sabotage", "gray_area_revenge"]}},
        "turn_in_role_hint": ["rival_meadery_owner_riften", "disgruntled_black_briar_employee", "thieves_guild_contact_riften"],
        "stages": [
            {
                "stage_name": "Whispers of Discontent",
                "objectives": [
                    {"id": "obj_meet_client_black_briar_sabotage", "type": "talk_to_npc", "npc_id": "sabotage_client_black_briar_ID", "note": "Meet with your **mysterious client** who wants to undermine Maven Black-Briar."},
                    {"id": "obj_learn_meadery_layout_black_briar", "type": "investigate", "location_name": "Black-Briar Meadery (Exterior/Public Areas)", "note": "Scout the **Black-Briar Meadery** to learn its layout and guard patrols (requires Sneak or Perception check DC 13)."}
                ],
                "on_completion_dialogue": "Your client outlines the plan: either poison the main mead vat or steal the recipe from Maven's office within the meadery. Both are risky.",
                "branch_options": [
                    {"choice_id": "poison_mead_black_briar", "text": "Attempt to poison the mead vats.", "next_stage_index": 1},
                    {"choice_id": "steal_recipe_black_briar", "text": "Attempt to steal the secret recipe.", "next_stage_index": 2}
                ]
            },
            { # Stage 1: Poison Mead
                "stage_name": "A Bitter Brew",
                "objectives": [
                    {"id": "obj_infiltrate_meadery_vats_black_briar", "type": "reach_location", "location_name": "Black-Briar Meadery (Vat Room)", "note": "Infiltrate the **meadery's vat room** undetected."},
                    {"id": "obj_poison_mead_vats_black_briar", "type": "use_item", "item_key": "potent_nonlethal_poison", "location_name": "Black-Briar Meadery (Vat Room)", "note": "Add the **special poison** to the main mead vats (requires Sneak check DC 16 or distraction)."}
                ],
                "on_completion_dialogue": "The mead is tainted. It won't kill, but it'll ruin the Black-Briar's reputation for a while. Escape and report to your client.",
                "reward_modifier": {"gold_bonus": 750, "experience_bonus": 150, "reputation_black_briar_family_penalty": -15, "reputation_thieves_guild_riften_bonus": 10},
                "final_stage": True
            },
            { # Stage 2: Steal Recipe
                "stage_name": "The Secret Ingredient",
                "objectives": [
                    {"id": "obj_infiltrate_mavens_office_meadery", "type": "reach_location", "location_name": "Black-Briar Meadery (Maven's Office)", "note": "Infiltrate **Maven Black-Briar's private office** within the meadery."},
                    {"id": "obj_steal_recipe_black_briar_secret", "type": "collect_item", "item_key": "black_briar_secret_mead_recipe", "count": 1, "location_name": "Black-Briar Meadery (Maven's Office)", "note": "Steal the **secret mead recipe** from Maven's safe or desk (requires Lockpicking DC 15 or Sneak check DC 17)."}
                ],
                "on_completion_dialogue": "You have the recipe! This will be a significant blow to the Black-Briars and a boon to their rivals. Escape and report to your client.",
                "reward_modifier": {"gold_bonus": 1000, "experience_bonus": 200, "reputation_black_briar_family_penalty": -20, "reputation_thieves_guild_riften_bonus": 15, "item_bonus": "unique_black_briar_mead_bottle_empty"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "riften_lost_prospect_mine_gold", # Specific ID
        "title_template": "The Prospector's Gamble: Gold Rush in the Rift",
        "desc_template": "The once-promising **Lost Prospect Mine** in the Rift, rumored to hold rich gold veins, has fallen silent. Its last prospector, Hafjorg, fears it's overrun by monstrous spiders or bandits. Reclaim the mine, clear its depths of any threats, and perhaps, rediscover its golden promise for him.",
        "lore_tags": ["the_rift", "mine_gold_abandoned_rift", "spider_infestation_cave", "bandit_lair_potential_mine", "reclamation_economic_small", "prospector_hopeful"],
        "location_tags_required": ["mine_abandoned_gold", "spider_infestation_potential", "lost_prospect_mine"], # Lost Prospect Mine is key
        "level_range": (3, 8),
        "flavor_tags": {"quest": {"type": ["clear_area_mine", "reclaim_resource", "economic_aid_individual"], "difficulty": ["medium"], "moral": ["ethical_helping", "mercenary_task"]}},
        "turn_in_role_hint": ["hafjorg_prospector_riften", "riften_jarls_steward_economy"],
        "stages": [
            {
                "stage_name": "A Silent Promise of Gold",
                "objectives": [
                    {"id": "obj_talk_to_hafjorg_prospector_riften", "type": "talk_to_npc", "npc_id": "hafjorg_nord_prospector_ID", "note": "Speak with the **anxious prospector Hafjorg** in Riften about the abandoned Lost Prospect Mine."},
                    {"id": "obj_reach_lost_prospect_mine_riften", "type": "reach_location", "location_name": "Lost Prospect Mine", "note": "Travel to the deserted **Lost Prospect Mine** in the Rift and assess the situation."}
                ],
                "on_completion_dialogue": "The mine's entrance is eerily quiet, save for the faint scuttling sounds from within. It's infested, just as Hafjorg feared. You must clear it.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Veins of Gold",
                "objectives": [
                    {"id": "obj_clear_spiders_or_bandits_lost_prospect", "type": "kill", "target_name": "Giant Frostbite Spider Patriarch", "target_id": "giant_frostbite_spider_patriarch_ID", "count": 1, "note": "Clear the mine of its **monstrous spider infestation** (or bandits, if they've taken over), including their leader."},
                    {"id": "obj_find_hafjorgs_journal_optional_lost_prospect", "type": "optional", "objective": {"id": "opt_obj_hafjorg_journal", "type": "collect_item", "item_key": "hafjorgs_mining_journal", "count": 1, "note": " (Optional) Search for **Hafjorg's lost mining journal** which might hint at a hidden rich gold vein (requires Investigation check DC 14)."}}
                ],
                "on_completion_dialogue": "The mine is clear! The gnawing threat is gone, and Hafjorg can return. You may have even found his journal pointing to more riches. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 500, "experience_bonus": 75, "reputation_riften_commoners_bonus": 8, "item_bonus": "gold_ore_samples_large"},
                "final_stage": True
            }
        ]
    }
    # Add more Rift specific quests here
]