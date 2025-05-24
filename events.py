import random
import traceback
from ui import UI
from quests import Quest, QUEST_REWARDS

# Exploration results
EXPLORATION_RESULTS = {
    "city": [
        "You navigate bustling streets where merchants loudly peddle wares and nobles glide past in silks, the clang of a distant blacksmith punctuating the city’s heartbeat.",
        "A hidden alley reveals a world apart—smugglers, thieves, and mysterious painted doors. Whispers of forbidden goods and secret societies abound.",
        "At the city square, performers juggle and play flutes while children dart between fountains, and rumors of a council scandal reach your ears.",
        "You stumble into a grand library, sunlight streaming through stained glass onto tomes of forbidden magic and dynastic history.",
        "A city guard in gleaming armor warns you of recent disappearances, his eyes darting nervously toward the shadowed southern gate.",
        "The aroma of spiced meats and fresh bread draws you to a packed tavern, where sailors exchange tales of sea serpents and lost cargo.",
        "You overhear a heated argument about taxes and trade embargoes at the gates to the merchant’s guild.",
        "A parade of masked revelers swirls past, their laughter hiding a deeper conspiracy that you sense but cannot yet grasp.",
        "In the city’s poorest quarter, you see a healer tending to the sick, and a grateful crowd murmurs prayers.",
        "You find a rooftop garden where a reclusive mage tends rare flowers, offering cryptic advice about the city’s fate"
    ],
    "tavern": [
        "Ale sloshes over wooden tables as a bard sings of long-lost heroes; regulars cheer and clap along, inviting you to join the chorus.",
        "A shadowy gambler invites you to a dice game, his gold teeth glinting as he promises fortune—if the cards favor you.",
        "You overhear mercenaries plotting a midnight heist against a rival inn; their maps are inked with the city’s secrets.",
        "The barkeep shares a whispered rumor about a secret passage in the cellar, but demands a favor in return.",
        "A serving maid hurriedly presses a cryptic note into your hand before vanishing into the kitchen.",
        "A group of traveling minstrels tries out a new, haunting ballad that seems to reference recent events in town.",
        "You find a wall hung with monster trophies—werewolf pelts, giant claws, and a frost troll’s tusk—each with a tale.",
        "A tipsy scholar insists that the local lord is not who he claims. His evidence? A strange birthmark seen after too much wine.",
        "You witness a brawl break out over an unpaid debt, and the barkeep quietly slips you a healing potion 'just in case.'",
        "A mysterious traveler in a broad hat offers to trade rare spices for any tales of haunted ruins you might know"
    ],
    "forest": [
        "Sunlight dapples the mossy earth as you follow deer tracks past ancient oaks and burbling brooks.",
        "A sudden hush falls; you spot a ring of mushrooms and recall tales of mischievous forest spirits.",
        "You hear faint chanting and discover a druidic circle, their hands raised to the sky in silent prayer.",
        "A fox darts by, chased by a child with a woven flower crown—her laughter echoing through the trees.",
        "You find a toppled pillar covered in runes, half-swallowed by the roots of a massive yew.",
        "A hunter invites you to share his fire and tells of a white stag said to grant wishes.",
        "You stumble on a ruined cottage, its chimney overgrown with wild roses and its hearth still faintly warm.",
        "Fireflies gather in a sunlit glade, swirling in intricate patterns as if spelling out a message.",
        "A sudden rain pelts the canopy, sending you scrambling for shelter under a broad-leaved fern.",
        "You follow a songbird to a nest of rare eggs—a prize for apothecaries, but sacred to local villagers."
    ],
    "plains": [
        "Tall grass sways in endless waves, hiding hares and nesting larks. The sky seems impossibly wide.",
        "You spot a lone bison, its massive form outlined against the sunset as it grazes near a shallow stream.",
        "A shepherd greets you, his flock spread over the hills, and shares news of a storm brewing to the west.",
        "You stumble upon a ring of standing stones, carved with sun symbols and offerings of grain.",
        "A sudden dust devil whirls across your path, and with it, a scrap of a lost letter bearing a royal seal.",
        "You find an abandoned camp, its fire pit cold and a single silver coin left behind.",
        "A column of ants carries away crumbs from a half-eaten pastry, a reminder of a recent traveler.",
        "The distant howl of wolves rises on the wind, mingling with the calls of circling hawks.",
        "Wild horses thunder past, their manes streaming and hooves churning up the soft earth.",
        "You find a patch of blue wildflowers—rare and said to grant luck if braided into your hair."
    ],
    "cave": [
        "You squeeze through a narrow crevice and emerge into a chamber glittering with quartz and strange fungi.",
        "A trickle of water echoes, leading you to a pool where blind fish dart away from your shadow.",
        "You spot a faded mural painted by ancient hands, depicting hunters and what might be dragons.",
        "A cold draft warns of a deeper tunnel where the air hums with an unnatural energy.",
        "Scattered bones crunch underfoot—recent, and gnawed as if by something larger than a wolf.",
        "A nest of bats stirs, and you duck as they swirl past, their wings beating a frantic rhythm.",
        "You find a pile of discarded equipment; among them, a rusted sword and a journal describing a doomed expedition.",
        "A tiny, luminescent beetle crawls onto your boot, its shell reflecting shifting colors.",
        "You hear distant voices, but when you call out, only the echo answers.",
        "A side passage is blocked by a rockfall, but you glimpse a glint of metal beyond—a lost treasure, perhaps?"
    ],
    "ruin": [
        "Crumbling arches frame a courtyard where wildflowers bloom among toppled statuary.",
        "You find a mosaic floor, its tiles faded but still depicting a long-forgotten battle.",
        "A hidden alcove contains offerings: coins, dried flowers, and a child’s wooden toy.",
        "You hear faint music—a lyre’s melody drifting from somewhere deeper in the ruins.",
        "An owl blinks at you from a shattered window, feathers dusted with ancient mortar.",
        "You discover a library, its shelves collapsed but a single scroll still intact and sealed.",
        "A spiral staircase leads down into darkness, the air heavy with the scent of damp parchment.",
        "You spot a ghostly figure who vanishes when you blink, leaving behind only a chill.",
        "A sudden breeze scatters leaves across a sunbeam, illuminating faded runes on the wall.",
        "You find a silver goblet set atop a stone altar, crusted with dried berries—an offering to something old."
    ],
    "barrow": [
        "The air is cold and thick with the scent of old stone. Rows of carved sarcophagi line the walls.",
        "You brush past cobwebs to find a mural of armored warriors ascending to the afterlife.",
        "A faint blue glow emanates from a crack in the floor—wisp lights, said to guard the slumbering dead.",
        "You hear the clatter of bone on bone and freeze; the sound fades, but your heart pounds.",
        "A weathered shield leans against a tomb, inscribed with a family crest you recognize from a local legend.",
        "You find a rusted lockbox—inside, a faded love letter and a ring of braided copper.",
        "A cold wind extinguishes your torch for a moment, and you sense unseen eyes watching.",
        "You spot a tiny door at ankle height, perhaps for a long-forgotten burial custom.",
        "You come across a pile of offerings: coins, carved figurines, and a bowl of salt.",
        "The ceiling is painted with constellations, some familiar, others lost to time."
    ],
    "hold": [
        "From a rocky outcrop, you survey the valley—herds of elk, distant lakes, and the glint of snow on distant peaks.",
        "A band of Stormcloaks practices swordplay beneath fluttering blue banners.",
        "You help a traveler whose cart wheel broke, and she rewards you with a pouch of sweetmeats.",
        "A local thane greets you at his campfire and shares news of a giant’s recent rampage.",
        "You pass a field of wild flax, its blue blossoms nodding in the wind.",
        "A pack of wolves circles a lone bull, and you watch the drama unfold from a safe distance.",
        "You find a cairn with fresh flowers—a memorial to a hero lost in the last war.",
        "A shepherd’s pipe music drifts up the hillside, mingling with the calls of distant hawks.",
        "A sudden rainstorm sweeps in, forcing you to seek shelter beneath a rocky overhang.",
        "You discover a hot spring hidden in a hollow, steam rising into the cold air."
    ],
    "tundra": [
        "The wind howls over the endless snow, and you spot a herd of mammoths lumbering past, their wool thick and frost-laden.",
        "A lone saber cat prowls a frozen riverbank, pausing to drink from a hole in the ice.",
        "You find a cluster of hardy blue flowers poking up through the snow, defying the bitter cold.",
        "A distant aurora shimmers green and violet across the night sky.",
        "You come across an abandoned camp, its fire pit choked with snow and its tent collapsed.",
        "The air is so cold your breath crystallizes instantly; you wrap your cloak tighter.",
        "You see a frost troll’s tracks and wisely choose another path.",
        "A lost Imperial courier stumbles into your camp, desperate for warmth and news.",
        "You discover a half-buried barrow, its entrance marked with ancient runes.",
        "A flight of white hawks circles overhead, hunting for unseen prey."
    ],
    "market": [
        "The air is thick with spices, roasting meats, and laughter as vendors hawk their exotic wares.",
        "A juggler performs for a crowd of children, his balls painted with the colors of distant lands.",
        "A merchant offers you a mysterious amulet, swearing it wards off curses—at a generous price.",
        "You hear a heated argument over a shipment of moon sugar; guards are called, but you slip away unnoticed.",
        "A fortune teller beckons you to her tent, her cards splayed out in a pattern you’ve never seen.",
        "You taste a candied apple, its sweetness offset by a hint of unfamiliar spice.",
        "A pickpocket tries his luck but is caught by an angry mob.",
        "You watch a rare animal—perhaps a tiny dragon?—on display in a gilded cage.",
        "An old woman sells hand-woven blankets, each with a story stitched in colored thread.",
        "You spot a rare book dealer displaying a tome that glows faintly in the twilight."
    ],
    "inn": [
        "A roaring fire warms the common room, where a bard’s music draws out smiles from even the grumpiest patrons.",
        "You sip mulled wine and listen to a merchant recount his harrowing journey through wolf-infested woods.",
        "A pair of adventurers compare scars, their laughter rising above the clink of mugs.",
        "The innkeeper discreetly asks if you’re seeking honest work—or something riskier.",
        "You find a guestbook filled with cryptic signatures and coded messages.",
        "A cat naps on the hearthrug, opening one eye to watch your every move.",
        "The aroma of fresh bread draws you to the kitchen, where the cook offers you a taste in exchange for news.",
        "You discover a secret door behind a bookcase, leading to a small, dusty storeroom.",
        "A mysterious guest in a velvet cloak asks pointed questions about local legends.",
        "You find a lost glove embroidered with a noble family’s crest, tucked beneath a bench."
    ],
    "desert": [
        "Blinding sunlight reflects off endless dunes, and the heat shimmers on the horizon.",
        "You find the skeleton of a camel, half-buried by blowing sand and picked clean by vultures.",
        "A nomad offers you a sip of pungent tea and shares a story of a lost city swallowed by the sands.",
        "You stumble across an oasis, its palm trees heavy with dates and its waters icy cool.",
        "A sandstorm whips up suddenly, forcing you to shelter behind a crumbling statue.",
        "At twilight, the desert comes alive with strange calls—jackals, owls, and something you cannot name.",
        "You spot a caravan in the distance, its camels laden with bolts of cloth and jars of spices.",
        "A mirage dances before your eyes, promising water and shade that vanish as you approach.",
        "You discover ancient petroglyphs carved into a red sandstone cliff.",
        "The night sky is a tapestry of stars, brighter and closer than anywhere else you've traveled."
    ],
    "river": [
        "The river’s song is ever-present, its waters sparkling with reflected sunlight.",
        "A fisherman waves from his boat and offers you a freshly caught trout in exchange for a tale.",
        "Dragonflies skim the surface, their wings glittering blue and gold.",
        "You find a smooth stone covered in ancient carvings—perhaps a marker for lost treasure?",
        "A family of otters plays in the shallows, sliding over mossy rocks.",
        "You cross a rickety wooden bridge and feel it sway alarmingly beneath your feet.",
        "A ferryman offers passage downstream, his price a single silver coin.",
        "You spot tracks of a giant mudcrab and hear rumors of a creature known as 'The River King.'",
        "A willow tree’s roots create a tangle of hiding places for small fish and lost trinkets.",
        "You fill your flask with icy water and find it refreshes you more than any potion."
    ],
    "farm": [
        "Golden fields of wheat ripple in the breeze, and the air is thick with the scent of hay.",
        "You help a farmer mend a broken fence, earning a wedge of sharp cheese and a grateful smile.",
        "A scarecrow with a crow perched on its shoulder seems to watch your every move.",
        "Children chase a runaway piglet through rows of carrots and beans.",
        "You stumble on a patch of wild strawberries, sweet and sun-warmed.",
        "A barn cat presents you with a mouse, proud of her hunting prowess.",
        "You hear the rhythmic thud of a millstone grinding grain in the distance.",
        "The farmer’s wife offers you a cup of fresh milk and news of a missing calf.",
        "A weathered wind vane creaks atop a red-tiled roof, pointing always north.",
        "You find a patch of blue cornflowers, rumored to keep evil spirits at bay."
    ],
    "village": [
        "Thatched cottages cluster around a well where villagers gather to share news and laughter.",
        "You meet a blacksmith who displays a sword said to be forged from a fallen star.",
        "Children play tag among stacks of firewood, their laughter ringing across the green.",
        "An old woman offers you a charm to keep away bad luck—if you’ll listen to her story.",
        "You witness a lively festival, with dancers in colorful ribbons and the scent of roasting meat.",
        "A dog leads you to a hidden garden behind the mill, filled with rare herbs.",
        "The village priest invites you into a chapel where candles flicker on ancient stone.",
        "A group of elders debates the best way to deal with wolves spotted near the sheepfold.",
        "You find a bundle of love letters hidden in a hollow tree.",
        "A traveling tinker sharpens your blade for a song."
    ],
    "mine": [
        "The air is thick with dust and the clang of pickaxes echoes through winding tunnels.",
        "You pass miners singing a work song, their faces smudged with soot.",
        "A cart rumbles past, heaped with glittering ore and guarded by a wary overseer.",
        "You find a rusty helmet, its crest still visible beneath the grime.",
        "A small lizard scurries away as you step over a trickle of water.",
        "You discover a lantern swinging from a nail, its flame stubbornly resisting the damp.",
        "A collapsed shaft blocks your way, but a faint draft hints at a hidden passage.",
        "You overhear a heated argument about missing gold.",
        "A miner offers to sell you a chunk of raw crystal said to contain magical energy.",
        "You glimpse a mysterious shadow flitting just out of sight, deeper in the mine."
    ],
    "camp": [
        "A ring of tents surrounds a crackling fire where adventurers trade boasts and share dried meat.",
        "You help pitch a tent and earn a story about the haunted keep nearby.",
        "A scout returns with news of a wolf pack spotted upriver.",
        "You find a forgotten journal filled with maps and coded entries.",
        "A healer tends to a sprained ankle and offers you a vial of herbal salve.",
        "You listen to a tale of lost love and a promise to return home after one last quest.",
        "The camp’s cook invites you to taste his famous rabbit stew.",
        "A game of stones and knucklebones draws laughter and friendly wagers.",
        "A sentry spots a shooting star and insists it’s a sign of good luck.",
        "You find a pouch of ancient coins beneath your sleeping mat."
    ]
}

