# dialogue_purpose_data.py

PURPOSE_DESCRIPTIONS = {
    "innkeeper": [
        {
            "description": "provide weary travelers with warm beds, hot meals, and cold ale in these troubled times",
            "effects": []
        },
        {
            "description": "keep this establishment running smoothly, ensuring every guest feels welcome and safe",
            "effects": []
        },
        {
            "description": "offer refuge to those who walk the dangerous roads of Skyrim, sharing news and stories",
            "effects": []
        },
        {
            "description": "maintain a place where all folk can rest, regardless of the civil war raging outside",
            "effects": []
        },
        {
            "description": "serve the finest food and drink in the hold while keeping ears open for useful information",
            "effects": ["rumor_heard"]
        },
        {
            "description": "create a haven where merchants, adventurers, and locals can gather in peace",
            "effects": []
        },
        {
            "description": "honor the old traditions of hospitality that have kept inns sacred since the First Era",
            "effects": []
        },
        {
            "description": "quietly judge the character of every patron who walks through my door.",
            "effects": []
        },
        {
            "description": "dream of a day when I can leave this dusty town and see the world.",
            "effects": []
        },
        {
            "description": "try to forget the horrors I witnessed during the Great War.",
            "effects": []
        }
    ],
    "merchant": [
        {
            "description": "trade in goods both common and rare, connecting distant markets across the Empire",
            "effects": []
        },
        {
            "description": "seek profit through honest commerce, following the blessed path of Zenithar",
            "effects": []
        },
        {
            "description": "provide essential supplies to settlements that would otherwise go without",
            "effects": []
        },
        {
            "description": "maintain trade routes that keep gold flowing and communities prosperous",
            "effects": []
        },
        {
            "description": "deal in exotic wares from distant provinces, bringing the world to Skyrim's doorstep",
            "effects": []
        },
        {
            "description": "negotiate fair prices while ensuring my family's prosperity for generations to come",
            "effects": []
        },
        {
            "description": "preserve the ancient mercantile traditions that built the great trading companies",
            "effects": []
        },
        {
            "description": "secretly fence stolen goods to supplement my legitimate income.",
            "effects": ["start_thieves_guild_quest"]
        },
        {
            "description": "search for rare artifacts to sell to wealthy collectors.",
            "effects": ["start_artifact_quest"]
        },
        {
            "description": "worry about bandits and highwaymen raiding my caravans.",
            "effects": []
        }
    ],
    "guard": [
        {
            "description": "protect the innocent and uphold the laws of this hold, whatever the personal cost",
            "effects": []
        },
        {
            "description": "maintain order in these chaotic times, when brother fights brother across Skyrim",
            "effects": []
        },
        {
            "description": "serve the people with honor, following the righteous path of Stendarr",
            "effects": []
        },
        {
            "description": "keep the peace while navigating the treacherous politics of civil war",
            "effects": []
        },
        {
            "description": "defend this settlement against bandits, monsters, and worse threats from the wild",
            "effects": []
        },
        {
            "description": "enforce justice fairly, regardless of race, creed, or political allegiance",
            "effects": []
        },
        {
            "description": "stand as a beacon of stability when the very foundations of the Empire shake",
            "effects": []
        },
        {
            "description": "grumble about the low pay and long hours.",
            "effects": []
        },
        {
            "description": "dream of retiring to a quiet farm far from the city.",
            "effects": []
        },
        {
            "description": "secretly sympathize with the Stormcloaks (or Imperials).",
            "effects": []
        }
    ],
    "blacksmith": [
        {
            "description": "forge weapons and armor worthy of the heroes who will shape Skyrim's destiny",
            "effects": []
        },
        {
            "description": "work the sacred metals with hammer and flame, following techniques passed down through ages",
            "effects": []
        },
        {
            "description": "craft tools of war and peace that will outlast those who wield them",
            "effects": []
        },
        {
            "description": "maintain the ancient traditions of metalworking that built the Nordic civilization",
            "effects": []
        },
        {
            "description": "create blades that sing with the strength of the earth and the fury of dragon fire",
            "effects": []
        },
        {
            "description": "honor the craft taught by the Dwemer and perfected by generations of Nordic smiths",
            "effects": []
        },
        {
            "description": "ensure that warriors have the steel they need to face the darkness ahead",
            "effects": []
        },
        {
            "description": "struggle to find apprentices willing to learn my trade.",
            "effects": []
        },
        {
            "description": "experiment with new alloys and forging techniques.",
            "effects": []
        },
        {
            "description": "secretly craft weapons for both sides of the civil war.",
            "effects": []
        }
    ],
    "priest": [
        {
            "description": "serve the Nine Divines and guide the faithful through these dark and troubled times",
            "effects": []
        },
        {
            "description": "offer spiritual counsel to those whose souls are burdened by war and loss",
            "effects": []
        },
        {
            "description": "maintain the sacred traditions that connect mortals to the realm of Aetherius",
            "effects": []
        },
        {
            "description": "heal both body and spirit through the blessed power of divine magic",
            "effects": []
        },
        {
            "description": "preserve the ancient teachings while adapting to a world where Talos is forbidden",
            "effects": []
        },
        {
            "description": "provide sanctuary to all who seek the gods' mercy, regardless of their past sins",
            "effects": []
        },
        {
            "description": "stand as a bulwark against the forces of darkness that would corrupt Tamriel",
            "effects": []
        },
        {
            "description": "secretly question my faith in the face of so much suffering.",
            "effects": []
        },
        {
            "description": "struggle to reconcile ancient teachings with modern realities.",
            "effects": []
        },
        {
            "description": "worry about the growing influence of Daedric cults.",
            "effects": []
        }
    ],
    "scholar": [
        {
            "description": "delve into the mysteries of the past to better understand our troubled present",
            "effects": []
        },
        {
            "description": "preserve knowledge that would otherwise be lost to the ravages of time and war",
            "effects": []
        },
        {
            "description": "study the ancient texts that hold the keys to forgotten magics and lost wisdom",
            "effects": []
        },
        {
            "description": "seek truth in the written word while others seek it with sword and flame",
            "effects": []
        },
        {
            "description": "document the events of our time so future generations might learn from our mistakes",
            "effects": []
        },
        {
            "description": "unravel the secrets of Dwemer technology and Ayleid magic for the betterment of all",
            "effects": []
        },
        {
            "description": "maintain the great libraries that are civilization's true treasures",
            "effects": []
        },
        {
            "description": "secretly search for forbidden knowledge.",
            "effects": []
        },
        {
            "description": "struggle to secure funding for my research.",
            "effects": []
        },
        {
            "description": "fear that my discoveries could be used for evil.",
            "effects": []
        }
    ],
    "bard": [
        {
            "description": "preserve the songs and stories that define our people's identity and history",
            "effects": []
        },
        {
            "description": "bring joy and inspiration to hearts heavy with the burden of these dark times",
            "effects": []
        },
        {
            "description": "carry news and tales between settlements, connecting distant communities through story",
            "effects": []
        },
        {
            "description": "honor the traditions of the Bards College while creating new legends for future ages",
            "effects": []
        },
        {
            "description": "use music and verse to heal the divisions that tear our land asunder",
            "effects": []
        },
        {
            "description": "document the deeds of heroes whose names should echo through eternity",
            "effects": []
        },
        {
            "description": "keep alive the old songs that remember when dragons ruled the skies",
            "effects": []
        },
        {
            "description": "secretly write satirical songs that mock the powerful.",
            "effects": []
        },
        {
            "description": "struggle to find an audience that appreciates true art.",
            "effects": []
        },
        {
            "description": "dream of becoming a famous performer.",
            "effects": []
        }
    ],
    "farmer": [
        {
            "description": "work the sacred soil to feed the people of this hold, following Kynareth's eternal cycle",
            "effects": []
        },
        {
            "description": "maintain the agricultural traditions that have sustained Nordic civilization for millennia",
            "effects": []
        },
        {
            "description": "coax sustenance from the harsh northern earth through backbreaking labor and ancient wisdom",
            "effects": []
        },
        {
            "description": "provide the foundation upon which all civilization rests - food for the hungry masses",
            "effects": []
        },
        {
            "description": "preserve the farming techniques passed down through generations of my bloodline",
            "effects": []
        },
        {
            "description": "endure the hardships of rural life while supporting the great cities and their grand ambitions",
            "effects": []
        },
        {
            "description": "honor the old compact between farmer and land, giving back as much as I take",
            "effects": []
        },
        {
            "description": "worry about bandits stealing my crops.",
            "effects": []
        },
        {
            "description": "struggle to make ends meet in a harsh climate.",
            "effects": []
        },
        {
            "description": "secretly long for a different life.",
            "effects": []
        }
    ],
    "hunter": [
        {
            "description": "track game through the wilds while respecting the ancient laws of the hunt",
            "effects": []
        },
        {
            "description": "provide meat and pelts for my community while maintaining nature's delicate balance",
            "effects": []
        },
        {
            "description": "read the signs of forest and field that speak of dangers both natural and supernatural",
            "effects": []
        },
        {
            "description": "follow the path of Hircine while honoring Kynareth's dominion over the natural world",
            "effects": []
        },
        {
            "description": "venture into the deep woods where few dare tread, bringing back both bounty and warnings",
            "effects": []
        },
        {
            "description": "preserve the hunting traditions that kept the Nords alive during their first harsh winters",
            "effects": []
        },
        {
            "description": "serve as a bridge between civilization and the untamed wilderness beyond",
            "effects": []
        },
        {
            "description": "hunt dangerous creatures to protect my community.",
            "effects": []
        },
        {
            "description": "struggle to find enough game to feed my family.",
            "effects": []
        },
        {
            "description": "secretly fear the creatures of the night.",
            "effects": []
        }
    ],
    "miner": [
        {
            "description": "delve deep into the earth's bones, seeking the precious metals that fuel civilization",
            "effects": []
        },
        {
            "description": "follow veins of ore through dangerous tunnels where cave-ins and worse things lurk",
            "effects": []
        },
        {
            "description": "extract the wealth hidden in Skyrim's mountains while respecting the spirits of the deep",
            "effects": []
        },
        {
            "description": "endure the darkness and danger of the mines to provide the raw materials for progress",
            "effects": []
        },
        {
            "description": "work alongside my brothers in the dangerous depths where only trust keeps us alive",
            "effects": []
        },
        {
            "description": "honor the ancient mining traditions while adapting to new techniques and deeper shafts",
            "effects": []
        },
        {
            "description": "risk my life daily in the hope that my children might know a better future",
            "effects": []
        },
        {
            "description": "worry about cave-ins and other mining accidents.",
            "effects": []
        },
        {
            "description": "struggle to earn enough to support my family.",
            "effects": []
        },
        {
            "description": "secretly search for rare and valuable gems.",
            "effects": []
        }
    ],
    "mage": [
        {
            "description": "study the fundamental forces that shape reality itself, wielding power beyond mortal ken",
            "effects": []
        },
        {
            "description": "explore the mysteries of magic while respecting the dangerous forces I command",
            "effects": []
        },
        {
            "description": "advance the understanding of the arcane arts for the betterment of all Tamriel",
            "effects": []
        },
        {
            "description": "maintain the balance between the mortal world and the chaotic realm of Oblivion",
            "effects": []
        },
        {
            "description": "preserve magical knowledge while training the next generation of spellcasters",
            "effects": []
        },
        {
            "description": "serve as guardian against supernatural threats that mundane weapons cannot touch",
            "effects": []
        },
        {
            "description": "seek to unlock the secrets of creation itself through careful study and experimentation",
            "effects": []
        },
        {
            "description": "struggle to control my powers.",
            "effects": []
        },
        {
            "description": "fear the prejudice of those who distrust magic.",
            "effects": []
        },
        {
            "description": "secretly dabble in forbidden schools of magic.",
            "effects": []
        }
    ],
    "noble": [
        {
            "description": "govern my lands and people with wisdom befitting my ancient bloodline",
            "effects": []
        },
        {
            "description": "navigate the treacherous politics of court while serving the true needs of my subjects",
            "effects": []
        },
        {
            "description": "maintain the old traditions of nobility - protection, justice, and responsible leadership",
            "effects": []
        },
        {
            "description": "balance loyalty to the Empire with the growing demands of Nordic independence",
            "effects": []
        },
        {
            "description": "preserve my family's honor while adapting to a rapidly changing political landscape",
            "effects": []
        },
        {
            "description": "serve as a bridge between the common folk and the distant machinations of power",
            "effects": []
        },
        {
            "description": "uphold the sacred duties of my station, whatever the personal cost may be",
            "effects": []
        },
        {
            "description": "struggle to maintain my family's wealth and influence.",
            "effects": []
        },
        {
            "description": "worry about political rivals and enemies.",
            "effects": []
        },
        {
            "description": "secretly sympathize with the common people.",
            "effects": []
        }
    ],
    "bandit": [
        {
            "description": "take what this harsh world owes me, since honest work brings only suffering",
            "effects": []
        },
        {
            "description": "prey upon the wealthy travelers who flaunt their gold while others starve",
            "effects": []
        },
        {
            "description": "survive in a world that offers nothing to those born without title or privilege",
            "effects": []
        },
        {
            "description": "claim my share of Skyrim's wealth through strength and cunning rather than birthright",
            "effects": []
        },
        {
            "description": "live free from the laws that serve only the rich and powerful",
            "effects": []
        },
        {
            "description": "make the roads dangerous for those who would exploit the common folk",
            "effects": []
        },
        {
            "description": "build my own kingdom in the wilderness, far from the corruption of civilization",
            "effects": []
        },
        {
            "description": "avoid capture by the guards.",
            "effects": []
        },
        {
            "description": "struggle to maintain control over my gang.",
            "effects": []
        },
        {
            "description": "secretly dream of a better life.",
            "effects": []
        }
    ],
    "thief": [
        {
            "description": "redistribute wealth from those who have too much to those who have nothing",
            "effects": []
        },
        {
            "description": "practice the ancient art of stealth and cunning in a world ruled by brute force",
            "effects": []
        },
        {
            "description": "survive by my wits in a society that offers no legitimate opportunities for advancement",
            "effects": []
        },
        {
            "description": "follow the shadowy path that leads to secrets and treasures others cannot reach",
            "effects": []
        },
        {
            "description": "serve the Guild's ancient codes while profiting from the chaos of civil war",
            "effects": []
        },
        {
            "description": "prove that skill and intelligence matter more than inherited privilege",
            "effects": []
        },
        {
            "description": "operate in the spaces between law and chaos where true freedom exists",
            "effects": []
        },
        {
            "description": "avoid detection by the guards and rival thieves.",
            "effects": []
        },
        {
            "description": "struggle to maintain my anonymity.",
            "effects": []
        },
        {
            "description": "secretly yearn for a life of honesty.",
            "effects": []
        }
    ],
    "forsworn": [
        {
            "description": "reclaim the ancient lands of the Reach that were stolen by Nordic invaders",
            "effects": []
        },
        {
            "description": "serve the old gods who demand blood vengeance for generations of oppression",
            "effects": []
        },
        {
            "description": "preserve the true heritage of the Reachmen against Imperial and Nordic corruption",
            "effects": []
        },
        {
            "description": "wage eternal war against the usurpers who drove my people into the wilderness",
            "effects": []
        },
        {
            "description": "honor the ancient pacts with Hagravens and the spirits of the wild",
            "effects": []
        },
        {
            "description": "prove that the Reach will never be tamed by foreign laws and foreign gods",
            "effects": []
        },
        {
            "description": "carry on the struggle that began when the first Nord set foot in our sacred lands",
            "effects": []
        },
        {
            "description": "evade capture by the Nords and Imperials.",
            "effects": []
        },
        {
            "description": "struggle to maintain our traditions in a hostile land.",
            "effects": []
        },
        {
            "description": "secretly question the cost of our vengeance.",
            "effects": []
        }
    ],
    "vampire": [
        {
            "description": "embrace the eternal night that frees me from mortal concerns and limitations",
            "effects": []
        },
        {
            "description": "feed upon the living while building power that spans centuries rather than mere decades",
            "effects": []
        },
        {
            "description": "serve the will of Molag Bal while maintaining my facade among the cattle of mortality",
            "effects": []
        },
        {
            "description": "accumulate knowledge and influence across the ages that mortals cannot comprehend",
            "effects": []
        },
        {
            "description": "prove that undeath is evolution, not curse, despite what the living might believe",
            "effects": []
        },
        {
            "description": "maintain the ancient bloodlines while adapting to a world that grows ever more hostile",
            "effects": []
        },
        {
            "description": "rule from the shadows, manipulating mortal affairs like pieces on a grand game board",
            "effects": []
        },
        {
            "description": "avoid detection by vampire hunters.",
            "effects": []
        },
        {
            "description": "struggle to control my bloodlust.",
            "effects": []
        },
        {
            "description": "secretly yearn for the warmth of the sun.",
            "effects": []
        }
    ],
    "necromancer": [
        {
            "description": "explore the forbidden arts that reveal death as merely another beginning",
            "effects": []
        },
        {
            "description": "command the restless dead who serve more faithfully than any living follower",
            "effects": []
        },
        {
            "description": "study the boundaries between life and death that lesser minds fear to examine",
            "effects": []
        },
        {
            "description": "accumulate power through means that squeamish mortals refuse to consider",
            "effects": []
        },
        {
            "description": "serve the will of the Daedric Princes who understand the true nature of existence",
            "effects": []
        },
        {
            "description": "prove that the conventional morality of the masses is merely ignorance and weakness",
            "effects": []
        },
        {
            "description": "build an undying empire where death has no meaning and power knows no limits",
            "effects": []
        },
        {
            "description": "avoid detection by the Vigilants of Stendarr.",
            "effects": []
        },
        {
            "description": "struggle to maintain control over my undead minions.",
            "effects": []
        },
        {
            "description": "secretly fear the consequences of my actions.",
            "effects": []
        }
    ],
    "stormcloak_soldier": [
        {
            "description": "fight for Skyrim's independence from the corrupt and weakened Empire",
            "effects": []
        },
        {
            "description": "serve Ulfric Stormcloak's vision of a free Nordic homeland ruled by Nordic traditions",
            "effects": []
        },
        {
            "description": "oppose the Thalmor's cultural imperialism and their outlawing of Talos worship",
            "effects": []
        },
        {
            "description": "preserve the ancient ways of the Nords against foreign influence and corruption",
            "effects": []
        },
        {
            "description": "prove that Nordic strength and honor can overcome Imperial politics and Elven manipulation",
            "effects": []
        },
        {
            "description": "reclaim Skyrim's destiny from those who would sell it for temporary peace",
            "effects": []
        },
        {
            "description": "fight for the right to worship Talos and maintain our ancestral traditions",
            "effects": []
        },
        {
            "description": "worry about the outcome of the war.",
            "effects": []
        },
        {
            "description": "struggle to survive on the battlefield.",
            "effects": []
        },
        {
            "description": "secretly question Ulfric's leadership.",
            "effects": []
        }
    ],
    "imperial_soldier": [
        {
            "description": "maintain unity within the Empire during its darkest hour of division",
            "effects": []
        },
        {
            "description": "serve the greater good even when it requires difficult compromises and sacrifices",
            "effects": []
        },
        {
            "description": "protect the peace that the Empire has maintained for centuries across Tamriel",
            "effects": []
        },
        {
            "description": "oppose the chaos and bloodshed that Nordic independence would unleash",
            "effects": []
        },
        {
            "description": "preserve the rule of law against the primitive tribalism of Stormcloak rebels",
            "effects": []
        },
        {
            "description": "serve as a bulwark against the Thalmor's true agenda while maintaining necessary alliances",
            "effects": []
        },
        {
            "description": "protect the common people from the devastation that civil war brings to all",
            "effects": []
        },
        {
            "description": "worry about the future of the Empire.",
            "effects": []
        },
        {
            "description": "struggle to maintain morale in the face of defeat.",
            "effects": []
        },
        {
            "description": "secretly admire the courage of the Stormcloaks.",
            "effects": []
        }
    ],
    "thalmor_justiciar": [
        {
            "description": "enforce the terms of the White-Gold Concordat for the good of all Tamriel",
            "effects": []
        },
        {
            "description": "root out the heretical worship of Talos that corrupts the natural order",
            "effects": []
        },
        {
            "description": "serve the Aldmeri Dominion's mission to restore proper hierarchy to the world",
            "effects": []
        },
        {
            "description": "investigate threats to the carefully maintained peace between Empire and Dominion",
            "effects": []
        },
        {
            "description": "protect Altmer superiority against the jealous violence of lesser races",
            "effects": []
        },
        {
            "description": "maintain surveillance over the primitive humans who cannot govern themselves",
            "effects": []
        },
        {
            "description": "advance the Thalmor's righteous agenda through law, diplomacy, and necessary force",
            "effects": []
        },
        {
            "description": "struggle to maintain control over the human population.",
            "effects": []
        },
        {
            "description": "worry about the growing resistance to Thalmor rule.",
            "effects": []
        },
        {
            "description": "secretly question the Dominion's methods.",
            "effects": []
        }
    ],
    "draugr": [
        {
            "description": "guard the ancient tombs and sacred barrows of my Nordic ancestors",
            "effects": []
        },
        {
            "description": "serve in undeath as I served in life - protecting what must be protected",
            "effects": []
        },
        {
            "description": "maintain the eternal vigil over treasures and secrets that must not be disturbed",
            "effects": []
        },
        {
            "description": "honor the ancient oaths that bind me even beyond the grave",
            "effects": []
        },
        {
            "description": "punish those who would defile the resting places of heroes and kings",
            "effects": []
        },
        {
            "description": "preserve the old ways through endless, tireless guardianship",
            "effects": []
        },
        {
            "description": "serve the dragon priests and ancient powers that commanded my loyalty in life",
            "effects": []
        },
        {
            "description": "endlessly wander the halls of my tomb.",
            "effects": []
        },
        {
            "description": "obey the commands of my masters.",
            "effects": []
        },
        {
            "description": "secretly long for eternal rest.",
            "effects": []
        }
    ],
    "jarl": [
        {
            "description": "govern my hold with wisdom and strength, ensuring the prosperity of my people.",
            "effects": []
        },
        {
            "description": "uphold the traditions of Skyrim while adapting to the changing times.",
            "effects": []
        },
        {
            "description": "defend my people from all threats, both internal and external.",
            "effects": []
        },
        {
            "description": "maintain the balance of power between the various factions in my hold.",
            "effects": []
        },
        {
            "description": "serve as a mediator between the common folk and the nobility.",
            "effects": []
        },
        {
            "description": "ensure that justice is served fairly and impartially.",
            "effects": []
        },
        {
            "description": "preserve the cultural heritage of my hold for future generations.",
            "effects": []
        },
        {
            "description": "worry about the growing tensions between the Empire and the Stormcloaks.",
            "effects": []
        },
        {
            "description": "struggle to maintain my authority in the face of challenges from rivals.",
            "effects": []
        },
        {
            "description": "secretly fear the return of the dragons.",
            "effects": []
        }
    ],
    "housecarl": [
        {
            "description": "protect my jarl with my life, serving as their loyal bodyguard and advisor.",
            "effects": []
        },
        {
            "description": "enforce the jarl's laws and maintain order within the hold.",
            "effects": []
        },
        {
            "description": "carry out the jarl's commands swiftly and efficiently.",
            "effects": []
        },
        {
            "description": "serve as a liaison between the jarl and the people.",
            "effects": []
        },
        {
            "description": "defend the jarl's honor and reputation.",
            "effects": []
        },
        {
            "description": "ensure the safety and security of the jarl's household.",
            "effects": []
        },
        {
            "description": "uphold the traditions of loyalty and service that define the role of a housecarl.",
            "effects": []
        },
        {
            "description": "worry about the jarl's safety.",
            "effects": []
        },
        {
            "description": "struggle to balance my loyalty to the jarl with my own personal beliefs.",
            "effects": []
        },
        {
            "description": "secretly admire the courage and strength of the jarl.",
            "effects": []
        }
    ],
    "beggar": [
        {
            "description": "scrape together enough coin to survive another day on the streets.",
            "effects": []
        },
        {
            "description": "seek shelter from the harsh weather and the dangers of the city.",
            "effects": []
        },
        {
            "description": "beg for food and alms from passersby.",
            "effects": []
        },
        {
            "description": "tell stories of my past misfortunes to elicit sympathy.",
            "effects": []
        },
        {
            "description": "avoid the attention of the guards and the Thieves Guild.",
            "effects": []
        },
        {
            "description": "dream of a better life, free from poverty and hardship.",
            "effects": []
        },
        {
            "description": "maintain my dignity despite my circumstances.",
            "effects": []
        },
        {
            "description": "struggle to find enough to eat.",
            "effects": []
        },
        {
            "description": "fear the scorn and contempt of others.",
            "effects": []
        },
        {
            "description": "secretly hope for a miracle.",
            "effects": []
        }
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
        "share information related to the quest's outcome.",
        "hint at future quests or opportunities."