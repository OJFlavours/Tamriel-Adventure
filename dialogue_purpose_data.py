# dialogue_purpose_data.py

PURPOSE_DESCRIPTIONS = {
    "innkeeper": [
        "provide weary travelers with warm beds, hot meals, and cold ale in these troubled times",
        "keep this establishment running smoothly, ensuring every guest feels welcome and safe",
        "offer refuge to those who walk the dangerous roads of Skyrim, sharing news and stories",
        "maintain a place where all folk can rest, regardless of the civil war raging outside",
        "serve the finest food and drink in the hold while keeping ears open for useful information",
        "create a haven where merchants, adventurers, and locals can gather in peace",
        "honor the old traditions of hospitality that have kept inns sacred since the First Era",
        "quietly judge the character of every patron who walks through my door.",
        "dream of a day when I can leave this dusty town and see the world.",
        "try to forget the horrors I witnessed during the Great War."
    ],
    "merchant": [
        "trade in goods both common and rare, connecting distant markets across the Empire",
        "seek profit through honest commerce, following the blessed path of Zenithar",
        "provide essential supplies to settlements that would otherwise go without",
        "maintain trade routes that keep gold flowing and communities prosperous",
        "deal in exotic wares from distant provinces, bringing the world to Skyrim's doorstep",
        "negotiate fair prices while ensuring my family's prosperity for generations to come",
        "preserve the ancient mercantile traditions that built the great trading companies",
        "secretly fence stolen goods to supplement my legitimate income.",
        "search for rare artifacts to sell to wealthy collectors.",
        "worry about bandits and highwaymen raiding my caravans."
    ],
    "guard": [
        "protect the innocent and uphold the laws of this hold, whatever the personal cost",
        "maintain order in these chaotic times, when brother fights brother across Skyrim",
        "serve the people with honor, following the righteous path of Stendarr",
        "keep the peace while navigating the treacherous politics of civil war",
        "defend this settlement against bandits, monsters, and worse threats from the wild",
        "enforce justice fairly, regardless of race, creed, or political allegiance",
        "stand as a beacon of stability when the very foundations of the Empire shake",
        "grumble about the low pay and long hours.",
        "dream of retiring to a quiet farm far from the city.",
        "secretly sympathize with the Stormcloaks (or Imperials)."
    ],
    "blacksmith": [
        "forge weapons and armor worthy of the heroes who will shape Skyrim's destiny",
        "work the sacred metals with hammer and flame, following techniques passed down through ages",
        "craft tools of war and peace that will outlast those who wield them",
        "maintain the ancient traditions of metalworking that built the Nordic civilization",
        "create blades that sing with the strength of the earth and the fury of dragon fire",
        "honor the craft taught by the Dwemer and perfected by generations of Nordic smiths",
        "ensure that warriors have the steel they need to face the darkness ahead",
        "struggle to find apprentices willing to learn my trade.",
        "experiment with new alloys and forging techniques.",
        "secretly craft weapons for both sides of the civil war."
    ],
    "priest": [
        "serve the Nine Divines and guide the faithful through these dark and troubled times",
        "offer spiritual counsel to those whose souls are burdened by war and loss",
        "maintain the sacred traditions that connect mortals to the realm of Aetherius",
        "heal both body and spirit through the blessed power of divine magic",
        "preserve the ancient teachings while adapting to a world where Talos is forbidden",
        "provide sanctuary to all who seek the gods' mercy, regardless of their past sins",
        "stand as a bulwark against the forces of darkness that would corrupt Tamriel",
        "secretly question my faith in the face of so much suffering.",
        "struggle to reconcile ancient teachings with modern realities.",
        "worry about the growing influence of Daedric cults."
    ],
    "scholar": [
        "delve into the mysteries of the past to better understand our troubled present",
        "preserve knowledge that would otherwise be lost to the ravages of time and war",
        "study the ancient texts that hold the keys to forgotten magics and lost wisdom",
        "seek truth in the written word while others seek it with sword and flame",
        "document the events of our time so future generations might learn from our mistakes",
        "unravel the secrets of Dwemer technology and Ayleid magic for the betterment of all Tamriel",
        "maintain the great libraries that are civilization's true treasures",
        "secretly search for forbidden knowledge.",
        "struggle to secure funding for my research.",
        "fear that my discoveries could be used for evil."
    ],
    "bard": [
        "preserve the songs and stories that define our people's identity and history",
        "bring joy and inspiration to hearts heavy with the burden of these dark times",
        "carry news and tales between settlements, connecting distant communities through story",
        "honor the traditions of the Bards College while creating new legends for future ages",
        "use music and verse to heal the divisions that tear our land asunder",
        "document the deeds of heroes whose names should echo through eternity",
        "keep alive the old songs that remember when dragons ruled the skies",
        "secretly write satirical songs that mock the powerful.",
        "struggle to find an audience that appreciates true art.",
        "dream of becoming a famous performer."
    ],
    "farmer": [
        "work the sacred soil to feed the people of this hold, following Kynareth's eternal cycle",
        "maintain the agricultural traditions that have sustained Nordic civilization for millennia",
        "coax sustenance from the harsh northern earth through backbreaking labor and ancient wisdom",
        "provide the foundation upon which all civilization rests - food for the hungry masses",
        "preserve the farming techniques passed down through generations of my bloodline",
        "endure the hardships of rural life while supporting the great cities and their grand ambitions",
        "honor the old compact between farmer and land, giving back as much as I take",
        "worry about bandits stealing my crops.",
        "struggle to make ends meet in a harsh climate.",
        "secretly long for a different life."
    ],
    "hunter": [
        "track game through the wilds while respecting the ancient laws of the hunt",
        "provide meat and pelts for my community while maintaining nature's delicate balance",
        "read the signs of forest and field that speak of dangers both natural and supernatural",
        "follow the path of Hircine while honoring Kynareth's dominion over the natural world",
        "venture into the deep woods where few dare tread, bringing back both bounty and warnings",
        "preserve the hunting traditions that kept the Nords alive during their first harsh winters",
        "serve as a bridge between civilization and the untamed wilderness beyond",
        "hunt dangerous creatures to protect my community.",
        "struggle to find enough game to feed my family.",
        "secretly fear the creatures of the night."
    ],
    "miner": [
        "delve deep into the earth's bones, seeking the precious metals that fuel civilization",
        "follow veins of ore through dangerous tunnels where cave-ins and worse things lurk",
        "extract the wealth hidden in Skyrim's mountains while respecting the spirits of the deep",
        "endure the darkness and danger of the mines to provide the raw materials for progress",
        "work alongside my brothers in the dangerous depths where only trust keeps us alive",
        "honor the ancient mining traditions while adapting to new techniques and deeper shafts",
        "risk my life daily in the hope that my children might know a better future",
        "worry about cave-ins and other mining accidents.",
        "struggle to earn enough to support my family.",
        "secretly search for rare and valuable gems."
    ],
    "mage": [
        "study the fundamental forces that shape reality itself, wielding power beyond mortal ken",
        "explore the mysteries of magic while respecting the dangerous forces I command",
        "advance the understanding of the arcane arts for the betterment of all Tamriel",
        "maintain the balance between the mortal world and the chaotic realm of Oblivion",
        "preserve magical knowledge while training the next generation of spellcasters",
        "serve as guardian against supernatural threats that mundane weapons cannot touch",
        "seek to unlock the secrets of creation itself through careful study and experimentation",
        "struggle to control my powers.",
        "fear the prejudice of those who distrust magic.",
        "secretly dabble in forbidden schools of magic."
    ],
    "noble": [
        "govern my lands and people with wisdom befitting my ancient bloodline",
        "navigate the treacherous politics of court while serving the true needs of my subjects",
        "maintain the old traditions of nobility - protection, justice, and responsible leadership",
        "balance loyalty to the Empire with the growing demands of Nordic independence",
        "preserve my family's honor while adapting to a rapidly changing political landscape",
        "serve as a bridge between the common folk and the distant machinations of power",
        "uphold the sacred duties of my station, whatever the personal cost may be",
        "struggle to maintain my family's wealth and influence.",
        "worry about political rivals and enemies.",
        "secretly sympathize with the common people."
    ],
    "bandit": [
        "take what this harsh world owes me, since honest work brings only suffering",
        "prey upon the wealthy travelers who flaunt their gold while others starve",
        "survive in a world that offers nothing to those born without title or privilege",
        "claim my share of Skyrim's wealth through strength and cunning rather than birthright",
        "live free from the laws that serve only the rich and powerful",
        "make the roads dangerous for those who would exploit the common folk",
        "build my own kingdom in the wilderness, far from the corruption of civilization",
        "avoid capture by the guards.",
        "struggle to maintain control over my gang.",
        "secretly dream of a better life."
    ],
    "thief": [
        "redistribute wealth from those who have too much to those who have nothing",
        "practice the ancient art of stealth and cunning in a world ruled by brute force",
        "survive by my wits in a society that offers no legitimate opportunities for advancement",
        "follow the shadowy path that leads to secrets and treasures others cannot reach",
        "serve the Guild's ancient codes while profiting from the chaos of civil war",
        "prove that skill and intelligence matter more than inherited privilege",
        "operate in the spaces between law and chaos where true freedom exists",
        "avoid detection by the guards and rival thieves.",
        "struggle to maintain my anonymity.",
        "secretly yearn for a life of honesty."
    ],
    "forsworn": [
        "reclaim the ancient lands of the Reach that were stolen by Nordic invaders",
        "serve the old gods who demand blood vengeance for generations of oppression",
        "preserve the true heritage of the Reachmen against Imperial and Nordic corruption",
        "wage eternal war against the usurpers who drove my people into the wilderness",
        "honor the ancient pacts with Hagravens and the spirits of the wild",
        "prove that the Reach will never be tamed by foreign laws and foreign gods",
        "carry on the struggle that began when the first Nord set foot in our sacred lands",
        "evade capture by the Nords and Imperials.",
        "struggle to maintain our traditions in a hostile land.",
        "secretly question the cost of our vengeance."
    ],
    "vampire": [
        "embrace the eternal night that frees me from mortal concerns and limitations",
        "feed upon the living while building power that spans centuries rather than mere decades",
        "serve the will of Molag Bal while maintaining my facade among the cattle of mortality",
        "accumulate knowledge and influence across the ages that mortals cannot comprehend",
        "prove that undeath is evolution, not curse, despite what the living might believe",
        "maintain the ancient bloodlines while adapting to a world that grows ever more hostile",
        "rule from the shadows, manipulating mortal affairs like pieces on a grand game board",
        "avoid detection by vampire hunters.",
        "struggle to control my bloodlust.",
        "secretly yearn for the warmth of the sun."
    ],
    "necromancer": [
        "explore the forbidden arts that reveal death as merely another beginning",
        "command the restless dead who serve more faithfully than any living follower",
        "study the boundaries between life and death that lesser minds fear to examine",
        "accumulate power through means that squeamish mortals refuse to consider",
        "serve the will of the Daedric Princes who understand the true nature of existence",
        "prove that the conventional morality of the masses is merely ignorance and weakness",
        "build an undying empire where death has no meaning and power knows no limits",
        "avoid detection by the Vigilants of Stendarr.",
        "struggle to maintain control over my undead minions.",
        "secretly fear the consequences of my actions."
    ],
    "stormcloak_soldier": [
        "fight for Skyrim's independence from the corrupt and weakened Empire",
        "serve Ulfric Stormcloak's vision of a free Nordic homeland ruled by Nordic traditions",
        "oppose the Thalmor's cultural imperialism and their outlawing of Talos worship",
        "preserve the ancient ways of the Nords against foreign influence and corruption",
        "prove that Nordic strength and honor can overcome Imperial politics and Elven manipulation",
        "reclaim Skyrim's destiny from those who would sell it for temporary peace",
        "fight for the right to worship Talos and maintain our ancestral traditions",
        "worry about the outcome of the war.",
        "struggle to survive on the battlefield.",
        "secretly question Ulfric's leadership."
    ],
    "imperial_soldier": [
        "maintain unity within the Empire during its darkest hour of division",
        "serve the greater good even when it requires difficult compromises and sacrifices",
        "protect the peace that the Empire has maintained for centuries across Tamriel",
        "oppose the chaos and bloodshed that Nordic independence would unleash",
        "preserve the rule of law against the primitive tribalism of Stormcloak rebels",
        "serve as a bulwark against the Thalmor's true agenda while maintaining necessary alliances",
        "protect the common people from the devastation that civil war brings to all",
        "worry about the future of the Empire.",
        "struggle to maintain morale in the face of defeat.",
        "secretly admire the courage of the Stormcloaks."
    ],
    "thalmor_justiciar": [
        "enforce the terms of the White-Gold Concordat for the good of all Tamriel",
        "root out the heretical worship of Talos that corrupts the natural order",
        "serve the Aldmeri Dominion's mission to restore proper hierarchy to the world",
        "investigate threats to the carefully maintained peace between Empire and Dominion",
        "protect Altmer superiority against the jealous violence of lesser races",
        "maintain surveillance over the primitive humans who cannot govern themselves",
        "advance the Thalmor's righteous agenda through law, diplomacy, and necessary force",
        "struggle to maintain control over the human population.",
        "worry about the growing resistance to Thalmor rule.",
        "secretly question the Dominion's methods."
    ],
    "draugr": [
        "guard the ancient tombs and sacred barrows of my Nordic ancestors",
        "serve in undeath as I served in life - protecting what must be protected",
        "maintain the eternal vigil over treasures and secrets that must not be disturbed",
        "honor the ancient oaths that bind me even beyond the grave",
        "punish those who would defile the resting places of heroes and kings",
        "preserve the old ways through endless, tireless guardianship",
        "serve the dragon priests and ancient powers that commanded my loyalty in life",
        "endlessly wander the halls of my tomb.",
        "obey the commands of my masters.",
        "secretly long for eternal rest."
    ],
    "jarl": [
        "govern my hold with wisdom and strength, ensuring the prosperity of my people.",
        "uphold the traditions of Skyrim while adapting to the changing times.",
        "defend my people from all threats, both internal and external.",
        "maintain the balance of power between the various factions in my hold.",
        "serve as a mediator between the common folk and the nobility.",
        "ensure that justice is served fairly and impartially.",
        "preserve the cultural heritage of my hold for future generations.",
        "worry about the growing tensions between the Empire and the Stormcloaks.",
        "struggle to maintain my authority in the face of challenges from rivals.",
        "secretly fear the return of the dragons."
    ],
    "housecarl": [
        "protect my jarl with my life, serving as their loyal bodyguard and advisor.",
        "enforce the jarl's laws and maintain order within the hold.",
        "carry out the jarl's commands swiftly and efficiently.",
        "serve as a liaison between the jarl and the people.",
        "defend the jarl's honor and reputation.",
        "ensure the safety and security of the jarl's household.",
        "uphold the traditions of loyalty and service that define the role of a housecarl.",
        "worry about the jarl's safety.",
        "struggle to balance my loyalty to the jarl with my own personal beliefs.",
        "secretly admire the courage and strength of the jarl."
    ],
    "beggar": [
        "scrape together enough coin to survive another day on the streets.",
        "seek shelter from the harsh weather and the dangers of the city.",
        "beg for food and alms from passersby.",
        "tell stories of my past misfortunes to elicit sympathy.",
        "avoid the attention of the guards and the Thieves Guild.",
        "dream of a better life, free from poverty and hardship.",
        "maintain my dignity despite my circumstances.",
        "struggle to find enough to eat.",
        "fear the scorn and contempt of others.",
        "secretly hope for a miracle."
    ]
}

