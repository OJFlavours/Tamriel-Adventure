LOCATIONS = [
    # WHITERUN HOLD
    {
        "id": 1,
        "name": "Whiterun Hold",
        "desc": "The fertile heartland of Skyrim, marked by golden plains and the bustling city of Whiterun. A center of commerce, conflict, and tradition.",
        "tags": ["hold", "plains", "central", "commerce"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["Riften", "Windhelm", "Markarth", "Solitude"],
            "paths": ["Riverwood", "Rorikstead"]
        },
        "sub_locations": [
            {
                "id": 10,
                "name": "Whiterun",
                "desc": "A thriving trade city built around the great keep Dragonsreach. Its bustling market and legendary mead hall form the heart of the hold.",
                "tags": ["city", "capital", "trade", "whiterun", "market", "jarls_seat"],
                "sub_locations": [
                    {
                        "id": 1001,
                        "name": "Dragonsreach",
                        "desc": "The imposing keep of the Jarl, an iconic symbol of Nord authority and power.",
                        "tags": ["keep", "government"]
                    },
                    {
                        "id": 1002,
                        "name": "Jorrvaskr",
                        "desc": "The ancient mead hall and headquarters of the Companions, where warriors forge bonds in battle.",
                        "tags": ["meadhall", "companions"]
                    },
                    {
                        "id": 1003,
                        "name": "The Bannered Mare",
                        "desc": "A lively tavern where travelers and locals share stories over hearty ale.",
                        "tags": ["tavern", "social"]
                    },
                    {
                        "id": 1004,
                        "name": "Warmaiden's",
                        "desc": "A masterful smithy known for crafting legendary weapons and armor.",
                        "tags": ["blacksmith"]
                    },
                    {
                        "id": 1005,
                        "name": "Arcadia's Cauldron",
                        "desc": "A cozy apothecary brimming with rare ingredients and potent potions.",
                        "tags": ["alchemy", "shop"]
                    },
                    {
                        "id": 1006,
                        "name": "Temple of Kynareth",
                        "desc": "A serene temple devoted to the wind and healing, frequented by local worshippers.",
                        "tags": ["temple", "healer"]
                    },
                    {
                        "id": 1007,
                        "name": "Plains District Market",
                        "desc": "Bustling stalls offering regional produce, crafts, and curiosities.",
                        "tags": ["market"]
                    }
                ]
            },
            {
                "id": 11,
                "name": "Riverwood",
                "desc": "A quaint logging village along the White River, known for its simplicity and rustic charm.",
                "tags": ["village", "lumber"],
                "sub_locations": [
                    {
                        "id": 1101,
                        "name": "Sleeping Giant Inn",
                        "desc": "A warm inn that serves as a gathering point for weary travelers.",
                        "tags": ["inn", "tavern"]
                    },
                    {
                        "id": 1102,
                        "name": "Riverwood Trader",
                        "desc": "A modest shop offering a variety of everyday goods.",
                        "tags": ["shop"]
                    },
                    {
                        "id": 1103,
                        "name": "Alvor's Smithy",
                        "desc": "The local blacksmith renowned for practical and durable tools.",
                        "tags": ["blacksmith"]
                    }
                ]
            },
            {
                "id": 12,
                "name": "Rorikstead",
                "desc": "A fertile farming village that supplies Whiterun with delicious produce, demonstrating the rugged yet bountiful nature of Skyrim.",
                "tags": ["village", "farm"]
            },
            {
                "id": 13,
                "name": "Honningbrew Meadery",
                "desc": "Famed for its exceptionally smooth mead, a visit here is both a taste of history and local culture.",
                "tags": ["meadery", "brewery"]
            },
            {
                "id": 14,
                "name": "Western Watchtower",
                "desc": "A ruined guard tower on the outskirts, scarred by dragon fire and a potential site for hidden quests.",
                "tags": ["watchtower", "ruin", "dragon"]
            },
            {
                "id": 15,
                "name": "Bleak Falls Barrow",
                "desc": "An ancient Nordic tomb high among the mountains, crawling with draugr and secrets of old.",
                "tags": ["barrow", "dungeon", "undead"]
            },
            {
                "id": 16,
                "name": "Silent Moons Camp",
                "desc": "A clandestine bandit camp hidden in the wilderness, offering both danger and the thrill of adventure.",
                "tags": ["bandit", "ruin", "camp"]
            }
        ]
    },

    # THE PALE
    {
        "id": 2,
        "name": "The Pale",
        "desc": "A frozen hold of bleak beauty, stretching from snow-tipped plains to the Sea of Ghosts. Harsh and unforgiving, yet full of untold opportunities.",
        "tags": ["hold", "snow", "coastal", "mining"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {
            "roads": ["Dawnstar", "Windhelm"],
            "paths": ["Icespire", "Frost Road"]
        },
        "sub_locations": [
            {
                "id": 20,
                "name": "Dawnstar",
                "desc": "A resilient town on the northern edge, thriving on fishing, mining, and hardy tradition.",
                "tags": ["town", "port", "dawnstar", "isolated"],  # Added "dawnstar" tag
                "sub_locations": [
                    {
                        "id": 2001,
                        "name": "Windpeak Inn",
                        "desc": "The cozy inn that offers respite from the icy winds.",
                        "tags": ["inn", "tavern"]
                    },
                    {
                        "id": 2002,
                        "name": "Quicksilver Mine",
                        "desc": "A treacherous mine rich in precious metals, now frequented by bandits.",
                        "tags": ["mine", "dungeon"]
                    },
                    {
                        "id": 2003,
                        "name": "The Mortar and Pestle",
                        "desc": "A humble alchemy shop where local brews and potions are concocted.",
                        "tags": ["alchemy", "shop"]
                    },
                                        {
                        "id": 2004,
                        "name": "The Frozen Tankard",
                        "desc": "A local tavern known for its strong ales and sea shanties.",
                        "tags": ["tavern", "social"]
                    }
                ]
            },
            {
                "id": 21,
                "name": "Nightcaller Temple",
                "desc": "An eerie, abandoned temple clinging to rugged cliffs, rumored to have been dedicated to a Daedric Prince.",
                "tags": ["temple", "daedric", "ruin"]
            },
            {
                "id": 22,
                "name": "Iron-Breaker Mine",
                "desc": "A dilapidated mine known for its rich veins of iron, now a hotbed for daring adventurers.",
                "tags": ["mine", "dungeon"]
            },
            {
                "id": 23,
                "name": "Wreck of the Brinehammer",
                "desc": "The ghostly remains of a long-forgotten shipwreck scattered along the storm-battered coast.",
                "tags": ["wreck", "ruin"]
            },
            {
                "id": 24,
                "name": "Frostflow Lighthouse",
                "desc": "A solitary lighthouse standing guard over treacherous waters, haunted by the echoes of shipwrecks.",
                "tags": ["lighthouse", "haunted"]
            }
        ]
    },

    # WINTERHOLD HOLD
    {
        "id": 3,
        "name": "Winterhold",
        "desc": "A shattered hold on the northern coast, now synonymous with magic, ruin, and the enigmatic College of Winterhold.",
        "tags": ["hold", "snow", "coastal", "magic", "ruin"],
        "demographics": {"Nord": 75, "Altmer": 10, "Dunmer": 10, "Others": 5},
        "travel": {
            "roads": ["Dawnstar", "Windhelm"],
            "paths": ["Saarthal", "Icespire"]
        },
        "sub_locations": [
            {
                "id": 30,
                "name": "Winterhold (Town)",
                "desc": "A ghost town clinging to remnants of its past amid the ruins left by the sea.",
                "tags": ["town", "ruin", "winterhold", "magical"],  # Added "winterhold" tag
                "sub_locations": [
                    {
                        "id": 3001,
                        "name": "The Frozen Hearth",
                        "desc": "The sole remaining inn, where whispers of arcane power and lost histories abound.",
                        "tags": ["inn", "tavern"]
                    },
                    {
                        "id": 3002,
                        "name": "College of Winterhold",
                        "desc": "A venerable institution of magic, rife with secrets and forbidden lore.",
                        "tags": ["college", "magic", "guild"]
                    },
                    {
                        "id": 3003,
                        "name": "Jarl's Longhouse",
                        "desc": "The crumbling seat of local authority, a relic of Winterhold's former glory.",
                        "tags": ["government"]
                    }
                ]
            },
            {
                "id": 31,
                "name": "Saarthal",
                "desc": "The excavated ruins of one of Skyrim's first settlements, echoing with the voices of the dead.",
                "tags": ["ruin", "dungeon", "undead"]
            },
            {
                "id": 32,
                "name": "Hob's Fall Cave",
                "desc": "A shadowy coastal cave rumored to shelter both lost treasures and sinister forces.",
                "tags": ["cave", "necromancer", "dungeon"]
            },
            {
                "id": 33,
                "name": "Yngol Barrow",
                "desc": "A mournful tomb where ancient magics linger and the dead whisper their secrets.",
                "tags": ["barrow", "undead", "ruin"]
            }
        ]
    },

    # HJAALMARCH (Morthal Hold)
    {
        "id": 4,
        "name": "Hjaalmarch",
        "desc": "A bleak, marshy hold shrouded in perpetual mist and steeped in superstition, dominated by the enigmatic town of Morthal.",
        "tags": ["hold", "marsh", "swamp", "isolated"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {
            "roads": ["Dawnstar"],
            "paths": ["Stonehills", "Marsh Way"]
        },
        "sub_locations": [
            {
                "id": 40,
                "name": "Morthal",
                "desc": "A somber town wrapped in fog and mystery, where every shadow hides an untold story.",
                "tags": ["town", "marsh", "morthal", "superstitious"],  # Added "morthal" tag
                "sub_locations": [
                    {
                        "id": 4001,
                        "name": "Highmoon Hall",
                        "desc": "The austere residence of the Jarl, echoing with whispered decrees.",
                        "tags": ["government"]
                    },
                    {
                        "id": 4002,
                        "name": "Moorside Inn",
                        "desc": "A humble inn providing shelter for travelers daring to brave the murky swamps.",
                        "tags": ["inn", "tavern"]
                    },
                                        {
                        "id": 4003,
                        "name": "The Foggy Bottle",
                        "desc": "A dimly lit tavern known for its potent drinks and hushed conversations.",
                        "tags": ["tavern", "social"]
                    }
                ]
            },
            {
                "id": 41,
                "name": "Movarth's Lair",
                "desc": "A dank cave rumoured to be the den of a fearsome vampire, where darkness reigns supreme.",
                "tags": ["cave", "vampire", "dungeon"]
            },
            {
                "id": 42,
                "name": "Ustengrav",
                "desc": "A sprawling Nordic tomb filled with stalwart draugr and relics of a time long past.",
                "tags": ["barrow", "dungeon", "undead"]
            },
            {
                "id": 43,
                "name": "Stonehills",
                "desc": "A modest mining outpost hidden in the marshes, a source of ore and local legends.",
                "tags": ["village", "mine"]
            }
        ]
    },

    # FALKREATH HOLD
    {
        "id": 5,
        "name": "Falkreath Hold",
        "desc": "A heavily forested hold in southern Skyrim, enveloped in mystery and dark legends, renowned for its sprawling graveyard and haunting tales.",
        "tags": ["hold", "forest", "southern", "graveyard"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["Whiterun"],
            "paths": ["Helgen", "Deep Woods", "Forest Trail"]
        },
        "sub_locations": [
            {
                "id": 50,
                "name": "Falkreath",
                "desc": "A quiet town immersed in lore and veiled in legend, where the past and present converge.",
                "tags": ["town", "forest", "falkreath", "lore"],  # Added "falkreath" tag
                "sub_locations": [
                    {
                        "id": 5001,
                        "name": "Dead Man's Drink",
                        "desc": "The local tavern where the echoes of long-gone heroes are exchanged over hearty ale.",
                        "tags": ["tavern", "social"]
                    },
                    {
                        "id": 5002,
                        "name": "Jarl's Longhouse",
                        "desc": "The center of authority and solemn traditions in Falkreath.",
                        "tags": ["government"]
                    },
                    {
                        "id": 5003,
                        "name": "Falkreath Graveyard",
                        "desc": "An expansive cemetery said to be haunted by the restless spirits of ancient warriors.",
                        "tags": ["graveyard", "haunted"]
                    }
                ]
            },
            {
                "id": 51,
                "name": "Pinewatch",
                "desc": "A secluded farmhouse with whispers of a secret bandit hideout hidden beneath its pastoral veneer.",
                "tags": ["farm", "bandit", "dungeon"]
            },
            {
                "id": 52,
                "name": "Halldir's Cairn",
                "desc": "A solemn Nordic barrow that stands as a silent monument to battles of old.",
                "tags": ["barrow", "dungeon", "ghost"]
            }
        ]
    },

    # THE REACH (Markarth Hold)
    {
        "id": 6,
        "name": "The Reach",
        "desc": "A wild, mountainous region of ancient ruins, rebel encampments, and hidden wonders, with Markarth as its crown jewel.",
        "tags": ["hold", "mountain", "dwemer", "forsworn"],
        "demographics": {"Nord": 60, "Reachmen": 30, "Others": 10},
        "travel": {
            "roads": ["Whiterun", "Solitude"],
            "paths": ["Dushnikh Yal", "Deep Canyons", "Mountain Pass"]
        },
        "sub_locations": [
            {
                "id": 60,
                "name": "Markarth",
                "desc": "A city hewn from ancient Dwemer stone where treachery and treasures hide in its labyrinthine passages.",
                "tags": ["city", "dwemer", "mountain", "markarth", "rebellion"],  # Added "markarth" tag
                "sub_locations": [
                    {
                        "id": 6001,
                        "name": "Silver-Blood Inn",
                        "desc": "A bustling tavern and meeting point for rebels, traders, and mercenaries.",
                        "tags": ["tavern"]
                    },
                    {
                        "id": 6002,
                        "name": "Understone Keep",
                        "desc": "An ancient fortification carved into the rock, the seat of local power.",
                        "tags": ["keep", "government", "dwemer"]
                    },
                    {
                        "id": 6003,
                        "name": "Cidhna Mine",
                        "desc": "A notorious mine and prison, steeped in controversy and legend.",
                        "tags": ["mine", "prison"]
                    }
                ]
            },
            {
                "id": 61,
                "name": "Karthwasten",
                "desc": "A rugged mining village amid strife and shadow, whispered to be touched by the hand of rebellion.",
                "tags": ["village", "mining"]
            },
            {
                "id": 62,
                "name": "Druadach Redoubt",
                "desc": "A hidden Forsworn encampment tucked away in the high mountains, where rebel hearts beat defiantly.",
                "tags": ["camp", "forsworn", "wilderness"]
            },
            {
                "id": 63,
                "name": "Deep Folk Crossing",
                "desc": "An ancient Dwemer bridge spanning a tumultuous river, a relic obscured by time and mystery.",
                "tags": ["dwemer", "bridge", "ruin"]
            }
        ]
    },

    # EASTMARCH (Windhelm Hold)
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A fierce, volcanic hold dominated by the storied city of Windhelm, where ancient traditions clash with modern strife.",
        "tags": ["hold", "volcanic", "nordic", "stormcloak"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Others": 5},
        "travel": {
            "roads": ["Whiterun", "Riften"],
            "paths": ["High Lava Pass", "Stony Road"]
        },
        "sub_locations": [
            {
                "id": 70,
                "name": "Windhelm",
                "desc": "One of Skyrim's oldest cities, imbued with the spirit of Stormcloaks and ancient Nordic valor.",
                "tags": ["city", "capital", "nordic", "windhelm", "historic"],  # Added "windhelm" tag
                "sub_locations": [
                    {
                        "id": 7001,
                        "name": "Candlehearth Hall",
                        "desc": "A historic tavern celebrated for its robust mead and stirring tales.",
                        "tags": ["tavern", "social"]
                    },
                    {
                        "id": 7002,
                        "name": "Oengul's Smithy",
                        "desc": "A renowned forge where mightiest weapons are crafted.",
                        "tags": ["blacksmith"]
                    },
                    {
                        "id": 7003,
                        "name": "Palace of the Kings",
                        "desc": "The formidable seat of Ulfric Stormcloak, echoing with the voices of ancient warriors.",
                        "tags": ["government", "military"]
                    },
                    {
                        "id": 7004,
                        "name": "The White Phial",
                        "desc": "An esteemed apothecary known for rare elixirs and mysterious remedies.",
                        "tags": ["alchemy", "shop"]
                    }
                ]
            },
            {
                "id": 71,
                "name": "Kynesgrove",
                "desc": "A small, industrious mining village clinging to the volcanic slopes near Windhelm.",
                "tags": ["village", "mining"]
            },
            {
                "id": 72,
                "name": "Fort Greymoor",
                "desc": "A weathered, battle-scarred fort that has witnessed countless clashes.",
                "tags": ["fort", "ruin", "military"]
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove where pilgrims and druids seek solace and natural healing.",
                "tags": ["sanctuary", "sacred", "forest"]
            }
        ]
    },

    # HAAFINGAR (Solitude Hold)
    {
        "id": 8,
        "name": "Haafingar",
        "desc": "A coastal hold rich in Imperial influence and maritime heritage, led by the stately city of Solitude.",
        "tags": ["hold", "coastal", "imperial", "maritime"],
        "demographics": {"Nord": 70, "Imperial": 20, "Others": 10},
        "travel": {
            "roads": ["Markarth", "Whiterun", "Dawnstar"],
            "paths": ["Dragon Bridge", "Coastal Way"]
        },
        "sub_locations": [
            {
                "id": 80,
                "name": "Solitude",
                "desc": "A majestic city perched atop a rocky promontory, epitomizing Imperial grandeur and Nordic resilience.",
                "tags": ["city", "capital", "imperial", "solitude", "wealth"],  # Added "solitude" tag
                "sub_locations": [
                    {
                        "id": 8001,
                        "name": "Blue Palace",
                        "desc": "The opulent palace that stands as the seat of government and royal authority.",
                        "tags": ["palace", "government"]
                    },
                    {
                        "id": 8002,
                        "name": "Castle Dour",
                        "desc": "A robust fortification housing the Imperial Legion and guarding the western frontier.",
                        "tags": ["fort", "military"]
                    },
                    {
                        "id": 8003,
                        "name": "The Winking Skeever",
                        "desc": "A favorite tavern where locals and travelers exchange hearty tales and libations.",
                        "tags": ["tavern", "social"]
                    }
                ]
            },
            {
                "id": 81,
                "name": "Dragon Bridge",
                "desc": "A quaint village built around an ancient stone bridge adorned with dragon motifs.",
                "tags": ["village", "bridge"]
            },
            {
                "id": 82,
                "name": "Wolfskull Cave",
                "desc": "A dark, foreboding cave reputed to harbor necromancers and restless spirits.",
                "tags": ["cave", "dungeon", "haunted"]
            },
            {
                "id": 83,
                "name": "Fort Hraggstad",
                "desc": "An Imperial outpost that stands as a bulwark against the wild lands beyond.",
                "tags": ["fort", "military"]
            }
        ]
    },

    # THE RIFT (Riften Hold)
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A lush, verdant hold defined by dense forests, flowing rivers, and the enigmatic city of Riften, where intrigue and mystery intertwine.",
        "tags": ["hold", "forest", "water", "autumnal"],
        "demographics": {"Nord": 75, "Dunmer": 10, "Argonian": 10, "Others": 5},
        "travel": {
            "roads": ["Whiterun", "Windhelm"],
            "paths": ["Hidden Trails", "River Paths"]
        },
        "sub_locations": [
            {
                "id": 90,
                "name": "Riften",
                "desc": "A city of contrasts, where gleaming canals meet the dark secrets of the underground Ratway.",
                "tags": ["city", "underground", "riften", "thieves"],  # Added "riften" tag
                "sub_locations": [
                    {
                        "id": 9001,
                        "name": "The Bee and Barb",
                        "desc": "A smoky tavern favored by the Thieves Guild and shadowy figures.",
                        "tags": ["tavern", "social", "thieves"]
                    },
                    {
                        "id": 9002,
                        "name": "Black-Briar Meadery",
                        "desc": "A thriving establishment blending commerce with an air of mystery.",
                        "tags": ["shop", "tavern"]
                    },
                    {
                        "id": 9003,
                        "name": "The Pawned Prawn",
                        "desc": "An eclectic shop offering rare curios and oddities.",
                        "tags": ["shop", "general"]
                    },
                    {
                        "id": 9004,
                        "name": "Mistveil Keep",
                        "desc": "A symbol of order amidst chaos, the keep watches over the city.",
                        "tags": ["keep", "government"]
                    },
                    {
                        "id": 9005,
                        "name": "The Ratway",
                        "desc": "A labyrinthine network of tunnels beneath the city, fraught with hidden dangers.",
                        "tags": ["dungeon", "underground"]
                    }
                ]
            },
            {
                "id": 91,
                "name": "Lost Prospect Mine",
                "desc": "An abandoned mine where bandits lurk and dark secrets await the brave.",
                "tags": ["mine", "dungeon"]
            },
            {
                "id": 92,
                "name": "Broken Helm Hollow",
                "desc": "A secluded cave and bandit refuge deep in the forest, promising peril and potential treasure.",
                "tags": ["bandit", "cave", "wilderness"]
            }
        ]
    },

    # ADDITIONAL NOTABLE LOCATIONS & DYNAMIC ADVENTURE SITES
    {
        "id": 100,
        "name": "High Hrothgar",
        "desc": "Perched atop the Throat of the World, High Hrothgar is the sacred fortress of the Greybeards and a pilgrimage site for the Dragonborn.",
        "tags": ["monastery", "mountain", "sacred", "greybeards"],
        "demographics": {"Nord": 100},
        "travel": {
            "roads": [],
            "paths": ["Ivarstead"]
        }
    },
    {
        "id": 101,
        "name": "Throat of the World",
        "desc": "Tamriel’s highest peak, a snow-clad titan honored by the Nords and Kynareth. Its frozen summit inspires awe and trepidation.",
        "tags": ["mountain", "sacred", "snowy", "divine"],
        "demographics": {"Nord": 100},
        "travel": {
            "roads": [],
            "paths": ["High Hrothgar"]
        }
    },
    {
        "id": 102,
        "name": "Blackreach",
        "desc": "A sprawling, luminous underground cavern teeming with bioluminescent flora, ancient Dwemer relics, and lurking Falmer. Accessible via well-known Dwemer passages.",
        "tags": ["underground", "dwemer", "falmer", "cavern", "ruin"],
        "demographics": {"Falmer": 100},
        "travel": {
            "roads": ["Secret Dwemer Road"],
            "paths": ["Alftand Passage", "Mzinchaleft Tunnel"]
        }
    },
    {
        "id": 104,
        "name": "Labyrinthian",
        "desc": "A vast, maze-like ruin once a grand Nord city, now overrun by draugr and cursed with the lingering magic of a forgotten dragon priest.",
        "tags": ["ruin", "nordic", "undead", "maze", "dungeon"],
        "demographics": {"Nord": 100},
        "travel": {
            "roads": ["Ancient Road"],
            "paths": ["Morthal"]
        }
    },
    {
        "id": 105,
        "name": "Alftand",
        "desc": "A mysterious Dwemer ruin in the frozen wastes near Winterhold, rumored to be a gateway into the depths of Blackreach.",
        "tags": ["dwemer", "ruin", "snowy", "underground", "mechanical"],
        "demographics": {"Dwemer": 100},
        "travel": {
            "roads": ["Forgotten Trail"],
            "paths": ["Winterhold"]
        }
    },
    {
        "id": 106,
        "name": "Mzinchaleft",
        "desc": "A sprawling Dwemer ruin in the Pale with bronze corridors and ingenious mechanisms that hint at a lost civilization.",
        "tags": ["dwemer", "ruin", "mechanical", "snowy"],
        "demographics": {"Dwemer": 100},
        "travel": {
            "roads": ["Dwarven Way"],
            "paths": ["Dawnstar"]
        }
    },
    {
        "id": 107,
        "name": "Ustengrav",
        "desc": "A vast Nordic tomb in Hjaalmarch\'s marshes, its dark corridors echo with the clamor of ancient battles and the lure of cursed treasures.",
        "tags": ["barrow", "nordic", "undead", "swamp", "dungeon"],
        "demographics": {"Nord": 100},
        "travel": {
            "roads": ["Marsh Path"],
            "paths": ["Morthal"]
        }
    },
    {
        "id": 108,
        "name": "Forelhost",
        "desc": "A spectral ruin in the Rift’s high mountains, once a stronghold of the Dragon Cult, now haunted by the remnants of draconic power.",
        "tags": ["ruin", "nordic", "undead", "mountain", "dragon", "cursed"],
        "demographics": {"Nord": 100},
        "travel": {
            "roads": ["Mountain Trail"],
            "paths": ["Riften"]
        }
    }
]