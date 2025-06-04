MISC_LOCATIONS = [
    # ADDITIONAL NOTABLE LOCATIONS & DYNAMIC ADVENTURE SITES
    # (Adjusted for 4E 200 - Dragons are ancient, Dragonborn prophecy not active in current events)
    {
        "id": 100,
        "name": "High Hrothgar",
        "desc": "Perched atop the Throat of the World, High Hrothgar is the ancient and sacred monastery of the Greybeards, masters of the Way of the Voice. Pilgrims rarely brave the Seven Thousand Steps to seek their wisdom.",
        "travel_desc": "Ancient monastery of the Greybeards atop the Throat of the World.",
        "tags": ["structure_type_monastery_ancient_sacred", "terrain_mountain_peak_settlement_remote_throat_of_world", "religious_site_aedric_kyne_sacred_voice_worship", "faction_greybeards_hq_masters_of_the_voice", "cultural_historical_significance_way_of_the_voice_masters_ancient_nordic_tradition", "unique_landmark_iconic_architecture_nordic_monastery", "travel_hub_pilgrimage_arduous_seven_thousand_steps_ivarstead", "climate_alpine_extreme_weather_blizzards", "quest_location_main_story_early_greybeards_summons", "magical_properties_ancient_wards_active_peaceful_aura"],
        "demographics": {"Nord Greybeards": 100},
        "travel": {
            "links": [
                {"name": "Seven Thousand Steps from Ivarstead", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 101,
        "name": "Throat of the World",
        "desc": "Tamriel’s highest peak, a snow-clad titan revered by Nords and sacred to Kyne. Its summit holds ancient secrets, a Word Wall, and is the secluded domain of Paarthurnax, ancient leader of the Greybeards, though few know of his true nature or presence.",
        "travel_desc": "Tamriel’s highest peak, sacred to Kyne, home to Paarthurnax.",
        "tags": ["terrain_mountain_peak_summit_sacred_tamriel_highest", "religious_site_aedric_kyne_most_sacred_sky_goddess", "climate_glacial_extreme_weather_thin_air", "dragon_lore_ancient_paarthurnax_hidden_leader_greybeards", "specific_landmark_type_word_wall_location_powerful_ancient", "unique_natural_formation_highest_peak_skyrim", "faction_greybeards_leader_domain_paarthurnax", "cultural_historical_significance_creation_myth_site_potential_nordic_lore", "quest_location_main_story_late_game_paarthurnax_alduin_confrontation", "magical_properties_otherworldly_influence_time_wound_potential"],
        "demographics": {"Dragons (Paarthurnax, hidden)": 1, "Nord Spirits (conceptual)": 99},
        "travel": {
            "links": [
                {"name": "Path from High Hrothgar Summit (restricted)", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 102,
        "name": "Blackreach",
        "desc": "A vast, luminous subterranean cavern system beneath Skyrim, filled with bioluminescent flora, ancient Dwemer cities, Falmer hordes, and valuable resources like Crimson Nirnroot. A dangerous and wondrous lost world.",
        "travel_desc": "Vast subterranean cavern with Dwemer cities and Falmer.",
        "tags": ["environment_underground_realm_vast_luminous", "dwemer_ruin_major_city_extensive_subterranean_blackreach_cities", "falmer_presence_strong_territory_dominant_inhabitants", "unique_natural_formation_bioluminescent_cavern_flora_fauna", "unique_ecosystem_subterranean_flora_fauna_crimson_nirnroot", "alchemy_ingredient_source_rich_crimson_nirnroot_unique", "resource_node_geode_veins_rare_soul_gems_ores", "dungeon_large_complex_dangerous_exploration_interconnected", "mechanical_constructs_dwemer_heavy_potential_guardians_centurions", "chaurus_nest_major_potential_falmer_beasts", "cultural_historical_significance_lost_world_dwemer_falmer_history", "specific_landmark_type_blackreach_elevator_access_multiple"],
        "demographics": {"Falmer": 80, "Chaurus": 15, "Dwemer Constructs (Automated)": 5},
        "travel": {
            "links": [
                {"name": "Alftand Elevator", "connection_type": "Elevator"},
                {"name": "Mzinchaleft Elevator", "connection_type": "Elevator"},
                {"name": "Raldbthar Elevator (hidden access points)", "connection_type": "Elevator"}
            ]
        }
    },
    {
        "id": 103,
        "name": "Sovngarde",
        "desc": "The revered afterlife of the Nords in Aetherius, a realm of valor, feasting, and eternal glory in the Hall of Valor. Normally accessible only to the spirits of worthy departed Nords.",
        "travel_desc": "Revered afterlife of the Nords, realm of valor and feasting.",
        "tags": ["plane_of_existence_aetherius_nordic_afterlife_sovngarde", "cultural_historical_significance_nordic_paradise_valor_eternal_feasting_battle", "unique_landmark_hall_of_valor_legendary_shor_throne", "faction_nord_hero_spirits_ancient_modern", "magical_properties_otherworldly_divine_aedric_influence", "state_or_condition_current_not_normally_accessible_living_spirit_realm", "quest_location_main_story_epic_conclusion_potential_alduin_defeat", "unique_environment_otherworldly_beautiful_misty"],
        "demographics": {"Nord Hero Spirits": 100},
        "travel": {
            "links": [
                {"name": "Passage via extreme spiritual/magical means (highly restricted/legendary)", "connection_type": "Portal"}
            ]
        }
    },
    {
        "id": 104,
        "name": "Labyrinthian",
        "desc": "The sprawling, maze-like ruins of the ancient Nordic city of Bromjunaar, once a center of the Dragon Cult. Now haunted by draugr, ghosts, and the powerful Dragon Priest Morokei, who guards the Staff of Magnus.",
        "travel_desc": "Sprawling ruins of Bromjunaar, haunted by Dragon Priest Morokei.",
        "tags": ["nordic_burial_site_major_city_ruins_labyrinthian", "cultural_historical_significance_dragon_cult_capital_bromjunaar_ancient", "undead_presence_strong_powerful_draugr_ghosts_skeletal_dragon", "dungeon_large_complex_labyrinthine_dangerous", "cultural_historical_significance_dragon_cult_lair_priest_morokei", "quest_location_college_of_winterhold_staff_of_magnus_archmage_quest", "artifact_location_powerful_staff_of_magnus_mask_morokei", "magical_properties_arcane_nexus_powerful_ancient_magic", "terrain_hjaalmarch_foothills_ruins_snowy", "puzzle_ancient_nordic_dragon_cult_lore"],
        "demographics": {"Draugr": 70, "Skeletons": 20, "Ghosts": 9, "Dragon Priest (Morokei)": 1},
        "travel": {
            "links": [
                {"name": "Ancient Nordic Path (decayed)", "connection_type": "Road"},
                {"name": "Hjaalmarch Foothills (near Morthal, treacherous approach)", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 109,
        "name": "Skuldafn Temple",
        "desc": "An exceptionally remote and legendary Nordic temple complex, rumored to be hidden high in the Velothi Mountains. Ancient tales speak of it as a Dragon Cult stronghold and a gateway to Sovngarde, but its location is lost to modern knowledge, likely inaccessible.",
        "travel_desc": "Remote, legendary Nordic temple, rumored gateway to Sovngarde.",
        "tags": ["nordic_burial_site_major_temple_complex_legendary_skuldafn", "cultural_historical_significance_dragon_cult_stronghold_ancient_lost_alduin_portal", "portal_to_sovngarde_rumored_legendary_alduin_access", "structure_condition_highly_inaccessible_ruin_dragon_guarded", "magical_properties_ancient_magic_wards_powerful_dragon_cult", "terrain_velothi_mountains_remote_hidden_skyrim_morrowind_border", "dungeon_large_complex_epic_potential_outdoor_indoor", "dragon_presence_ancient_guardians_potential_alduin_lieutenants", "undead_presence_strong_draugr_priests_powerful", "quest_location_main_story_epic_final_skyrim_approach_alduin"],
        "demographics": {"Draugr (ancient guardians)": 90, "Dragon Priest (lingering spirit - potential)": 10},
        "travel": {
            "links": [
                {"name": "Unknown/Magical means only (legendary)", "connection_type": "Portal"}
            ]
        }
    },
    {
        "id": 110,
        "name": "Shrine of Azura",
        "desc": "A colossal statue and shrine dedicated to the Daedric Prince Azura, located high in the mountains south of Winterhold. A place of pilgrimage for her followers and where prophecies may be received.",
        "travel_desc": "Colossal statue and shrine to Daedric Prince Azura.",
        "tags": ["religious_site_daedric_azura_major_shrine", "structure_type_colossal_statue_shrine_azura", "travel_hub_pilgrimage_daedric_azura_followers", "magical_properties_daedric_influence_overt_prophecy_visions", "quest_location_daedric_artifact_azuras_star", "terrain_mountain_peak_remote_winterhold_border_south", "unique_landmark_iconic_statue_visible_afar", "dunmer_culture_strong_pilgrimage_azura_worship", "faction_azura_cult_priestess_aranea_ienith"],
        "demographics": {"Priestess of Azura (Aranea Ienith)": 1, "Pilgrims (occasional)": 5, "Dunmer Followers (occasional)": 5},
        "travel": {
            "links": [
                {"name": "Winding mountain path from Winterhold vicinity (difficult)", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 111,
        "name": "Shrine of Mehrunes Dagon (Mythic Dawn Museum/Shrine)",
        "desc": "A hidden shrine and museum dedicated to Mehrunes Dagon, Prince of Destruction, located in the mountains of The Pale, maintained by Silus Vesuius. He seeks to reforge Mehrunes' Razor.",
        "travel_desc": "Hidden shrine and museum to Mehrunes Dagon.",
        "tags": ["religious_site_daedric_mehrunes_dagon_hidden_shrine_museum", "faction_mythic_dawn_remnants_shrine_museum_silus_vesuius", "quest_location_daedric_artifact_mehrunes_razor_reforging", "terrain_mountain_shrine_secret_pale_dawnstar_vicinity", "cultural_historical_significance_oblivion_crisis_related_mythic_dawn", "monster_den_dremora_summoned_potential_ritual_guardians", "artifact_location_daedric_razor_pieces", "magical_properties_daedric_influence_overt_mehrunes_dagon"],
        "demographics": {"Silus Vesuius (Curator/Cultist)": 1, "Dremora (summoned during ritual)": 100},
        "travel": {
            "links": [
                {"name": "Obscure path from The Pale foothills, near Dawnstar", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 112,
        "name": "Largashbur (Shrine of Malacath)",
        "desc": "The Orc stronghold of Largashbur in The Rift, which also serves as a shrine to Malacath. The tribe is currently cursed by giants and seeks aid from an outsider to appease their angered god.",
        "travel_desc": "Orc stronghold and shrine to Malacath, tribe cursed by giants.",
        "tags": ["orc_stronghold_largashbur", "religious_site_daedric_malacath_tribal_shrine", "state_or_condition_current_cursed_by_giants_weakened_tribe", "quest_location_daedric_artifact_volendrung_cursed_tribe", "monster_infestation_giant_attacks_ongoing_curse_related", "orc_culture_strong_shamanism_malacath_code", "terrain_rift_mountains_isolated_southern", "faction_orc_tribe_largashbur_cursed", "artifact_location_daedric_volendrung_hammer", "magical_properties_daedric_influence_overt_malacath_curse"],
        "demographics": {"Orcs (cursed and weakened)": 90, "Giants (hostile)": 10},
        "travel": {
            "links": [
                {"name": "Path from The Rift plains, near Forelhost", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 113,
        "name": "Sacellum of Boethiah",
        "desc": "A Daedric shrine high in the mountains east of Windhelm, where followers of Boethiah engage in deadly rituals of sacrifice and combat to prove their worth to the Prince of Plots.",
        "travel_desc": "Daedric shrine where followers of Boethiah engage in deadly rituals.",
        "tags": ["religious_site_daedric_boethiah_major_sacellum", "faction_boethiah_cult_arena_tournament_of_souls", "ritual_site_sacrifice_combat_active_prove_worth", "quest_location_daedric_artifact_ebony_mail", "terrain_mountain_shrine_remote_eastmarch_windhelm_east", "structure_type_arena_outdoor_ritualistic_daedric", "magical_properties_daedric_influence_overt_boethiah_prince_of_plots", "artifact_location_daedric_ebony_mail", "state_or_condition_current_active_cultist_gathering_dangerous"],
        "demographics": {"Boethiah Cultists (various races)": 100},
        "travel": {
            "links": [
                {"name": "Treacherous path from Eastmarch mountains, east of Traitor's Post", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 114,
        "name": "Shrine to Peryite",
        "desc": "A remote Daedric shrine in The Reach, dedicated to Peryite, the Taskmaster. His afflicted followers gather here, seeking a cure from their debilitating disease by communing with the Prince.",
        "travel_desc": "Remote Daedric shrine to Peryite, the Taskmaster.",
        "tags": ["religious_site_daedric_peryite_remote_shrine", "faction_peryite_cult_afflicted_diseased_followers", "quest_location_daedric_artifact_spellbreaker_taskmaster_quest", "terrain_mountain_shrine_remote_reach_karthwasten_northwest", "dangerous_environment_fumes_disease_affliction", "ritual_site_alchemy_communion_incense_fumes", "magical_properties_daedric_influence_overt_peryite_taskmaster", "artifact_location_daedric_spellbreaker_shield", "unique_encounter_kesh_the_clean_khajiit_priest"],
        "demographics": {"Afflicted Followers (Bretons, Nords)": 100, "Kesh the Clean (Khajiit Priest)":1},
        "travel": {
            "links": [
                {"name": "Isolated path from The Reach mountains, northwest of Karthwasten", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 116,
        "name": "Statue to Meridia",
        "desc": "A towering statue dedicated to the Daedric Prince Meridia, located on Mount Kilkreath in Haafingar. It is a beacon against the undead, and Meridia offers a quest to cleanse her temple of a necromancer's defilement.",
        "travel_desc": "Towering statue to Daedric Prince Meridia.",
        "tags": ["religious_site_daedric_meridia_major_statue_temple", "structure_type_colossal_statue_shrine_meridia", "quest_location_daedric_artifact_dawnbreaker_cleanse_temple", "terrain_mountain_peak_kilkreath_haafingar_solitude_west", "magical_properties_holy_ground_daedric_anti_undead_light_magic", "specific_landmark_type_necromancer_lair_defiled_temple_nearby_kilkreath_ruins", "artifact_location_daedric_dawnbreaker_sword", "unique_landmark_iconic_statue_beacon_of_light", "boss_fight_necromancer_malkoran_powerful"],
        "demographics": {"Malkoran (Necromancer Spirit - Boss)": 1, "Corrupted Shades (initially)": 100},
        "travel": {
            "links": [
                {"name": "Path from Dragon Bridge area, Mount Kilkreath ascent", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 117,
        "name": "Forgotten Vale (Legendary Site)",
        "desc": "A legendary, hidden glacial valley in northwestern Skyrim, whispered to be an ancient sanctuary of the Snow Elves. Its existence is unconfirmed, and access is thought to be through impossibly hidden cave systems like Darkfall Cave.",
        "travel_desc": "Legendary, hidden glacial valley, ancient Snow Elf sanctuary.",
        "tags": ["terrain_hidden_valley_legendary_glacial_forgotten_vale", "cultural_historical_significance_snow_elf_sanctuary_mythical_last_refuge", "falmer_presence_ancient_origins_rumored_devolved_snow_elves", "unique_ecosystem_glacial_valley_rumored_unique_flora_fauna", "structure_type_ancient_ruins_snow_elf_lost_temples_wayshrines", "state_or_condition_current_highly_inaccessible_mythical_legendary", "dungeon_large_complex_potential_vale_exploration", "quest_location_dawnguard_potential_alt_auriels_bow", "dragon_lore_ancient_site_potential_dragons_frozen_lair", "artifact_location_powerful_auriels_bow_shield_potential"],
        "demographics": {"Unknown (Legends speak of Falmer, ancient guardians)": 100},
        "travel": {
            "links": [
                {"name": "Darkfall Cave system (legendary, undiscovered)", "connection_type": "Cave System"}
            ]
        }
    },
    {
        "id": 118,
        "name": "Soul Cairn (Plane of Oblivion)",
        "desc": "A desolate plane of Oblivion where souls are trapped, often by necromancers or Daedric pacts. A realm of eerie landscapes, undead, and soul husks, rarely accessed by mortals.",
        "travel_desc": "Desolate plane of Oblivion where souls are trapped.",
        "tags": ["plane_of_existence_oblivion_soul_cairn_desolate", "undead_presence_strong_realm_eternal_spirits_skeletons_wraiths", "magical_properties_soul_trap_magic_dominant_ideal_masters_control", "faction_vampire_lore_ancient_ideal_masters_soul_bargains", "necromancy_focus_soul_magic_powerful_trapped_souls", "unique_environment_otherworldly_bleak_eerie_landscapes_soul_husks", "travel_hub_portal_access_via_dark_ritual_only_vampire_castle_volkihar_potential", "quest_location_dawnguard_potential_alt_serana_valerica", "monster_den_bonemen_mistmen_wrathmen_keepers"],
        "demographics": {"Undead (various spirits, skeletons, wraiths)": 80, "Soul Husks": 10, "Ideal Masters (conceptual rulers)": 10},
        "travel": {
            "links": [
                {"name": "Portal via specific, powerful necromantic ritual or vampire pact (extremely rare)", "connection_type": "Portal"}
            ]
        }
    },
    {
        "id": 119,
        "name": "Castle Volkihar (Ancient Vampire Lair)",
        "desc": "An ancient, imposing fortress on a remote island off the coast of Haafingar, rumored to be the stronghold of a powerful and reclusive vampire clan, the Volkihar. Few who seek it ever return.",
        "travel_desc": "Ancient fortress, rumored stronghold of the Volkihar vampire clan.",
        "tags": ["structure_type_castle_fortress_gothic_island_volkihar", "specific_landmark_type_vampire_ancient_lair_volkihar_clan", "magical_properties_haunted_aura_strong_ancient_vampiric_magic", "faction_vampire_volkihar_clan_rumored_powerful_lord_harkon", "terrain_island_remote_sea_of_ghosts_haafingar_coast", "dungeon_major_castle_complex_labyrinthine", "quest_location_dawnguard_potential_alt_vampire_lord_storyline", "state_or_condition_current_highly_dangerous_inaccessible_vampire_stronghold", "monster_den_vampires_death_hounds_gargoyles"],
        "demographics": {"Volkihar Vampires (ancient and powerful)": 90, "Death Hounds (spectral/undead)": 10},
        "travel": {
            "links": [
                {"name": "Icewater Jetty (Haafingar north coast - perilous journey)", "connection_type": "Boat"}
            ]
        }
    },
    {
        "id": 120,
        "name": "Fort Dawnguard (Ruined Fortress)",
        "desc": "A ruined fortress in a secluded canyon in The Rift, once belonging to an ancient order of vampire hunters. It is now dilapidated and forgotten, though some say its old purpose might one day be revived.",
        "travel_desc": "Ruined fortress, once belonged to vampire hunters.",
        "tags": ["structure_type_ruined_fort_secluded_canyon_dawnguard", "faction_dawnguard_hq_ancient_ruined_potential_revival", "cultural_historical_significance_vampire_hunter_order_historic_forgotten", "state_or_condition_current_dilapidated_forgotten_awaiting_rediscovery", "quest_location_dawnguard_potential_alt_restoration_recruitment", "terrain_rift_canyon_hidden_dayspring_canyon", "dungeon_minor_ruins_potential_fort_structure", "faction_dawnguard_potential_future_base"],
        "demographics": {"Wildlife": 90, "Bandit Scavengers (potential)": 10},
        "travel": {
            "links": [
                {"name": "Hidden path through Dayspring Canyon (The Rift)", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 121,
        "name": "Raven Rock (Solstheim)",
        "desc": "A struggling Dunmer settlement on the southern coast of Solstheim, originally an East Empire Company mining colony. Now under the protection of House Redoran, it faces hardship from ashfall and dwindling resources.",
        "travel_desc": "Struggling Dunmer settlement on Solstheim.",
        "tags": ["populated_town_solstheim_raven_rock", "dunmer_culture_strong_colonial_refugee", "economic_activity_mining_ebony_struggling_red_mountain_eruption_aftermath", "political_influence_house_redoran_protection_councilor_morvayn", "terrain_ashfall_coastal_solstheim_southern", "climate_volcanic_ashland_harsh_red_mountain_proximity", "east_empire_company_presence_historic_founding", "quest_location_dragonborn_dlc_main_potential_alt_miraak_cultists", "travel_hub_sea_windhelm_solstheim_route", "urban_issues_or_atmosphere_struggling_community_ash_blight_potential"],
        "demographics": {"Dunmer": 90, "Nords (few)": 5, "Redoran Guard": 5},
        "travel": {
            "links": [
                {"name": "Ship from Windhelm Docks (Solstheim)", "connection_type": "Ship"}
            ]
        }
    },
    {
        "id": 122,
        "name": "Tel Mithryn (Solstheim)",
        "desc": "The bizarre mushroom tower home of the eccentric but powerful Telvanni wizard, Master Neloth, located in the ashy wastes of Solstheim. A place of strange magical experiments.",
        "travel_desc": "Bizarre mushroom tower home of Telvanni wizard Neloth.",
        "tags": ["structure_type_wizard_tower_mushroom_telvanni_tel_mithryn", "faction_telvanni_mage_neloth_residence_master_wizard", "unique_architecture_magical_mushroom_grown_structure", "magical_properties_arcane_nexus_powerful_experimental_telvanni_magic", "terrain_ashfall_wastes_solstheim_southeastern", "monster_den_ash_spawn_nearby_guardians_experiments", "quest_location_dragonborn_dlc_neloth_quests_potential_alt_hermaeus_mora_black_books", "alchemy_ingredient_source_rich_unique_mushroom_parts_solstheim_flora", "scholar_retreat_rumor_eccentric_wizard_neloth"],
        "demographics": {"Telvanni Wizard (Neloth)": 1, "Apprentice (Talvas Fathryon)": 1, "Ash Spawn (surrounding area)": 98},
        "travel": {
            "links": [
                {"name": "Path across Solstheim ashlands (dangerous)", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 123,
        "name": "Apocrypha (Plane of Hermaeus Mora)",
        "desc": "The Daedric plane of Oblivion belonging to Hermaeus Mora, Prince of Knowledge and Fate. A vast, endless library filled with forbidden lore, writhing tentacles, and ghostly Seekers. Access is only through forbidden Black Books.",
        "travel_desc": "Daedric plane of Hermaeus Mora, vast endless library.",
        "tags": ["plane_of_existence_oblivion_hermaeus_mora_apocrypha", "unique_environment_endless_library_eldritch_shifting_corridors", "forbidden_knowledge_dangerous_repository_countless_tomes", "monster_den_seekers_lurkers_tentacles_guardians_of_lore", "magical_properties_daedric_influence_overt_knowledge_fate_hermaeus_mora", "travel_hub_portal_access_via_black_books_only_solstheim_tamriel", "quest_location_dragonborn_dlc_main_potential_alt_miraak_confrontation", "artifact_location_black_books_forbidden_powers", "unique_landmark_otherworldly_plane_apocrypha"],
        "demographics": {"Seekers (guardians of lore)": 70, "Lurkers (behemoths)": 30},
        "travel": {
            "links": [
                {"name": "Black Books (portals from Solstheim and Tamriel, rare and hidden)", "connection_type": "Portal"}
            ]
        }
    },
    {
        "id": 124,
        "name": "Hall of the Vigilant (Pre-Destruction)",
        "desc": "A fortified lodge near The Pale, serving as a headquarters for the Vigilants of Stendarr in Skyrim. From here, they coordinate their hunts against Daedra, vampires, and other abominations.",
        "travel_desc": "Fortified lodge, HQ for Vigilants of Stendarr.",
        "tags": ["structure_type_lodge_fortified_vigilant_hq", "faction_vigilants_of_stendarr_hq_skyrim_pre_destruction", "religious_military_order_anti_daedra_vampire_witch", "stendarr_worship_center_vigilant_order", "quest_location_vigilant_tasks_potential_bounties_investigations", "terrain_pale_border_mountains_near_dawnstar", "state_or_condition_current_functional_active_pre_vampire_attack", "quest_location_dawnguard_potential_alt_start_point_destruction_event"],
        "demographics": {"Vigilants of Stendarr": 100},
        "travel": {
            "links": [
                {"name": "Path from Whiterun-Pale border mountains", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 125,
        "name": "Sleeping Giant's Thumb",
        "desc": "A towering rock formation in the plains of Whiterun Hold resembling a colossal thumb, considered a sacred landmark by some local Nord tribes and giants.",
        "travel_desc": "Towering rock formation resembling a colossal thumb.",
        "tags": ["unique_natural_formation_rock_thumb_colossal", "cultural_historical_significance_local_legend_sacred_site_nordic_giant", "specific_landmark_type_giant_camp_reverence_site_potential_nearby", "terrain_plains_whiterun_hold_landmark_prominent", "folklore_location_nordic_giant_mythology", "scenic_vista_unique_plains_landmark", "exploration_point_natural_wonder"],
        "demographics": {"Giants (nearby)": 20, "Nord Hunters/Pilgrims (occasional)": 80},
        "travel": {
            "links": [
                {"name": "Open plains of Whiterun Hold", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 126,
        "name": "The Karthspire Forsworn Camp",
        "desc": "A large and heavily fortified Forsworn encampment at the foot of the Karthspire mountain, fiercely guarding the only known path leading towards the rumored Sky Haven Temple.",
        "travel_desc": "Heavily fortified Forsworn camp guarding path to Sky Haven Temple.",
        "tags": ["structure_type_fortified_camp_forsworn_major_karthspire_base", "faction_forsworn_stronghold_karthspire_base_guardians", "guardian_force_sky_haven_temple_access_fierce", "dangerous_terrain_approach_fortified_narrow_paths", "quest_location_main_story_access_sky_haven_temple", "terrain_mountain_base_reach_karthspire", "state_or_condition_current_forsworn_controlled_area_heavy_fortified", "hagraven_presence_potential_leaders_ritualists"],
        "demographics": {"Forsworn Warriors": 80, "Forsworn Briarhearts": 10, "Hagravens": 10},
        "travel": {
            "links": [
                {"name": "Path from Old Hroldan area", "connection_type": "Path"}
            ]
        }
    },
    {
        "id": 127,
        "name": "Dunmeth Pass Watchtower (Skyrim Side)",
        "desc": "A sturdy Imperial watchtower on the Skyrim side of Dunmeth Pass, guarding the treacherous route to Morrowind. Manned by a small Imperial garrison.",
        "travel_desc": "Imperial watchtower guarding Dunmeth Pass to Morrowind.",
        "tags": ["structure_type_watchtower_fortified_border_imperial", "military_presence_imperial_legion_garrison_small", "morrowind_border_region_dunmeth_pass_skyrim_side_watch", "strategic_location_border_defense_monitoring_morrowind", "isolated_location_outpost_remote", "travel_route_major_dangerous_monitoring_dunmeth_pass", "climate_alpine_harsh_pass_conditions"],
        "demographics": {"Imperial Soldiers": 100},
        "travel": {
            "links": [
                {"name": "Dunmeth Pass Road", "connection_type": "Road"}
            ]
        }
    },
    {
        "id": 128,
        "name": "Guldun Rock",
        "desc": "A large, isolated rock formation in the volcanic tundra of Eastmarch, riddled with caves that are often used as a den by trolls or other dangerous creatures. Sometimes bandits try to establish a hideout here.",
        "travel_desc": "Large rock formation riddled with caves, den for trolls.",
        "tags": ["unique_natural_formation_rock_volcanic_caves_guldun", "structure_type_natural_cave_system_riddled", "monster_den_troll_major_potential_cave_trolls", "bandit_minor_camp_potential_hideout_temporary", "terrain_volcanic_tundra_eastmarch_wilderness_isolated", "dungeon_minor_complex_potential_cave_network", "exploration_challenge_dangerous_creatures_terrain", "alchemy_ingredient_source_rich_troll_fat_minerals_potential"],
        "demographics": {"Trolls/Creatures": 80, "Bandits (occasional)": 20},
        "travel": {
            "links": [
                {"name": "Path from Kynesgrove vicinity", "connection_type": "Path"}
            ]
        }
    }
]