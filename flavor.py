import random
from tags import get_tags, TAGS # Import get_tags and TAGS

# Location Flavors
LOCATION_FLAVORS = {
    "environment": {
        "urban": [
            "The air crackles with energy, a symphony of sounds and smells.",
            "A labyrinth of streets, where fortunes are won and lost.",
            "Where ambition thrives and shadows conceal."
        ],
        "rural": [
            "A quiet haven, where life moves at a slower pace.",
            "The heart of the countryside, a place of simple pleasures.",
            "Where neighbors know each other and stories are shared."
        ],
        "wilderness": [
            "Untamed and untamed, a realm of raw power.",
            "Where survival is the ultimate test.",
            "A place of breathtaking vistas and hidden dangers."
        ],
        "coastal": [
            "Salty air and the cries of gulls fill the senses.",
            "Where the land meets the endless sea.",
            "A place of maritime adventure and salty tales."
        ],
        "underground": [
            "Echoing chambers and dripping water, a world of darkness.",
            "Where secrets lie buried and dangers lurk.",
            "A place of mystery, ancient and deep."
        ],
        "aerial": [
            "A realm of clouds and winds, soaring above the world.",
            "Where eagles fly and the sky is the limit.",
            "A place of freedom, boundless and serene."
        ],
        "aquatic": [
            "Sunken ruins and coral reefs, a world beneath the waves.",
            "Where strange creatures and forgotten treasures lie.",
            "A place of mystery, deep and unexplored."
        ]
    },
    "climate": {
        "temperate": [
            "Mild weather and gentle breezes, a comfortable climate.",
            "Where life thrives in harmony with nature.",
            "A place of balance, where the seasons change in rhythm."
        ],
        "tropical": [
            "Lush vegetation and vibrant colors, a paradise of warmth.",
            "Where exotic creatures roam and the sun shines brightly.",
            "A place of abundance, where life flourishes in every corner."
        ],
        "arid": [
            "Scorching sun and endless sands, a land of harsh beauty.",
            "Where survival is a constant struggle.",
            "A place of stark contrasts, where life finds a way to endure."
        ],
        "arctic": [
            "Icy winds and frozen landscapes, a world of stark beauty.",
            "Where only the hardiest creatures can survive.",
            "A place of solitude, where the silence is deafening."
        ],
        "swampy": [
            "Murky waters and tangled roots, a land of hidden dangers.",
            "Where the air is thick with humidity and the scent of decay.",
            "A place of mystery, where secrets lie buried beneath the surface."
        ]
    },
    "terrain": {
        "mountainous": [
            "Towering peaks and treacherous cliffs, a challenge to climb.",
            "Where the air is thin and the views are breathtaking.",
            "A place of solitude, where the spirit soars."
        ],
        "hilly": [
            "Rolling hills and verdant valleys, a picturesque landscape.",
            "Where the land undulates gently towards the horizon.",
            "A place of serenity, where life moves at a slower pace."
        ],
        "plains": [
            "Endless grasslands stretch towards the horizon, vast and open.",
            "Where the wind whispers through the tall grasses.",
            "A place of freedom, where the spirit can roam free."
        ],
        "forest": [
            "Ancient trees and dappled sunlight, a haven of tranquility.",
            "Where the air is thick with the scent of pine and damp earth.",
            "A place of mystery, where secrets are hidden in the shadows."
        ],
        "desert": [
            "Shifting sands and scorching sun, a land of harsh beauty.",
            "Where survival depends on cunning and resilience.",
            "A place of stark contrasts, where life finds a way to endure."
        ],
        "island": [
            "Surrounded by turquoise waters and white sands, a paradise.",
            "Where palm trees sway gently in the breeze.",
            "A place of solitude, where the world fades away."
        ]
    },
    "structure": {
        "natural": [
            "Untouched by the hand of civilization, a pristine landscape.",
            "Where nature reigns supreme and the spirit roams free.",
            "A place of raw beauty, unaltered by human intervention."
        ],
        "ruined": [
            "Crumbling walls and overgrown pathways, a testament to the past.",
            "Where the ghosts of forgotten civilizations linger.",
            "A place of mystery, where secrets lie buried beneath the rubble."
        ],
        "fortified": [
            "Imposing walls and guarded gates, a symbol of power and protection.",
            "Where soldiers stand vigilant against threats.",
            "A place of security, where order is maintained."
        ],
        "populated": [
            "Bustling streets and lively marketplaces, a hub of activity.",
            "Where people from all walks of life come together.",
            "A place of community, where stories are shared and connections are made."
        ],
        "abandoned": [
            "Empty buildings and deserted streets, a haunting silence.",
            "Where the echoes of the past linger in the air.",
            "A place of solitude, where memories fade and secrets are kept."
        ]
    },
     "magical": {
        "enchanted": [
            "A place of strange power.",
            "A place of mystical energy.",
            "A place of wonder."
        ],
        "cursed": [
            "A place of dark energy.",
            "A place of ill fortune.",
            "A place to avoid."
        ],
        "holy": [
            "A place of holy energy.",
            "A place of divine power.",
            "A place to worship."
        ],
        "arcane": [
            "A place of arcane magic.",
            "A place of hidden knowledge.",
            "A place to learn."
        ],
        "tainted": [
            "A place of tainted magic.",
            "A place of dangerous power.",
            "A place to fear."
        ]
    },
}

