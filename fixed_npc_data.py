# fixed_npc_data.py

# This file contains the data for all fixed, named NPCs in the game world.
# The structure is a dictionary where keys are location IDs and values are lists
# of NPC data dictionaries.
# Roles used here (e.g., "jarl") are reserved for these characters and are not
# intended for use by the random NPC generator.

FIXED_NPC_DATA = {
    # === WHITERUN HOLD ===
    # Whiterun City
    1001: [ # Dragonsreach
        {"name": "Balgruuf the Greater", "gender": "Male", "race": "Nord", "role": "jarl", "level": 20, "class": "Noble"},
        {"name": "Irileth", "gender": "Female", "race": "Dunmer", "role": "housecarl", "level": 25, "class": "Noble"},
        {"name": "Proventus Avenicci", "gender": "Male", "race": "Imperial", "role": "steward", "level": 10, "class": "Noble"},
        {"name": "Farengar Secret-Fire", "gender": "Male", "race": "Nord", "role": "court_wizard", "level": 12, "class": "Noble"},
        {"name": "Hrongar", "gender": "Male", "race": "Nord", "role": "warrior_noble", "level": 18, "class": "Noble"},
        {"name": "Dagny", "gender": "Female", "race": "Nord", "role": "jarl_child", "level": 1, "class": "Noble"},
        {"name": "Frothar", "gender": "Male", "race": "Nord", "role": "jarl_child", "level": 1, "class": "Noble"},
        {"name": "Nelkir", "gender": "Male", "race": "Nord", "role": "jarl_child_whispering", "level": 1, "class": "Noble"},
        {"name": "Gerda", "gender": "Female", "race": "Nord", "role": "servant", "level": 2, "class": "Commoner"},
    ],
    1002: [ # Jorrvaskr
        {"name": "Kodlak Whitemane", "gender": "Male", "race": "Nord", "role": "harbinger_companion", "level": 50, "class": "Noble"},
        {"name": "Vilkas", "gender": "Male", "race": "Nord", "role": "companion_master_at_arms", "level": 30, "class": "Commoner"},
        {"name": "Farkas", "gender": "Male", "race": "Nord", "role": "companion_master_at_arms", "level": 30, "class": "Commoner"},
        {"name": "Aela the Huntress", "gender": "Female", "race": "Nord", "role": "companion_huntress", "level": 32, "class": "Commoner"},
        {"name": "Skjor", "gender": "Male", "race": "Nord", "role": "companion_warrior", "level": 30, "class": "Commoner"},
        {"name": "Athis", "gender": "Male", "race": "Dunmer", "role": "companion_warrior", "level": 15, "class": "Commoner"},
        {"name": "Njada Stonearm", "gender": "Female", "race": "Nord", "role": "companion_warrior", "level": 15, "class": "Commoner"},
        {"name": "Ria", "gender": "Female", "race": "Imperial", "role": "companion_warrior_new", "level": 10, "class": "Commoner"},
        {"name": "Torvar", "gender": "Male", "race": "Nord", "role": "companion_warrior", "level": 15, "class": "Commoner"},
        {"name": "Vignar Gray-Mane", "gender": "Male", "race": "Nord", "role": "companion_elder", "level": 20, "class": "Noble"},
        {"name": "Tilma the Haggard", "gender": "Female", "race": "Nord", "role": "servant_caretaker", "level": 4, "class": "Commoner"},
    ],
    1003: [ # The Bannered Mare
        {"name": "Hulda", "gender": "Female", "race": "Nord", "role": "innkeeper", "level": 8, "class": "Commoner"},
        {"name": "Saadia", "gender": "Female", "race": "Redguard", "role": "server_fugitive", "level": 5, "class": "Commoner"},
        {"name": "Uthgerd the Unbroken", "gender": "Female", "race": "Nord", "role": "warrior_mercenary", "level": 10, "class": "Commoner"},
        {"name": "Mikael", "gender": "Male", "race": "Nord", "role": "bard", "level": 4, "class": "Commoner"},
        {"name": "Sinmir", "gender": "Male", "race": "Nord", "role": "warrior_patron", "level": 7, "class": "Commoner"},
    ],
    1004: [ # Warmaiden's
        {"name": "Adrianne Avenicci", "gender": "Female", "race": "Imperial", "role": "blacksmith", "level": 7, "class": "Commoner"},
        {"name": "Ulfberth War-Bear", "gender": "Male", "race": "Nord", "role": "merchant_blacksmith_shopkeeper", "level": 6, "class": "Commoner"},
    ],
    1005: [ # Arcadia's Cauldron
        {"name": "Arcadia", "gender": "Female", "race": "Imperial", "role": "alchemist_merchant", "level": 5, "class": "Commoner"},
    ],
    1006: [ # Temple of Kynareth
        {"name": "Danica Pure-Spring", "gender": "Female", "race": "Nord", "role": "priestess_healer", "level": 9, "class": "Commoner"},
        {"name": "Acolyte Jenssen", "gender": "Male", "race": "Nord", "role": "priest_acolyte", "level": 3, "class": "Commoner"},
    ],
    1008: [ # The Drunken Huntsman
        {"name": "Elrindir", "gender": "Male", "race": "Bosmer", "role": "merchant_huntsman", "level": 6, "class": "Commoner"},
        {"name": "Anoriath", "gender": "Male", "race": "Bosmer", "role": "hunter_merchant", "level": 5, "class": "Commoner"},
        {"name": "Jenassa", "gender": "Female", "race": "Dunmer", "role": "mercenary_archer", "level": 8, "class": "Commoner"},
    ],
    1009: [ # Belethor's General Goods
        {"name": "Belethor", "gender": "Male", "race": "Breton", "role": "merchant_general_goods", "level": 4, "class": "Commoner"},
        {"name": "Sigurd", "gender": "Male", "race": "Nord", "role": "shop_assistant_woodcutter", "level": 2, "class": "Commoner"},
    ],
    1010: [ # Carlotta Valentia's House
        {"name": "Carlotta Valentia", "gender": "Female", "race": "Imperial", "role": "merchant_stall_produce", "level": 3, "class": "Commoner"},
        {"name": "Mila Valentia", "gender": "Female", "race": "Imperial", "role": "child", "level": 1, "class": "Commoner"},
    ],
    1012: [ # Heimskr's House / Talos Shrine
        {"name": "Heimskr", "gender": "Male", "race": "Nord", "role": "priest_talos_preacher", "level": 5, "class": "Commoner"},
    ],
    1013: [ # House of Clan Gray-Mane
        {"name": "Fralia Gray-Mane", "gender": "Female", "race": "Nord", "role": "matriarch_stall_merchant", "level": 4, "class": "Noble"},
        {"name": "Eorlund Gray-Mane", "gender": "Male", "race": "Nord", "role": "blacksmith_skyforge", "level": 15, "class": "Noble"},
        {"name": "Olfina Gray-Mane", "gender": "Female", "race": "Nord", "role": "warrior_noble", "level": 6, "class": "Noble"},
        {"name": "Jon Battle-Born", "gender": "Male", "race": "Nord", "role": "bard_noble", "level": 5, "class": "Noble"},
    ],
    1014: [ # House of Clan Battle-Born
        {"name": "Olfrid Battle-Born", "gender": "Male", "race": "Nord", "role": "patriarch_noble", "level": 10, "class": "Noble"},
        {"name": "Bergritte Battle-Born", "gender": "Female", "race": "Nord", "role": "matriarch_noble", "level": 5, "class": "Noble"},
        {"name": "Alfhild Battle-Born", "gender": "Female", "race": "Nord", "role": "servant", "level": 2, "class": "Commoner"},
        {"name": "Lars Battle-Born", "gender": "Male", "race": "Nord", "role": "child", "level": 1, "class": "Noble"},
    ],
    1016: [ # Hall of the Dead
        {"name": "Andurs", "gender": "Male", "race": "Nord", "role": "priest_arkay", "level": 4, "class": "Commoner"},
    ],
    1017: [ # Whiterun Caravan Camp
        {"name": "Ri'saad", "gender": "Male", "race": "Khajiit", "role": "caravan_leader", "level": 10, "class": "Commoner"},
        {"name": "Atahbah", "gender": "Female", "race": "Khajiit", "role": "caravan_guard", "level": 8, "class": "Commoner"},
        {"name": "Ma'jhad", "gender": "Male", "race": "Khajiit", "role": "merchant_fence", "level": 6, "class": "Commoner"},
        {"name": "Kharjo", "gender": "Male", "race": "Khajiit", "role": "caravan_guard", "level": 12, "class": "Commoner"},
    ],
    1000: [ # Whiterun Streets
        {"name": "Brenuin", "gender": "Male", "race": "Redguard", "role": "beggar", "level": 1, "class": "Commoner"},
        {"name": "Amren", "gender": "Male", "race": "Redguard", "role": "warrior_veteran", "level": 8, "class": "Commoner"},
        {"name": "Saffir", "gender": "Female", "race": "Redguard", "role": "citizen", "level": 3, "class": "Commoner"},
        {"name": "Braith", "gender": "Female", "race": "Redguard", "role": "child_bully", "level": 1, "class": "Commoner"},
        {"name": "Nazeem", "gender": "Male", "race": "Redguard", "role": "noble_landowner_pompous", "level": 4, "class": "Noble"},
        {"name": "Ahlam", "gender": "Female", "race": "Redguard", "role": "citizen", "level": 3, "class": "Commoner"},
        {"name": "Lydia", "gender": "Female", "race": "Nord", "role": "housecarl_dragonborn", "level": 10, "class": "Noble"},
    ],
    1101: [ # Sleeping Giant Inn
        {"name": "Delphine", "gender": "Female", "race": "Breton", "role": "innkeeper_blade", "level": 35, "class": "Commoner"},
        {"name": "Orgnar", "gender": "Male", "race": "Nord", "role": "innkeeper_assistant", "level": 5, "class": "Commoner"},
    ],
    1102: [ # Riverwood Trader
        {"name": "Lucan Valerius", "gender": "Male", "race": "Imperial", "role": "merchant", "level": 4, "class": "Commoner"},
        {"name": "Camilla Valerius", "gender": "Female", "race": "Imperial", "role": "shop_assistant", "level": 3, "class": "Commoner"},
    ],
    1103: [ # Alvor and Sigrid's House
        {"name": "Alvor", "gender": "Male", "race": "Nord", "role": "blacksmith", "level": 6, "class": "Commoner"},
        {"name": "Sigrid", "gender": "Female", "race": "Nord", "role": "blacksmith_spouse", "level": 3, "class": "Commoner"},
        {"name": "Dorthe", "gender": "Female", "race": "Nord", "role": "child", "level": 1, "class": "Commoner"},
    ],
    1104: [ # Faendal's House
        {"name": "Faendal", "gender": "Male", "race": "Bosmer", "role": "hunter_woodcutter_archer", "level": 4, "class": "Commoner"},
    ],
    1105: [ # Sven and Hilde's House
        {"name": "Sven", "gender": "Male", "race": "Nord", "role": "bard_woodcutter", "level": 4, "class": "Commoner"},
        {"name": "Hilde", "gender": "Female", "race": "Nord", "role": "mother_elder", "level": 2, "class": "Commoner"},
    ],
    1106: [ # Hod and Gerdur's House
        {"name": "Hod", "gender": "Male", "race": "Nord", "role": "miller", "level": 5, "class": "Commoner"},
        {"name": "Gerdur", "gender": "Female", "race": "Nord", "role": "miller", "level": 5, "class": "Commoner"},
        {"name": "Frodnar", "gender": "Male", "race": "Nord", "role": "child", "level": 1, "class": "Commoner"},
    ],
    1201: [ # Frostfruit Inn
        {"name": "Mralki", "gender": "Male", "race": "Nord", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Erik", "gender": "Male", "race": "Nord", "role": "farmer_aspiring_adventurer", "level": 5, "class": "Commoner"},
        {"name": "Jouane Manette", "gender": "Male", "race": "Breton", "role": "farmer", "level": 3, "class": "Commoner"},
    ],
    1202: [ # Rorik's Manor
        {"name": "Rorik", "gender": "Male", "race": "Nord", "role": "landowner_elder", "level": 8, "class": "Noble"},
    ],
    10001: [ # High Hrothgar
        {"name": "Arngeir", "gender": "Male", "race": "Nord", "role": "greybeard", "level": 100, "class": "Noble"},
        {"name": "Borri", "gender": "Male", "race": "Nord", "role": "greybeard", "level": 100, "class": "Noble"},
        {"name": "Einarth", "gender": "Male", "race": "Nord", "role": "greybeard", "level": 100, "class": "Noble"},
        {"name": "Wulfgar", "gender": "Male", "race": "Nord", "role": "greybeard", "level": 100, "class": "Noble"},
    ],
    10002: [ # Throat of the World
        {"name": "Paarthurnax", "gender": "Male", "race": "Dragon", "role": "dragon_master_greybeard", "level": 150, "class": "Noble"},
    ],
    10003: [ # White River Watch
        {"name": "Hajvarr Iron-Hand", "gender": "Male", "race": "Nord", "role": "bandit_leader", "level": 10, "class": "Commoner"},
    ],
    10004: [ # Silent Moons Camp
        {"name": "Movarth Piquine", "gender": "Male", "race": "Breton", "role": "vampire_master", "level": 25, "class": "Noble"},
    ],
    10005: [ # Halted Stream Camp
        {"name": "Orthorn", "gender": "Male", "race": "Breton", "role": "mage_renegade", "level": 8, "class": "Commoner"},
    ],
    10006: [ # Redoran's Retreat
        {"name": "Drahff", "gender": "Male", "race": "Nord", "role": "bandit", "level": 6, "class": "Commoner"},
        {"name": "Hewnon Black-Skeever", "gender": "Male", "race": "Breton", "role": "bandit_leader", "level": 9, "class": "Commoner"},
    ],
    2001: [ # The Windpeak Inn
        {"name": "Thoring", "gender": "Male", "race": "Nord", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Karita", "gender": "Female", "race": "Nord", "role": "bard_local", "level": 4, "class": "Commoner"},
        {"name": "Abelone", "gender": "Female", "race": "Nord", "role": "farmer", "level": 3, "class": "Commoner"},
    ],
    2002: [ # The Quicksilver Mine
        {"name": "Leigelf", "gender": "Male", "race": "Nord", "role": "mine_owner", "level": 7, "class": "Commoner"},
        {"name": "Beitild", "gender": "Female", "race": "Nord", "role": "mine_owner_rival", "level": 7, "class": "Commoner"},
    ],
    2003: [ # The Mortar and Pestle
        {"name": "Frida", "gender": "Female", "race": "Nord", "role": "alchemist_merchant_elder", "level": 5, "class": "Commoner"},
    ],
    2004: [ # The White Hall
        {"name": "Skald the Elder", "gender": "Male", "race": "Nord", "role": "jarl_stormcloak", "level": 10, "class": "Noble"},
        {"name": "Jod", "gender": "Male", "race": "Nord", "role": "housecarl", "level": 12, "class": "Noble"},
        {"name": "Madena", "gender": "Female", "race": "Imperial", "role": "court_wizard", "level": 10, "class": "Noble"},
    ],
    2005: [ # Rustleif's House
        {"name": "Rustleif", "gender": "Male", "race": "Nord", "role": "blacksmith", "level": 6, "class": "Commoner"},
        {"name": "Seren", "gender": "Female", "race": "Redguard", "role": "blacksmith_spouse", "level": 3, "class": "Commoner"},
    ],
    2006: [ # Brina's House
        {"name": "Brina Merilis", "gender": "Female", "race": "Imperial", "role": "legionnaire_veteran", "level": 15, "class": "Commoner"},
        {"name": "Horik Halfhand", "gender": "Male", "race": "Nord", "role": "legionnaire_veteran", "level": 15, "class": "Commoner"},
    ],
    2008: [ # Dawnstar Caravan Camp
        {"name": "Ahkari", "gender": "Female", "race": "Khajiit", "role": "caravan_leader", "level": 10, "class": "Commoner"},
        {"name": "Zaynabi", "gender": "Female", "race": "Khajiit", "role": "merchant", "level": 5, "class": "Commoner"},
        {"name": "Dro'marash", "gender": "Male", "race": "Khajiit", "role": "caravan_guard", "level": 8, "class": "Commoner"},
    ],
    20001: [ # Nightcaller Temple
        {"name": "Erandur", "gender": "Male", "race": "Dunmer", "role": "priest_mara_former_daedra_worshipper", "level": 20, "class": "Commoner"},
    ],
    3001: [ # The Frozen Hearth
        {"name": "Dagur", "gender": "Male", "race": "Nord", "role": "innkeeper", "level": 7, "class": "Commoner"},
        {"name": "Nelacar", "gender": "Male", "race": "Altmer", "role": "scholar_mage_reclusive", "level": 25, "class": "Commoner"},
        {"name": "Harald", "gender": "Male", "race": "Nord", "role": "patron", "level": 3, "class": "Commoner"},
        {"name": "Ranmir", "gender": "Male", "race": "Nord", "role": "patron_drunk", "level": 2, "class": "Commoner"},
    ],
    3002: [ # The Jarl's Longhouse
        {"name": "Korir", "gender": "Male", "race": "Nord", "role": "jarl", "level": 9, "class": "Noble"},
        {"name": "Thonjolf", "gender": "Male", "race": "Nord", "role": "housecarl", "level": 11, "class": "Noble"},
        {"name": "Asha", "gender": "Female", "race": "Nord", "role": "jarl_child", "level": 1, "class": "Noble"},
    ],
    3004: [ # Birna's Oddments
        {"name": "Birna", "gender": "Female", "race": "Nord", "role": "merchant_general_goods", "level": 3, "class": "Commoner"},
    ],
    3101: [ # Hall of the Elements
        {"name": "Mirabelle Ervine", "gender": "Female", "race": "Breton", "role": "master_wizard", "level": 30, "class": "Noble"},
        {"name": "Tolfdir", "gender": "Male", "race": "Nord", "role": "master_wizard_alteration", "level": 35, "class": "Noble"},
        {"name": "Ancano", "gender": "Male", "race": "Altmer", "role": "thalmor_advisor", "level": 40, "class": "Noble"},
    ],
    3102: [ # Hall of Attainment
        {"name": "J'zargo", "gender": "Male", "race": "Khajiit", "role": "mage_apprentice", "level": 8, "class": "Commoner"},
        {"name": "Brelyna Maryon", "gender": "Female", "race": "Dunmer", "role": "mage_apprentice", "level": 8, "class": "Commoner"},
        {"name": "Onmund", "gender": "Male", "race": "Nord", "role": "mage_apprentice", "level": 8, "class": "Commoner"},
    ],
    3103: [ # Hall of Countenance
        {"name": "Phinis Gestor", "gender": "Male", "race": "Breton", "role": "expert_wizard_conjuration", "level": 25, "class": "Commoner"},
        {"name": "Colette Marence", "gender": "Female", "race": "Breton", "role": "expert_wizard_restoration", "level": 25, "class": "Commoner"},
        {"name": "Drevis Neloren", "gender": "Male", "race": "Dunmer", "role": "master_wizard_illusion", "level": 35, "class": "Noble"},
        {"name": "Faralda", "gender": "Female", "race": "Altmer", "role": "expert_wizard_destruction", "level": 25, "class": "Commoner"},
        {"name": "Sergius Turrianus", "gender": "Male", "race": "Imperial", "role": "expert_wizard_enchanting", "level": 25, "class": "Commoner"},
    ],
    3104: [ # The Arcanaeum
        {"name": "Urag gro-Shub", "gender": "Male", "race": "Orc", "role": "librarian_mage", "level": 20, "class": "Commoner"},
    ],
    3105: [ # Arch-Mage's Quarters
        {"name": "Savos Aren", "gender": "Male", "race": "Dunmer", "role": "arch_mage", "level": 50, "class": "Noble"},
    ],
    30001: [ # Yngvild
        {"name": "Arondil", "gender": "Male", "race": "Altmer", "role": "necromancer_ghost_lover", "level": 20, "class": "Commoner"},
    ],
    4001: [ # Highmoon Hall
        {"name": "Idgrod Ravencrone", "gender": "Female", "race": "Nord", "role": "jarl_mystic", "level": 15, "class": "Noble"},
        {"name": "Gorm", "gender": "Male", "race": "Nord", "role": "housecarl", "level": 12, "class": "Noble"},
        {"name": "Idgrod the Younger", "gender": "Female", "race": "Nord", "role": "jarl_daughter", "level": 7, "class": "Noble"},
    ],
    4002: [ # Moorside Inn
        {"name": "Jonna", "gender": "Female", "race": "Nord", "role": "innkeeper", "level": 5, "class": "Commoner"},
        {"name": "Lurbuk", "gender": "Male", "race": "Orc", "role": "untalented_bard", "level": 3, "class": "Commoner"},
        {"name": "Benor", "gender": "Male", "race": "Nord", "role": "warrior_for_hire", "level": 8, "class": "Commoner"},
    ],
    4005: [ # Alva's House
        {"name": "Alva", "gender": "Female", "race": "Nord", "role": "vampire_conspirator", "level": 10, "class": "Commoner"},
        {"name": "Hroggar", "gender": "Male", "race": "Nord", "role": "vampire_thrall_miller", "level": 4, "class": "Commoner"},
    ],
    4006: [ # Falion's House
        {"name": "Falion", "gender": "Male", "race": "Redguard", "role": "mage_conjurer_vampire_expert", "level": 25, "class": "Commoner"},
        {"name": "Agni", "gender": "Female", "race": "Nord", "role": "child_apprentice", "level": 1, "class": "Commoner"},
    ],
    40001: [ # Robber's Gorge
        {"name": "Ulfgar the Unending", "gender": "Male", "race": "Nord", "role": "bandit_leader_ghost", "level": 15, "class": "Commoner"},
    ],
    5001: [ # Dead Man's Drink
        {"name": "Valga Vinicia", "gender": "Female", "race": "Imperial", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Narri", "gender": "Female", "race": "Nord", "role": "server", "level": 3, "class": "Commoner"},
    ],
    5002: [ # Jarl's Longhouse
        {"name": "Siddgeir", "gender": "Male", "race": "Nord", "role": "jarl_imperial", "level": 8, "class": "Noble"},
        {"name": "Nenya", "gender": "Female", "race": "Altmer", "role": "steward", "level": 10, "class": "Noble"},
        {"name": "Helvard", "gender": "Male", "race": "Nord", "role": "housecarl", "level": 12, "class": "Noble"},
    ],
    5003: [ # Hall of the Dead
        {"name": "Runil", "gender": "Male", "race": "Altmer", "role": "priest_arkay", "level": 8, "class": "Commoner"},
    ],
    5004: [ # Gray Pine Goods
        {"name": "Solaf", "gender": "Male", "race": "Nord", "role": "merchant_general_goods", "level": 5, "class": "Commoner"},
    ],
    5005: [ # Lod's House
        {"name": "Lod", "gender": "Male", "race": "Nord", "role": "blacksmith", "level": 6, "class": "Commoner"},
    ],
    5006: [ # Dengeir's House
        {"name": "Dengeir of Stuhn", "gender": "Male", "race": "Nord", "role": "former_jarl_noble", "level": 12, "class": "Noble"},
    ],
    5008: [ # Dark Brotherhood Sanctuary
        {"name": "Astrid", "gender": "Female", "race": "Nord", "role": "dark_brotherhood_leader", "level": 35, "class": "Commoner"},
        {"name": "Arnbjorn", "gender": "Male", "race": "Nord", "role": "dark_brotherhood_assassin_werewolf", "level": 32, "class": "Commoner"},
        {"name": "Gabriella", "gender": "Female", "race": "Dunmer", "role": "dark_brotherhood_assassin", "level": 30, "class": "Commoner"},
        {"name": "Festus Krex", "gender": "Male", "race": "Imperial", "role": "dark_brotherhood_assassin_mage", "level": 30, "class": "Commoner"},
        {"name": "Veezara", "gender": "Male", "race": "Argonian", "role": "dark_brotherhood_assassin", "level": 28, "class": "Commoner"},
        {"name": "Nazir", "gender": "Male", "race": "Redguard", "role": "dark_brotherhood_assassin", "level": 28, "class": "Commoner"},
        {"name": "Babette", "gender": "Female", "race": "Breton", "role": "dark_brotherhood_assassin_vampire", "level": 40, "class": "Commoner"},
        {"name": "Cicero", "gender": "Male", "race": "Imperial", "role": "dark_brotherhood_keeper", "level": 30, "class": "Commoner"},
    ],
    50001: [ # Knifepoint Ridge
        {"name": "Rigel Strong-Arm", "gender": "Female", "race": "Nord", "role": "bandit_leader_former_sailor", "level": 14, "class": "Commoner"},
    ],
    50002: [ # Bilegulch Mine
        {"name": "Gat gro-Shargakh", "gender": "Male", "race": "Orc", "role": "orc_bandit_leader", "level": 12, "class": "Commoner"},
    ],
    6001: [ # Silver-Blood Inn
        {"name": "Kleppr", "gender": "Male", "race": "Nord", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Frabbi", "gender": "Female", "race": "Nord", "role": "server", "level": 4, "class": "Commoner"},
        {"name": "Cosnach", "gender": "Male", "race": "Breton", "role": "patron_drunk_porter", "level": 3, "class": "Commoner"},
    ],
    6002: [ # Understone Keep
        {"name": "Igmund", "gender": "Male", "race": "Nord", "role": "jarl", "level": 18, "class": "Noble"},
        {"name": "Raerek", "gender": "Male", "race": "Nord", "role": "steward", "level": 10, "class": "Noble"},
        {"name": "Faleen", "gender": "Female", "race": "Redguard", "role": "housecarl", "level": 15, "class": "Noble"},
        {"name": "Calcelmo", "gender": "Male", "race": "Altmer", "role": "court_wizard_scholar", "level": 30, "class": "Noble"},
        {"name": "Ondolemar", "gender": "Male", "race": "Altmer", "role": "thalmor_justiciar", "level": 25, "class": "Noble"},
    ],
    6003: [ # Temple of Dibella
        {"name": "Hamal", "gender": "Female", "race": "Breton", "role": "priestess_dibella_high", "level": 20, "class": "Commoner"},
        {"name": "Anwen", "gender": "Female", "race": "Redguard", "role": "priestess_dibella", "level": 5, "class": "Commoner"},
        {"name": "Senna", "gender": "Female", "race": "Imperial", "role": "priestess_dibella", "level": 5, "class": "Commoner"},
    ],
    6004: [ # Arnleif and Sons Trading Company
        {"name": "Lisbet", "gender": "Female", "race": "Nord", "role": "merchant_general_goods", "level": 5, "class": "Commoner"},
    ],
    6005: [ # The Hag's Cure
        {"name": "Bothela", "gender": "Female", "race": "Breton", "role": "alchemist_merchant_elder", "level": 8, "class": "Commoner"},
        {"name": "Muiri", "gender": "Female", "race": "Breton", "role": "alchemist_apprentice", "level": 3, "class": "Commoner"},
    ],
    6006: [ # Cidhna Mine
        {"name": "Madanach", "gender": "Male", "race": "Breton", "role": "forsworn_king_in_rags", "level": 30, "class": "Noble"},
        {"name": "Borkul the Beast", "gender": "Male", "race": "Orc", "role": "forsworn_prisoner_guard", "level": 15, "class": "Commoner"},
    ],
    6007: [ # Treasury House
        {"name": "Thonar Silver-Blood", "gender": "Male", "race": "Nord", "role": "noble_mine_owner", "level": 12, "class": "Noble"},
        {"name": "Thongvor Silver-Blood", "gender": "Male", "race": "Nord", "role": "noble_thane", "level": 15, "class": "Noble"},
    ],
    6008: [ # Ghorza's Smithy
        {"name": "Ghorza gra-Bagol", "gender": "Female", "race": "Orc", "role": "blacksmith_trainer", "level": 7, "class": "Commoner"},
        {"name": "Tacitus Sallustius", "gender": "Male", "race": "Imperial", "role": "blacksmith_apprentice", "level": 3, "class": "Commoner"},
    ],
    6101: [ # Karthwasten Hall
        {"name": "Ainethach", "gender": "Male", "race": "Breton", "role": "mine_owner_community_leader", "level": 7, "class": "Commoner"},
    ],
    60002: [ # Dushnikh Yal
        {"name": "Chief Burguk", "gender": "Male", "race": "Orc", "role": "orc_stronghold_chief", "level": 20, "class": "Noble"},
    ],
    60003: [ # Hag's End
        {"name": "Moira", "gender": "Female", "race": "Hagraven", "role": "hagraven_witch", "level": 22, "class": "Commoner"},
    ],
    60004: [ # Dead Crone Rock
        {"name": "Drascua", "gender": "Female", "race": "Hagraven", "role": "hagraven_leader", "level": 20, "class": "Commoner"},
    ],
    7001: [ # Candlehearth Hall
        {"name": "Elda Early-Dawn", "gender": "Female", "race": "Nord", "role": "innkeeper", "level": 7, "class": "Commoner"},
        {"name": "Luaffyn", "gender": "Female", "race": "Bosmer", "role": "bard", "level": 4, "class": "Commoner"},
        {"name": "Adonato Leotelli", "gender": "Male", "race": "Imperial", "role": "author_patron", "level": 3, "class": "Commoner"},
    ],
    7003: [ # Palace of the Kings
        {"name": "Ulfric Stormcloak", "gender": "Male", "race": "Nord", "role": "jarl_rebel_leader", "level": 50, "class": "Noble"},
        {"name": "Galmar Stone-Fist", "gender": "Male", "race": "Nord", "role": "stormcloak_general", "level": 40, "class": "Noble"},
        {"name": "Jorleif", "gender": "Male", "race": "Nord", "role": "steward", "level": 10, "class": "Noble"},
        {"name": "Wuunferth the Unliving", "gender": "Male", "race": "Nord", "role": "court_wizard", "level": 25, "class": "Noble"},
    ],
    7005: [ # Aretino Residence
        {"name": "Aventus Aretino", "gender": "Male", "race": "Imperial", "role": "child_orphan_ritualist", "level": 2, "class": "Commoner"},
    ],
    7008: [ # Calixto's House of Curiosities
        {"name": "Calixto Corrium", "gender": "Male", "race": "Imperial", "role": "curator_murderer", "level": 8, "class": "Commoner"},
    ],
    7009: [ # The White Phial
        {"name": "Nurelion", "gender": "Male", "race": "Altmer", "role": "alchemist_merchant_elder", "level": 10, "class": "Commoner"},
        {"name": "Quintus Navale", "gender": "Male", "race": "Imperial", "role": "alchemist_apprentice", "level": 4, "class": "Commoner"},
    ],
    7010: [ # Oengul's Smithy
        {"name": "Oengul War-Anvil", "gender": "Male", "race": "Nord", "role": "blacksmith_stormcloak_supporter", "level": 8, "class": "Commoner"},
        {"name": "Hermir Strong-Heart", "gender": "Female", "race": "Nord", "role": "blacksmith_apprentice", "level": 4, "class": "Commoner"},
    ],
    7011: [ # Argonian Assemblage
        {"name": "Scouts-Many-Marshes", "gender": "Male", "race": "Argonian", "role": "dockworker_foreman", "level": 5, "class": "Commoner"},
        {"name": "Shahvee", "gender": "Female", "race": "Argonian", "role": "dockworker", "level": 3, "class": "Commoner"},
    ],
    7012: [ # East Empire Company
        {"name": "Orthus Endario", "gender": "Male", "race": "Imperial", "role": "east_empire_clerk", "level": 6, "class": "Commoner"},
    ],
    7013: [ # New Gnisis Cornerclub
        {"name": "Ambarys Rendar", "gender": "Male", "race": "Dunmer", "role": "innkeeper_dunmer_community", "level": 6, "class": "Commoner"},
        {"name": "Suvaris Atheron", "gender": "Female", "race": "Dunmer", "role": "farmer_dunmer", "level": 3, "class": "Commoner"},
    ],
    7000: [ # Windhelm Streets
        {"name": "Angrenor Once-Honored", "gender": "Male", "race": "Nord", "role": "beggar_veteran", "level": 2, "class": "Commoner"},
        {"name": "Brunwulf Free-Winter", "gender": "Male", "race": "Nord", "role": "warrior_noble", "level": 15, "class": "Noble"},
        {"name": "Hillevi Cruel-Sea", "gender": "Female", "race": "Nord", "role": "noble", "level": 5, "class": "Noble"},
        {"name": "Rolff Stone-Fist", "gender": "Male", "race": "Nord", "role": "citizen_racist", "level": 4, "class": "Commoner"},
        {"name": "Silda the Unseen", "gender": "Female", "race": "Nord", "role": "beggar", "level": 1, "class": "Commoner"},
        {"name": "Sofie", "gender": "Female", "race": "Nord", "role": "child_orphan_flower_girl", "level": 1, "class": "Commoner"},
        {"name": "Viola Giordano", "gender": "Female", "race": "Imperial", "role": "citizen_busybody", "level": 4, "class": "Commoner"},
    ],
    7101: [ # Braidwood Inn
        {"name": "Iddra", "gender": "Female", "race": "Nord", "role": "innkeeper", "level": 5, "class": "Commoner"},
        {"name": "Gemma", "gender": "Female", "race": "Imperial", "role": "server", "level": 3, "class": "Commoner"},
    ],
    7102: [ # Steamscorch Mine
        {"name": "Kjar", "gender": "Male", "race": "Nord", "role": "miner", "level": 4, "class": "Commoner"},
        {"name": "Dravynea the Stoneweaver", "gender": "Female", "race": "Dunmer", "role": "mage_miner", "level": 8, "class": "Commoner"},
    ],
    70001: [ # Gallows Rock
        {"name": "Krev the Skinner", "gender": "Male", "race": "Nord", "role": "werewolf_silver_hand_leader", "level": 20, "class": "Commoner"},
    ],
    70002: [ # Ansilvund
        {"name": "Lu'ah Al-Skaven", "gender": "Female", "race": "Breton", "role": "necromancer_leader", "level": 22, "class": "Commoner"},
    ],
    8001: [ # Blue Palace
        {"name": "Elisif the Fair", "gender": "Female", "race": "Nord", "role": "jarl", "level": 18, "class": "Noble"},
        {"name": "Sybille Stentor", "gender": "Female", "race": "Breton", "role": "court_wizard_vampire", "level": 30, "class": "Noble"},
        {"name": "Falk Firebeard", "gender": "Male", "race": "Nord", "role": "steward", "level": 12, "class": "Noble"},
        {"name": "Bryling", "gender": "Female", "race": "Nord", "role": "thane", "level": 10, "class": "Noble"},
        {"name": "Erikur", "gender": "Male", "race": "Nord", "role": "thane_east_empire", "level": 12, "class": "Noble"},
    ],
    8002: [ # Castle Dour
        {"name": "General Tullius", "gender": "Male", "race": "Imperial", "role": "legion_general", "level": 50, "class": "Noble"},
        {"name": "Legate Rikke", "gender": "Female", "race": "Nord", "role": "legion_legate", "level": 40, "class": "Noble"},
        {"name": "Captain Aldis", "gender": "Male", "race": "Nord", "role": "legion_captain", "level": 20, "class": "Commoner"},
    ],
    8003: [ # The Winking Skeever
        {"name": "Corpulus Vinius", "gender": "Male", "race": "Imperial", "role": "innkeeper", "level": 7, "class": "Commoner"},
        {"name": "Gulum-Ei", "gender": "Male", "race": "Argonian", "role": "shady_patron_thief", "level": 8, "class": "Commoner"},
        {"name": "Belrand", "gender": "Male", "race": "Nord", "role": "mercenary_spellsword", "level": 10, "class": "Commoner"},
    ],
    8004: [ # Bits and Pieces
        {"name": "Sayma", "gender": "Female", "race": "Redguard", "role": "merchant_general_goods", "level": 6, "class": "Commoner"},
    ],
    8005: [ # Angeline's Aromatics
        {"name": "Angeline Morrard", "gender": "Female", "race": "Breton", "role": "alchemist_merchant", "level": 5, "class": "Commoner"},
    ],
    8006: [ # Radiant Raiment
        {"name": "Taarie", "gender": "Female", "race": "Altmer", "role": "merchant_clothing_tailor_haughty", "level": 5, "class": "Commoner"},
        {"name": "Endarie", "gender": "Female", "race": "Altmer", "role": "merchant_clothing_tailor", "level": 5, "class": "Commoner"},
    ],
    8007: [ # Fletcher
        {"name": "Fihada", "gender": "Male", "race": "Redguard", "role": "merchant_fletcher", "level": 6, "class": "Commoner"},
    ],
    8008: [ # Solitude Blacksmith
        {"name": "Beirand", "gender": "Male", "race": "Nord", "role": "blacksmith", "level": 7, "class": "Commoner"},
    ],
    8009: [ # Bards College
        {"name": "Viarmo", "gender": "Male", "race": "Altmer", "role": "headmaster_bards_college", "level": 10, "class": "Noble"},
        {"name": "Giraud Gemane", "gender": "Male", "race": "Breton", "role": "bard_teacher", "level": 8, "class": "Commoner"},
        {"name": "Pantea Ateia", "gender": "Female", "race": "Imperial", "role": "bard_teacher", "level": 8, "class": "Commoner"},
        {"name": "Lisette", "gender": "Female", "race": "Breton", "role": "bard", "level": 5, "class": "Commoner"},
    ],
    8011: [ # East Empire Company Warehouse
        {"name": "Vittoria Vici", "gender": "Female", "race": "Imperial", "role": "east_empire_trader_noble", "level": 8, "class": "Noble"},
    ],
    8012: [ # Solitude Caravan Camp
        {"name": "Ma'dran", "gender": "Male", "race": "Khajiit", "role": "caravan_leader", "level": 10, "class": "Commoner"},
        {"name": "Ra'zhinda", "gender": "Female", "race": "Khajiit", "role": "merchant_fence", "level": 6, "class": "Commoner"},
    ],
    80001: [ # The Katariah
        {"name": "Captain Avidius", "gender": "Male", "race": "Imperial", "role": "imperial_navy_captain", "level": 25, "class": "Commoner"},
    ],
    9001: [ # The Bee and Barb
        {"name": "Talen-Jei", "gender": "Male", "race": "Argonian", "role": "publican", "level": 6, "class": "Commoner"},
        {"name": "Keerava", "gender": "Female", "race": "Argonian", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Maramal", "gender": "Male", "race": "Redguard", "role": "priest_mara", "level": 7, "class": "Commoner"},
        {"name": "Mjoll the Lioness", "gender": "Female", "race": "Nord", "role": "warrior_vigilante", "level": 25, "class": "Commoner"},
        {"name": "Aerin", "gender": "Male", "race": "Imperial", "role": "citizen_rescuer", "level": 4, "class": "Commoner"},
    ],
    9003: [ # Black-Briar Meadery
        {"name": "Hemming Black-Briar", "gender": "Male", "race": "Nord", "role": "noble_bully", "level": 10, "class": "Noble"},
        {"name": "Indaryn", "gender": "Male", "race": "Dunmer", "role": "meadery_foreman", "level": 8, "class": "Commoner"},
        {"name": "Romlyn Dreth", "gender": "Male", "race": "Dunmer", "role": "meadery_worker_smuggler", "level": 3, "class": "Commoner"},
    ],
    9004: [ # Mistveil Keep
        {"name": "Laila Law-Giver", "gender": "Female", "race": "Nord", "role": "jarl", "level": 17, "class": "Noble"},
        {"name": "Anuriel", "gender": "Female", "race": "Bosmer", "role": "steward_thief", "level": 10, "class": "Noble"},
        {"name": "Unmid Snow-Shod", "gender": "Male", "race": "Nord", "role": "housecarl", "level": 15, "class": "Noble"},
        {"name": "Wylandriah", "gender": "Female", "race": "Bosmer", "role": "court_wizard_absentminded", "level": 12, "class": "Noble"},
        {"name": "Maven Black-Briar", "gender": "Female", "race": "Nord", "role": "matriarch_criminal_mastermind", "level": 30, "class": "Noble"},
    ],
    9005: [ # The Ragged Flagon
        {"name": "Brynjolf", "gender": "Male", "race": "Nord", "role": "thieves_guild_lieutenant", "level": 35, "class": "Commoner"},
        {"name": "Delvin Mallory", "gender": "Male", "race": "Breton", "role": "thieves_guild_master", "level": 30, "class": "Commoner"},
        {"name": "Vex", "gender": "Female", "race": "Nord", "role": "thieves_guild_master", "level": 30, "class": "Commoner"},
        {"name": "Tonilia", "gender": "Female", "race": "Redguard", "role": "thieves_guild_fence", "level": 15, "class": "Commoner"},
        {"name": "Dirge", "gender": "Male", "race": "Nord", "role": "thieves_guild_bouncer", "level": 18, "class": "Commoner"},
        {"name": "Sapphire", "gender": "Female", "race": "Nord", "role": "thieves_guild_member", "level": 12, "class": "Commoner"},
    ],
    9006: [ # Temple of Mara
        {"name": "Dinya Baliu", "gender": "Female", "race": "Dunmer", "role": "priestess_mara", "level": 7, "class": "Commoner"},
    ],
    9007: [ # Honorhall Orphanage
        {"name": "Grelod the Kind", "gender": "Female", "race": "Nord", "role": "orphanage_headmistress_cruel", "level": 2, "class": "Commoner"},
        {"name": "Constance Michel", "gender": "Female", "race": "Imperial", "role": "orphanage_assistant", "level": 3, "class": "Commoner"},
    ],
    9008: [ # The Scorched Hammer
        {"name": "Balimund", "gender": "Male", "race": "Nord", "role": "blacksmith", "level": 8, "class": "Commoner"},
    ],
    9009: [ # Elgrim's Elixirs
        {"name": "Elgrim", "gender": "Male", "race": "Altmer", "role": "alchemist_merchant", "level": 7, "class": "Commoner"},
        {"name": "Hafjorg", "gender": "Female", "race": "Nord", "role": "alchemist_merchant_spouse", "level": 5, "class": "Commoner"},
    ],
    9101: [ # Vilemyr Inn
        {"name": "Wilhelm", "gender": "Male", "race": "Nord", "role": "innkeeper", "level": 6, "class": "Commoner"},
        {"name": "Klimmek", "gender": "Male", "race": "Nord", "role": "citizen_climber", "level": 4, "class": "Commoner"},
    ],
    9102: [ # Shor's Stone
        {"name": "Filnjar", "gender": "Male", "race": "Nord", "role": "blacksmith_foreman", "level": 7, "class": "Commoner"},
        {"name": "Sylgja", "gender": "Female", "race": "Nord", "role": "miner", "level": 3, "class": "Commoner"},
    ],
    90001: [ # Treva's Watch
        {"name": "Stalleo", "gender": "Male", "race": "Nord", "role": "warrior_homesteader", "level": 18, "class": "Commoner"},
    ],
    90002: [ # Nilheim
        {"name": "Telrav", "gender": "Male", "race": "Breton", "role": "bandit_leader_deceiver", "level": 10, "class": "Commoner"},
    ],
    11001: [ # The Retching Netch
        {"name": "Geldis Sadri", "gender": "Male", "race": "Dunmer", "role": "cornerclub_owner", "level": 7, "class": "Commoner"},
        {"name": "Drovas Relvi", "gender": "Male", "race": "Dunmer", "role": "server_wizard_apprentice", "level": 4, "class": "Commoner"},
    ],
    11002: [ # Morvayn Manor
        {"name": "Lleril Morvayn", "gender": "Male", "race": "Dunmer", "role": "house_redoran_councilor", "level": 25, "class": "Noble"},
        {"name": "Adril Arano", "gender": "Male", "race": "Dunmer", "role": "second_councilor", "level": 20, "class": "Noble"},
        {"name": "Cindiri Arano", "gender": "Female", "race": "Dunmer", "role": "councilor_spouse", "level": 8, "class": "Noble"},
    ],
    11003: [ # Glover Mallory's House
        {"name": "Glover Mallory", "gender": "Male", "race": "Breton", "role": "blacksmith_thief", "level": 15, "class": "Commoner"},
    ],
    11004: [ # Raven Rock Mine
        {"name": "Crescius Caerellius", "gender": "Male", "race": "Imperial", "role": "mine_foreman_elder", "level": 8, "class": "Commoner"},
        {"name": "Aphia Velothi", "gender": "Female", "race": "Dunmer", "role": "mine_foreman_spouse", "level": 5, "class": "Commoner"},
    ],
    11006: [ # The Bulwark
        {"name": "Captain Veleth", "gender": "Male", "race": "Dunmer", "role": "redoran_guard_captain", "level": 20, "class": "Commoner"},
    ],
    11007: [ # Severin Manor
        {"name": "Vendil Severin", "gender": "Male", "race": "Dunmer", "role": "conspirator", "level": 15, "class": "Commoner"},
        {"name": "Mirri Severin", "gender": "Female", "race": "Dunmer", "role": "conspirator", "level": 12, "class": "Commoner"},
        {"name": "Tilisu Severin", "gender": "Female", "race": "Dunmer", "role": "conspirator", "level": 12, "class": "Commoner"},
    ],
    11101: [ # Tel Mithryn
        {"name": "Neloth", "gender": "Male", "race": "Dunmer", "role": "master_wizard_telvanni", "level": 60, "class": "Noble"},
        {"name": "Talvas Fathryon", "gender": "Male", "race": "Dunmer", "role": "mage_apprentice", "level": 10, "class": "Commoner"},
        {"name": "Varona Nelas", "gender": "Female", "race": "Dunmer", "role": "steward", "level": 5, "class": "Commoner"},
        {"name": "Elynea Mothren", "gender": "Female", "race": "Dunmer", "role": "alchemist_merchant", "level": 8, "class": "Commoner"},
    ],
    11201: [ # Skaal Village Greathall
        {"name": "Storn Crag-Strider", "gender": "Male", "race": "Nord", "role": "skaal_shaman", "level": 40, "class": "Noble"},
        {"name": "Frea", "gender": "Female", "race": "Nord", "role": "skaal_warrior", "level": 30, "class": "Commoner"},
        {"name": "Fanari Strong-Voice", "gender": "Female", "race": "Nord", "role": "skaal_chieftain", "level": 15, "class": "Noble"},
        {"name": "Deor Woodcutter", "gender": "Male", "race": "Nord", "role": "skaal_hunter", "level": 7, "class": "Commoner"},
    ],
    110001: [ # Ashfallow Citadel
        {"name": "Vendil Ulen", "gender": "Male", "race": "Dunmer", "role": "morag_tong_assassin", "level": 25, "class": "Commoner"},
    ],
    12001: [ # Fort Dawnguard
        {"name": "Isran", "gender": "Male", "race": "Redguard", "role": "dawnguard_leader", "level": 45, "class": "Commoner"},
        {"name": "Celann", "gender": "Male", "race": "Breton", "role": "dawnguard_warrior", "level": 25, "class": "Commoner"},
        {"name": "Durak", "gender": "Male", "race": "Orc", "role": "dawnguard_warrior_scout", "level": 25, "class": "Commoner"},
        {"name": "Sorine Jurard", "gender": "Female", "race": "Breton", "role": "dawnguard_expert_dwemer", "level": 20, "class": "Commoner"},
        {"name": "Gunmar", "gender": "Male", "race": "Nord", "role": "dawnguard_expert_blacksmith", "level": 20, "class": "Commoner"},
        {"name": "Florentius Baenius", "gender": "Male", "race": "Imperial", "role": "dawnguard_priest_arkay", "level": 15, "class": "Commoner"},
        {"name": "Agmaer", "gender": "Male", "race": "Nord", "role": "dawnguard_recruit", "level": 8, "class": "Commoner"},
    ],
    12002: [ # Castle Volkihar
        {"name": "Lord Harkon", "gender": "Male", "race": "Nord", "role": "vampire_lord_volkihar", "level": 70, "class": "Noble"},
        {"name": "Serana", "gender": "Female", "race": "Nord", "role": "vampire_lord_ancient", "level": 50, "class": "Noble"},
        {"name": "Vingalmo", "gender": "Male", "race": "Altmer", "role": "vampire_advisor", "level": 40, "class": "Noble"},
        {"name": "Orthjolf", "gender": "Male", "race": "Nord", "role": "vampire_master", "level": 35, "class": "Commoner"},
        {"name": "Garan Marethi", "gender": "Male", "race": "Dunmer", "role": "vampire_ritualist", "level": 30, "class": "Commoner"},
        {"name": "Fura Bloodmouth", "gender": "Female", "race": "Nord", "role": "vampire_master", "level": 30, "class": "Commoner"},
    ],
    12004: [ # The Forgotten Vale
        {"name": "Knight-Paladin Gelebor", "gender": "Male", "race": "Snow Elf", "role": "falmer_knight_ancient", "level": 60, "class": "Noble"},
        {"name": "Arch-Curate Vyrthur", "gender": "Male", "race": "Snow Elf", "role": "falmer_vampire_arch_curate", "level": 75, "class": "Noble"},
    ],
    12005: [ # Soul Cairn
        {"name": "Valerica", "gender": "Female", "race": "Nord", "role": "vampire_lady_alchemist", "level": 55, "class": "Noble"},
        {"name": "Durnehviir", "gender": "Male", "race": "Dragon", "role": "dragon_undead", "level": 40, "class": "Noble"},
    ],
    13001: [ # Apocrypha
        {"name": "Miraak", "gender": "Male", "race": "Nord", "role": "first_dragonborn_antagonist", "level": 150, "class": "Noble"},
    ],
    13002: [ # Sovngarde
        {"name": "Tsun", "gender": "Male", "race": "Nord", "role": "god_guardian", "level": 200, "class": "Noble"},
    ],
    14001: [ # Traveling
        {"name": "Mai'q the Liar", "gender": "Male", "race": "Khajiit", "role": "traveler_mysterious", "level": 20, "class": "Commoner"},
        {"name": "Talsgar the Wanderer", "gender": "Male", "race": "Nord", "role": "traveling_bard", "level": 6, "class": "Commoner"},
    ],
    14002: [ # Angi's Camp
        {"name": "Angi", "gender": "Female", "race": "Nord", "role": "archer_hermit_trainer", "level": 10, "class": "Commoner"},
    ],
    14003: [ # Froki's Shack
        {"name": "Froki Whetted-Blade", "gender": "Male", "race": "Nord", "role": "hunter_hermit_elder", "level": 9, "class": "Commoner"},
        {"name": "Haming", "gender": "Male", "race": "Nord", "role": "child_hunter", "level": 1, "class": "Commoner"},
    ],
}