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
        {"name": "Balgruuf the Greater", "race": "Nord", "role": "jarl", "level": 20},
        {"name": "Irileth", "race": "Dunmer", "role": "housecarl", "level": 15},
        {"name": "Proventus Avenicci", "race": "Imperial", "role": "steward", "level": 10},
        {"name": "Farengar Secret-Fire", "race": "Nord", "role": "court_wizard", "level": 12},
    ],
    1002: [ # Jorrvaskr
        {"name": "Kodlak Whitemane", "race": "Nord", "role": "companion", "level": 25},
        {"name": "Vilkas", "race": "Nord", "role": "companion", "level": 15},
        {"name": "Farkas", "race": "Nord", "role": "companion", "level": 15},
        {"name": "Aela the Huntress", "race": "Nord", "role": "companion", "level": 16},
        {"name": "Skjor", "race": "Nord", "role": "companion", "level": 16},
    ],
    1003: [ # The Bannered Mare
        {"name": "Hulda", "race": "Nord", "role": "innkeeper", "level": 8},
        {"name": "Saadia", "race": "Redguard", "role": "server", "level": 3},
        {"name": "Uthgerd the Unbroken", "race": "Nord", "role": "warrior", "level": 6},
    ],
    1004: [ # Warmaiden's
        {"name": "Adrianne Avenicci", "race": "Imperial", "role": "blacksmith", "level": 7},
        {"name": "Ulfberth War-Bear", "race": "Nord", "role": "merchant_blacksmith_shopkeeper", "level": 6}
    ],
    1005: [ # Arcadia's Cauldron
        {"name": "Arcadia", "race": "Imperial", "role": "alchemist_merchant", "level": 5}
    ],
    1008: [ # The Drunken Huntsman
        {"name": "Elrindir", "race": "Bosmer", "role": "innkeeper", "level": 6},
        {"name": "Jenassa", "race": "Dunmer", "role": "mercenary_archer", "level": 5}
    ],
    1009: [ # Belethor's General Goods
        {"name": "Belethor", "race": "Breton", "role": "merchant_general_goods", "level": 4},
        {"name": "Sigurd", "race": "Nord", "role": "shop_assistant_woodcutter", "level": 2}
    ],
    # Riverwood
    1101: [ # Sleeping Giant Inn
        {"name": "Delphine", "race": "Breton", "role": "innkeeper_secretive", "level": 15},
        {"name": "Orgnar", "race": "Nord", "role": "innkeeper", "level": 5},
    ],
    1102: [ # Riverwood Trader
        {"name": "Lucan Valerius", "race": "Imperial", "role": "merchant", "level": 4},
        {"name": "Camilla Valerius", "race": "Imperial", "role": "shop_assistant", "level": 3},
    ],
    1103: [ # Alvor's Smithy
        {"name": "Alvor", "race": "Nord", "role": "blacksmith", "level": 6},
        {"name": "Sigrid", "race": "Nord", "role": "blacksmith_spouse", "level": 3}
    ],
     1201: [ # Frostfruit Inn (Rorikstead)
        {"name": "Mralki", "race": "Nord", "role": "innkeeper", "level": 6},
        {"name": "Erikur", "race": "Nord", "role": "innkeeper_spouse", "level": 5}
    ],
    # Other Whiterun Hold Locations
    10003: [ # White River Watch
        {"name": "Hajvarr Iron-Hand", "race": "Nord", "role": "bandit_leader", "level": 10}
    ],

    # === THE PALE (Dawnstar) ===
    2001: [ # Windpeak Inn
        {"name": "Thoring", "race": "Nord", "role": "innkeeper", "level": 6},
        {"name": "Karita", "race": "Nord", "role": "bard_local", "level": 4}
    ],
    2002: [ # Quicksilver Mine
       {"name": "Leigelf", "race": "Nord", "role": "mine_owner", "level": 7}
    ],
    2003: [ # The Mortar and Pestle
        {"name": "Frida", "race": "Nord", "role": "alchemist_merchant", "level": 5}
    ],
    2004: [ # The White Hall
        {"name": "Skald the Elder", "race": "Nord", "role": "jarl_stormcloak", "level": 10},
        {"name": "Brina Merilis", "race": "Imperial", "role": "jarl_advisor", "level": 8}
    ],
    2005: [ # Rustleif's House and Smithy
        {"name": "Rustleif", "race": "Nord", "role": "blacksmith", "level": 6},
        {"name": "Seren", "race": "Redguard", "role": "blacksmith_spouse", "level": 3}
    ],

    # === WINTERHOLD ===
    3001: [ # The Frozen Hearth
        {"name": "Dagur", "race": "Nord", "role": "innkeeper", "level": 7},
        {"name": "Nelacar", "race": "Altmer", "role": "scholar_mage_reclusive", "level": 10}
    ],
    3004: [ # Birna's Oddments
        {"name": "Birna", "race": "Nord", "role": "merchant_general_goods", "level": 3}
    ],

    # === HJAALMARCH (Morthal) ===
    4002: [ # Moorside Inn
        {"name": "Jonna", "race": "Nord", "role": "innkeeper", "level": 5},
        {"name": "Lurbuk", "race": "Orc", "role": "untalented_bard", "level": 3}
    ],
     4003: [ # Thaumaturgist's Hut
        {"name": "Falion", "race": "Redguard", "role": "mage_conjurer_scholar_vampire_expert", "level": 12}
    ],

    # === FALKREATH HOLD ===
    5001: [ # Dead Man's Drink
        {"name": "Valga Vinicia", "race": "Imperial", "role": "innkeeper", "level": 6},
        {"name": "Narri", "race": "Nord", "role": "tavern_staff_server", "level": 3},
        {"name": "Tekla", "race": "Nord", "role": "tavern_staff_server", "level": 3}
    ],
    5004: [ # Gray Pine Goods
        {"name": "Solaf", "race": "Nord", "role": "merchant_general_goods", "level": 5}
    ],
    5005: [ # Lod's House and Smithy
        {"name": "Lod", "race": "Nord", "role": "blacksmith", "level": 6}
    ],

    # === THE REACH (Markarth) ===
    6001: [ # Silver-Blood Inn
        {"name": "Kleppr", "race": "Nord", "role": "innkeeper", "level": 6},
        {"name": "Frabbi", "race": "Nord", "role": "server", "level": 4}
    ],
    6004: [ # Arnleif and Sons Trading Company
        {"name": "Lisbet", "race": "Breton", "role": "merchant_general_goods", "level": 5}
    ],
    6005: [ # The Hag's Cure
        {"name": "Bothela", "race": "Breton", "role": "alchemist_merchant_elder", "level": 8},
        {"name": "Muiri", "race": "Breton", "role": "alchemist_apprentice", "level": 3}
    ],
    6008: [ # Ghorza's Smithy
        {"name": "Ghorza gra-Bagol", "race": "Orc", "role": "blacksmith_trainer", "level": 7}
    ],
    # Karthwasten
    6101: [ # Karthwasten Hall
        {"name": "Ainethach", "race": "Breton", "role": "mine_owner_community_leader", "level": 7}
    ],

    # === EASTMARCH (Windhelm) ===
    7001: [ # Candlehearth Hall
        {"name": "Elda Early-Dawn", "race": "Nord", "role": "innkeeper", "level": 7},
        {"name": "Susanna the Wicked", "race": "Nord", "role": "tavern_staff_server", "level": 4}
    ],
    7002: [ # Oengul's Smithy
        {"name": "Oengul War-Anvil", "race": "Nord", "role": "blacksmith_stormcloak_supporter", "level": 8},
        {"name": "Hermir Strong-Heart", "race": "Nord", "role": "blacksmith_apprentice", "level": 4}
    ],
    7003: [ # Palace of the Kings
        {"name": "Ulfric Stormcloak", "race": "Nord", "role": "jarl", "level": 30},
        {"name": "Galmar Stone-Fist", "race": "Nord", "role": "stormcloak_general", "level": 25},
        {"name": "Wuunferth the Unliving", "race": "Nord", "role": "court_wizard", "level": 20},
    ],
    7005: [ # Sadri's Used Wares
        {"name": "Revyn Sadri", "race": "Dunmer", "role": "merchant_general_goods", "level": 4}
    ],
    7006: [ # Windhelm Market Square
        {"name": "Aval Atheron", "race": "Dunmer", "role": "merchant_stall_general", "level": 3},
        {"name": "Niranye", "race": "Altmer", "role": "merchant_stall_pawnbroker_fence", "level": 6}
    ],
    7013: [ # New Gnisis Cornerclub
        {"name": "Ambarys Rendar", "race": "Dunmer", "role": "innkeeper_dunmer_community", "level": 6}
    ],
    # Kynesgrove
    7101: [ # Braidwood Inn
        {"name": "Iddra", "race": "Nord", "role": "innkeeper", "level": 5},
        {"name": "Roggi Knot-Beard", "race": "Nord", "role": "miner_patron", "level": 3}
    ],


    # === HAAFINGAR (Solitude) ===
    8001: [ # Blue Palace
        {"name": "Elisif the Fair", "race": "Nord", "role": "jarl", "level": 18},
        {"name": "Sybille Stentor", "race": "Breton", "role": "court_wizard", "level": 15},
        {"name": "Falk Firebeard", "race": "Nord", "role": "steward", "level": 12},
    ],
    8002: [ # Castle Dour
        {"name": "General Tullius", "race": "Imperial", "role": "legion_legate", "level": 25},
        {"name": "Legate Rikke", "race": "Nord", "role": "imperial_soldier", "level": 18},
    ],
    8003: [ # The Winking Skeever
        {"name": "Corpulus Vinius", "race": "Imperial", "role": "innkeeper", "level": 7},
        {"name": "Gulum-Ei", "race": "Argonian", "role": "shady_patron", "level": 5},
    ],
    8004: [ # Bits and Pieces
        {"name": "Sayma", "race": "Imperial", "role": "merchant_general_goods", "level": 6}
    ],
    8006: [ # Radiant Raiment
        {"name": "Taarie", "race": "Altmer", "role": "merchant_clothing_tailor_haughty", "level": 5},
        {"name": "Endarie", "race": "Altmer", "role": "merchant_clothing_tailor", "level": 5}
    ],
    8007: [ # Fletcher
        {"name": "Fihada", "race": "Redguard", "role": "merchant_fletcher", "level": 6}
    ],
    8009: [ # Bards College
        {"name": "Viarmo", "race": "Altmer", "role": "headmaster_bards_college", "level": 10},
        {"name": "Giraud Gemane", "race": "Breton", "role": "bard", "level": 8},
    ],

    # === THE RIFT (Riften) ===
    9001: [ # The Bee and Barb
        {"name": "Talen-Jei", "race": "Argonian", "role": "publican", "level": 6},
        {"name": "Keerava", "race": "Argonian", "role": "publican", "level": 6}
    ],
    9004: [ # Mistveil Keep
        {"name": "Laila Law-Giver", "race": "Nord", "role": "jarl", "level": 17},
        {"name": "Maven Black-Briar", "race": "Nord", "role": "noble", "level": 22},
    ],
    90051: [ # The Ragged Flagon
        {"name": "Brynjolf", "race": "Nord", "role": "thieves_guild_member", "level": 18},
        {"name": "Delvin Mallory", "race": "Breton", "role": "thieves_guild_member", "level": 16},
        {"name": "Vex", "race": "Nord", "role": "thieves_guild_member", "level": 16},
    ],
    90052: [ # The Cistern
        {"name": "Mercer Frey", "race": "Breton", "role": "guild_master_thieves", "level": 25},
    ]
}