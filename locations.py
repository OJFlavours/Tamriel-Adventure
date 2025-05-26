LOCATIONS = [
    # WHITERUN HOLD
    {
        "id": 1,
        "name": "Whiterun Hold",
        "desc": "The fertile heartland of Skyrim, marked by golden plains and the bustling city of Whiterun. A center of commerce, conflict, and tradition.",
        "tags": ["hold", "plains", "central", "commerce", "nordic"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["The Rift", "Eastmarch", "The Reach", "Haafingar", "Falkreath Hold", "The Pale"], # Roads connect to holds now
            "paths": ["Riverwood", "Rorikstead", "Helgen"] # Specific paths
        },
        "sub_locations": [
            {
                "id": 10,
                "name": "Whiterun",
                "desc": "A thriving trade city built around the great keep Dragonsreach. Its bustling market and legendary mead hall form the heart of the hold.",
                "tags": ["city", "capital", "trade", "whiterun", "market", "jarls_seat", "companions_guild", "temple", "imperial_presence"],
                "sub_locations": [
                    {
                        "id": 1001,
                        "name": "Dragonsreach",
                        "desc": "The imposing keep of the Jarl, an iconic symbol of Nord authority and power, once used to imprison a dragon.",
                        "tags": ["keep", "government", "historic", "jarls_seat"]
                    },
                    {
                        "id": 1002,
                        "name": "Jorrvaskr",
                        "desc": "The ancient mead hall and headquarters of the Companions, where warriors forge bonds in battle and honor tradition.",
                        "tags": ["meadhall", "companions_guild", "warrior_guild", "historic"]
                    },
                    {
                        "id": 1003,
                        "name": "The Bannered Mare",
                        "desc": "A lively tavern where travelers and locals share stories over hearty ale, a central hub of Whiterun's social life.",
                        "tags": ["tavern", "social", "inn"]
                    },
                    {
                        "id": 1004,
                        "name": "Warmaiden's",
                        "desc": "A masterful smithy known for crafting legendary weapons and armor, run by Adrianne Avenicci and Ulfberth War-Bear.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    },
                    {
                        "id": 1005,
                        "name": "Arcadia's Cauldron",
                        "desc": "A cozy apothecary brimming with rare ingredients and potent potions, run by the alchemist Arcadia.",
                        "tags": ["alchemy", "shop", "magic_vendor"]
                    },
                    {
                        "id": 1006,
                        "name": "Temple of Kynareth",
                        "desc": "A serene temple devoted to the wind and healing, centered around the Gildergreen tree and frequented by worshippers.",
                        "tags": ["temple", "religious", "healer", "kynareth"]
                    },
                    {
                        "id": 1007,
                        "name": "Plains District Market",
                        "desc": "Bustling stalls offering regional produce, crafts, and curiosities, the commercial heart of Whiterun.",
                        "tags": ["market", "trade"]
                    },
                    {
                        "id": 1008,
                        "name": "The Drunken Huntsman",
                        "desc": "A tavern popular with hunters and adventurers, known for its rustic charm and owned by Elrindir.",
                        "tags": ["tavern", "social"]
                    },
                    {
                        "id": 1009,
                        "name": "Belethor's General Goods",
                        "desc": "A shop stocking a wide variety of items, where Belethor claims everything is for sale... if the price is right.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 1010,
                        "name": "Hall of the Dead",
                        "desc": "A solemn place beneath the Temple of Kynareth where the Nords of Whiterun honor their ancestors and inter their dead.",
                        "tags": ["catacombs", "religious", "undead_potential"]
                    },
                    {
                        "id": 1011,
                        "name": "Carlotta Valentia's House",
                        "desc": "The home of Carlotta Valentia, a food vendor in the market, and her daughter Mila.",
                        "tags": ["residence"]
                    },
                    {
                        "id": 1012,
                        "name": "House Gray-Mane",
                        "desc": "A prominent and respected Nord family in Whiterun, known for their traditional values and support for the Stormcloaks.",
                        "tags": ["residence", "noble_house", "stormcloak_sympathizers"]
                    },
                    {
                        "id": 1013,
                        "name": "House Battle-Born",
                        "desc": "A wealthy and influential Nord family in Whiterun, strong supporters of the Empire.",
                        "tags": ["residence", "noble_house", "imperial_sympathizers"]
                    },
                    { # Added player home for completeness, though game mechanics for it aren't defined
                        "id": 1014,
                        "name": "Breezehome",
                        "desc": "A modest but cozy home available for purchase in Whiterun, conveniently located near the city gates.",
                        "tags": ["residence", "player_home"]
                    }
                ]
            },
            {
                "id": 11,
                "name": "Riverwood",
                "desc": "A quaint logging village along the White River, known for its simplicity and rustic charm, often the first stop for travelers from Helgen.",
                "tags": ["village", "lumber", "river"],
                "sub_locations": [
                    {
                        "id": 1101,
                        "name": "Sleeping Giant Inn",
                        "desc": "A warm inn that serves as a gathering point for weary travelers and locals, run by Orgnar.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 1102,
                        "name": "Riverwood Trader",
                        "desc": "A modest shop offering a variety of everyday goods, run by Lucan Valerius and his sister Camilla.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 1103,
                        "name": "Alvor's Smithy",
                        "desc": "The local blacksmith renowned for practical and durable tools, run by Alvor, Hadvar's uncle.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    },
                    {
                        "id": 1104,
                        "name": "Faendal's House",
                        "desc": "The home of Faendal, a Bosmer archer and lumberjack in Riverwood.",
                        "tags": ["residence"]
                    },
                    {
                        "id": 1105,
                        "name": "Sven and Hilde's House",
                        "desc": "The home of Sven, a local bard, and his mother Hilde.",
                        "tags": ["residence"]
                    }
                ]
            },
            {
                "id": 12,
                "name": "Rorikstead",
                "desc": "A fertile farming village that supplies Whiterun with delicious produce, demonstrating the rugged yet bountiful nature of Skyrim. Some whisper of dark dealings related to its unusual prosperity.",
                "tags": ["village", "farm", "mysterious"],
                "sub_locations": [
                    {
                        "id": 1201,
                        "name": "Frostfruit Inn",
                        "desc": "A cozy inn known for its warm hearth and local cider, run by Mralki.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 1202,
                        "name": "Rorikstead General Goods", # Generic name, as no specific shop is named in lore
                        "desc": "A small shop run by a local, offering essential supplies and some farm produce.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 1203,
                        "name": "Lemkil's Farmhouse",
                        "desc": "The farmstead of Lemkil, a local farmer in Rorikstead with two daughters.",
                        "tags": ["farm", "residence"]
                    },
                    {
                        "id": 1204,
                        "name": "Jouane Manette's House",
                        "desc": "The home of Jouane Manette, a Breton farmer in Rorikstead.",
                        "tags": ["residence", "farm"]
                    }
                ]
            },
            {
                "id": 13,
                "name": "Honningbrew Meadery",
                "desc": "Famed for its exceptionally smooth mead, a visit here is both a taste of history and local culture. It has recently faced competition and sabotage.",
                "tags": ["meadery", "brewery", "shop", "quest_location"]
            },
            {
                "id": 14,
                "name": "Western Watchtower",
                "desc": "A ruined guard tower on the outskirts of Whiterun, scarred by dragon fire. It was the site of the first dragon sighting in Whiterun Hold in the Fourth Era.",
                "tags": ["watchtower", "ruin", "dragon", "historic_event"]
            },
            {
                "id": 15,
                "name": "Bleak Falls Barrow",
                "desc": "An ancient Nordic tomb high among the mountains overlooking Riverwood, crawling with draugr and secrets of old, including a Word Wall.",
                "tags": ["barrow", "dungeon", "undead", "nordic_ruin", "dragon_word", "quest_location"]
            },
            {
                "id": 16,
                "name": "Silent Moons Camp",
                "desc": "A clandestine bandit camp hidden in the wilderness north-west of Whiterun, known for its lunar-enchanted weapons.",
                "tags": ["bandit_camp", "ruin", "dungeon", "lunar_forge"]
            },
            {
                "id": 17,
                "name": "Lund's Hut",
                "desc": "A small, isolated hut north of Rorikstead, once home to the unfortunate Lund.",
                "tags": ["hut", "abandoned", "wilderness"]
            },
            {
                "id": 18,
                "name": "Gjukar's Monument",
                "desc": "A stone monument south of Rorikstead, marking the site of an ancient battle and the resting place of the warrior Gjukar.",
                "tags": ["monument", "historic", "ghost_encounter"]
            },
            {
                "id": 19,
                "name": "Secunda's Kiss",
                "desc": "A giant's camp located west of Whiterun, named for the nearby moon Secunda.",
                "tags": ["giant_camp", "wilderness"]
            },
            {
                "id": 10001, # Adjusted ID to be unique from Whiterun sublocations
                "name": "Sleeping Tree Camp",
                "desc": "A giant's camp west of Whiterun, notable for a strange, glowing tree and the sap it produces.",
                "tags": ["giant_camp", "unique_flora", "alchemy_ingredient"]
            },
            {
                "id": 10002,
                "name": "Swindler's Den",
                "desc": "A cave system west of Whiterun, serving as a hideout for bandits and Kematu's Alik'r warriors.",
                "tags": ["cave", "bandit_hideout", "dungeon", "quest_location"]
            },
            {
                "id": 10003,
                "name": "White River Watch",
                "desc": "A small cave east of Honningbrew Meadery, inhabited by bandits led by Hajvarr Iron-Hand.",
                "tags": ["cave", "bandit_hideout", "dungeon"]
            },
            {
                "id": 10004,
                "name": "Halted Stream Camp",
                "desc": "A bandit-occupied iron mine north of Whiterun, containing a valuable spell tome.",
                "tags": ["mine", "bandit_camp", "dungeon", "spell_tome"]
            }
        ]
    },

    # THE PALE
    {
        "id": 2,
        "name": "The Pale",
        "desc": "A frozen hold of bleak beauty, stretching from snow-tipped plains to the Sea of Ghosts. Harsh and unforgiving, known for its mining town of Dawnstar and dangerous wildlife.",
        "tags": ["hold", "snow", "coastal", "mining", "nordic", "stormcloak_territory"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {
            "roads": ["Whiterun Hold", "Winterhold", "Eastmarch", "Hjaalmarch"],
            "paths": ["Icespire Trail", "Frostmere Road"]
        },
        "sub_locations": [
            {
                "id": 20,
                "name": "Dawnstar",
                "desc": "A resilient port town on the northern coast, thriving on fishing and mining. It is plagued by mysterious nightmares.",
                "tags": ["town", "port", "dawnstar", "isolated", "mining_town", "nightmares", "daedric_quest"],
                "sub_locations": [
                    {
                        "id": 2001,
                        "name": "Windpeak Inn",
                        "desc": "The cozy inn of Dawnstar, offering respite from the icy winds and a place for locals to gather.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 2002,
                        "name": "Quicksilver Mine",
                        "desc": "A productive quicksilver mine that is vital to Dawnstar's economy.",
                        "tags": ["mine", "resource", "economy"]
                    },
                    {
                        "id": 2003,
                        "name": "The Mortar and Pestle",
                        "desc": "Frida's alchemy shop, where local brews and potions are concocted.",
                        "tags": ["alchemy", "shop", "magic_vendor"]
                    },
                    {
                        "id": 2004,
                        "name": "The White Hall", # Jarl's Longhouse
                        "desc": "The seat of Dawnstar's Jarl, where decisions affecting The Pale are made.",
                        "tags": ["government", "jarls_seat"]
                    },
                    {
                        "id": 2005,
                        "name": "Rustleif's House and Smithy",
                        "desc": "The home and workshop of Rustleif, Dawnstar's blacksmith.",
                        "tags": ["blacksmith", "shop", "crafting", "residence"]
                    },
                    {
                        "id": 2006,
                        "name": "Dawnstar Sanctuary",
                        "desc": "A hidden sanctuary of the Dark Brotherhood, though its current status may be unknown or compromised.",
                        "tags": ["dark_brotherhood", "assassin_guild", "secret_location", "ruined_potential"]
                    }
                ]
            },
            {
                "id": 21,
                "name": "Nightcaller Temple",
                "desc": "An eerie, abandoned temple on a clifftop overlooking Dawnstar, source of the town's nightmares and dedicated to Vaermina.",
                "tags": ["temple", "daedric_shrine", "ruin", "dungeon", "vaermina", "quest_location"]
            },
            {
                "id": 22,
                "name": "Iron-Breaker Mine",
                "desc": "An iron mine located just outside Dawnstar, contributing to the town's resources.",
                "tags": ["mine", "resource"]
            },
            {
                "id": 23,
                "name": "Wreck of the Brinehammer",
                "desc": "The ghostly remains of a long-forgotten shipwreck scattered along the storm-battered coast south of Dawnstar.",
                "tags": ["wreck", "ruin", "dungeon", "coastal"]
            },
            {
                "id": 24,
                "name": "Frostflow Lighthouse",
                "desc": "A solitary lighthouse west of Dawnstar, now a scene of a gruesome mystery involving Falmer.",
                "tags": ["lighthouse", "haunted", "dungeon", "falmer", "quest_location"]
            },
            {
                "id": 25,
                "name": "Loreius Farm",
                "desc": "A small farmstead south of Dawnstar, owned by Vantus Loreius.",
                "tags": ["farm", "residence"]
            },
            {
                "id": 26,
                "name": "Nightgate Inn",
                "desc": "An isolated inn located at a pass on the road between The Pale and Eastmarch.",
                "tags": ["inn", "tavern", "isolated", "travel_stop"]
            },
            {
                "id": 27,
                "name": "Red Road Pass",
                "desc": "A bandit-infested pass through the mountains in the southern part of The Pale.",
                "tags": ["mountain_pass", "bandit_camp", "dungeon"]
            },
            {
                "id": 28,
                "name": "Shearpoint",
                "desc": "A dragon lair and Word Wall atop a mountain in The Pale, guarded by Krosis, a dragon priest.",
                "tags": ["dragon_lair", "dragon_word", "dragon_priest", "mountain_peak", "dungeon"]
            },
            {
                "id": 29,
                "name": "Shrouded Grove",
                "desc": "A small, hidden grove in The Pale, sometimes a site for unusual encounters or rituals.",
                "tags": ["grove", "wilderness", "mysterious"]
            },
            {
                "id": 20001, # Unique ID
                "name": "Silverdrift Lair",
                "desc": "A Nordic ruin west of Nightgate Inn, overrun by draugr.",
                "tags": ["nordic_ruin", "dungeon", "undead"]
            },
            {
                "id": 20002,
                "name": "Weynon Stones",
                "desc": "A small ruin southeast of Dawnstar, possibly with some minor significance or bandit activity.",
                "tags": ["ruin", "minor_landmark"]
            },
            {
                "id": 20003,
                "name": "Fort Dunstad",
                "desc": "A large fort in The Pale, strategically important and often contested during the Civil War.",
                "tags": ["fort", "military", "civil_war_site", "dungeon"]
            }
        ]
    },

    # WINTERHOLD HOLD (many locations are ruins or icy caves)
    {
        "id": 3,
        "name": "Winterhold Hold",
        "desc": "A shattered hold on the northern coast, defined by icy gales, ancient ruins, and the dominant presence of the College of Winterhold. Much of the original city was lost to the Great Collapse.",
        "tags": ["hold", "snow", "coastal", "magic", "ruin", "nordic", "college_of_winterhold"],
        "demographics": {"Nord": 75, "Altmer": 10, "Dunmer": 10, "Others": 5},
        "travel": {
            "roads": ["The Pale", "Eastmarch"],
            "paths": ["Saarthal Trail", "Glacial Path"]
        },
        "sub_locations": [
            {
                "id": 30,
                "name": "Winterhold (Town)",
                "desc": "A ghost of its former glory, this small town clings to the cliffs, overshadowed by the imposing College. Most of the original city lies beneath the waves.",
                "tags": ["town", "ruin", "winterhold", "magical", "great_collapse_site"],
                "sub_locations": [
                    {
                        "id": 3001,
                        "name": "The Frozen Hearth",
                        "desc": "The sole remaining inn in Winterhold, offering shelter and rumors to travelers and College members.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 3002,
                        "name": "College of Winterhold",
                        "desc": "A venerable institution of magic, perched precariously on a separated clifftop, a beacon for mages across Tamriel.",
                        "tags": ["college", "magic_guild", "mages_guild", "learning_center", "historic"]
                    },
                    {
                        "id": 3003,
                        "name": "Jarl's Longhouse (Winterhold)", # Renamed for clarity
                        "desc": "The modest seat of Winterhold's Jarl, a relic of the town's diminished status.",
                        "tags": ["government", "jarls_seat"]
                    },
                    {
                        "id": 3004,
                        "name": "Birna's Oddments",
                        "desc": "A small shop run by Birna, offering a curious selection of goods, often scavenged or of questionable origin.",
                        "tags": ["shop", "general"]
                    }
                ]
            },
            {
                "id": 31,
                "name": "Saarthal",
                "desc": "The excavated ruins of one of Skyrim's first human settlements, a site of great magical power and ancient Nordic mysteries, closely tied to the College.",
                "tags": ["nordic_ruin", "dungeon", "undead", "magic_artifact", "quest_location", "historic"]
            },
            {
                "id": 32,
                "name": "Hob's Fall Cave",
                "desc": "A shadowy coastal cave north of Winterhold, a den for necromancers and their unholy experiments.",
                "tags": ["cave", "necromancer", "dungeon", "coastal"]
            },
            {
                "id": 33,
                "name": "Yngol Barrow",
                "desc": "A mournful Nordic tomb east of Windhelm (close to Winterhold's border), where ancient magics linger and the ghost of Yngol's shade may be found.",
                "tags": ["barrow", "nordic_ruin", "undead", "dungeon", "ghost_encounter"]
            },
            { # Alftand is a major Dwemer ruin, critical for Blackreach access
                "id": 34, # New ID for Alftand as a primary location within Winterhold hold
                "name": "Alftand", # Already listed as ID 105, needs consolidation if this structure is preferred.
                "desc": "A vast and treacherous Dwemer ruin deep within the mountains of Winterhold, one of the primary entrances to Blackreach.",
                "tags": ["dwemer_ruin", "dungeon", "mechanical", "falmer", "blackreach_entrance", "quest_location"],
                "sub_locations": [
                    {
                        "id": 3401,
                        "name": "Alftand Glacial Ruins",
                        "desc": "The icy, upper exterior sections of Alftand, often patrolled by Falmer.",
                        "tags": ["ruin_exterior", "snow"]
                    },
                    {
                        "id": 3402,
                        "name": "Alftand Animonculory",
                        "desc": "The main Dwemer manufactory within Alftand, filled with constructs and traps.",
                        "tags": ["dwemer_constructs", "traps"]
                    },
                    {
                        "id": 3403,
                        "name": "Alftand Cathedral",
                        "desc": "The grand central chamber of Alftand, leading deeper into the earth and towards Blackreach.",
                        "tags": ["dwemer_architecture", "boss_area"]
                    }
                ]
            },
            {
                "id": 35,
                "name": "Frostmere Crypt", # Straddles Pale/Winterhold border
                "desc": "A Nordic barrow south of Dawnstar, near the Winterhold border, home to bandits and a legendary weapon known as 'The Pale Blade'.",
                "tags": ["nordic_ruin", "dungeon", "undead", "bandit_lair", "quest_location"]
            },
            {
                "id": 36,
                "name": "Pilgrim's Trench",
                "desc": "A shipwreck graveyard in the icy waters north of Winterhold, treacherous to navigate.",
                "tags": ["shipwreck_site", "underwater", "coastal", "dangerous_waters"]
            },
            {
                "id": 37,
                "name": "Sightless Pit",
                "desc": "A deep, dark chasm leading into a Falmer-infested cave system, located in the southwestern mountains of Winterhold.",
                "tags": ["cave", "falmer_den", "dungeon", "chasm"]
            },
            {
                "id": 38,
                "name": "Skytemple Ruins",
                "desc": "Ruined Nordic towers atop a mountain, offering a commanding view but little shelter.",
                "tags": ["nordic_ruin", "tower", "mountain_peak"]
            },
            {
                "id": 39,
                "name": "Snowpoint Beacon",
                "desc": "A ruined watchtower on the northern coast of Winterhold, now a desolate landmark.",
                "tags": ["watchtower", "ruin", "coastal"]
            },
            {
                "id": 30001, # Unique ID
                "name": "Ysgramor's Tomb",
                "desc": "The final resting place of the legendary Ysgramor, founder of the Companions. A revered and dangerous Nordic tomb.",
                "tags": ["nordic_ruin", "tomb", "historic", "companions_quest", "undead", "dungeon"]
            },
            {
                "id": 30002,
                "name": "The Serpent Stone",
                "desc": "A Standing Stone located on an island in the Sea of Ghosts, north of the College of Winterhold, granting a unique magical power.",
                "tags": ["standing_stone", "magic_buff", "island", "coastal"]
            },
            {
                "id": 30003,
                "name": "Driftshade Refuge",
                "desc": "An abandoned fort in Winterhold, later occupied by the Silver Hand.",
                "tags": ["fort", "ruin", "silver_hand_lair", "dungeon"]
            }
        ]
    },
    # HJAALMARCH (Morthal Hold)
    {
        "id": 4,
        "name": "Hjaalmarch",
        "desc": "A bleak, marshy hold shrouded in perpetual mist and steeped in superstition. Its capital, Morthal, is known for its reclusive nature and troubles with vampires and strange occurrences.",
        "tags": ["hold", "marsh", "swamp", "isolated", "nordic", "superstition", "vampire_threat"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {
            "roads": ["The Pale", "The Reach", "Haafingar"],
            "paths": ["Stonehills Trail", "Drajkmyr Marsh"]
        },
        "sub_locations": [
            {
                "id": 40,
                "name": "Morthal",
                "desc": "A somber town built on the edge of the Drajkmyr Marsh, wrapped in fog and mystery. It is the site of recent tragedies and vampire hunts.",
                "tags": ["town", "marsh", "morthal", "superstitious", "vampire_quest", "jarls_seat"],
                "sub_locations": [
                    {
                        "id": 4001,
                        "name": "Highmoon Hall",
                        "desc": "The austere residence of the Jarl of Hjaalmarch, Idgrod Ravencrone.",
                        "tags": ["government", "jarls_seat"]
                    },
                    {
                        "id": 4002,
                        "name": "Moorside Inn",
                        "desc": "A humble inn providing shelter for travelers daring to brave the murky swamps, run by Jonna.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 4003,
                        "name": "Thaumaturgist's Hut (Falion's House)",
                        "desc": "The home of Falion, Morthal's resident wizard and expert on vampirism, offering magical services.",
                        "tags": ["shop", "alchemy", "magic_vendor", "residence", "quest_giver"]
                    },
                    {
                        "id": 4004,
                        "name": "Jorgen and Lami's House", # Lami is the alchemist apprentice
                        "desc": "The home of Jorgen, Lami, and the mill workers.",
                        "tags": ["residence", "lumber_mill"]
                    }
                ]
            },
            {
                "id": 41,
                "name": "Movarth's Lair",
                "desc": "A dank cave north of Morthal, the den of the master vampire Movarth Piquine and his thralls.",
                "tags": ["cave", "vampire_lair", "dungeon", "quest_location"]
            },
            {
                "id": 42,
                "name": "Ustengrav", # Also ID 107. This ID structure needs review for duplicates.
                "desc": "A sprawling Nordic tomb deep within Hjaalmarch's marshes, said to hold the Horn of Jurgen Windcaller.",
                "tags": ["barrow", "nordic_ruin", "dungeon", "undead", "quest_location", "dragon_word"]
            },
            {
                "id": 43,
                "name": "Stonehills",
                "desc": "A modest mining outpost in Hjaalmarch, focused on excavating iron ore.",
                "tags": ["village", "mine", "resource"],
                "sub_locations": [
                    {
                        "id": 4301,
                        "name": "Rockwallow Mine",
                        "desc": "The iron mine that sustains the small settlement of Stonehills.",
                        "tags": ["mine", "resource"]
                    },
                    {
                        "id": 4302,
                        "name": "Sorli's House", # Sorli the Builder is a key NPC
                        "desc": "The residence of Sorli the Builder, an important figure in Stonehills.",
                        "tags": ["residence"]
                    }
                ]
            },
            {
                "id": 44,
                "name": "Apprentice Stone",
                "desc": "A Standing Stone located in the marshes northwest of Morthal, granting faster Magicka regeneration.",
                "tags": ["standing_stone", "magic_buff", "marsh"]
            },
            {
                "id": 45,
                "name": "Brood Cavern",
                "desc": "A small cave in Hjaalmarch, often infested with spiders or other creatures.",
                "tags": ["cave", "monster_den", "dungeon_minor"]
            },
            {
                "id": 46,
                "name": "Chillwind Depths",
                "desc": "A large cave system south of Dragon Bridge (near Hjaalmarch border), inhabited by Falmer and Chaurus.",
                "tags": ["cave", "falmer_den", "chaurus_nest", "dungeon"]
            },
            {
                "id": 47,
                "name": "Dead Men's Respite",
                "desc": "A Nordic ruin southwest of Morthal, connected to the Bards College and King Olaf.",
                "tags": ["nordic_ruin", "dungeon", "undead", "bards_college_quest", "dragon_word"]
            },
            {
                "id": 48,
                "name": "Folgunthur",
                "desc": "An ancient Nordic ruin south of Solitude, near the Hjaalmarch border, where the Gauldur Amulet fragment is sought.",
                "tags": ["nordic_ruin", "dungeon", "undead", "quest_location", "gauldur_amulet"]
            },
            {
                "id": 49,
                "name": "Kjenstag Ruins",
                "desc": "Ruined Nordic structures in the marshes, sometimes haunted or occupied by bandits.",
                "tags": ["nordic_ruin", "marsh", "haunted_potential"]
            },
            {
                "id": 40001, # Unique ID
                "name": "Meeko's Shack",
                "desc": "A small, abandoned shack south of Solitude Sawmill, once home to Meeko and his now-deceased master.",
                "tags": ["hut", "abandoned", "animal_companion"]
            },
            {
                "id": 40002,
                "name": "Robber's Gorge",
                "desc": "A bandit-controlled ravine and bridge southwest of Rorikstead, on the edge of Hjaalmarch.",
                "tags": ["bandit_camp", "ravine", "dungeon", "road_ambush_site"]
            },
            {
                "id": 40003,
                "name": "Wreck of the Icerunner",
                "desc": "A shipwreck on the northern coast of Hjaalmarch, west of Solitude, often containing bandits and loot.",
                "tags": ["shipwreck_site", "bandit_lair", "coastal", "dungeon"]
            }
        ]
    },
    # FALKREATH HOLD
    {
        "id": 5,
        "name": "Falkreath Hold",
        "desc": "A heavily forested hold in southern Skyrim, known for its ancient woods, towering mountains, and the somber town of Falkreath with its large graveyard. It borders Cyrodiil.",
        "tags": ["hold", "forest", "southern", "graveyard", "mountain", "cyrodiil_border", "nordic"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["Whiterun Hold", "The Reach", "Cyrodiil (conceptual)"],
            "paths": ["Helgen Pass", "Pine Forest Trail", "Jerall Mountains Path"]
        },
        "sub_locations": [
            {
                "id": 50,
                "name": "Falkreath (Town)",
                "desc": "A quiet, somewhat gloomy town nestled in the southern forests, known for its extensive graveyard and timber industry. It is the seat of Jarl Siddgeir.",
                "tags": ["town", "forest", "falkreath", "lore", "graveyard", "jarls_seat", "daedric_quest"],
                "sub_locations": [
                    {
                        "id": 5001,
                        "name": "Dead Man's Drink",
                        "desc": "The local tavern in Falkreath, a place for locals and weary travelers to find mead and solace.",
                        "tags": ["tavern", "social", "inn"]
                    },
                    {
                        "id": 5002,
                        "name": "Jarl's Longhouse (Falkreath)",
                        "desc": "The seat of authority in Falkreath Hold, residence of Jarl Siddgeir.",
                        "tags": ["government", "jarls_seat"]
                    },
                    {
                        "id": 5003,
                        "name": "Falkreath Graveyard",
                        "desc": "An expansive and ancient cemetery, the largest in Skyrim, said to be haunted by restless spirits.",
                        "tags": ["graveyard", "haunted", "historic"]
                    },
                    {
                        "id": 5004,
                        "name": "Gray Pine Goods",
                        "desc": "Solaf's shop in Falkreath, offering general supplies, hunting gear, and lumber.",
                        "tags": ["shop", "general", "hunting_supply"]
                    },
                    {
                        "id": 5005,
                        "name": "Lod's House and Smithy",
                        "desc": "The home and workshop of Lod, Falkreath's blacksmith, who can often be found working his forge.",
                        "tags": ["blacksmith", "shop", "crafting", "residence"]
                    },
                    {
                        "id": 5006,
                        "name": "Hall of the Dead (Falkreath)",
                        "desc": "Falkreath's hall for honoring the dead, managed by Runil, a priest of Arkay.",
                        "tags": ["temple_minor", "religious", "arkay_shrine"]
                    },
                    {
                        "id": 5007,
                        "name": "Dark Brotherhood Sanctuary (Falkreath Entrance)",
                        "desc": "A hidden sanctuary of the Dark Brotherhood, concealed within the pine forests near Falkreath.",
                        "tags": ["dark_brotherhood", "assassin_guild", "secret_location", "dungeon_entrance"]
                    }
                ]
            },
            {
                "id": 51,
                "name": "Pinewatch",
                "desc": "A secluded farmhouse north of Falkreath, which serves as a front for a secret bandit hideout.",
                "tags": ["farm", "bandit_hideout", "dungeon", "quest_location"]
            },
            {
                "id": 52,
                "name": "Halldir's Cairn",
                "desc": "A solemn Nordic barrow southwest of Falkreath, haunted by the draugr Halldir and his elemental thralls.",
                "tags": ["barrow", "nordic_ruin", "dungeon", "ghost", "elemental_magic"]
            },
            {
                "id": 53,
                "name": "Helgen",
                "desc": "Once a bustling town at the southern border of Whiterun Hold, now infamous for being the site of Alduin's return. Its ruins are a grim reminder.",
                "tags": ["village_ruined", "dragon_attack_site", "historic_event", "imperial_presence_former", "quest_start_location"],
                 "sub_locations": [
                    {
                        "id": 5301,
                        "name": "Helgen Keep",
                        "desc": "The ruined keep of Helgen, offering a dangerous passage for those fleeing the dragon attack.",
                        "tags": ["keep", "ruin", "dungeon", "escape_route"]
                    },
                    {
                        "id": 5302,
                        "name": "Helgen Homestead", # Generic name for a surviving/ruined house
                        "desc": "A burnt-out shell of a home in what remains of Helgen.",
                        "tags": ["residence_ruined"]
                    }
                ]
            },
            {
                "id": 54,
                "name": "Ancestor Glade",
                "desc": "A hidden, serene glade sacred to the Moth Priests, located in the southern mountains of Falkreath Hold. It's a place of profound natural beauty and ancient ritual.",
                "tags": ["sacred_grove", "dawnguard_quest", "unique_location", "moth_priest_lore", "vampire_lore"]
            },
            {
                "id": 55,
                "name": "Bloodlet Throne",
                "desc": "A ruined fort atop a mountain in Falkreath, now a lair for vampires.",
                "tags": ["fort_ruined", "vampire_lair", "dungeon", "mountain_peak"]
            },
            {
                "id": 56,
                "name": "Brittleshin Pass",
                "desc": "A small cave system serving as a pass through the mountains south of Falkreath, often inhabited by necromancers or undead.",
                "tags": ["cave", "mountain_pass", "necromancer_lair_potential", "undead", "dungeon_minor"]
            },
            {
                "id": 57,
                "name": "Embershard Mine",
                "desc": "An iron mine located between Riverwood and Helgen, often occupied by bandits.",
                "tags": ["mine", "bandit_camp", "dungeon", "resource_iron"]
            },
            {
                "id": 58,
                "name": "Evergreen Grove",
                "desc": "A small, secluded grove west of Falkreath, known for its spriggans and natural tranquility.",
                "tags": ["grove", "spriggan_den", "wilderness", "alchemy_ingredients"]
            },
            {
                "id": 59,
                "name": "Knifepoint Ridge",
                "desc": "A bandit-occupied mine and camp in the northwestern part of Falkreath Hold.",
                "tags": ["mine", "bandit_camp", "dungeon", "quest_location_daedric"]
            },
            {
                "id": 50001, # Unique ID
                "name": "Moss Mother Cavern",
                "desc": "A cave system east of Falkreath, home to various creatures and connected to local legends.",
                "tags": ["cave", "monster_den", "quest_location", "dungeon"]
            },
            {
                "id": 50002,
                "name": "Peak's Shade Tower",
                "desc": "A ruined tower south of Falkreath, often a lair for hagravens or other malevolent creatures.",
                "tags": ["tower_ruined", "hagraven_lair_potential", "wilderness"]
            },
            {
                "id": 50003,
                "name": "Roadside Ruins",
                "desc": "Crumbling Nordic ruins along the road in Falkreath Hold, sometimes attracting spriggans or bandits.",
                "tags": ["nordic_ruin_minor", "roadside_encounter"]
            },
            {
                "id": 50004,
                "name": "Sunderstone Gorge",
                "desc": "A large cave system in the southern mountains of Falkreath, housing a Word Wall and various magical inhabitants.",
                "tags": ["cave", "dungeon", "dragon_word", "magic_users", "fire_elementals"]
            },
            {
                "id": 50005,
                "name": "Cracked Tusk Keep",
                "desc": "A ruined fort in Falkreath Hold, now occupied by Orc bandits and containing a piece of Mehrunes' Razor.",
                "tags": ["fort_ruined", "orc_camp", "bandit_lair", "daedric_artifact_piece", "dungeon"]
            }
            # ... More Falkreath locations can be added
        ]
    },
    # THE REACH
    {
        "id": 6,
        "name": "The Reach",
        "desc": "A wild, rugged, and mountainous region in western Skyrim, dominated by steep cliffs, deep valleys, and ancient Dwemer ruins. It is the heartland of the native Forsworn.",
        "tags": ["hold", "mountain", "dwemer_ruin_heavy", "forsworn_territory", "mining_region", "nordic", "rebellion"],
        "demographics": {"Nord": 50, "Breton (Reachmen)": 40, "Orc": 5, "Others": 5}, # Reachmen are culturally distinct Bretons
        "travel": {
            "roads": ["Whiterun Hold", "Haafingar", "Falkreath Hold", "Hjaalmarch"],
            "paths": ["Karth River Valley", "Sundered Hills Pass", "Hag Rock Trail"]
        },
        "sub_locations": [
            {
                "id": 60,
                "name": "Markarth",
                "desc": "A city built into the stone cliffs by the Dwemer, now the capital of the Reach. It is known for its silver mines, political intrigue, and strong Forsworn presence.",
                "tags": ["city", "dwemer_architecture", "mountain_city", "markarth", "rebellion", "silver_mine", "jarls_seat", "forsworn_conspiracy"],
                "sub_locations": [
                    {
                        "id": 6001,
                        "name": "Silver-Blood Inn",
                        "desc": "A bustling tavern in Markarth, owned by the influential Silver-Blood family, a common place for rumors and shady deals.",
                        "tags": ["tavern", "social", "inn", "intrigue"]
                    },
                    {
                        "id": 6002,
                        "name": "Understone Keep",
                        "desc": "An ancient Dwemer fortification carved into the rock, serving as the Jarl's palace and housing a Dwemer museum and Nchuand-Zel entrance.",
                        "tags": ["keep", "government", "dwemer_ruin_integrated", "museum", "jarls_seat", "nchuand_zel_access"]
                    },
                    {
                        "id": 6003,
                        "name": "Cidhna Mine",
                        "desc": "Markarth's infamous silver mine, which also serves as a prison for Forsworn and other criminals. Conditions are brutal.",
                        "tags": ["mine", "prison", "silver_resource", "forsworn_quest", "quest_location"]
                    },
                    {
                        "id": 6004,
                        "name": "Arnleif and Sons Trading Company",
                        "desc": "A general goods store in Markarth, run by Lisbet, offering a variety of wares.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 6005,
                        "name": "The Hag's Cure",
                        "desc": "Bothela's apothecary shop in Markarth, providing potions, ingredients, and alchemical supplies.",
                        "tags": ["alchemy", "shop", "magic_vendor"]
                    },
                    {
                        "id": 6006,
                        "name": "Markarth Market Square",
                        "desc": "An open-air market in the heart of the city where various vendors sell their goods, often under the watchful eye of city guards.",
                        "tags": ["market", "trade"]
                    },
                    {
                        "id": 6007,
                        "name": "Temple of Dibella",
                        "desc": "A grand temple dedicated to Dibella, the goddess of beauty and love, home to several priestesses.",
                        "tags": ["temple", "religious", "dibella", "quest_location"]
                    },
                    {
                        "id": 6008,
                        "name": "Ghorza's Smithy",
                        "desc": "The workshop of Ghorza gra-Bagol, an Orc blacksmith in Markarth.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    }
                ]
            },
            {
                "id": 61,
                "name": "Karthwasten",
                "desc": "A rugged mining village in the Reach, centered around Sanuarach Mine and Fenn's Gulch Mine. It is often caught between Markarth's control and Forsworn raids.",
                "tags": ["village", "mining", "forsworn_conflict", "resource_silver"],
                 "sub_locations": [
                    {
                        "id": 6101,
                        "name": "Karthwasten Hall",
                        "desc": "The primary gathering place in Karthwasten, sometimes serving as a makeshift inn or meeting hall.",
                        "tags": ["social_hub", "meeting_hall"] # Not a full inn typically
                    },
                    {
                        "id": 6102,
                        "name": "Sanuarach Mine",
                        "desc": "A silver mine in Karthwasten, a key source of income for the village.",
                        "tags": ["mine", "resource_silver"]
                    },
                    {
                         "id": 6103,
                         "name": "Fenn's Gulch Mine",
                         "desc": "Another mine in Karthwasten, primarily for silver.",
                         "tags": ["mine", "resource_silver"]
                    }
                ]
            },
            {
                "id": 62,
                "name": "Druadach Redoubt",
                "desc": "A major Forsworn encampment and cave system hidden in the mountains southwest of Karthwasten, a stronghold of the rebellion.",
                "tags": ["forsworn_camp", "cave_system", "dungeon", "rebel_stronghold", "quest_location_choice"]
            },
            {
                "id": 63,
                "name": "Deep Folk Crossing", # More of a landmark than a settlement
                "desc": "An ancient Dwemer bridge spanning a tumultuous river high in the mountains, a relic obscured by time and mystery.",
                "tags": ["dwemer_bridge", "ruin_landmark", "scenic_view"]
            },
            {
                "id": 64,
                "name": "Dushnikh Yal", # Orc Stronghold
                "desc": "An Orc stronghold in the southwestern Reach, adhering to the ancient Code of Malacath. Known for its skilled warriors and miners.",
                "tags": ["orc_stronghold", "tribal", "mountain_settlement", "mining_community", "warrior_culture"],
                 "sub_locations": [
                    {
                        "id": 6401,
                        "name": "Burguk's Longhouse",
                        "desc": "The longhouse of Chief Burguk, the leader of Dushnikh Yal.",
                        "tags": ["government", "chieftains_hall", "residence"]
                    },
                    {
                        "id": 6402,
                        "name": "Dushnikh Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, providing valuable ore for Orcish smithing.",
                        "tags": ["mine", "resource_orichalcum"]
                    },
                    {
                        "id": 6403,
                        "name": "Gharol's Smithy",
                        "desc": "The forge of Gharol, the blacksmith of Dushnikh Yal.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    }
                ]
            },
            {
                "id": 65,
                "name": "Blind Cliff Cave",
                "desc": "A cave system north of Markarth, a den for Forsworn and hagravens.",
                "tags": ["cave", "forsworn_camp", "hagraven_lair", "dungeon"]
            },
            {
                "id": 66,
                "name": "Bruca's Leap Redoubt",
                "desc": "A Forsworn encampment built around a waterfall and river, east of Karthwasten.",
                "tags": ["forsworn_camp", "waterfall_location", "dungeon"]
            },
            {
                "id": 67,
                "name": "Dead Crone Rock",
                "desc": "A ruined tower and Forsworn stronghold west of Markarth, site of a daedric quest related to Mehrunes' Razor.",
                "tags": ["tower_ruined", "forsworn_camp", "hagraven_lair", "daedric_artifact_piece", "dungeon"]
            },
            {
                "id": 68,
                "name": "Deepwood Redoubt",
                "desc": "A large Forsworn encampment and Nordic ruin complex northwest of Markarth, leading to Hag's End.",
                "tags": ["forsworn_camp", "nordic_ruin_integrated", "dungeon", "quest_location"]
            },
            {
                "id": 69,
                "name": "Dragontooth Crater",
                "desc": "A volcanic crater and dragon lair in the northern mountains of the Reach.",
                "tags": ["dragon_lair", "volcanic_crater", "mountain_peak", "dungeon"]
            },
            {
                "id": 60001, # Unique ID
                "name": "Hag Rock Redoubt",
                "desc": "A Forsworn-occupied ruin south of Markarth, often a target for bounty hunters.",
                "tags": ["forsworn_camp", "ruin", "dungeon"]
            },
            {
                "id": 60002,
                "name": "Hag's End",
                "desc": "A ruined tower accessible through Deepwood Redoubt, home to powerful hagravens and a Word Wall.",
                "tags": ["tower_ruined", "hagraven_lair", "dungeon", "dragon_word", "quest_location"]
            },
            {
                "id": 60003,
                "name": "Karthspire Camp", # Note: Karthspire itself is the mountain for Sky Haven Temple
                "desc": "A large Forsworn encampment at the base of the Karthspire mountain, guarding the way to Sky Haven Temple.",
                "tags": ["forsworn_camp", "dungeon", "quest_location_main"]
            },
            {
                "id": 60004,
                "name": "Kolskeggr Mine",
                "desc": "A gold mine east of Markarth, frequently overrun by Forsworn.",
                "tags": ["mine", "resource_gold", "forsworn_conflict", "quest_location"]
            },
            {
                "id": 60005,
                "name": "Left Hand Mine",
                "desc": "An iron mine located just outside Markarth, owned by Skaggi Scar-Face.",
                "tags": ["mine", "resource_iron", "mining_town_minor"]
            },
            {
                "id": 60006,
                "name": "Lost Valley Redoubt",
                "desc": "A major Forsworn encampment built around scenic waterfalls and ancient Nordic structures, home to powerful Forsworn Briarhearts.",
                "tags": ["forsworn_camp", "waterfall_location", "nordic_ruin_integrated", "dungeon", "dragon_word"]
            },
            {
                "id": 60007,
                "name": "Reachcliff Cave",
                "desc": "A cave south of Markarth, initially occupied by undead until cleared for a daedric quest.",
                "tags": ["cave", "undead_initial", "daedric_quest_location", "dungeon"]
            },
            {
                "id": 60008,
                "name": "Reachwind Eyrie",
                "desc": "A ruined Dwemer tower on a clifftop overlooking the Karth River, often a bandit or Forsworn outpost.",
                "tags": ["dwemer_tower_ruined", "forsworn_outpost_potential", "scenic_view"]
            },
            {
                "id": 60009,
                "name": "Red Eagle Redoubt",
                "desc": "A large Forsworn camp and Nordic ruin complex, central to the legend of Red Eagle.",
                "tags": ["forsworn_camp", "nordic_ruin_integrated", "dungeon", "legendary_figure_lore", "quest_location"]
            },
            {
                "id": 60010,
                "name": "Sky Haven Temple",
                "desc": "The ancient hidden sanctuary of the Blades, located atop the Karthspire mountain, accessible after navigating a Forsworn camp and a puzzle.",
                "tags": ["blades_headquarters", "historic_temple", "secret_location", "dragon_lore", "quest_location_main", "mountain_stronghold"],
                "sub_locations": [
                    {
                        "id": 600101,
                        "name": "Alduin's Wall",
                        "desc": "A prophetic mural within Sky Haven Temple depicting Alduin's history and the Dragonborn prophecy.",
                        "tags": ["prophecy_site", "historic_artifact"]
                    },
                    {
                        "id": 600102,
                        "name": "Armory of Sky Haven Temple",
                        "desc": "Contains ancient Blades armor and weapons.",
                        "tags": ["armory", "unique_gear"]
                    }
                ]
            },
            {
                "id": 60011,
                "name": "Soljund's Sinkhole",
                "desc": "A moonstone mine east of Markarth that has broken into a draugr-infested Nordic ruin.",
                "tags": ["mine", "nordic_ruin_breach", "undead", "dungeon", "resource_moonstone"]
            },
            {
                "id": 60012,
                "name": "Old Hroldan Inn",
                "desc": "An ancient inn located in the Reach, south of Soljund's Sinkhole, said to have been visited by Tiber Septim.",
                "tags": ["inn", "tavern", "historic_site", "ghost_quest", "isolated"]
            }
            # ... More Reach locations
        ]
    },
    # EASTMARCH
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A harsh, volcanic hold in eastern Skyrim, dominated by the ancient city of Windhelm, the capital of the Stormcloak rebellion. Known for its hot springs, giants, and fierce Nordic traditions.",
        "tags": ["hold", "volcanic", "nordic_stronghold", "stormcloak_capital", "hot_springs", "giant_country", "imperial_conflict"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Argonian": 3, "Others": 2}, # Windhelm has significant Dunmer and Argonian populations in specific districts
        "travel": {
            "roads": ["Whiterun Hold", "The Rift", "The Pale", "Winterhold"],
            "paths": ["Volcanic Tundra Trail", "Dunmeth Pass to Morrowind (conceptual)"]
        },
        "sub_locations": [
            {
                "id": 70,
                "name": "Windhelm",
                "desc": "One of Skyrim's oldest cities, the traditional capital of the First Empire, and current stronghold of Ulfric Stormcloak. It is a city of stone, snow, and strong anti-Imperial sentiment.",
                "tags": ["city", "capital_stormcloak", "nordic_architecture", "windhelm", "historic_city", "stormcloak_presence", "dunmer_quarter", "argonian_assemblage", "imperial_conflict_focus"],
                "sub_locations": [
                    {
                        "id": 7001,
                        "name": "Candlehearth Hall",
                        "desc": "A historic and popular tavern in Windhelm, known for its large central hearth and warm atmosphere.",
                        "tags": ["tavern", "social", "inn", "historic_building"]
                    },
                    {
                        "id": 7002,
                        "name": "Oengul's Smithy",
                        "desc": "The workshop of Oengul War-Anvil and his apprentice Hermir Strong-Heart, providing quality arms and armor.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    },
                    {
                        "id": 7003,
                        "name": "Palace of the Kings",
                        "desc": "The formidable ancient seat of Ysgramor's dynasty, now serving as Ulfric Stormcloak's residence and military headquarters.",
                        "tags": ["government", "jarls_seat", "military_hq", "historic_palace", "stormcloak_leader_residence"]
                    },
                    {
                        "id": 7004,
                        "name": "The White Phial",
                        "desc": "An esteemed apothecary shop run by Nurelion, focused on a legendary artifact of the same name.",
                        "tags": ["alchemy", "shop", "magic_vendor", "quest_location_artifact"]
                    },
                    {
                        "id": 7005,
                        "name": "Sadri's Used Wares",
                        "desc": "Revyn Sadri's shop in the Dunmer quarter, offering a variety of second-hand goods and curiosities.",
                        "tags": ["shop", "general", "dunmer_business"]
                    },
                    {
                        "id": 7006,
                        "name": "Windhelm Market Square",
                        "desc": "A bustling open-air market with various stalls near the city gates, offering food, goods, and services.",
                        "tags": ["market", "trade"]
                    },
                    {
                        "id": 7007,
                        "name": "Temple of Talos (Windhelm)",
                        "desc": "A place of worship for Talos, significant given the Stormcloak cause, though officially banned by the White-Gold Concordat.",
                        "tags": ["temple", "religious", "talos_worship", "stormcloak_ideology"]
                    },
                    {
                        "id": 7008,
                        "name": "Gray Quarter (Dunmer District)",
                        "desc": "The segregated district where most of Windhelm's Dunmer population resides, often facing prejudice.",
                        "tags": ["district_dunmer", "social_tension", "refugee_area"]
                    },
                    {
                        "id": 7009,
                        "name": "Argonian Assemblage (Docks)",
                        "desc": "The dockside area where Windhelm's Argonian dockworkers are forced to live.",
                        "tags": ["district_argonian", "docks", "social_tension", "laborer_area"]
                    },
                    {
                        "id": 7010,
                        "name": "Aretino Residence",
                        "desc": "The home of Aventus Aretino, a young boy attempting to perform the Black Sacrament to contact the Dark Brotherhood.",
                        "tags": ["residence", "dark_brotherhood_quest_start"]
                    },
                    {
                        "id": 7011,
                        "name": "Hall of the Dead (Windhelm)",
                        "desc": "Windhelm's catacombs for honoring the dead, maintained by a priestess of Arkay.",
                        "tags": ["catacombs", "religious", "arkay_shrine"]
                    }
                ]
            },
            {
                "id": 71,
                "name": "Kynesgrove",
                "desc": "A small, industrious mining village on the slopes of the volcanic tundra, known for its malachite mine and proximity to a dragon burial site.",
                "tags": ["village", "mining", "resource_malachite", "dragon_threat_potential"],
                 "sub_locations": [
                    {
                        "id": 7101,
                        "name": "Braidwood Inn",
                        "desc": "The local inn in Kynesgrove, providing food, lodging, and news to miners and travelers.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 7102,
                        "name": "Steamscorch Mine",
                        "desc": "The malachite mine that is the lifeblood of Kynesgrove, recently troubled by a dragon.",
                        "tags": ["mine", "resource_malachite", "quest_location"]
                    }
                ]
            },
            {
                "id": 72,
                "name": "Fort Amol",
                "desc": "A strategic fort in Eastmarch, often a focal point of conflict in the Civil War, guarding the pass to Whiterun.",
                "tags": ["fort", "military", "civil_war_site", "dungeon_potential"] # Can be ruined or active
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove hidden in Eastmarch, home to the ancient Eldergleam tree. A place of pilgrimage and natural wonder.",
                "tags": ["sacred_grove", "kynareth_shrine", "unique_tree", "quest_location", "natural_wonder"]
            },
            {
                "id": 74,
                "name": "Narzulbur", # Orc Stronghold
                "desc": "An Orc stronghold in Eastmarch, situated near a rich ebony mine. They adhere strictly to the Code of Malacath.",
                "tags": ["orc_stronghold", "tribal", "mining_community_ebony", "warrior_culture"],
                "sub_locations": [
                    {
                        "id": 7401,
                        "name": "Largashbur Longhouse", # Chief's hall in Narzulbur context
                        "desc": "The longhouse of Chief Mauhulakh, leader of Narzulbur.",
                        "tags": ["government", "chieftains_hall", "residence"]
                    },
                    {
                        "id": 7402,
                        "name": "Gloombound Mine (Ebony)",
                        "desc": "Narzulbur's productive ebony mine, a source of great wealth and Orcish pride.",
                        "tags": ["mine", "resource_ebony", "orc_controlled"]
                    }
                ]
            },
            {
                "id": 75,
                "name": "Ansilvund",
                "desc": "A Nordic ruin in Eastmarch, haunted by draugr and connected to a tragic love story and necromancy.",
                "tags": ["nordic_ruin", "dungeon", "undead", "necromancer_lair", "quest_location", "dragon_word"]
            },
            {
                "id": 76,
                "name": "Bonestrewn Crest",
                "desc": "A dragon lair and Word Wall atop a peak in the southern volcanic region of Eastmarch.",
                "tags": ["dragon_lair", "dragon_word", "mountain_peak", "dungeon"]
            },
            {
                "id": 77,
                "name": "Cronvangr Cave",
                "desc": "A large cave system in the hot springs region of Eastmarch, heavily infested with giant frostbite spiders and vampires.",
                "tags": ["cave", "spider_nest", "vampire_lair_secondary", "dungeon", "hot_springs_area"]
            },
            {
                "id": 78,
                "name": "Darkwater Crossing",
                "desc": "A small mining settlement on the Darkwater River, primarily focused on corundum ore. Some Argonians also reside here.",
                "tags": ["village_minor", "mining", "resource_corundum", "argonian_presence"],
                "sub_locations": [
                    {
                        "id": 7801,
                        "name": "Goldenrock Mine",
                        "desc": "The corundum mine that supports Darkwater Crossing.",
                        "tags": ["mine", "resource_corundum"]
                    }
                ]
            },
            {
                "id": 79,
                "name": "Gallows Rock",
                "desc": "A ruined fort southwest of Windhelm, now serving as a major stronghold for the Silver Hand werewolf hunters.",
                "tags": ["fort_ruined", "silver_hand_lair", "companions_quest", "dungeon"]
            },
            {
                "id": 70001, # Unique ID
                "name": "Gloomreach",
                "desc": "A cave system in the southern mountains of Eastmarch, often inhabited by Falmer or other dangerous creatures.",
                "tags": ["cave", "falmer_den_potential", "dungeon"]
            },
            {
                "id": 70002,
                "name": "Lost Knife Hideout",
                "desc": "A large cave system serving as a major bandit hideout, located near the border with The Rift.",
                "tags": ["cave", "bandit_stronghold", "dungeon", "quest_location_bounty"]
            },
            {
                "id": 70003,
                "name": "Mixwater Mill",
                "desc": "A lumber mill on the White River in Eastmarch, run by Gilfre.",
                "tags": ["lumber_mill", "settlement_minor", "resource_wood"]
            },
            {
                "id": 70004,
                "name": "Morvunskar",
                "desc": "A ruined fort south of Windhelm, now occupied by hostile mages and a portal to Sanguine's realm during a daedric quest.",
                "tags": ["fort_ruined", "mage_lair", "daedric_quest_location", "dungeon", "sanguine_portal"]
            },
            {
                "id": 70005,
                "name": "Refugees' Rest",
                "desc": "A small, ruined Nordic structure east of Windhelm, marking a somber historical event.",
                "tags": ["nordic_ruin_minor", "historic_marker", "ghost_encounter_potential"]
            },
            {
                "id": 70006,
                "name": "Riverside Shack",
                "desc": "A small, isolated shack on the banks of the White River, sometimes home to a reclusive individual or creature.",
                "tags": ["hut", "isolated", "river_location"]
            },
            {
                "id": 70007,
                "name": "Stony Creek Cave",
                "desc": "A cave in the southern part of Eastmarch's volcanic tundra, inhabited by bandits and containing a valuable alchemical ingredient.",
                "tags": ["cave", "bandit_lair", "dungeon", "alchemy_ingredient_unique"]
            },
            {
                "id": 70008,
                "name": "Traitor's Post",
                "desc": "A small, abandoned shack east of Windhelm, often used as a hideout by bandits or renegades.",
                "tags": ["hut", "abandoned", "bandit_outpost_potential"]
            },
            {
                "id": 70009,
                "name": "Uttering Hills Cave",
                "desc": "A cave system southwest of Windhelm, serving as a hideout for a group of bandits.",
                "tags": ["cave", "bandit_hideout", "dungeon"]
            },
            {
                "id": 70010,
                "name": "Witchmist Grove",
                "desc": "A mystical grove in the southern hot springs region of Eastmarch, home to unique flora and often spriggans or other magical creatures.",
                "tags": ["grove", "magic_heavy", "spriggan_den_potential", "hot_springs_area", "alchemy_ingredients"]
            }
            # ... More Eastmarch locations
        ]
    },
    # HAAFINGAR
    {
        "id": 8,
        "name": "Haafingar",
        "desc": "A strategic coastal hold in northwestern Skyrim, dominated by the majestic capital city of Solitude. It is a major Imperial stronghold and a hub for maritime trade.",
        "tags": ["hold", "coastal", "imperial_stronghold", "maritime_trade", "nordic", "solitude_capital", "bards_college_location"],
        "demographics": {"Nord": 70, "Imperial": 20, "Breton": 5, "Others": 5},
        "travel": {
            "roads": ["The Reach", "Whiterun Hold", "Hjaalmarch"],
            "paths": ["Dragon Bridge Road", "Coastal Sea Route (conceptual)"]
        },
        "sub_locations": [
            {
                "id": 80,
                "name": "Solitude",
                "desc": "The grand capital of Haafingar and a major Imperial city, perched atop a natural stone arch. It is home to the Blue Palace, Castle Dour, and the Bards College.",
                "tags": ["city", "capital_haafingar", "imperial_city", "solitude", "wealth", "imperial_presence", "bards_college", "major_port", "architecture_grand"],
                "sub_locations": [
                    {
                        "id": 8001,
                        "name": "Blue Palace",
                        "desc": "The opulent palace residence of Jarl Elisif the Fair and the seat of Imperial power in Solitude.",
                        "tags": ["palace", "government", "jarls_seat", "imperial_court"]
                    },
                    {
                        "id": 8002,
                        "name": "Castle Dour",
                        "desc": "A robust Imperial fortification within Solitude, headquarters of General Tullius and the Imperial Legion in Skyrim.",
                        "tags": ["fort", "military_hq", "imperial_legion_base"]
                    },
                    {
                        "id": 8003,
                        "name": "The Winking Skeever",
                        "desc": "A popular and well-known tavern in Solitude, frequented by locals, travelers, and a certain boastful mercenary.",
                        "tags": ["tavern", "social", "inn", "quest_giver_potential"]
                    },
                    {
                        "id": 8004,
                        "name": "Bits and Pieces",
                        "desc": "Sayma's general goods store in Solitude, offering a wide variety of items.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 8005,
                        "name": "Angeline's Aromatics",
                        "desc": "An apothecary shop run by Angeline Morrard, selling potions, ingredients, and alchemical supplies.",
                        "tags": ["alchemy", "shop", "magic_vendor"]
                    },
                    {
                        "id": 8006,
                        "name": "Radiant Raiment",
                        "desc": "A fine clothing store run by Taarie and Endarie, offering fashionable attire and tailoring services.",
                        "tags": ["shop", "clothing", "tailor"]
                    },
                    {
                        "id": 8007,
                        "name": "Fletcher",
                        "desc": "Fihada's shop specializing in bows, arrows, and other archery supplies.",
                        "tags": ["shop", "archery_vendor", "crafting_archery"]
                    },
                    {
                        "id": 8008,
                        "name": "Solitude Blacksmith (Beirand)",
                        "desc": "Beirand's smithy, located near Castle Dour, providing weapons, armor, and smithing services.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    },
                    {
                        "id": 8009,
                        "name": "Bards College",
                        "desc": "A renowned institution dedicated to preserving Skyrim's history and fostering the talents of bards, musicians, and performers.",
                        "tags": ["college", "guild", "bards", "learning_center", "music_lore", "quest_line"]
                    },
                    {
                        "id": 8010,
                        "name": "Temple of the Divines (Solitude)",
                        "desc": "A grand temple in Solitude dedicated to the worship of all Eight (or Nine) Divines, a center of religious life.",
                        "tags": ["temple_major", "religious", "eight_divines_shrine", "talos_shrine_secret_potential"]
                    },
                    {
                        "id": 8011,
                        "name": "Solitude Docks",
                        "desc": "The bustling port area of Solitude, handling sea trade and home to the East Empire Company Warehouse.",
                        "tags": ["docks", "port", "trade_hub", "east_empire_company"]
                    },
                    {
                        "id": 8012,
                        "name": "Erikur's House",
                        "desc": "The lavish residence of Thane Erikur, an influential and somewhat corrupt noble in Solitude.",
                        "tags": ["residence", "noble_house", "political_intrigue"]
                    }
                ]
            },
            {
                "id": 81,
                "name": "Dragon Bridge",
                "desc": "A quaint village in northwestern Haafingar, built around an ancient and iconic stone bridge. It serves as a strategic crossing point.",
                "tags": ["village", "bridge_landmark", "strategic_location", "lumber_mill_nearby"],
                 "sub_locations": [
                    {
                        "id": 8101,
                        "name": "Four Shields Tavern",
                        "desc": "The inn at Dragon Bridge, a common stop for Imperial soldiers and travelers on the road to Solitude.",
                        "tags": ["inn", "tavern", "social", "travel_stop"]
                    },
                    {
                        "id": 8102,
                        "name": "Dragon Bridge Lumber Camp",
                        "desc": "The lumber mill that supports the village of Dragon Bridge.",
                        "tags": ["lumber_mill", "resource_wood"]
                    },
                    {
                        "id": 8103,
                        "name": "Penitus Oculatus Outpost",
                        "desc": "A small Imperial outpost near Dragon Bridge, sometimes used by the Emperor's personal guard.",
                        "tags": ["military_outpost", "imperial_penitus_oculatus"]
                    }
                ]
            },
            {
                "id": 82,
                "name": "Wolfskull Cave",
                "desc": "A dark, foreboding cave system high in the mountains of Haafingar, where necromancers attempt to resurrect Potema, the Wolf Queen.",
                "tags": ["cave", "dungeon", "haunted", "necromancer_ritual_site", "potema_wolf_queen", "quest_location_major"]
            },
            {
                "id": 83,
                "name": "Fort Hraggstad",
                "desc": "An Imperial fort northwest of Solitude, guarding the coastline. It can be captured during the Civil War.",
                "tags": ["fort", "military", "civil_war_site", "dungeon_potential", "coastal_defense"]
            },
            {
                "id": 84,
                "name": "Brinewater Grotto",
                "desc": "A coastal cave system south of Solitude Docks, often used by smugglers and bandits.",
                "tags": ["cave", "smuggler_den", "bandit_lair", "coastal", "dungeon"]
            },
            {
                "id": 85,
                "name": "Broken Oar Grotto",
                "desc": "A large, hidden coastal cave system north of Solitude, serving as a major pirate and bandit stronghold.",
                "tags": ["cave", "pirate_hideout", "bandit_stronghold", "coastal", "dungeon", "quest_location"]
            },
            {
                "id": 86,
                "name": "Ironback Hideout", # Minor location
                "desc": "A small cave or ruin serving as a minor bandit hideout in the wilderness of Haafingar.",
                "tags": ["cave_minor", "bandit_outpost", "dungeon_minor"]
            },
            {
                "id": 87,
                "name": "Pinemoon Cave",
                "desc": "A cave system in the mountains of Haafingar, often inhabited by vampires or other dangerous creatures.",
                "tags": ["cave", "vampire_lair_potential", "monster_den", "dungeon"]
            },
            {
                "id": 88,
                "name": "Potema's Catacombs", # Accessed via Temple of Divines
                "desc": "The extensive catacombs beneath Solitude where the Wolf Queen Potema's spirit is finally confronted.",
                "tags": ["catacombs", "undead_heavy", "dungeon_major", "quest_location_major", "boss_fight_potema"]
            },
            {
                "id": 89,
                "name": "Ravenscar Hollow",
                "desc": "A small cave on the northern coast of Haafingar, typically home to hagravens.",
                "tags": ["cave", "hagraven_lair", "coastal", "dungeon_minor"]
            },
            {
                "id": 80001, # Unique ID
                "name": "Shadowgreen Cavern",
                "desc": "A lush, hidden cave system with unique flora and fauna, located southwest of Solitude.",
                "tags": ["cave", "unique_environment", "alchemy_ingredients_rare", "spriggan_den_potential", "dungeon"]
            },
            {
                "id": 80002,
                "name": "Steepfall Burrow",
                "desc": "A small cave system or den, likely inhabited by frost trolls or other creatures, in the snowy mountains of Haafingar.",
                "tags": ["cave", "monster_den_frost_troll", "mountain_location", "dungeon_minor"]
            },
            {
                "id": 80003,
                "name": "Stillborn Cave", # Minor cave
                "desc": "A small, eerie cave in Haafingar, perhaps with a dark secret or minor encounter.",
                "tags": ["cave_minor", "eerie_atmosphere"]
            },
            {
                "id": 80004,
                "name": "The Steed Stone",
                "desc": "A Standing Stone located northwest of Solitude, granting increased carry weight and movement speed benefits.",
                "tags": ["standing_stone", "utility_buff", "mountain_location"]
            },
            {
                "id": 80005,
                "name": "Katla's Farm",
                "desc": "A farm located just outside Solitude's main gates, providing produce and horses.",
                "tags": ["farm", "stables", "resource_food", "horse_vendor"]
            }
            # ... More Haafingar locations
        ]
    },
    # THE RIFT
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A temperate, autumnal hold in southeastern Skyrim, known for its golden forests, numerous lakes, and the city of Riften, a haven for the Thieves Guild. It borders Morrowind and Cyrodiil.",
        "tags": ["hold", "forest_autumnal", "lake_region", "thieves_guild_hub", "nordic", "morrowind_border", "cyrodiil_border", "beautiful_scenery"],
        "demographics": {"Nord": 75, "Dunmer": 10, "Argonian": 10, "Khajiit": 3, "Others": 2}, # Riften has a diverse underbelly
        "travel": {
            "roads": ["Whiterun Hold", "Eastmarch", "Falkreath Hold", "Cyrodiil (conceptual)", "Morrowind (conceptual)"],
            "paths": ["Goldenglow Path", "Jerall Mountain Trail", "Velothi Mountains Pass"]
        },
        "sub_locations": [
            {
                "id": 90,
                "name": "Riften",
                "desc": "A city built upon a lake, with canals running through its wooden structures. It is infamous for corruption, the Black-Briar family's influence, and being the headquarters of the Thieves Guild.",
                "tags": ["city", "lake_city", "canals", "riften", "thieves_guild_hq", "black_briar_influence", "corrupt_city", "jarls_seat"],
                "sub_locations": [
                    {
                        "id": 9001,
                        "name": "The Bee and Barb",
                        "desc": "A popular tavern in Riften, owned by Keerava and Talen-Jei. A common meeting place and source of rumors.",
                        "tags": ["tavern", "social", "inn", "quest_giver_potential"]
                    },
                    {
                        "id": 9002,
                        "name": "Black-Briar Meadery (Riften Building)",
                        "desc": "The main office and shopfront for the powerful Black-Briar Meadery within Riften, a symbol of Maven Black-Briar's control.",
                        "tags": ["shop", "meadery_hq", "black_briar_family", "economic_power"]
                    },
                    {
                        "id": 9003,
                        "name": "The Pawned Prawn",
                        "desc": "A general goods store in Riften, run by Bersi Honey-Hand, offering a variety of items.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 9004,
                        "name": "Mistveil Keep",
                        "desc": "The Jarl's residence in Riften, currently home to Jarl Laila Law-Giver or Maven Black-Briar depending on allegiances.",
                        "tags": ["keep", "government", "jarls_seat", "political_intrigue"]
                    },
                    {
                        "id": 9005,
                        "name": "The Ratway",
                        "desc": "A dangerous, labyrinthine network of tunnels beneath Riften, serving as the entrance to the Ragged Flagon and the Thieves Guild headquarters.",
                        "tags": ["dungeon_city_undercity", "thieves_guild_access", "criminal_hideout", "dangerous_area"],
                        "sub_locations": [
                            {
                                "id": 90051,
                                "name": "The Ragged Flagon",
                                "desc": "A hidden tavern within the Ratway, serving as the main gathering area for the Thieves Guild.",
                                "tags": ["tavern_secret", "thieves_guild_bar", "fence_location"]
                            },
                            {
                                "id": 90052,
                                "name": "The Cistern",
                                "desc": "The secure, inner sanctum and living quarters of the Thieves Guild, deep within the Ratway.",
                                "tags": ["thieves_guild_inner_sanctum", "training_area", "sleeping_quarters"]
                            }
                        ]
                    },
                    {
                        "id": 9006,
                        "name": "Temple of Mara (Riften)",
                        "desc": "A prominent temple dedicated to Mara, the Divine of Love and Compassion. It is a place for marriages and seeking guidance.",
                        "tags": ["temple_major", "religious", "mara_shrine", "marriage_location", "quest_line_mara"]
                    },
                    {
                        "id": 9007,
                        "name": "The Scorched Hammer",
                        "desc": "Balimund's smithy in Riften, known for its quality craftsmanship and Balimund's expertise.",
                        "tags": ["blacksmith", "shop", "crafting"]
                    },
                     {
                        "id": 9008,
                        "name": "Elgrim's Elixirs",
                        "desc": "An apothecary shop run by Elgrim and his wife Hafjorg, located on Riften's lower platforms.",
                        "tags": ["alchemy", "shop", "magic_vendor"]
                    },
                    {
                        "id": 9009,
                        "name": "Riften Marketplace",
                        "desc": "The central market area of Riften, with various stalls selling food, jewelry, and other goods.",
                        "tags": ["market", "trade"]
                    },
                    {
                        "id": 9010,
                        "name": "Honorhall Orphanage",
                        "desc": "Riften's orphanage, run by the cruel Grelod the Kind until her timely demise.",
                        "tags": ["orphanage", "dark_brotherhood_quest_start", "social_issue"]
                    },
                    {
                        "id": 9011,
                        "name": "Black-Briar Manor",
                        "desc": "The grand residence of the powerful and influential Black-Briar family.",
                        "tags": ["residence", "noble_house", "black_briar_family_home", "political_power"]
                    }
                ]
            },
            {
                "id": 91,
                "name": "Shor's Stone", # Village
                "desc": "A small mining village in the northern Rift, primarily focused on an ebony mine that has recently been troubled by frostbite spiders.",
                "tags": ["village", "mining", "resource_ebony", "spider_infestation", "quest_location"],
                "sub_locations": [
                    {
                        "id": 9101,
                        "name": "Redbelly Mine",
                        "desc": "The ebony mine that is the main source of livelihood for Shor's Stone.",
                        "tags": ["mine", "resource_ebony"]
                    },
                    {
                        "id": 9102,
                        "name": "Sylgja's House", # Notable NPC
                        "desc": "The home of Sylgja, a miner in Shor's Stone.",
                        "tags": ["residence"]
                    }
                ]
            },
            {
                "id": 92,
                "name": "Ivarstead", # Village, already somewhat detailed but ensuring it's here
                "desc": "A small village at the foot of the Throat of the World, on the shores of Lake Geir. It is the starting point for the pilgrimage to High Hrothgar.",
                "tags": ["village", "pilgrimage_start", "lake_settlement", "greybeards_path"],
                "sub_locations": [
                    {
                        "id": 9201, # Adjusted from 9301 for consistency
                        "name": "Vilemyr Inn",
                        "desc": "The local inn of Ivarstead, offering rest to those journeying to High Hrothgar, run by Wilhelm.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 9202, # Adjusted from 9302
                        "name": "Shroud Hearth Barrow", # Barrow entrance is in Ivarstead
                        "desc": "An ancient Nordic barrow located within Ivarstead itself, haunted by undead and containing a mystery.",
                        "tags": ["barrow", "nordic_ruin", "dungeon", "undead", "quest_location_local"]
                    },
                    {
                        "id": 9203,
                        "name": "Klimmek's House",
                        "desc": "The home of Klimmek, a resident of Ivarstead who makes deliveries to High Hrothgar.",
                        "tags": ["residence", "quest_giver_minor"]
                    }
                ]
            },
            {
                "id": 93,
                "name": "Lost Prospect Mine", # Was ID 91
                "desc": "An abandoned gold mine in the Rift, often occupied by bandits or Forsworn. It is rumored to be played out.",
                "tags": ["mine_abandoned", "resource_gold_former", "bandit_lair_potential", "dungeon_minor"]
            },
            {
                "id": 94,
                "name": "Broken Helm Hollow", # Was ID 92
                "desc": "A secluded cave system east of Riften, serving as a bandit hideout.",
                "tags": ["cave", "bandit_hideout", "dungeon"]
            },
            {
                "id": 95,
                "name": "Avanchnzel",
                "desc": "A large and dangerous Dwemer ruin in the southern mountains of the Rift, containing ancient technology and Falmer.",
                "tags": ["dwemer_ruin", "dungeon_major", "mechanical", "falmer", "quest_location_daedric_artifact_related"]
            },
            {
                "id": 96,
                "name": "Boulderfall Cave",
                "desc": "A cave in the eastern Rift, often inhabited by necromancers or other dark mages.",
                "tags": ["cave", "necromancer_lair_potential", "dungeon"]
            },
            {
                "id": 97,
                "name": "Clearspring Tarn",
                "desc": "A small, picturesque tarn and cave system west of Shor's Stone, often home to trolls or other creatures, and a treasure hunter's note.",
                "tags": ["cave", "troll_den_potential", "scenic_spot", "treasure_hunter_lore"]
            },
            {
                "id": 98,
                "name": "Crystaldrift Cave",
                "desc": "A small ice cave south of Riften, notable for its unique crystal formations and often a den for frost creatures.",
                "tags": ["cave_ice", "frost_creature_den", "unique_geology"]
            },
            {
                "id": 99,
                "name": "Darklight Tower",
                "desc": "A ruined tower southwest of Riften, now a den for hagravens and the site of a Daedric quest involving Illia.",
                "tags": ["tower_ruined", "hagraven_lair", "daedric_quest_location", "dungeon", "quest_companion"]
            },
            {
                "id": 90001, # Unique ID
                "name": "Faldar's Tooth",
                "desc": "A ruined fort west of Riften, overrun by wolves and later bandits or the Silver Hand.",
                "tags": ["fort_ruined", "wolf_den_initial", "bandit_lair_potential", "silver_hand_lair_potential", "dungeon"]
            },
            {
                "id": 90002,
                "name": "Fort Greenwall",
                "desc": "A large fort in the eastern Rift, strategically important and often a site of conflict in the Civil War.",
                "tags": ["fort", "military", "civil_war_site", "dungeon_potential"]
            },
            {
                "id": 90003,
                "name": "Froki's Shack",
                "desc": "The isolated shack of Froki Whetted-Blade, an old hunter, located in the southern mountains of the Rift.",
                "tags": ["hut", "isolated", "hunter_hermitage", "quest_giver_minor", "kyne_worship"]
            },
            {
                "id": 90004,
                "name": "Goldenglow Estate",
                "desc": "A large honey farm and apiary on an island in Lake Honrich, owned by Aringoth and central to a Thieves Guild questline.",
                "tags": ["farm_apiary", "island_location", "thieves_guild_quest", "mead_production_rival", "wealthy_estate"]
            },
            {
                "id": 90005,
                "name": "Heartwood Mill",
                "desc": "A lumber mill on the shores of Lake Honrich, run by Grosta.",
                "tags": ["lumber_mill", "settlement_minor", "resource_wood", "lake_location"]
            },
            {
                "id": 90006,
                "name": "Honeystrand Cave",
                "desc": "A small cave south of Ivarstead, often a den for bears.",
                "tags": ["cave", "bear_den", "dungeon_minor"]
            },
            {
                "id": 90007,
                "name": "Last Vigil", # Not a settlement, but a specific quest location
                "desc": "A ruined watchtower and dragon burial site in the mountains of the Rift, related to the Dawnguard DLC.",
                "tags": ["watchtower_ruined", "dragon_burial_site", "dawnguard_quest", "mountain_peak"]
            },
            {
                "id": 90008,
                "name": "Merryfair Farm",
                "desc": "A farmstead located near Riften, owned by Dravin Llanith.",
                "tags": ["farm", "residence"]
            },
            {
                "id": 90009,
                "name": "Nightingale Hall",
                "desc": "The secret sanctuary and headquarters of the Nightingales, hidden within a cave system in the Rift.",
                "tags": ["secret_sanctuary", "nightingale_hq", "daedric_shrine_nocturnal", "thieves_guild_elite", "dungeon_quest"]
            },
            {
                "id": 90010,
                "name": "Nilheim",
                "desc": "A ruined watchtower east of Ivarstead, occupied by bandits who employ a clever ambush.",
                "tags": ["watchtower_ruined", "bandit_camp", "ambush_site", "dungeon"]
            },
            {
                "id": 90011,
                "name": "Northwind Summit",
                "desc": "A dragon lair and Word Wall on a mountain peak in the northern Rift, near Shor's Stone.",
                "tags": ["dragon_lair", "dragon_word", "mountain_peak", "dungeon"]
            },
            {
                "id": 90012,
                "name": "Pinepeak Cavern",
                "desc": "A cave system near Ivarstead, often inhabited by bears.",
                "tags": ["cave", "bear_den", "dungeon_minor"]
            },
            {
                "id": 90013,
                "name": "Redwater Den", # Dawnguard DLC location
                "desc": "A former skooma den that serves as a front for a vampire operation dealing in Redwater Skooma.",
                "tags": ["skooma_den", "vampire_lair", "dawnguard_quest", "dungeon", "deception"]
            },
            {
                "id": 90014,
                "name": "Sarethi Farm",
                "desc": "A farmstead near Ivarstead, run by Avrusa Sarethi, known for growing Nirnroot.",
                "tags": ["farm", "residence", "alchemy_ingredient_nirnroot", "quest_giver_minor"]
            },
            {
                "id": 90015,
                "name": "Snapleg Cave",
                "desc": "A cave system south of Ivarstead, often home to spriggans, witches, or hagravens.",
                "tags": ["cave", "spriggan_den_potential", "hagraven_lair_potential", "dungeon"]
            },
            {
                "id": 90016,
                "name": "Snow-Shod Farm",
                "desc": "A farmstead near Riften, owned by the Snow-Shod family, who are involved in local politics and conflicts.",
                "tags": ["farm", "residence", "political_family"]
            },
            {
                "id": 90017,
                "name": "Stendarr's Beacon",
                "desc": "A ruined watchtower in the eastern Rift, now maintained by the Vigilants of Stendarr as an outpost.",
                "tags": ["watchtower_ruined", "vigilant_of_stendarr_outpost", "daedra_hunting_base"]
            },
            {
                "id": 90018,
                "name": "Treva's Watch",
                "desc": "A ruined fort west of Ivarstead, taken over by bandits. Clearing it is part of a local quest.",
                "tags": ["fort_ruined", "bandit_lair", "quest_location", "dungeon"]
            },
            {
                "id": 90019,
                "name": "Tolvald's Cave",
                "desc": "A very large and dangerous cave system in the Velothi Mountains on the border with Morrowind, infested with Falmer and Chaurus.",
                "tags": ["cave_major", "falmer_den_major", "chaurus_nest", "dungeon_large", "morrowind_border_area"]
            }
            # ... More Rift locations
        ]
    },

    # ADDITIONAL NOTABLE LOCATIONS & DYNAMIC ADVENTURE SITES
    # IDs 100+ are for unique, cross-hold, or very significant landmarks
    {
        "id": 100,
        "name": "High Hrothgar",
        "desc": "Perched atop the Throat of the World, High Hrothgar is the sacred monastery of the Greybeards, masters of the Way of the Voice. A pilgrimage site for the Dragonborn.",
        "tags": ["monastery", "mountain_peak_settlement", "sacred_site", "greybeards_home", "dragonborn_quest", "way_of_the_voice", "unique_architecture"],
        "demographics": {"Nord Greybeards": 100},
        "travel": { "roads": [], "paths": ["Seven Thousand Steps from Ivarstead"] }
    },
    {
        "id": 101,
        "name": "Throat of the World",
        "desc": "Tamriel’s highest peak, a snow-clad titan revered by Nords and sacred to Kyne. Its summit holds ancient secrets, a Word Wall, and is where Paarthurnax resides.",
        "tags": ["mountain_summit", "sacred_peak", "snowy_extreme", "divine_kyne", "dragon_lair_paarthurnax", "dragon_word", "unique_vista", "end_game_location_potential"],
        "demographics": {"Dragons": 1, "Nord Spirits (conceptual)": 99},
        "travel": { "roads": [], "paths": ["High Hrothgar Summit Path"] }
    },
    {
        "id": 102,
        "name": "Blackreach",
        "desc": "A vast, luminous subterranean cavern system beneath Skyrim, filled with bioluminescent flora, ancient Dwemer cities, Falmer hordes, and valuable resources like Crimson Nirnroot.",
        "tags": ["underground_realm", "dwemer_city_ruined", "falmer_territory", "cavern_bioluminescent", "unique_ecosystem", "alchemy_ingredient_crimson_nirnroot", "geode_veins", "dangerous_exploration"],
        "demographics": {"Falmer": 80, "Chaurus": 15, "Dwemer Constructs": 5},
        "travel": { "roads": [], "paths": ["Alftand Elevator", "Mzinchaleft Elevator", "Raldbthar Elevator"] } # Accessed via specific Dwemer ruins
    },
    {
        "id": 103,
        "name": "Sovngarde", # Conceptual location, access is magical
        "desc": "The revered afterlife of the Nords in Aetherius, a realm of valor, feasting, and eternal glory in the Hall of Valor, accessible only to the worthy departed or via a special portal during Alduin's crisis.",
        "tags": ["afterlife_nordic", "aetherius_realm", "hall_of_valor", "heroic_spirits", "end_game_location_main", "unique_celestial"],
        "demographics": {"Nord Hero Spirits": 100},
        "travel": { "roads": [], "paths": ["Portal at Skuldafn (quest specific)"] }
    },
    {
        "id": 104,
        "name": "Labyrinthian",
        "desc": "The sprawling, maze-like ruins of the ancient Nordic city of Bromjunaar, once a center of the Dragon Cult. Now haunted by draugr, ghosts, and the powerful Dragon Priest Morokei.",
        "tags": ["nordic_ruin_major", "city_ruined_ancient", "undead_heavy", "maze_complex", "dragon_priest_morokei", "college_of_winterhold_quest", "staff_of_magnus_location", "dungeon_large"],
        "demographics": {"Draugr": 70, "Skeletons": 20, "Ghosts": 9, "Dragon Priest": 1},
        "travel": { "roads": ["Ancient Nordic Path"], "paths": ["Hjaalmarch Foothills (near Morthal)"] }
    },
    # ID 105 (Alftand) and 106 (Mzinchaleft) are better integrated into Winterhold/Pale as primary entrances to Blackreach.
    # ID 107 (Ustengrav) is detailed under Hjaalmarch.
    # ID 108 (Forelhost) is detailed under The Rift.
    # Adding new unique locations starting from 109 to avoid re-using those specific concepts unless explicitly merging.
    {
        "id": 109,
        "name": "Skuldafn Temple",
        "desc": "An ancient Nordic temple complex high in the Velothi Mountains, accessible only by dragon flight or hidden paths. It serves as a stronghold for Alduin's forces and guards the portal to Sovngarde.",
        "tags": ["nordic_temple_remote", "dragon_cult_stronghold", "alduin_forces", "sovngarde_portal_site", "end_game_dungeon", "dragon_priest_nahkriin", "dungeon_flying_access_only"],
        "demographics": {"Draugr": 80, "Dragons": 10, "Dragon Priest": 1},
        "travel": {"roads": [], "paths": ["Flight on Odahviing (quest specific)"]}
    },
    {
        "id": 110,
        "name": "Shrine of Azura",
        "desc": "A colossal statue and shrine dedicated to the Daedric Prince Azura, located high in the mountains south of Winterhold. A place of pilgrimage and prophecy.",
        "tags": ["daedric_shrine_azura", "colossal_statue", "pilgrimage_site", "prophecy_location", "quest_location_daedric_artifact", "mountain_shrine", "scenic_vista"],
        "demographics": {"Priestess of Azura": 1, "Pilgrims (occasional)": 5},
        "travel": {"roads": [], "paths": ["Winding mountain path from Winterhold vicinity"]}
    },
    {
        "id": 111,
        "name": "Shrine of Mehrunes Dagon",
        "desc": "A Daedric shrine dedicated to Mehrunes Dagon, Prince of Destruction, located in the mountains of The Pale. Site of a ritual to reforge Mehrunes' Razor.",
        "tags": ["daedric_shrine_dagon", "destruction_cult", "quest_location_daedric_artifact", "mountain_shrine", "dremora_guardians"],
        "demographics": {"Dremora": 100}, # During quest
        "travel": {"roads": [], "paths": ["Path from The Pale foothills"]}
    },
    {
        "id": 112,
        "name": "Shrine of Malacath (Largashbur)",
        "desc": "The Orc stronghold of Largashbur in The Rift, which also serves as a shrine to Malacath. The tribe is cursed and seeks aid.",
        "tags": ["orc_stronghold", "daedric_shrine_malacath", "cursed_tribe", "quest_location_daedric_artifact", "giant_attack_site"],
        "demographics": {"Orcs (cursed)": 100},
        "travel": {"roads": [], "paths": ["Path from The Rift plains"]}
    },
    {
        "id": 113,
        "name": "Shrine of Boethiah",
        "desc": "A Daedric shrine high in the mountains east of Windhelm, where followers of Boethiah engage in deadly rituals of sacrifice and combat.",
        "tags": ["daedric_shrine_boethiah", "deceit_cult", "ritual_sacrifice_site", "quest_location_daedric_artifact", "mountain_shrine", "arena_combat"],
        "demographics": {"Boethiah Cultists": 100},
        "travel": {"roads": [], "paths": ["Path from Eastmarch mountains"]}
    },
    {
        "id": 114,
        "name": "Shrine of Peryite",
        "desc": "A remote Daedric shrine in The Reach, dedicated to Peryite, the Taskmaster. His afflicted followers seek a cure.",
        "tags": ["daedric_shrine_peryite", "plague_cult", "quest_location_daedric_artifact", "remote_shrine", "alchemy_ritual"],
        "demographics": {"Afflicted Followers": 100},
        "travel": {"roads": [], "paths": ["Path from The Reach mountains"]}
    },
    {
        "id": 115,
        "name": "Sacellum of Boethiah", # Alternative/duplicate name for Shrine of Boethiah, ensuring it's covered.
        "desc": "The ritual grounds and shrine for the Daedric Prince Boethiah, located in the mountains of Eastmarch.",
        "tags": ["daedric_shrine_boethiah", "ritual_site", "mountain_location"],
        "demographics": {"Boethiah Cultists": 100},
        "travel": {"roads": [], "paths": ["Eastmarch mountains"]}
    },
    {
        "id": 116,
        "name": "Statue to Meridia",
        "desc": "A towering statue dedicated to the Daedric Prince Meridia, located on Mount Kilkreath in Haafingar. Site of a quest to cleanse her temple.",
        "tags": ["daedric_shrine_meridia", "colossal_statue", "quest_location_daedric_artifact", "mountain_shrine", "undead_cleansing_quest"],
        "demographics": {"Corrupted Shades (initially)": 100},
        "travel": {"roads": [], "paths": ["Path from Dragon Bridge area"]}
    },
    {
        "id": 117,
        "name": "Forgotten Vale", # Dawnguard DLC
        "desc": "A vast, hidden glacial valley in northwestern Skyrim, an ancient sanctuary of the Snow Elves before their corruption into Falmer. Accessed via Darkfall Cave.",
        "tags": ["hidden_valley", "snow_elf_sanctuary", "glacial_landscape", "falmer_presence", "dawnguard_quest_major", "unique_ecosystem", "ancient_ruins_snow_elf"],
        "demographics": {"Falmer": 70, "Frost Giants": 10, "Chaurus": 10, "Snow Elf Spirits (rare)": 10},
        "travel": {"roads": [], "paths": ["Darkfall Cave system"]}
    },
    {
        "id": 118,
        "name": "Soul Cairn", # Dawnguard DLC
        "desc": "A desolate plane of Oblivion where souls are trapped, often by necromancers or Daedric pacts. A realm of eerie landscapes, undead, and soul husks.",
        "tags": ["oblivion_plane", "undead_realm", "trapped_souls", "dawnguard_quest_major", "vampire_lore", "necromancy_focus", "unique_otherworldly"],
        "demographics": {"Undead (various)": 80, "Soul Husks": 10, "Ideal Masters (conceptual)": 10},
        "travel": {"roads": [], "paths": ["Portal from Castle Volkihar (quest specific)"]}
    },
    {
        "id": 119,
        "name": "Castle Volkihar", # Dawnguard DLC
        "desc": "An ancient, imposing fortress on an island off the coast of Haafingar, the primary stronghold of the Volkihar vampire clan led by Lord Harkon.",
        "tags": ["vampire_stronghold", "castle_ancient", "island_fortress", "dawnguard_quest_major", "volkihar_clan", "gothic_architecture", "powerful_vampires"],
        "demographics": {"Volkihar Vampires": 90, "Death Hounds": 10},
        "travel": {"roads": [], "paths": ["Boat from Icewater Jetty (Haafingar north coast)"]}
    },
    {
        "id": 120,
        "name": "Fort Dawnguard", # Dawnguard DLC
        "desc": "A reclaimed fortress in The Rift, serving as the headquarters for the Dawnguard, an order dedicated to hunting vampires.",
        "tags": ["vampire_hunter_hq", "fort_reclaimed", "dawnguard_order", "dawnguard_quest_major", "military_order", "weapon_crafting_specialized"],
        "demographics": {"Dawnguard Members": 100},
        "travel": {"roads": [], "paths": ["Path from The Rift near Dayspring Canyon"]}
    },
    {
        "id": 121,
        "name": "Raven Rock", # Dragonborn DLC (Solstheim) - conceptual if Solstheim is added
        "desc": "A Dunmer settlement on the island of Solstheim, originally a mining colony of the East Empire Company, now a struggling town under House Redoran's protection.",
        "tags": ["solstheim_settlement", "dunmer_town", "mining_colony_former", "house_redoran", "dragonborn_dlc_hub", "ashfall_environment"],
        "demographics": {"Dunmer": 90, "Nords": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Ship from Windhelm Docks (Solstheim)"]}
    },
    {
        "id": 122,
        "name": "Tel Mithryn", # Dragonborn DLC (Solstheim)
        "desc": "The bizarre mushroom tower home of the eccentric Telvanni wizard, Master Neloth, located on Solstheim.",
        "tags": ["solstheim_location", "telvanni_wizard_tower", "mushroom_architecture", "dragonborn_dlc_quest", "powerful_mage_residence", "unique_magical"],
        "demographics": {"Telvanni Wizard": 1, "Apprentice": 1, "Ash Spawn (nearby)": 98},
        "travel": {"roads": [], "paths": ["Path across Solstheim ashlands"]}
    },
    {
        "id": 123,
        "name": "Apocrypha", # Dragonborn DLC
        "desc": "The Daedric plane of Oblivion belonging to Hermaeus Mora, Prince of Knowledge. A vast, endless library filled with forbidden lore, tentacles, and seekers.",
        "tags": ["oblivion_plane_hermaeus_mora", "endless_library", "forbidden_knowledge", "dragonborn_dlc_major", "tentacles_seekers_lurkers", "unique_otherworldly_books"],
        "demographics": {"Seekers": 70, "Lurkers": 30},
        "travel": {"roads": [], "paths": ["Black Books (portals from Solstheim)"]}
    }
]