LOCATION_PURPOSES = {
    "windhelm": [
        "uphold the ancient traditions of the Nords in this proud city.",
        "maintain order in the face of growing tensions between Nords and Dunmer.",
        "serve the Jarl and the people of Windhelm with loyalty and dedication.",
        "protect the city from the dangers of the wilderness and the civil war.",
        "preserve the cultural heritage of Windhelm for future generations."
    ],
    "solitude": [
        "maintain the elegance and sophistication of the capital city.",
        "serve the Empress and the Empire with unwavering loyalty.",
        "protect the city from the dangers of the sea and the Stormcloak rebellion.",
        "uphold the traditions of the Imperial Legion.",
        "preserve the cultural heritage of Solitude for future generations."
    ],
    "riften": [
        "navigate the treacherous politics of the Thieves Guild and the Black-Briar family.",
        "maintain order in a city rife with corruption and crime.",
        "serve the Jarl and the people of Riften with caution and discretion.",
        "protect the city from the dangers of the Rift and the civil war.",
        "preserve the cultural heritage of Riften for future generations."
    ]
}

DYNAMIC_PURPOSES = {
    "quest_completed": [
        "express gratitude for the player's assistance in completing the quest.",
        "offer a reward for the player's efforts.",
        "share information related to the quest's outcome."
    ]
}

RACIAL_MODIFIERS = {
    "imperial": ["a charismatic negotiator", "a shrewd merchant", "a skilled administrator"],
    "nord": ["a fierce warrior", "a hardy explorer", "a respected hunter"],
    "elf": ["an enigmatic mage", "a wise scholar", "a graceful artist"],
    "dark elf": ["a cunning assassin", "a secretive spy", "a powerful sorcerer"],
    "orc": ["a brutal fighter", "a strong blacksmith", "a loyal mercenary"]
}

GENERIC_PURPOSES = [
    "wandering the streets",
    "visiting the local tavern",
    "browsing the market",
    "guarding the city gates",
    "patrolling the area"
]

ENTHUSIASM_MODIFIERS = [
    "with great enthusiasm",
    "with unwavering dedication",
    "with infectious excitement",
    "with boundless energy",
    "with pure joy"
]

CYNICAL_MODIFIERS = [
    "with obvious disdain",
    "with thinly veiled contempt",
    "with a dismissive shrug",
    "with cynical resignation",
    "with ill-concealed boredom"
]