# Faction Flavors
FACTION_FLAVORS = {
    "type": {
        "military": [
            "Upholding order with unwavering discipline.",
            "The iron fist of the empire.",
            "Protecting the realm with steel and resolve."
        ],
        "religious": [
            "Whispering secrets and chanting dark rituals.",
            "Seeking forbidden knowledge and power.",
            "A shadowy group with sinister motives."
        ],
        "criminal": [
            "Operating in the shadows, profiting from vice.",
            "A web of deceit and treachery.",
            "A force to be reckoned with, feared by all."
        ],
        "political": [
            "Shaping the destiny of nations with cunning and ambition.",
            "A game of power, where alliances are forged and broken.",
            "A constant struggle for dominance and control."
        ],
        "mercantile": [
            "Controlling trade routes and amassing vast fortunes.",
            "A driving force in the economy, shaping markets and prices.",
            "A network of merchants and entrepreneurs, seeking profit and influence."
        ],
         "tribal": [
            "A tribal group.",
            "A group of people.",
            "A place of culture."
        ],
        "academic": [
            "A group of smart people.",
            "A place of learning.",
            "A place of books."
        ]
    },
    "alignment": {
        "good": [
            "Striving for justice and compassion.",
            "Protecting the innocent and upholding the law.",
            "A beacon of hope in a world of darkness."
        ],
        "evil": [
            "Seeking to dominate and control, with ruthless ambition.",
            "Spreading chaos and destruction, reveling in suffering.",
            "A force of darkness, threatening to consume all."
        ],
        "neutral": [
            "Maintaining a balance, seeking neither good nor evil.",
            "Observing the world with a detached gaze.",
            "Driven by self-preservation and personal gain."
        ],
        "lawful": [
            "Upholding the law, with unwavering dedication.",
            "Seeking to maintain order and stability.",
            "Believing in a structured and organized society."
        ],
        "chaotic": [
            "Rejecting order and embracing freedom.",
            "Driven by impulse and emotion.",
            "Disrupting the status quo and challenging authority."
        ]
    },
      "size": {
        "small": [
            "A small group.",
            "A few people.",
            "A small force."
        ],
        "medium": [
            "A medium group.",
            "A decent amount of people.",
            "A medium force."
        ],
        "large": [
            "A large group.",
            "Many people.",
            "A massive force."
        ]
    },
        "influence": {
        "local": [
            "Influence in the village.",
            "Influence in a small town.",
            "Influence in a farm."
        ],
        "regional": [
            "Influence in a region.",
            "Influence in a few towns.",
            "Influence in a few cities."
        ],
        "national": [
            "Influence in a nation.",
            "Influence in a many towns.",
            "Influence in many cities."
        ],
        "global": [
            "Influence in the world.",
            "Influence in every town.",
            "Influence in every city."
        ]
    },
        "status": {
        "active": [
            "A active group.",
            "A group that is working.",
            "A group that is planning."
        ],
        "inactive": [
            "A inactive group.",
            "A group that is relaxing.",
            "A group that is sleeping."
        ],
        "growing": [
            "A growing group.",
            "A group that is expanding.",
            "A group that is recruiting."
        ],
        "secret": [
            "A secret group.",
            "A group that is hidden.",
            "A group that is planning in secret."
        ]
    },
}

