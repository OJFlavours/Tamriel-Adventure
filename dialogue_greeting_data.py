# dialogue_greeting_data.py

import random

HOSTILE_GREETINGS = {
    "bandit": [
        "Hand over your coin, or I'll take it from your corpse!",
        "Wrong place, wrong time, stranger. This is bandit territory!",
        "You've walked into the wrong camp, fool. Prepare to die!",
        "Your purse or your life! Choose quickly!"
    ],
    "forsworn": [
        "Another Imperial dog comes to defile our sacred lands!",
        "The old gods demand your blood, outlander!",
        "You trespass on Forsworn territory. The Reach will have its revenge!",
        "By Hircine's bloody hunt, you will not leave here alive!"
    ],
    "thalmor": [
        "Another inferior being seeks audience with their betters.",
        "You dare approach an agent of the Aldmeri Dominion so brazenly?",
        "Your very presence offends the natural order, mortal.",
        "State your business quickly, before I lose what little patience I have."
    ],
    "vampire": [
        "You reek of mortality... how deliciously fragile you are.",
        "Another warm-blooded fool wanders into my domain.",
        "Your blood calls to me, mortal. Resist if you can.",
        "The living should not disturb the eternal. You will regret this."
    ],
    "necromancer": [
        "You interrupt my communion with death itself!",
        "Another soul to add to my collection... willing or not.",
        "The dark arts have shown me your fate, fool.",
        "Life is but a fleeting moment before eternal servitude!"
    ],
    "default": [
        "You picked the wrong person to cross!",
        "Get away from me before I do something we'll both regret!",
        "I don't have time for your kind!",
        "Move along before this gets ugly!"
    ]
}

UNFRIENDLY_GREETINGS = {
    "guard": [
        "Keep moving, citizen. Nothing to see here.",
        "State your business and make it quick.",
        "I've got my eye on you, stranger.",
        "Don't give me a reason to arrest you."
    ],
    "merchant": [
        "I suppose you want something. Coin first, questions later.",
        "My prices aren't negotiable, so don't waste my time haggling.",
        "What do you want? I'm busy running a business here.",
        "If you're not buying, then you're Browse. Don't touch anything."
    ],
    "noble": [
        "Do you have an appointment? No? Then this conversation is over.",
        "I don't associate with commoners without good reason.",
        "Your presence here is... unexpected. And unwelcome.",
        "Speak quickly. My time is far more valuable than yours."
    ],
    "priest": [
        "The gods test my patience with visitors like you.",
        "State your need for divine guidance... if you're worthy.",
        "Even the Divines grow weary of those who lack faith.",
        "What brings you to disturb my meditation?"
    ],
    "default": [
        "What do you want?",
        "Make it quick, I haven't got all day.",
        "I suppose you need something from me.",
        "This better be important."
    ]
}

NEUTRAL_GREETINGS = {
    "innkeeper": [
        "Welcome to my establishment. Room or board?",
        "What can I get for you today?",
        "Take a seat wherever you like. I'll be with you shortly.",
        "We've got food, drink, and beds. What's your pleasure?"
    ],
    "merchant": [
        "Browse my wares if you like. Prices are fair.",
        "I've got quality goods at reasonable prices.",
        "Looking for anything in particular today?",
        "Take a look around. I'm sure we can make a deal."
    ],
    "guard": [
        "Citizen. Keep your nose clean while you're in town.",
        "Just remember to follow the laws while you're here.",
        "Move along, nothing to see here.",
        "Keep the peace, and we won't have any problems."
    ],
    "blacksmith": [
        "I work with steel and iron. What do you need forged?",
        "My forge burns hot and my hammer rings true.",
        "Looking for weapons or armor? You've come to the right place.",
        "Quality smithwork takes time. What can I craft for you?"
    ],
    "farmer": [
        "Another traveler passes through our humble lands.",
        "The soil here is good, but the work is hard.",
        "Are you here about the crops, or just passing through?",
        "Times are tough for farmers, but we manage."
    ],
    "miner": [
        "Long days in the mines make for short conversations.",
        "The deeper you dig, the more dangers you find.",
        "Mining's honest work, if you can handle the darkness.",
        "These mountains hold more secrets than gold."
    ],
    "hunter": [
        "The wilds provide for those who respect them.",
        "Game's been scarce lately. Something's got them spooked.",
        "A hunter learns to read the signs the land provides.",
        "These forests hold both bounty and danger in equal measure."
    ],
    "scholar": [
        "Knowledge is the greatest treasure of all.",
        "I seek understanding in the written word.",
        "Ancient lore holds answers to modern questions.",
        "Learning never ends for those who truly seek wisdom."
    ],
    "bard": [
        "Every person has a story worth telling.",
        "Music and tales lighten even the darkest days.",
        "I collect stories like others collect coin.",
        "Would you care to hear a song, or perhaps share a tale?"
    ],
    "default": [
        "Hello there.",
        "Can I help you with something?",
        "What brings you here?",
        "Good to see another traveler."
    ]
}