# Dungeon names
DUNGEON_NAMES = ["Bleak Falls Barrow", "Dustman's Cairn", "Embershard Mine", "White River Watch", "Halted Stream Camp"]

# Specific location tags
SPECIFIC_LOCATION_TAGS = [
    "tavern", "inn", "market", "farm", "mine", "camp", "barrow", "ruin", "cave", "library"
]

# Random events
RANDOM_EVENTS = {
    "city": [
        {"type": "flavor", "description": "A street performer juggles flaming torches to the delight of onlookers."},
        {"type": "flavor", "description": "A heated political debate erupts between two well-dressed citizens."},
        {"type": "item", "description": "A clumsy merchant accidentally drops a valuable gem. You discreetly pocket it.", "item": "Small Gem"},
        {"type": "quest", "description": "A worried mother asks you to find her missing child, last seen near the market.", "quest": "Find the missing child"}
    ],
    "nord": [
        {"type": "flavor", "description": "A group of Nords boast loudly about their exploits in battle."},
        {"type": "flavor", "description": "A lone warrior sharpens their axe, their eyes fixed on the horizon."},
        {"type": "item", "description": "A friendly Nord offers you a swig of potent ale.", "item": "Bottle of Nord Ale"},
        {"type": "quest", "description": "A Nord asks for help protecting their farm from wild animals.", "quest": "Protect the farm from wild animals"}
    ],
    "trade": [
        {"type": "flavor", "description": "A Khajiit caravan arrives, their wares exotic and enticing."},
        {"type": "flavor", "description": "A tense negotiation takes place between two rival merchant guilds."},
        {"type": "item", "description": "A grateful merchant gifts you a discount on a rare item.", "item": "Discount Voucher"},
        {"type": "quest", "description": "A merchant seeks protection from bandits while traveling to a neighboring town.", "quest": "Escort the merchant to the neighboring town"}
    ],
    "thieves": [
        {"type": "flavor", "description": "A hooded figure whispers secrets in a dark alleyway."},
        {"type": "flavor", "description": "You spot a skilled pickpocket relieving a wealthy noble of their purse."},
        {"type": "item", "description": "You stumble upon a hidden stash containing a set of lockpicks.", "item": "Set of Lockpicks"},
        {"type": "quest", "description": "A mysterious contact offers you a lucrative but dangerous job.", "quest": "Complete the dangerous job"}
    ],
    "dwemer": [
        {"type": "flavor", "description": "A faint humming sound emanates from deep within the ruins."},
        {"type": "flavor", "description": "You discover a deactivated Dwemer automaton, its gears still gleaming."},
        {"type": "item", "description": "You find a curious Dwemer cogwheel, its purpose unknown.", "item": "Dwemer Cogwheel"},
        {"type": "quest", "description": "A scholar seeks your help in exploring a newly discovered Dwemer ruin.", "quest": "Explore the Dwemer ruin"}
    ],
    "forsworn": [
        {"type": "flavor", "description": "A group of Forsworn warriors perform a ritual dance around a bonfire."},
        {"type": "flavor", "description": "You overhear whispers of rebellion and hatred for the Nords."},
        {"type": "item", "description": "You find a crudely fashioned Forsworn amulet, adorned with feathers and bones.", "item": "Forsworn Amulet"},
        {"type": "quest", "description": "A Forsworn leader asks for your assistance in attacking a Nord settlement.", "quest": "Attack the Nord settlement"}
    ],
    "temple": [
        {"type": "flavor", "description": "A soothing hymn fills the air as worshippers gather to pray."},
        {"type": "flavor", "description": "A priestess offers guidance and blessings to those in need."},
        {"type": "item", "description": "You receive a blessed amulet, said to ward off evil spirits.", "item": "Blessed Amulet"},
        {"type": "quest", "description": "The temple requires assistance in recovering a stolen artifact from bandits.", "quest": "Recover the stolen artifact"}
    ],
    "vampire": [
        {"type": "flavor", "description": "A chill runs down your spine as you sense an unnatural presence nearby."},
        {"type": "flavor", "description": "You notice a group of pale-faced individuals lurking in the shadows."},
        {"type": "item", "description": "You find a vial of mysterious crimson liquid.", "item": "Vial of Crimson Liquid"},
        {"type": "quest", "description": "A desperate villager begs you to investigate a series of strange disappearances.", "quest": "Investigate the disappearances"}
    ],
    "mountain": [
        {"type": "flavor", "description": "The wind howls through the peaks, carrying the scent of snow and pine."},
        {"type": "flavor", "description": "You spot a lone mountain goat skillfully navigating the treacherous terrain."},
        {"type": "item", "description": "You discover a rare herb with potent healing properties.", "item": "Rare Healing Herb"},
        {"type": "quest", "description": "A hermit living in the mountains asks for help retrieving a lost artifact.", "quest": "Retrieve the lost artifact"}
    ],
    "inn": [
        {"type": "flavor", "description": "The warm fire crackles merrily, filling the room with a cozy glow."},
        {"type": "flavor", "description": "A bard strums a lively tune, encouraging patrons to sing and dance."},
        {"type": "item", "description": "The innkeeper offers you a complimentary meal and a warm bed.", "item": "Free Meal and Bed"},
        {"type": "quest", "description": "The innkeeper needs help dealing with a group of rowdy mercenaries.", "quest": "Deal with the rowdy mercenaries"}
    ],
    "undead": [
        {"type": "flavor", "description": "A chilling moan echoes through the ancient crypt."},
        {"type": "flavor", "description": "You stumble upon a skeletal warrior, guarding its eternal resting place."},
        {"type": "item", "description": "You find a rusty sword, once wielded by a valiant warrior.", "item": "Rusty Sword"},
        {"type": "quest", "description": "A restless spirit seeks your help in finding peace.", "quest": "Help the restless spirit find peace"}
    ],
    "blades": [
        {"type": "flavor", "description": "A member of the Blades speaks of ancient prophecies and the return of dragons."},
        {"type": "flavor", "description": "You overhear whispers of a secret mission to protect the Dragonborn."},
        {"type": "item", "description": "A Blades agent provides you with a potion to resist dragon fire.", "item": "Potion of Dragon Resistance"},
        {"type": "quest", "description": "The Blades need your help in locating a hidden dragon lair.", "quest": "Locate the hidden dragon lair"}
    ],
    "marsh": [
        {"type": "flavor", "description": "The air hangs heavy with the scent of damp earth and decaying vegetation."},
        {"type": "flavor", "description": "Strange lights flicker in the distance, leading travelers astray."},
        {"type": "item", "description": "You find a rare mushroom with potent magical properties.", "item": "Rare Marsh Mushroom"},
        {"type": "quest", "description": "A villager asks for help retrieving a lost artifact from the depths of the swamp.", "quest": "Retrieve the lost artifact from the swamp"}
    ],
    "forest": [
        {"type": "flavor", "description": "Sunlight filters through the dense canopy, creating an ethereal glow."},
        {"type": "flavor", "description": "The sounds of birds and rustling leaves fill the air."},
        {"type": "item", "description": "You find a perfectly crafted hunting bow leaning against a tree.", "item": "Hunting Bow"},
        {"type": "quest", "description": "A hunter seeks your help in tracking a dangerous beast that has been terrorizing the local wildlife.", "quest": "Track and defeat the dangerous beast"}
    ],
    "cave": [
        {"type": "flavor", "description": "The air is cold and damp, and the only light comes from your torch."},
        {"type": "flavor", "description": "You hear the dripping of water and the skittering of unseen creatures."},
        {"type": "item", "description": "You discover a vein of valuable ore embedded in the cave wall.", "item": "Valuable Ore"},
        {"type": "quest", "description": "A miner asks for your help in clearing out a cave infested with goblins.", "quest": "Clear out the goblin-infested cave"}
    ],
    "desert": [
        {"type": "flavor", "description": "The sun beats down mercilessly, and the sand stretches endlessly in every direction."},
        {"type": "flavor", "description": "You spot a mirage shimmering on the horizon, offering false hope of water and shade."},
        {"type": "item", "description": "You find a sturdy waterskin, abandoned by a long-lost traveler.", "item": "Waterskin"},
        {"type": "quest", "description": "A caravan leader asks for your help in navigating the treacherous desert terrain.", "quest": "Help the caravan navigate the desert"}
    ]
}