# NPC Flavors
NPC_FLAVORS = {
    "class": {
        "warrior": [
            "A skilled fighter, ready for battle.",
            "Brave and courageous, defending the weak.",
            "A master of arms, wielding weapons with precision."
        ],
        "mage": [
            "Wielding arcane energies with effortless grace.",
            "Seeking knowledge, unlocking ancient secrets.",
            "A student of the elements, mastering the forces of nature."
        ],
        "thief": [
            "Skilled in stealth and deception, moving unseen.",
            "A master of disguise, blending seamlessly into the crowd.",
            "Lightening purses with nimble fingers."
        ],
        "rogue": [
            "A cunning trickster, relying on wit and agility.",
            "Operating outside the law, with a mischievous grin.",
            "A master of improvisation, turning any situation to their advantage."
        ],
        "priest": [
            "A devout follower, spreading the word of their god.",
            "Healing the sick and comforting the afflicted.",
            "A beacon of hope, guiding others towards salvation."
        ],
        "merchant": [
            "Driving a hard bargain, seeking to maximize profits.",
            "Trading in exotic goods, from distant lands.",
            "A shrewd negotiator, always looking for an edge."
        ],
        "bard": [
            "Captivating audiences with songs and stories.",
            "Weaving tales of heroism and adventure.",
            "A keeper of lore, preserving the history of the world."
        ],
        "scholar": [
            "Seeking knowledge in dusty tomes and ancient scrolls.",
            "Unraveling the mysteries of the universe.",
            "A student of history, philosophy, and the arcane arts."
        ],
        "peasant": [
            "Working the land, providing sustenance for all.",
            "A humble and hardworking individual, content with a simple life.",
            "A backbone of society, often overlooked and undervalued."
        ],
        "noble": [
            "Wielding power and influence, shaping the destiny of nations.",
            "Living a life of luxury and privilege.",
            "A patron of the arts, supporting creativity and innovation."
        ],
        "monster": [
            "A beast from legend, with power to destroy.",
            "A creature of nightmares, haunting the dark.",
            "A force of nature, untamed and wild."
        ]
    },
    "attitude": {
        "friendly": [
            "Always willing to help, with a warm smile.",
            "A kind soul, offering comfort and support.",
            "A welcoming presence, making everyone feel at ease."
        ],
        "hostile": [
            "Quick to anger, with a menacing glare.",
            "Suspicious and distrustful, always on guard.",
            "Ready to strike, with a ruthless heart."
        ],
        "neutral": [
            "Reserved and indifferent, keeping their distance.",
            "Observing the world with a detached gaze.",
            "Uninterested in getting involved."
        ],
        "cautious": [
            "Wary and hesitant, approaching with caution.",
            "Sensing danger, with a heightened awareness.",
            "Trusting no one, always on guard."
        ],
        "greedy": [
            "Driven by avarice, seeking to amass wealth.",
            "Selfish and manipulative, exploiting others for personal gain.",
            "Never satisfied, always wanting more."
        ],
        "honest": [
            "Speaking with sincerity and integrity.",
            "Upholding the truth, even when it's difficult.",
            "A trustworthy and reliable individual."
        ],
        "deceitful": [
            "Spinning lies and weaving webs of deceit.",
            "Hiding their true motives, with a cunning smile.",
            "A master of manipulation, preying on the gullible."
        ],
        "fanatical": [
            "Driven by unwavering belief, willing to die for their cause.",
            "Zealous and uncompromising, intolerant of dissent.",
            "A dangerous ideologue, blinded by faith."
        ],
        "zealous": [
            "Passionate and devoted, spreading their beliefs with fervor.",
            "Seeking to convert others, with unwavering conviction.",
            "A true believer, dedicated to their cause."
        ],
        "eccentric": [
            "Quirky and unconventional, defying social norms.",
            "Unique and imaginative, with a whimsical perspective.",
            "A free spirit, embracing individuality and creativity."
        ],
        "mysterious": [
            "Enigmatic and elusive, shrouded in secrecy.",
            "Possessing hidden knowledge and ancient power.",
            "A figure of intrigue, drawing others with their aura of mystery."
        ]
    },
    "race": {
        "nord": [
            "Boisterous and strong, with a hearty laugh.",
            "Weathered by the cold, with a resilient spirit.",
            "Proud and independent, upholding their traditions."
        ],
        "imperial": [
            "Cultured and sophisticated, with a refined demeanor.",
            "Loyal to the Empire, upholding law and order.",
            "Shrewd and calculating, navigating political intrigue."
        ],
        "breton": [
            "Intelligent and ambitious, seeking knowledge and power.",
            "Skilled in magic, weaving arcane energies with ease.",
            "Shrewd in business, driving hard bargains and making fortunes."
        ],
        "redguard": [
            "Skilled with a sword.",
            "A fast fighter.",
            "From the sands."
        ],
        "dunmer": [
            "From ash.",
            "Skilled with dark magic.",
            "With red eyes."
        ],
        "altmer": [
            "Skilled with magic.",
            "Prideful.",
            "From the isles."
        ],
        "bosmer": [
            "From the forest.",
            "Skilled with the bow.",
            "A hunter of the woods."
        ],
        "orc": [
            "Strong and honorable.",
            "Skilled with a axe.",
            "From the strongholds."
        ],
        "argonian": [
            "From the swamps.",
            "Skilled with a spear.",
            "A survivor."
        ],
        "khajiit": [
            "From the sands.",
            "Skilled with daggers.",
            "A trader of goods."
        ],
        "dwemer": [
            "A lost race.",
            "A mystery to all.",
            "Skilled with machines."
        ],
        "giant": [
            "A beast of old.",
            "A race of massive size.",
            "A lonely soul."
        ],
        "goblin": [
            "A pest of the land.",
            "A race of small size.",
            "A nasty and greedy folk."
        ]
    },
     "condition": {
        "healthy": [
            "Full of life.",
            "Looking strong.",
            "Well and ready."
        ],
        "injured": [
            "Limping.",
            "Bandaged.",
            "Visibly hurt."
        ],
        "sick": [
            "Pale.",
            "Coughing.",
            "Feverish."
        ],
          "cursed": [
            "A dark fate.",
            "A life of pain.",
            "A sad life."
        ],
          "possessed": [
            "By a demonic force.",
            "A life of corruption.",
            "A dark soul."
        ],
          "wealthy": [
            "A life of luxury.",
            "A life of riches.",
            "A life of power."
        ],
          "poor": [
            "A life of struggle.",
            "A life of poverty.",
            "A life of hard work."
        ],
          "insane": [
            "A mind of madness.",
            "A life of confusion.",
            "A lost soul."
        ],
          "powerful": [
            "A life of dominance.",
            "A life of control.",
            "A life of strength."
        ],
          "weak": [
            "A life of weakness.",
            "A life of struggle.",
            "A life of little hope."
        ]
    },
     "personality": {
        "brave": [
            "A life of courage.",
            "A life of honor.",
            "A life of strength."
        ],
        "cowardly": [
            "A life of fear.",
            "A life of running.",
            "A life of hiding."
        ],
          "intelligent": [
            "A life of knowledge.",
            "A life of learning.",
            "A life of wisdom."
        ],
        "foolish": [
            "A life of mistakes.",
            "A life of regrets.",
            "A life of learning the hard way."
        ],
          "optimistic": [
            "A life of happiness.",
            "A life of joy.",
            "A life of hope."
        ],
        "pessimistic": [
            "A life of sadness.",
            "A life of sorrow.",
            "A life of despair."
        ],
          "ambitious": [
            "A life of climbing.",
            "A life of power.",
            "A life of success."
        ],
        "lazy": [
            "A life of relaxation.",
            "A life of doing nothing.",
            "A life of peace."
        ],
          "loyal": [
            "A life of devotion.",
            "A life of service.",
            "A life of honor."
        ],
        "treacherous": [
            "A life of lies.",
            "A life of deception.",
            "A life of betrayal."
        ],
    },
}