FRIENDLY_GREETINGS = {
    "innkeeper": [
        "Welcome, welcome! Come warm yourself by the fire!",
        "Well met, traveler! The finest ale in the hold awaits you!",
        "A friendly face! Please, make yourself at home here.",
        "By the Eight and One, it's good to see a new face! What can I do for you?"
    ],
    "merchant": [
        "Ah, a discerning customer! I have just the thing for you!",
        "Welcome, friend! My wares are the finest you'll find anywhere!",
        "Excellent timing! I just received a new shipment you'll want to see.",
        "A shrewd buyer knows quality when they see it. Take a look around!"
    ],
    "guard": [
        "Well met, citizen. Always good to see law-abiding folk.",
        "Greetings! Your timing is good - the roads are safe today.",
        "Welcome to our fair city. May your stay be peaceful and profitable.",
        "A friendly face in these troubled times. How can I assist you?"
    ],
    "priest": [
        "The Divines bless this meeting, child. How may I serve?",
        "May Akatosh's light guide your path, traveler.",
        "Welcome to this sacred place. The gods smile upon the faithful.",
        "Peace be with you, friend. What spiritual guidance do you seek?"
    ],
    "blacksmith": [
        "Ah, someone who appreciates fine metalwork! Welcome to my forge!",
        "Well met! I take pride in every piece that leaves my workshop.",
        "A fellow admirer of steel and flame! What can I craft for you?",
        "The ring of hammer on anvil calls to all true warriors. How can I help?"
    ],
    "noble": [
        "Greetings, citizen. Your reputation precedes you.",
        "Well met! It's refreshing to encounter someone of quality.",
        "A person of distinction, I see. How may I be of service?",
        "Welcome! Your presence brings honor to my hall."
    ],
    "farmer": [
        "Well met, friend! The harvest has been kind this season.",
        "Welcome to our lands! Honest work makes for honest folk.",
        "Good to see a friendly traveler! The road treats you well, I hope.",
        "By Kynareth's grace, another good soul crosses our path!"
    ],
    "hunter": [
        "Well met, fellow wanderer! The wilds have been good to me lately.",
        "Greetings! A kindred spirit who appreciates nature's bounty.",
        "Welcome, friend! The forest provides for those who respect her.",
        "Good hunting to you! May your aim be true and your quarry plentiful."
    ],
    "scholar": [
        "Greetings, fellow seeker of knowledge! What wisdom do you pursue?",
        "Well met! A mind that questions is a mind that grows.",
        "Welcome! Perhaps we might share discoveries over scholarly discourse?",
        "Ah, another who values learning! What brings you to seek knowledge?"
    ],
    "bard": [
        "Well met, friend! Would you care to hear a tale of distant lands?",
        "Greetings! Every new face brings new stories to collect.",
        "A warm welcome to you! Music and merriment lift all spirits.",
        "Hail and well met! Perhaps you have a song or story to share?"
    ],
    "mage": [
        "Well met, traveler! The arcane arts reveal much about one's character.",
        "Greetings! I sense you have an appreciation for the mystical.",
        "Welcome! Knowledge of the magical arts is always worth sharing.",
        "Well encountered! The weave of magic connects all things."
    ],
    "default": [
        "Well met, friend!",
        "Greetings, traveler! Good to see you!",
        "Welcome! What brings you our way?",
        "A friendly face! How can I help you today?"
    ]
}