def explore_location(player, current_location, random_encounters, npc_registry, LOCATIONS, UI):
    """Explores the current location and triggers random events based on its tags."""
    try:
        UI.slow_print(f"You carefully explore {current_location['name']}...")

        present_specific_tags = [tag for tag in current_location["tags"] if tag in SPECIFIC_LOCATION_TAGS]
        available_results = []

        # Prefer results from specific tags (like tavern, inn, market, etc.)
        if present_specific_tags:
            for tag in present_specific_tags:
                if tag in EXPLORATION_RESULTS:
                    available_results.extend(EXPLORATION_RESULTS[tag])
        else:
            # If no specific tags, fall back to general tags
            for tag in current_location["tags"]:
                if tag in EXPLORATION_RESULTS:
                    available_results.extend(EXPLORATION_RESULTS[tag])

        # If still nothing, fall back to city/town/village if possible
        if not available_results:
            for fallback_tag in ["city", "town", "village"]:
                if fallback_tag in current_location["tags"] and fallback_tag in EXPLORATION_RESULTS:
                    available_results.extend(EXPLORATION_RESULTS[fallback_tag])

        num_results = min(2, len(available_results))
        if available_results:
            selected_results = random.sample(available_results, num_results)
            for result in selected_results:
                UI.slow_print(result)
                if "nearby dungeon" in result:
                    dungeon_name = random.choice(DUNGEON_NAMES)
                    UI.slow_print(f"You learn about a dungeon called {dungeon_name}.")
                    dungeon_location = next((loc for loc in LOCATIONS if loc["name"] == dungeon_name), None)
                    if dungeon_location:
                        from game import known_locations
                        known_locations.add(dungeon_location["id"])
                        UI.slow_print(f"{dungeon_name} has been marked on your map.")
        else:
            UI.slow_print("You find nothing out of the ordinary.")

        UI.press_enter()
    except Exception as e:
        print(f"Error in explore_location: {e}")
        import traceback
        traceback.print_exc()