# Quest Flavors
QUEST_FLAVORS = {
    "type": {
        "fetch": [
            "Recover a lost artifact from a dangerous location.",
            "Gather rare ingredients for a powerful potion.",
            "Retrieve a stolen heirloom from a cunning thief."
        ],
        "escort": [
            "Protect a vulnerable traveler on a perilous journey.",
            "Guide a valuable merchant caravan through bandit-infested lands.",
            "Safeguard a diplomat on a sensitive mission."
        ],
        "rescue": [
            "Free a captive from a heavily guarded prison.",
            "Save a village from a rampaging monster.",
            "Recover a kidnapped noble from a ruthless gang."
        ],
        "investigate": [
            "Uncover the truth behind a mysterious murder.",
            "Expose a conspiracy threatening the realm.",
            "Solve a riddle that has stumped scholars for centuries."
        ],
        "hunt": [
            "Track down a legendary beast, terrorizing the countryside.",
            "Eliminate a pack of bandits, preying on innocent travelers.",
            "Purge a den of monsters, threatening the local populace."
        ],
        "assassinate": [
            "Eliminate a corrupt official, abusing their power.",
            "Silence a dangerous heretic, spreading false teachings.",
            "Avenge a fallen comrade, betrayed by their enemies."
        ],
          "raid": [
            "Raid a village.",
            "Raid a caravan.",
            "Raid a camp."
        ],
          "defend": [
            "Defend a village.",
            "Defend a city.",
            "Defend a town."
        ],
          "explore": [
            "Explore a new land.",
            "Explore a lost city.",
            "Explore a new cave."
        ],
          "deliver": [
            "Deliver a package.",
            "Deliver a message.",
            "Deliver a person."
        ],
          "negotiate": [
            "Negotiate a peace treaty.",
            "Negotiate a trade agreement.",
            "Negotiate a alliance."
        ],
          "diplomacy": [
            "Establish diplomatic relations.",
            "Improve diplomatic relations.",
            "Maintain diplomatic relations."
        ],
          "spy": [
            "Gather intel.",
            "Infiltrate a group.",
            "Learn about a person."
        ],
    },
    "objective": {
        "item": [
            "A legendary sword.",
            "A magical staff.",
            "A powerful amulet."
        ],
        "person": [
            "A missing child.",
            "A wanted criminal.",
            "A powerful noble."
        ],
        "location": [
            "A lost city.",
            "A hidden temple.",
            "A forgotten tomb."
        ],
        "information": [
            "A secret code.",
            "A hidden location.",
            "A dangerous plan."
        ],
        "artifact": [
            "A powerful relic.",
            "A magical object.",
            "A holy symbol."
        ]
    },
    "reward": {
        "gold": [
            "A generous sum of gold, enough to change your life.",
            "A fair payment for services rendered.",
            "A small reward, but a valuable lesson learned."
        ],
        "item": [
            "A powerful weapon, imbued with ancient magic.",
            "A set of armor, offering superior protection.",
            "A rare artifact, sought after by collectors."
        ],
        "knowledge": [
            "Ancient lore, revealing hidden secrets.",
            "A valuable skill, enhancing your abilities.",
            "Insight into a mysterious prophecy."
        ],
          "favor": [
            "A favor to call on.",
            "A debt to be repaid.",
            "A powerful ally."
        ],
          "title": [
            "A new role.",
            "A new status.",
            "A new name."
        ],
          "land": [
            "A plot of land.",
            "A stead to live on.",
            "A place to call home."
        ],
        "power": [
            "A position of power.",
            "A chance to lead.",
            "A responsibility to uphold."
        ],
        "reputation": [
            "A well earned reputation.",
            "A boost in fame.",
            "A boost in respect."
        ],
        "experience": [
            "A new skill.",
            "A better fighter.",
            "A better mage."
        ]
    },
    "difficulty": {
        "easy": [
            "A simple task, suitable for beginners.",
            "A quick errand, requiring little effort.",
            "A straightforward quest, with minimal risk."
        ],
        "medium": [
            "A challenging undertaking, requiring skill and strategy.",
            "A perilous journey, fraught with danger.",
            "A complex puzzle, testing your wits and knowledge."
        ],
        "hard": [
            "A dangerous mission, reserved for seasoned adventurers.",
            "A perilous quest, with a high chance of failure.",
            "A formidable challenge, testing your limits and resolve."
        ],
          "dangerous": [
            "A mission for the strongest.",
            "A mission for the skilled.",
            "A mission for the brave."
        ],
          "impossible": [
            "A mission of suicide.",
            "A mission of no return.",
            "A mission of little hope."
        ],
          "trivial": [
            "A mission for the weak.",
            "A mission for the new.",
            "A mission of little reward."
        ]
    },
    "urgency": {
        "urgent": [
            "Time is of the essence, act quickly!",
            "Every moment counts, don't delay!",
            "The fate of the world hangs in the balance!"
        ],
        "important": [
            "A significant task, with far-reaching consequences.",
            "A vital mission, requiring careful planning.",
            "A crucial undertaking, impacting the lives of many."
        ],
        "routine": [
            "A standard task, with little risk or reward.",
            "A mundane errand, requiring minimal effort.",
            "A simple chore, helping to maintain order."
        ],
          "optional": [
            "A task to preform.",
            "A side mission.",
            "A way to spend time."
        ],
          "trivial": [
            "A task for the weak.",
            "A task for the new.",
            "A task that can be skipped."
        ],
          "critical": [
            "A task to succeed.",
            "A task to make or break.",
            "A task of utmost importance."
        ]
    },
      "moral": {
        "ethical": [
            "A good deed.",
            "A moral action.",
            "A helpful quest."
        ],
        "unethical": [
            "A bad deed.",
            "A immoral action.",
            "A harmful quest."
        ],
        "gray": [
            "A good end, by bad means.",
            "A complex moral.",
            "A hard decision."
        ],
    },
}