ADMIRING_GREETINGS = {
    "innkeeper": [
        "My friend! Welcome back to the finest establishment in all Skyrim!",
        "By the gods, if it isn't my most valued patron! Your usual table awaits!",
        "The hero graces my humble inn once more! Tonight, the ale flows freely!",
        "Welcome, welcome! Your legendary reputation brightens these halls!"
    ],
    "merchant": [
        "My most esteemed customer returns! I've saved my finest wares just for you!",
        "The realm's greatest hero honors my shop! Everything is at your disposal!",
        "By Zenithar's golden scales! Take whatever you need, my friend!",
        "Your patronage brings prosperity to my business and honor to my name!"
    ],
    "guard": [
        "An honor to serve alongside someone of your caliber, hero!",
        "The people sleep safely knowing heroes like you walk among us!",
        "By Stendarr's mercy, our city is blessed by your presence!",
        "Your deeds will be remembered for generations, champion!"
    ],
    "priest": [
        "The Divines themselves must have guided you to this sacred place!",
        "Blessed are we to receive one so favored by the gods!",
        "Your righteous deeds echo through the halls of Aetherius itself!",
        "May the Nine Divines continue to bless your noble quest!"
    ],
    "blacksmith": [
        "The legendary hero graces my forge! What weapon shall I craft for your next great deed?",
        "By Talos's hammer! Working steel for a true champion is a smith's greatest honor!",
        "Every blade I forge pales beside the legend you've already written!",
        "Your patronage makes my humble craft legendary by association!"
    ],
    "noble": [
        "My lord/lady! Your presence brings honor to my entire bloodline!",
        "The realm's greatest champion graces my halls! You are always welcome here!",
        "By my ancestors' honor, serving you is the privilege of a lifetime!",
        "Your legendary deeds have earned you a place in the songs of our bards!"
    ],
    "scholar": [
        "The living legend seeks knowledge! What wisdom can this humble scholar provide?",
        "Your deeds will be studied by generations of historians yet unborn!",
        "To share knowledge with one so renowned is a scholar's ultimate achievement!",
        "History itself bends around your actions, shaping the fate of empires!"
    ],
    "bard": [
        "The hero of legend walks among us! Your deeds surpass even the greatest epics!",
        "Every song I sing pales before the reality of your adventures!",
        "Bards across the realm compose verses about your magnificent deeds!",
        "To meet the subject of so many tales in person... what an honor!"
    ],
    "default": [
        "My friend! Always a pleasure to see you!",
        "The legendary hero returns! How may I serve?",
        "Your reputation precedes you, champion!",
        "By the gods, what an honor to speak with you again!"
    ]
}

# Add more diverse greetings
NEUTRAL_GREETINGS["child"] = [
    "Are you going to the Cloud District often? Oh, what am I saying - of course you don't.",
    "I saw a mudcrab the other day. Horrible creatures.",
    "Do you know my father? He's the Jarl's steward.",
    "I wish I was old enough to fight in the war."
]

NEUTRAL_GREETINGS["beggar"] = [
    "Spare a coin for a poor soul?",
    "Alms for the needy?",
    "Blessings of the Divines upon you, if you can spare a bit of bread.",
    "Anything to help an old beggar keep warm?"
]

NEUTRAL_GREETINGS["drunk"] = [
    "Hic... What'sh your name, friend?",
    "Another round, barkeep! Hic...",
    "Ishn't thish a lovely day? Hic...",
    "I've had better daysh... Hic..."
]

# Example of greetings based on player's reputation (dynamic greetings)
def get_dynamic_greeting(npc_type, player_reputation):
    if player_reputation > 50:
        return random.choice(FRIENDLY_GREETINGS.get(npc_type, FRIENDLY_GREETINGS["default"]))
    elif player_reputation < -50:
        return random.choice(HOSTILE_GREETINGS.get(npc_type, HOSTILE_GREETINGS["default"]))
    else:
        return random.choice(NEUTRAL_GREETINGS.get(npc_type, NEUTRAL_GREETINGS["default"]))

# Example of greeting effects (modify NPC behavior)
GREETING_EFFECTS = {
    "Spare a coin for a poor soul?": {"modify_disposition": 5},
    "Hand over your coin, or I'll take it from your corpse!": {"start_combat": True}
}

# Example of error handling
def process_greeting(npc_type, player_reputation):
    try:
        greeting = get_dynamic_greeting(npc_type, player_reputation)
        print(greeting)

        # Apply greeting effects
        effect = GREETING_EFFECTS.get(greeting)
        if effect:
            if effect.get("modify_disposition"):
                print("Modifying disposition")
            if effect.get("start_combat"):
                print("Starting combat")

    except Exception as e:
        print(f"Error processing greeting: {e}")

# Reorganize greeting data for better scalability
ALL_GREETINGS = {
    "hostile": HOSTILE_GREETINGS,
    "unfriendly": UNFRIENDLY_GREETINGS,
    "neutral": NEUTRAL_GREETINGS,
    "friendly": FRIENDLY_GREETINGS,
}

def get_greeting(disposition, npc_type):
    try:
        greeting_pool = ALL_GREETINGS.get(disposition.lower(), ALL_GREETINGS["neutral"])
        return random.choice(greeting_pool.get(npc_type, greeting_pool["default"]))
    except Exception as e:
        print(f"Error getting greeting: {e}")
        return "Greetings."  # Default greeting in case of error