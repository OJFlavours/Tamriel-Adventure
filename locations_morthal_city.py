MORTHAL_CITY_LOCATION_DATA = [
    {
        "id": 4001,
        "name": "Highmoon Hall",
        "desc": "The austere residence of Jarl Idgrod Ravencrone and her family, where she contemplates her visions.",
        "travel_desc": "Austere residence of Jarl Idgrod Ravencrone.",
        "tags": ["structure_type_palace_or_manor_austere", "settlement_features_jarls_longhouse", "government_local_jarl_idgrod_ravencrone", "magical_properties_arcane_focus_minor_potential_seer_jarl", "political_family_seer_jarl_idgrod", "quest_giver_potential_jarl_visions"],
        "density": "sparse",
        "exit_label_from_parent": "Hall Entrance",
        "exit_label_to_parent": "Exit Hall"
    },
    {
        "id": 4002,
        "name": "Moorside Inn",
        "desc": "Morthal's only inn, a somewhat rustic and humble establishment run by Jonna. It offers a warm fire and shelter from the surrounding Drajkmyr Marsh. Patrons often discuss local concerns, including the recent house fire and whispers of vampiric activity. Lurbuk, an Orcish bard of questionable talent, can sometimes be found performing here.",
        "travel_desc": "Morthal's humble inn, run by Jonna.",
        "tags": ["structure_type_inn_building_humble", "settlement_features_tavern", "social_hub_local", "rumor_source_local_fears_vampires", "food_drink_vendor", "lodging_available", "structure_condition_weathered", "quest_giver_potential_jonna_local_issues", "location_specific_moorside_inn"],
        "density": "sparse",
        "context_tags": ["interior", "urban_town", "tavern_type", "safe_zone"],
        "demographics": {"Nord": 90, "Breton": 5, "Imperial": 3, "Argonian": 2},
        "exit_label_from_parent": "Inn Door",
        "exit_label_to_parent": "Exit Inn"
    },
    {
        "id": 4003,
        "name": "Thaumaturgist's Hut (Falion's House)",
        "desc": "The somewhat isolated hut of Falion, Morthal's resident wizard. He is a Redguard scholar of arcane arts, with a particular expertise in conjuration and matters related to vampirism. While some locals view him with suspicion due to his reclusive nature and magical practices, he offers unique services, including curing vampirism, and may sell spell tomes or rare ingredients.",
        "travel_desc": "Hut of Falion, Morthal's resident wizard and expert on vampirism.",
        "tags": ["structure_type_shack_or_hut_wizard", "structure_type_residence_wizard", "settlement_features_alchemy_shop_notable_wizard_hut", "item_type_potion_vendor", "item_type_ingredient_vendor", "magical_properties_arcane_focus_vampire_lore", "quest_giver_vampire_cure_falion", "scholar_retreat_rumor_arcane_expert", "urban_issues_or_atmosphere_fear_and_superstition_falion_suspicion", "spell_vendor_conjuration_expert"],
        "density": "sparse",
        "context_tags": ["interior", "urban_town_edge", "shop_type_arcane", "residence_type"],
        "exit_label_from_parent": "Hut Door",
        "exit_label_to_parent": "Exit Hut"
    },
    {
        "id": 4004,
        "name": "Jorgen and Lami's House",
        "desc": "The home of Jorgen and Lami, who work at the local lumber mill. Lami is an aspiring alchemist.",
        "travel_desc": "Home of Jorgen and Lami, local workers.",
        "tags": ["structure_type_residence", "commoner_dwelling_logger_alchemist_apprentice", "economic_activity_logging_timber_worker_family", "alchemy_apprentice_potential_lami", "family_dwelling"],
        "density": "sparse",
        "exit_label_from_parent": "House Door",
        "exit_label_to_parent": "Exit House"
    },
    {
        "id": 4005,
        "name": "Burned House",
        "desc": "The charred ruins of Hroggar's house, site of a recent tragedy that has the town on edge and fuels rumors of dark magic.",
        "travel_desc": "Charred ruins of Hroggar's house, site of tragedy.",
        "tags": ["structure_type_ruined_shack_burned", "structure_condition_collapsed_charred", "tragedy_site_family_fire_death", "quest_location_vampire_investigation_laid_to_rest_clue", "urban_issues_or_atmosphere_haunted_rumors_strong_dark_magic", "mystery_local_fire_origin"],
        "density": "empty",
        "exit_label_from_parent": "Enter Ruins",
        "exit_label_to_parent": "Leave Ruins"
    }
]