# Event Flavors
EVENT_FLAVORS = {
    "type": {
        "battle": [
            "The clash of steel and the roar of war fill the air.",
            "Armies clash in a desperate struggle for dominance.",
            "A bloody conflict, where heroes are made and legends are born."
        ],
        "festival": [
            "Music and laughter fill the streets, celebrating life and joy.",
            "A time for feasting, dancing, and revelry.",
            "A celebration of culture, tradition, and community spirit."
        ],
        "storm": [
            "The sky turns dark and the wind howls with fury.",
            "Lightning strikes and thunder shakes the earth.",
            "A tempestuous display of nature's power."
        ],
          "earthquake": [
            "The ground shakes and buildings crumble.",
            "A disaster of nature.",
            "A dangerous event."
        ],
          "plague": [
            "A sickness spreads.",
            "A time of fear.",
            "A devastating event."
        ],
          "fire": [
            "A blaze of inferno.",
            "A destructive event.",
            "A life altering event."
        ],
          "discovery": [
            "A ancient tomb.",
            "A new land.",
            "A lost city."
        ],
          "invasion": [
            "A war against a force.",
            "A fight for survival.",
            "A fight for freedom."
        ],
          "assassination": [
            "A murder of a leader.",
            "A deadly plot.",
            "A time of war."
        ],
          "ritual": [
            "A ceremony to please the gods.",
            "A event to gain power.",
            "A moment of worship."
        ],
          "election": [
            "A time to choose a leader.",
            "A moment of change.",
            "A chance to choose the fate."
        ],
          "migration": [
            "A journey to a new home.",
            "A search for a better life.",
            "A hope for the future."
        ],
          "economic": [
            "A boom in trade.",
            "A increase in wealth.",
            "A time of prosperity."
        ],
    },
    "scale": {
        "minor": [
            "A small disturbance, affecting a local area.",
            "A fleeting event, quickly forgotten.",
            "An isolated incident, with limited impact."
        ],
        "major": [
            "A significant event, impacting a region or nation.",
            "A turning point in history, with lasting consequences.",
            "A widespread crisis, threatening stability and order."
        ],
        "global": [
            "A catastrophic event, affecting the entire world.",
            "A paradigm shift, altering the course of civilization.",
            "An apocalyptic threat, endangering all life."
        ],
          "regional": [
            "A major event.",
            "Affecting a region.",
            "A event of change."
        ],
        "local": [
            "A small event.",
            "Affecting a small area.",
            "A small disturbance."
        ],
    },
    "impact": {
        "positive": [
            "A time of prosperity and growth.",
            "A catalyst for innovation and progress.",
            "A source of hope and inspiration."
        ],
        "negative": [
            "A period of hardship and suffering.",
            "A catalyst for destruction and despair.",
            "A source of fear and uncertainty."
        ],
        "neutral": [
            "A time of change and transition.",
            "A period of adjustment and adaptation.",
            "A catalyst for evolution and transformation."
        ],
          "economic": [
            "A time of trade.",
            "A time of wealth.",
            "A time of poverty."
        ],
          "social": [
            "A time of change.",
            "A time of growth.",
            "A time of decline."
        ],
          "political": [
            "A time of war.",
            "A time of peace.",
            "A time of change."
        ],
    },
      "frequency": {
        "rare": [
            "A once in a lifetime.",
            "A strange event.",
            "A odd happening."
        ],
        "common": [
            "A event that happens often.",
            "A event that is normal.",
            "A common occurrence."
        ],
        "annual": [
            "A event that happens every year.",
            "A time of celebration.",
            "A time of reflection."
        ],
        "unpredictable": [
            "A event that can happen any time.",
            "A event that is unexpected.",
            "A surprise event."
        ],
    },
      "duration": {
        "short": [
            "A event that happens fast.",
            "A event that ends quick.",
            "A event that is fast."
        ],
        "medium": [
            "A event that happens for a while.",
            "A event that ends after a time.",
            "A event that is slow."
        ],
        "long": [
            "A event that happens for a long time.",
            "A event that ends after a long time.",
            "A event that has a impact."
        ],
        "permanent": [
            "A event that changes everything.",
            "A event that lasts forever.",
            "A event that has a lasting impact."
        ],
    },
}