def trigger_random_event(location_tags, player, UI):
    """Triggers a random event based on location tags."""
    try:
        possible_events = []
        for tag in location_tags:
            if tag in RANDOM_EVENTS:
                possible_events.extend(RANDOM_EVENTS[tag])

        if possible_events:
            event = random.choice(possible_events)
            UI.slow_print(event["description"])

            if event["type"] == "item":
                try:
                    from items import Item
                    # Create a placeholder Item object
                    item = Item(
                        name=event["item"],
                        weight=1.0,  # Default weight
                        value=10     # Default value
                    )
                    UI.slow_print(f"You receive: {item.name}")
                    if hasattr(player, "inventory") and player.inventory is not None:
                        player.inventory.append(item)
                        if hasattr(player.stats, "carry_weight"):
                            player.stats.carry_weight += item.weight
                    else:
                        UI.slow_print("You have no place to store this item.")
                except ImportError:
                    # Fallback if Item class is unavailable
                    UI.slow_print(f"You receive: {event['item']} (cannot store due to missing inventory system)")
            elif event["type"] == "quest":
                # Create a Quest object with a proper reward
                reward_type = random.choice(list(QUEST_REWARDS.keys()))
                reward = random.choice(QUEST_REWARDS[reward_type])
                quest = Quest(
                    quest_type="misc",
                    description=event["quest"],
                    reward=reward,
                    location_tags=location_tags
                )
                UI.slow_print(f"New quest: {quest.description}")
                if hasattr(player, "quest_log") and player.quest_log is not None:
                    player.quest_log.add_quest(quest)
                else:
                    UI.slow_print("You have no way to track this quest.")
        else:
            UI.slow_print("Nothing unusual happens today.")
        return event
    except Exception as e:
        UI.slow_print(f"Error in trigger_random_event: {e}")
        traceback.print_exc()
        return None