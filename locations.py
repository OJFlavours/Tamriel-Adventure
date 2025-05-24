LOCATIONS = [
    {
        "id": 1,
        "name": "Whiterun",
        "desc": "Whiterun, the heart of Skyrim, sprawls across the windswept plains, its towering Dragonsreach keep gazing over bustling markets and sturdy longhouses.",
        "tags": ["city", "nordic", "trade", "plains", "neutral"],
        "demographics": {"Nord": 80, "Imperial": 10, "Breton": 5, "Others": 5},
        "travel": {"roads": ["Riften", "Windhelm", "Markarth", "Solitude"], "paths": ["Riverwood", "Rorikstead"]},
        "sub_locations": [
            {"id": 1, "name": "The Bannered Mare", "desc": "A lively tavern filled with the aroma of mead and the chatter of locals.", "tags": ["tavern", "social"]},
            {"id": 2, "name": "Warmaiden's", "desc": "A blacksmith shop where Ulfberth War-Bear and Adrianne Avenicci forge fine weapons and armor.", "tags": ["shop", "blacksmith"]},
            {"id": 3, "name": "Arcadia's Cauldron", "desc": "A cozy apothecary where Arcadia sells potions and ingredients.", "tags": ["shop", "alchemy"]},
            {"id": 4, "name": "Belethor's General Goods", "desc": "A cluttered shop with a wide variety of items for sale.", "tags": ["shop", "general"]},
            {"id": 5, "name": "Dragonsreach", "desc": "The Jarl's keep, a formidable structure with a rich history.", "tags": ["government", "military"]}
        ]
    },
    {
        "id": 2,
        "name": "Riften",
        "desc": "Riften, nestled in the golden forests of the Rift, is a city of shadows and commerce. Its canals gleam, but the Ratway beneath hides the Thieves Guild’s schemes.",
        "tags": ["city", "nordic", "trade", "underworld", "forest", "canals", "thieves"],
        "demographics": {"Nord": 75, "Dunmer": 10, "Argonian": 10, "Others": 5},
        "travel": {"roads": ["Whiterun", "Windhelm"], "paths": ["Ivarstead", "Shor's Stone"]},
        "sub_locations": [
            {"id": 1, "name": "The Bee and Barb", "desc": "A shady tavern frequented by Thieves Guild members.", "tags": ["tavern", "social", "thieves"]},
            {"id": 2, "name": "Black-Briar Meadery", "desc": "The heart of Maven Black-Briar’s empire.", "tags": ["shop", "tavern"]},
            {"id": 3, "name": "The Pawned Prawn", "desc": "A curio shop with rare and unusual items.", "tags": ["shop", "general"]},
            {"id": 4, "name": "Mistveil Keep", "desc": "The Jarl's keep, overlooking the city.", "tags": ["government", "military"]},
            {"id": 5, "name": "The Ratway", "desc": "A dangerous network of tunnels beneath Riften.", "tags": ["underworld", "dungeon"]}
        ]
    },
    {
        "id": 3,
        "name": "Markarth",
        "desc": "Markarth, carved into the jagged cliffs of the Reach, is a fortress of Dwemer stone and Nord resilience.",
        "tags": ["city", "nordic", "reachmen", "mining", "cliffs", "dwemer", "forsworn"],
        "demographics": {"Nord": 70, "Reachmen": 20, "Breton": 5, "Others": 5},
        "travel": {"roads": ["Whiterun", "Solitude"], "paths": ["Karthwasten", "Dushnikh Yal"]},
        "sub_locations": [
            {"id": 1, "name": "Silver-Blood Inn", "desc": "A bustling inn owned by the powerful Silver-Blood family.", "tags": ["tavern", "social"]},
            {"id": 2, "name": "Arnleif and Sons Trading Company", "desc": "A general store stocked with goods from across Skyrim.", "tags": ["shop", "general"]},
            {"id": 3, "name": "The Treasury House", "desc": "The headquarters of the Silver-Blood family's financial operations.", "tags": ["government", "business"]},
            {"id": 4, "name": "Understone Keep", "desc": "A Dwemer ruin beneath Markarth, now used as a keep.", "tags": ["dwemer", "military"]},
            {"id": 5, "name": "Cidhna Mine", "desc": "A notorious mine and prison controlled by the Silver-Bloods.", "tags": ["mine", "prison"]}
        ]
    },
    {
        "id": 4,
        "name": "Winterhold",
        "desc": "Winterhold, perched on Skyrim’s icy northern coast, clings to its fading glory. Once a rival to Solitude, its collapse into the sea left only the College of Winterhold.",
        "tags": ["city", "nordic", "magic", "coastal", "ruined", "college", "snowy"],
        "demographics": {"Nord": 75, "Altmer": 10, "Dunmer": 10, "Others": 5},
        "travel": {"roads": ["Windhelm", "Dawnstar"], "paths": ["Saarthal"]},
        "sub_locations": [
            {"id": 1, "name": "The Frozen Hearth", "desc": "A small inn offering warmth and shelter in the frigid town.", "tags": ["tavern", "social"]},
            {"id": 2, "name": "The College of Winterhold", "desc": "A renowned school for mages and scholars.", "tags": ["magic", "school"]},
            {"id": 3, "name": "Jorunn's stall", "desc": "A small stall selling fish and supplies.", "tags": ["shop", "general"]},
        ]
    },
    {
        "id": 5,
        "name": "Solitude",
        "desc": "Solitude, Skyrim’s imperial jewel, crowns a rocky arch over the Karth River. As the High King’s seat and the Empire’s stronghold, its Blue Palace radiates authority.",
        "tags": ["city", "nordic", "imperial", "port", "capital", "coastal", "bards", "military"],
        "demographics": {"Nord": 70, "Imperial": 15, "Breton": 10, "Others": 5},
        "travel": {"roads": ["Markarth", "Whiterun", "Dawnstar"], "paths": ["Dragon Bridge"]},
        "sub_locations": [
            {"id": 1, "name": "The Winking Skeever", "desc": "A cozy tavern popular with travelers and soldiers.", "tags": ["tavern", "social"]},
            {"id": 2, "name": "Radiant Raiment", "desc": "A high-end clothing shop run by the Altmer sisters.", "tags": ["shop", "clothing"]},
            {"id": 3, "name": "Blue Palace", "desc": "The Jarl's palace, home to the High King of Skyrim.", "tags": ["government", "military"]},
            {"id": 4, "name": "Bits and Pieces", "desc": "A shop selling a variety of odds and ends.", "tags": ["shop", "general"]},
            {"id": 5, "name": "Castle Dour", "desc": "The headquarters of the Imperial Legion in Skyrim.", "tags": ["military"]}
        ]
    },
    {
        "id": 6,
        "name": "Windhelm",
        "desc": "Windhelm, the ancient seat of Ysgramor, stands as a frozen bastion of Nord pride. Its stone walls house Ulfric Stormcloak’s rebellion.",
        "tags": ["city", "nordic", "military", "snowy", "stormcloak", "ancient", "docks", "tense"],
        "demographics": {"Nord": 85, "Dunmer": 10, "Others": 5},
        "travel": {"roads": ["Whiterun", "Riften", "Winterhold"], "paths": ["Kynesgrove"]},
        "sub_locations": [
            {"id": 1, "name": "Candlehearth Hall", "desc": "A historic tavern where Stormcloak soldiers and locals share tales over mead.", "tags": ["tavern", "social", "stormcloak"]},
            {"id": 2, "name": "Oengul's Smithy", "desc": "Oengul War-Anvil’s forge produces sturdy weapons for Windhelm’s warriors.", "tags": ["shop", "blacksmith"]},
            {"id": 3, "name": "Palace of the Kings", "desc": "The seat of Ulfric Stormcloak and the Stormcloak rebellion.", "tags": ["government", "military"]},
            {"id": 4, "name": "The White Phial", "desc": "An apothecary shop with a reputation for rare and exotic ingredients.", "tags": ["shop", "alchemy"]},
            {"id": 5, "name": "Sadri's Used Wares", "desc": "A shop selling a variety of used goods.", "tags": ["shop", "general"]}
        ]
    },
    {
        "id": 7,
        "name": "Dawnstar",
        "desc": "Dawnstar, a windswept port on Skyrim’s northern coast, thrives on fishing and mining.",
        "tags": ["town", "nordic", "port", "snowy", "mining", "coastal", "darkbrotherhood"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {"roads": ["Solitude", "Winterhold"], "paths": ["Morthal"]}
    },
    {
        "id": 8,
        "name": "Falkreath",
        "desc": "Falkreath, nestled in southern Skyrim’s pine forests, is a somber town famed for its vast cemetery, where Nord heroes rest.",
        "tags": ["town", "nordic", "forest", "cemetery", "lake", "hunting", "imperial"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {"roads": ["Whiterun"], "paths": ["Helgen"]}
    },
    {
        "id": 9,
        "name": "Morthal",
        "desc": "Morthal, shrouded in the fog of Hjaalmarch’s marshes, is a town of mystery and suspicion.",
        "tags": ["town", "nordic", "swamp", "mystical", "foggy", "fishing", "vampire"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {"roads": ["Dawnstar"], "paths": ["Stonehills"]}
    },
    {
        "id": 10,
        "name": "Riverwood",
        "desc": "Riverwood, a tranquil logging village along the White River, is a haven of Nord simplicity.",
        "tags": ["village", "nordic", "river", "logging", "plains", "inn", "peaceful"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Whiterun", "Helgen"]}
    },
    {
        "id": 11,
        "name": "Ivarstead",
        "desc": "Ivarstead, a humble village at the foot of the Throat of the World, serves as a rest for pilgrims climbing to High Hrothgar.",
        "tags": ["village", "nordic", "mountain", "pilgrim", "river", "farming", "haunted"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Riften", "High Hrothgar"]}
    },
    {
        "id": 12,
        "name": "Karthwasten",
        "desc": "Karthwasten, a rugged mining village in the Reach, lies in the shadow of Markarth’s conflicts.",
        "tags": ["village", "nordic", "reachmen", "mining", "cliffs", "conflict", "silver"],
        "demographics": {"Nord": 60, "Reachmen": 30, "Breton": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Markarth"]}
    },
    {
        "id": 13,
        "name": "Dragon Bridge",
        "desc": "Dragon Bridge, a quaint village west of Solitude, is named for its ancient stone bridge adorned with dragon skulls.",
        "tags": ["village", "nordic", "river", "bridge", "lumber", "imperial", "travel"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {"roads": [], "paths": ["Solitude"]}
    },
    {
        "id": 14,
        "name": "Kynesgrove",
        "desc": "Kynesgrove, a small mining village in Eastmarch, clings to the volcanic slopes near Windhelm.",
        "tags": ["village", "nordic", "mining", "volcanic", "sacred", "malachite"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 15,
        "name": "Helgen",
        "desc": "Helgen, once a fortified town on Skyrim’s southern border, lies in ruins after a dragon’s fiery assault.",
        "tags": ["town", "nordic", "ruin", "destroyed", "mountain", "bandits", "dragon"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Riverwood", "Falkreath"]}
    },
    {
        "id": 16,
        "name": "Rorikstead",
        "desc": "Rorikstead, a fertile farming village in Whiterun’s plains, thrives despite Skyrim’s harsh climate.",
        "tags": ["village", "nordic", "farming", "plains", "inn", "fertile", "mysterious"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Whiterun"]}
    },
    {
        "id": 17,
        "name": "Shor's Stone",
        "desc": "Shor’s Stone, a hardy mining village in the Rift, extracts ebony from the volcanic earth.",
        "tags": ["village", "nordic", "mining", "volcanic", "ebony", "sacred", "spiders"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Riften"]}
    },
    {
        "id": 18,
        "name": "Stonehills",
        "desc": "Stonehills, a bleak mining camp in Hjaalmarch’s marshes, supports Morthal’s economy.",
        "tags": ["village", "nordic", "mining", "swamp", "iron", "haunted", "harsh"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {"roads": [], "paths": ["Morthal"]}
    },
    {
        "id": 19,
        "name": "High Hrothgar",
        "desc": "High Hrothgar, a sacred monastery perched on the Throat of the World, is home to the Greybeards, masters of the Thu’um.",
        "tags": ["monastery", "nordic", "mountain", "sacred", "greybeards", "thu’um", "isolated"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Ivarstead"]}
    },
    {
        "id": 20,
        "name": "Throat of the World",
        "desc": "The Throat of the World, Tamriel’s highest peak, towers over Skyrim, its snow-clad summit sacred to Kynareth and the Nords.",
        "tags": ["mountain", "nordic", "sacred", "snowy", "dragon", "isolated", "divine"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["High Hrothgar"]}
    },
    {
        "id": 21,
        "name": "Blackreach",
        "desc": "Blackreach, a colossal underground cavern beneath Skyrim, glows with eerie mushrooms and Dwemer ruins. Falmer skulk in its shadows, guarding the lost city of the Dwemer.",
        "tags": ["dwemer", "falmer", "underground", "cavern", "ruin", "eerie", "mushrooms"],
        "demographics": {"Falmer": 100},
        "travel": {"roads": [], "paths": []}
    },
    {
        "id": 22,
        "name": "Forgotten Vale",
        "desc": "The Forgotten Vale, a hidden glacial valley, shelters the last Snow Elves in its frost-kissed groves. Ancient Falmer ruins dot the landscape, and the Chantry of Auri-El glows with divine light.",
        "tags": ["snow elf", "falmer", "glacial", "sacred", "ruin", "isolated", "divine"],
        "demographics": {"Snow Elf": 100},
        "travel": {"roads": [], "paths": []}
    },
    {
        "id": 23,
        "name": "Bleak Falls Barrow",
        "desc": "Bleak Falls Barrow, an ancient Nordic tomb above Riverwood, harbors draugr and a dragon word wall.",
        "tags": ["barrow", "nordic", "undead", "mountain", "dragon", "ancient", "haunted"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Riverwood"]}
    },
    {
        "id": 24,
        "name": "Saarthal",
        "desc": "Saarthal, one of the first Nord settlements in Skyrim, lies in ruin near Winterhold. Excavated by the College, its icy chambers hold draugr and the Eye of Magnus.",
        "tags": ["ruin", "nordic", "undead", "snowy", "ancient", "arcane", "excavation"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Winterhold"]}
    },
    {
        "id": 25,
        "name": "Labyrinthian",
        "desc": "Labyrinthian, once a great Nord city, now a sprawling ruin in Hjaalmarch. Its draugr-infested halls and dragon priest masks draw adventurers.",
        "tags": ["ruin", "nordic", "undead", "maze", "dragon", "ancient", "haunted"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Morthal"]}
    },
    {
        "id": 26,
        "name": "Alftand",
        "desc": "Alftand, a Dwemer ruin in Winterhold’s frozen wastes, is a gateway to Blackreach. Its steam-filled corridors buzz with automatons and Falmer ambushes.",
        "tags": ["dwemer", "falmer", "ruin", "snowy", "underground", "mechanical", "trapped"],
        "demographics": {"Falmer": 100},
        "travel": {"roads": [], "paths": ["Winterhold"]}
    },
    {
        "id": 27,
        "name": "Mzinchaleft",
        "desc": "Mzinchaleft, a Dwemer ruin in the Pale, stands as a testament to the lost dwarven empire. Its bronze halls, guarded by automatons, hide intricate mechanisms.",
        "tags": ["dwemer", "ruin", "snowy", "mechanical", "wilderness", "bandits"],
        "demographics": {"Dwemer": 100},
        "travel": {"roads": [], "paths": ["Dawnstar"]}
    },
    {
        "id": 28,
        "name": "Ustengrav",
        "desc": "Ustengrav, a Nordic tomb in Hjaalmarch’s marshes, holds the Horn of Jurgen Windcaller. Its draugr-filled depths and mystical fog test the worthy.",
        "tags": ["barrow", "nordic", "undead", "swamp", "mystical", "ancient", "trapped"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Morthal"]}
    },
    {
        "id": 29,
        "name": "Volunruud",
        "desc": "Volunruud, a Nordic tomb in Whiterun’s tundra, entombs an ancient warlord and his ceremonial axes. Draugr patrol its dark halls.",
        "tags": ["barrow", "nordic", "undead", "tundra", "ancient", "haunted", "warlord"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Whiterun"]}
    },
    {
        "id": 30,
        "name": "Forelhost",
        "desc": "Forelhost, a Nordic ruin in the Rift’s mountains, was a stronghold of the Dragon Cult. Its draugr and dragon priest, Rahgot, guard a word wall.",
        "tags": ["ruin", "nordic", "undead", "mountain", "dragon", "cursed", "ancient"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Riften"]}
    },
    {
        "id": 31,
        "name": "Dushnikh Yal",
        "desc": "Dushnikh Yal, an Orc stronghold in the Reach, is a fortress of Malacath’s faithful. Its stone walls and forges ring with Orcish pride.",
        "tags": ["stronghold", "orcish", "cliffs", "forge", "isolated", "malacath", "warrior"],
        "demographics": {"Orc": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Markarth"]}
    },
    {
        "id": 32,
        "name": "Mor Khazgur",
        "desc": "Mor Khazgur, an Orc stronghold in western Skyrim, stands amid rugged hills. Its warriors hone their skills, and the mines yield valuable ore.",
        "tags": ["stronghold", "orcish", "hills", "mining", "warrior", "isolated", "malacath"],
        "demographics": {"Orc": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Solitude"]}
    },
    {
        "id": 33,
        "name": "Largashbur",
        "desc": "Largashbur, an Orc stronghold in the Rift, struggles against giant attacks and Malacath’s disfavor.",
        "tags": ["stronghold", "orcish", "forest", "besieged", "malacath", "shrine", "isolated"],
        "demographics": {"Orc": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Riften"]}
    },
    {
        "id": 34,
        "name": "Nar Zulbur",
        "desc": "Nar Zulbur, an Orc stronghold in Eastmarch, is renowned for its master smiths. Its clan works the volcanic forges, crafting weapons coveted across Skyrim.",
        "tags": ["stronghold", "orcish", "volcanic", "forge", "smithing", "isolated", "malacath"],
        "demographics": {"Orc": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 35,
        "name": "Karthspire",
        "desc": "Karthspire, a Forsworn camp in the Reach’s rugged canyons, is a haven for Reachmen rebels. Their briarheart warriors and hagraven allies plot against Markarth.",
        "tags": ["reachmen", "camp", "canyon", "forsworn", "rebel", "shrine", "wilderness"],
        "demographics": {"Reachmen": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Markarth"]}
    },
    {
        "id": 36,
        "name": "Sky Haven Temple",
        "desc": "Sky Haven Temple, a hidden Akaviri ruin in the Reach, serves as a sanctuary for the Blades. Its carved stone halls hold secrets of the Dragonborn.",
        "tags": ["ruin", "nordic", "akaviri", "blades", "hidden", "dragon", "ancient"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Karthspire"]}
    },
    {
        "id": 37,
        "name": "Ansilvund",
        "desc": "Ansilvund, a Nordic ruin in Eastmarch’s hills, is overrun by necromancers and their draugr thralls. Its ancient chambers hide dark rituals.",
        "tags": ["ruin", "nordic", "undead", "hills", "necromancy", "ancient", "haunted"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 38,
        "name": "Ragnvald",
        "desc": "Ragnvald, a Nordic tomb in the Reach’s cliffs, entombs ancient Nord kings and their draugr guardians. Its crypts, sealed with dragon priest masks, hold relics.",
        "tags": ["barrow", "nordic", "undead", "cliffs", "royal", "dragon", "ancient"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Markarth"]}
    },
    {
        "id": 39,
        "name": "Yngol Barrow",
        "desc": "Yngol Barrow, a coastal Nordic tomb near Windhelm, honors Ysgramor’s son. Its draugr and spectral helm guard the secrets of the Atmoran migration.",
        "tags": ["barrow", "nordic", "undead", "coastal", "ancient", "spectral", "atmoran"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 40,
        "name": "Dustman’s Cairn",
        "desc": "Dustman’s Cairn, a Nordic tomb in Whiterun’s tundra, is a proving ground for the Companions. Its draugr and silver hand foes guard a shard of Wuuthrad.",
        "tags": ["barrow", "nordic", "undead", "tundra", "companions", "ancient", "warrior"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Whiterun"]}
    },
    {
        "id": 41,
        "name": "Fort Dawnguard",
        "desc": "Fort Dawnguard, a rugged fortress in the Rift’s canyons, is the bastion of vampire hunters. Its warriors arm crossbows against the Volkihar clan.",
        "tags": ["fort", "nordic", "canyon", "vampire", "military", "hunters", "defensive"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {"roads": [], "paths": ["Riften"]}
    },
    {
        "id": 42,
        "name": "Castle Volkihar",
        "desc": "Castle Volkihar, a grim stronghold off Haafingar’s coast, is the lair of the Volkihar vampires. Its gothic spires pierce the fog.",
        "tags": ["fort", "vampire", "coastal", "gothic", "isolated", "haunted", "blood"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Solitude"]}
    },
    {
        "id": 43,
        "name": "Sovngarde",
        "desc": "Sovngarde, the Nordic afterlife, is a realm of eternal feasting and valor. Its misty halls welcome Nord heroes to the Hall of Valor.",
        "tags": ["nordic", "afterlife", "sacred", "heroic", "misty", "divine", "dragon"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": []}
    },
    {
        "id": 44,
        "name": "Skuldafn",
        "desc": "Skuldafn, a Nordic ruin in Eastmarch’s mountains, is a dragon priest stronghold and gateway to Sovngarde.",
        "tags": ["ruin", "nordic", "undead", "mountain", "dragon", "portal", "ancient"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 45,
        "name": "Fort Greymoor",
        "desc": "Fort Greymoor, a crumbling fort in Whiterun’s tundra, is a battleground for bandits, Imperials, and Stormcloaks.",
        "tags": ["fort", "nordic", "tundra", "contested", "military", "ruined", "bandits"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {"roads": [], "paths": ["Whiterun"]}
    },
    {
        "id": 46,
        "name": "Angarvunde",
        "desc": "Angarvunde, a Nordic ruin in the Rift’s forests, is a draugr-infested crypt of ancient treasures. Its arches draw adventurers.",
        "tags": ["ruin", "nordic", "undead", "forest", "ancient", "haunted", "treasure"],
        "demographics": {"Nord": 100},
        "travel": {"roads": [], "paths": ["Riften"]}
    },
    {
        "id": 47,
        "name": "Whiterun Imperial Camp",
        "desc": "The Whiterun Imperial Camp, a fortified outpost in the plains, supports the Empire’s hold on central Skyrim.",
        "tags": ["camp", "imperial", "plains", "military", "temporary", "strategic"],
        "demographics": {"Imperial": 80, "Nord": 15, "Others": 5},
        "travel": {"roads": [], "paths": ["Whiterun"]}
    },
    {
        "id": 48,
        "name": "Eastmarch Stormcloak Camp",
        "desc": "The Eastmarch Stormcloak Camp, hidden in the volcanic hills near Windhelm, rallies Ulfric’s rebels.",
        "tags": ["camp", "nordic", "volcanic", "military", "stormcloak", "temporary"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 49,
        "name": "Eldergleam Sanctuary",
        "desc": "Eldergleam Sanctuary, a verdant grove in Eastmarch, cradles a sacred tree blessed by Kynareth. Nord pilgrims seek its healing sap.",
        "tags": ["sanctuary", "nordic", "forest", "sacred", "kynareth", "healing", "spriggans"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    },
    {
        "id": 50,
        "name": "Kagrenzel",
        "desc": "Kagrenzel, a mysterious Dwemer ruin in Eastmarch’s cliffs, is a labyrinth of traps and automatons. Its orb defies explanation.",
        "tags": ["dwemer", "ruin", "cliffs", "mechanical", "trapped", "mysterious", "ancient"],
        "demographics": {"Dwemer": 100},
        "travel": {"roads": [], "paths": ["Windhelm"]}
    }
]