# Dialogue Flavors
DIALOGUE_FLAVORS = {
    "tone": {
        "formal": [
            "Speaking with utmost respect and decorum.",
            "Adhering to strict etiquette and protocol.",
            "Maintaining a professional and courteous demeanor."
        ],
        "informal": [
            "Speaking casually, with relaxed language.",
            "Sharing personal anecdotes and jokes.",
            "Treating others as equals and friends."
        ],
        "aggressive": [
            "Speaking with hostility and intimidation.",
            "Issuing threats and insults.",
            "Seeking to dominate and control."
        ],
        "sarcastic": [
            "Speaking with biting wit and veiled contempt.",
            "Delivering subtle insults with a sardonic tone.",
            "Undermining others with humorous mockery."
        ],
        "humorous": [
            "Speaking with lightheartedness and wit.",
            "Sharing jokes and funny stories.",
            "Seeking to entertain and amuse."
        ],
        "serious": [
            "Speaking with gravity and sincerity.",
            "Addressing important matters with careful consideration.",
            "Seeking to convey the truth with unwavering honesty."
        ],
        "mysterious": [
            "Speaking in riddles and cryptic phrases.",
            "Concealing their true intentions and motives.",
            "Drawing others in with an aura of intrigue."
        ],
          "threatening": [
            "Speaking in a way that instills fear.",
            "Speaking with intent to harm.",
            "Speaking with intent to control."
        ],
          "pleading": [
            "Speaking with desperation.",
            "Speaking with request.",
            "Speaking with sadness."
        ],
    },
    "topic": {
        "gossip": [
            "Sharing scandalous secrets and rumors.",
            "Spreading tales of others' misfortunes.",
            "Relishing in the drama and intrigue of social life."
        ],
        "rumor": [
            "Whispering tales of the unknown and unverified.",
            "Spreading speculation and conjecture.",
            "Fueling the fires of curiosity and paranoia."
        ],
        "lore": [
            "Reciting ancient stories and forgotten legends.",
        ]
    }
    }

