# fixed_npc_data.py

# This file contains the data for all fixed, named NPCs in the game world.
# The structure is a dictionary where keys are location IDs and values are lists
# of NPC data dictionaries.
# Roles used here (e.g., "jarl") are reserved for these characters and are not
# intended for use by the random NPC generator.

FIXED_NPC_DATA = {
    # === WHITERUN HOLD ===
    # Dragonsreach (ID: 1001)
    1001: [
        {"name": "Balgruuf the Greater", "race": "Nord", "role": "jarl", "level": 20},
        {"name": "Irileth", "race": "Dunmer", "role": "housecarl", "level": 15},
        {"name": "Proventus Avenicci", "race": "Imperial", "role": "steward", "level": 10},
        {"name": "Farengar Secret-Fire", "race": "Nord", "role": "court_wizard", "level": 12},
    ],
    # Jorrvaskr (ID: 1002)
    1002: [
        {"name": "Kodlak Whitemane", "race": "Nord", "role": "companion", "level": 25},
        {"name": "Vilkas", "race": "Nord", "role": "companion", "level": 15},
        {"name": "Farkas", "race": "Nord", "role": "companion", "level": 15},
        {"name": "Aela the Huntress", "race": "Nord", "role": "companion", "level": 16},
        {"name": "Skjor", "race": "Nord", "role": "companion", "level": 16},
    ],
    # The Bannered Mare (ID: 1003)
    1003: [
        {"name": "Hulda", "race": "Nord", "role": "innkeeper", "level": 8},
        {"name": "Saadia", "race": "Redguard", "role": "server", "level": 3},
        {"name": "Uthgerd the Unbroken", "race": "Nord", "role": "warrior", "level": 6},
    ],
    # Warmaiden's (ID: 1004)
    1004: [
        {"name": "Adrianne Avenicci", "race": "Imperial", "role": "blacksmith", "level": 7},
        {"name": "Ulfberth War-Bear", "race": "Nord", "role": "merchant", "level": 6},
    ],
    # Arcadia's Cauldron (ID: 1005)
    1005: [
        {"name": "Arcadia", "race": "Imperial", "role": "alchemist", "level": 5},
    ],
    # Belethor's General Goods (ID: 1009)
    1009: [
        {"name": "Belethor", "race": "Breton", "role": "merchant", "level": 4},
    ],
    # Riverwood (various sub-locations)
    1101: [ # Sleeping Giant Inn
        {"name": "Delphine", "race": "Breton", "role": "innkeeper", "level": 15},
        {"name": "Orgnar", "race": "Nord", "role": "innkeeper", "level": 5},
    ],
    1102: [ # Riverwood Trader
        {"name": "Lucan Valerius", "race": "Imperial", "role": "merchant", "level": 4},
        {"name": "Camilla Valerius", "race": "Imperial", "role": "shop_assistant", "level": 3},
    ],

    # === HAAFINGAR (Solitude) ===
    # Blue Palace (ID: 8001)
    8001: [
        {"name": "Elisif the Fair", "race": "Nord", "role": "jarl", "level": 18},
        {"name": "Sybille Stentor", "race": "Breton", "role": "court_wizard", "level": 15},
        {"name": "Falk Firebeard", "race": "Nord", "role": "steward", "level": 12},
    ],
    # Castle Dour (ID: 8002)
    8002: [
        {"name": "General Tullius", "race": "Imperial", "role": "legion_legate", "level": 25},
        {"name": "Legate Rikke", "race": "Nord", "role": "imperial_soldier", "level": 18}, # Role is soldier, rank is implicit
    ],
    # The Winking Skeever (ID: 8003)
    8003: [
        {"name": "Corpulus Vinius", "race": "Imperial", "role": "innkeeper", "level": 7},
        {"name": "Gulum-Ei", "race": "Argonian", "role": "thief", "level": 5},
    ],
    # Bards College (ID: 8009)
    8009: [
        {"name": "Viarmo", "race": "Altmer", "role": "bard", "level": 10}, # Role as headmaster
        {"name": "Giraud Gemane", "race": "Breton", "role": "bard", "level": 8},
    ],

    # === THE RIFT (Riften) ===
    # Mistveil Keep (ID: 9004)
    9004: [
        {"name": "Laila Law-Giver", "race": "Nord", "role": "jarl", "level": 17},
        {"name": "Maven Black-Briar", "race": "Nord", "role": "noble", "level": 22},
    ],
    # The Ragged Flagon (ID: 90051)
    90051: [
        {"name": "Brynjolf", "race": "Nord", "role": "thieves_guild_member", "level": 18},
        {"name": "Delvin Mallory", "race": "Breton", "role": "thieves_guild_member", "level": 16},
        {"name": "Vex", "race": "Nord", "role": "thieves_guild_member", "level": 16},
    ],
    # The Cistern (ID: 90052)
    90052: [
        {"name": "Mercer Frey", "race": "Breton", "role": "thieves_guild_member", "level": 25}, # Guild Master
    ],

    # === EASTMARCH (Windhelm) ===
    # Palace of the Kings (ID: 7003)
    7003: [
        {"name": "Ulfric Stormcloak", "race": "Nord", "role": "jarl", "level": 30},
        {"name": "Galmar Stone-Fist", "race": "Nord", "role": "stormcloak_general", "level": 25},
        {"name": "Wuunferth the Unliving", "race": "Nord", "role": "court_wizard", "level": 20},
    ],

    # === WINTERHOLD (Town Remnants) ===
    # The Frozen Hearth (ID: 3001)
    3001: [
        {"name": "Dagur", "race": "Nord", "role": "innkeeper", "level": 7},
        {"name": "Nelacar", "race": "Altmer", "role": "scholar_mage_reclusive", "level": 10}
    ],
    # Birna's Oddments (ID: 3004)
    3004: [
        {"name": "Birna", "race": "Nord", "role": "merchant_general_goods", "level": 3}
    ],

    # === DAWNSTAR (City) ===
    # Windpeak Inn (ID: 2001)
    2001: [
        {"name": "Thoring", "race": "Nord", "role": "innkeeper", "level": 6},
        {"name": "Karita", "race": "Nord", "role": "bard_local", "level": 4}
    ],
    # Quicksilver Mine (ID: 2002)
    2002: [
       {"name": "Leigelf", "race": "Nord", "role": "mine_owner", "level": 7}
    ],
    # The Mortar and Pestle (ID: 2003)
    2003: [
        {"name": "Frida", "race": "Nord", "role": "alchemist_merchant", "level": 5}
    ],
    # The White Hall (ID: 2004)
    2004: [
        {"name": "Skald the Elder", "race": "Nord", "role": "jarl_stormcloak", "level": 10},
        {"name": "Brina Merilis", "race": "Imperial", "role": "jarl_advisor", "level": 8}
    ],
    # Rustleif's House and Smithy (ID: 2005)
    2005: [
        {"name": "Rustleif", "race": "Nord", "role": "blacksmith", "level": 6},
        {"name": "Seren", "race": "Redguard", "role": "blacksmith_spouse", "level": 3}
    ],

    # === FALKREATH (Town) ===
    # Dead Man's Drink (ID: 5001)
    5001: [
        {"name": "Valga Vinicia", "race": "Imperial", "role": "innkeeper", "level": 6},
        {"name": "Narri", "race": "Nord", "role": "tavern_staff_server", "level": 3},
        {"name": "Tekla", "race": "Nord", "role": "tavern_staff_server", "level": 3}
    ],
    # Gray Pine Goods (ID: 5004)
    5004: [
        {"name": "Solaf", "race": "Nord", "role": "merchant_general_goods", "level": 5}
    ],
    # Lod's House and Smithy (ID: 5005)
    5005: [
        {"name": "Lod", "race": "Nord", "role": "blacksmith", "level": 6}
    ],

    # === EASTMARCH (Kynesgrove) ===
    # Braidwood Inn (ID: 7101)
    7101: [
        {"name": "Iddra", "race": "Nord", "role": "innkeeper", "level": 5},
        {"name": "Roggi Knot-Beard", "race": "Nord", "role": "miner_patron", "level": 3}
    ],

    # === MARKARTH (City) ===
    # Silver-Blood Inn (ID: 6001)
    6001: [
        {"name": "Kleppr", "race": "Nord", "role": "innkeeper", "level": 6},
        {"name": "Frabbi", "race": "Nord", "role": "server", "level": 4}
    ],
    # Arnleif and Sons Trading Company (ID: 6004)
    6004: [
        {"name": "Lisbet", "race": "Breton", "role": "merchant_general_goods", "level": 5}
    ],
    # The Hag's Cure (ID: 6005)
    6005: [
        {"name": "Bothela", "race": "Breton", "role": "alchemist_merchant_elder", "level": 8},
        {"name": "Muiri", "race": "Breton", "role": "alchemist_apprentice", "level": 3}
    ],
    # Ghorza's Smithy (ID: 6008)
    6008: [
        {"name": "Ghorza gra-Bagol", "race": "Orc", "role": "blacksmith_trainer", "level": 7}
    ],

    # === RIFTEN (City) ===
    # The Bee and Barb (ID: 9001)
    9001: [
        {"name": "Talen-Jei", "race": "Argonian", "gender": "Male", "role": "publican", "level": 6},
        {"name": "Keerava", "race": "Argonian", "gender": "Female", "role": "publican", "level": 6}
    ]
    # This dictionary can be expanded with every fixed NPC in Skyrim.
}