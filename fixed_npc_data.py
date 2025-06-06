# fixed_npc_data.py

# This file contains the data for all fixed, named NPCs in the game world.
# The structure is a dictionary where keys are location IDs and values are lists
# of NPC data dictionaries.

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
    ]
    # ...This dictionary can be expanded with every fixed NPC in Skyrim.
}