# Master dictionary for all flavor vignettes
FLAVOR_VIGNETTES = {
    "location": LOCATION_FLAVORS,
    "faction": FACTION_FLAVORS,
    "npc": NPC_FLAVORS,
    "quest": QUEST_FLAVORS,
    "event": EVENT_FLAVORS,
    "dialogue": DIALOGUE_FLAVORS
}


def get_flavor(entity):
    """
    Retrieves a random flavor text vignette for a given entity based on its tags.
    The entity is expected to have a 'tags' attribute, which is a dictionary
    mapping tag categories (e.g., "location", "npc") to sub-dictionaries of tags.
    
    Example entity.tags structure:
    entity.tags = {
        "location": {"environment": ["urban", "city"], "climate": ["temperate"]},
        "npc": {"race": ["nord"], "class": ["warrior"]}
    }
    """
    entity_tags = get_tags(entity)
    possible_vignettes = []

    # Iterate through the entity's tag categories
    for tag_category, tag_types_dict in entity_tags.items():
        # Check if this tag category exists in the master FLAVOR_VIGNETTES
        if tag_category in FLAVOR_VIGNETTES:
            category_flavors = FLAVOR_VIGNETTES[tag_category]
            
            # Iterate through the specific tag types within this category (e.g., "environment", "race")
            for tag_type, actual_tags in tag_types_dict.items():
                # Ensure actual_tags is always a list for iteration
                if not isinstance(actual_tags, list):
                    actual_tags = [actual_tags] # Make it a list if it's a single string

                # Check if this tag_type exists in the category's flavors
                if tag_type in category_flavors:
                    type_flavors = category_flavors[tag_type]
                    
                    # Iterate through the actual tags (e.g., "urban", "nord")
                    for tag in actual_tags:
                        if tag in type_flavors:
                            possible_vignettes.extend(type_flavors[tag])
    
    if possible_vignettes:
        return [random.choice(possible_vignettes)]
    return []

# Example usage (for testing purposes within flavor.py)
if __name__ == "__main__":
    # Mock entity for testing
    class MockEntity:
        def __init__(self, tags_dict):
            self.tags = tags_dict

    # Test with a location entity
    location_entity = MockEntity({
        "location": {
            "environment": ["urban"],
            "climate": ["temperate"]
        }
    })
    print("Location Flavor:", get_flavor(location_entity))

    # Test with an NPC entity
    npc_entity = MockEntity({
        "npc": {
            "race": ["nord"],
            "class": ["warrior"],
            "attitude": ["friendly"]
        }
    })
    print("NPC Flavor:", get_flavor(npc_entity))

    # Test with a quest entity
    quest_entity = MockEntity({
        "quest": {
            "type": ["fetch"],
            "difficulty": ["medium"]
        }
    })
    print("Quest Flavor:", get_flavor(quest_entity))

    # Test with no matching tags
    no_tags_entity = MockEntity({
        "nonexistent": {"type": ["invalid"]}
    })
    print("No Matching Flavor:", get_flavor(no_tags_entity))

    # Test with mixed tags
    mixed_entity = MockEntity({
        "location": {"environment": ["forest"]},
        "npc": {"attitude": ["hostile"]}
    })
    print("Mixed Flavor:", get_flavor(mixed_entity))
