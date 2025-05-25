import random
import traceback
from ui import UI
from quests import Quest, generate_reward # Import generate_reward instead of QUEST_REWARDS
from items import Item # Import Item class for reward formatting

# Exploration results
EXPLORATION_RESULTS = {
    "city": [
        "You navigate the bustling streets of the city, the air thick with the scent of roasted meats and exotic spices. A Redguard merchant loudly hawks his wares.",
        "A shadowy alley reveals a den of thieves and smugglers. Whispers of skooma and stolen artifacts fill the air.",
        "At the city square, a bard sings a ballad of Talos, his voice echoing through the crowd. A heated debate about the White-Gold Concordat ensues.",
        "You stumble upon the College of Mages, where arcane energies crackle and the air hums with magical potential.",
        "A city guard, clad in steel armor, warns you of a Daedric cult operating within the city walls.",
        "The aroma of sujamma and honeyed bread draws you to a packed tavern, where sailors exchange tales of shipwrecks and krakens.",
        "You overhear a heated argument about trade routes and Imperial taxes at the gates of the Merchant's Guild.",
        "A parade of masked revelers celebrates a Daedric festival, their laughter masking a darker purpose.",
        "In the city's poorest quarter, a priest of Arkay tends to the sick, his face etched with compassion.",
        "You find a hidden garden where a reclusive alchemist cultivates rare Nirnroot, offering cryptic advice about the Dragonborn."
    ],
    "tavern": [
        "Mead sloshes over wooden tables as a bard sings of the Dragonborn; patrons cheer and clap along, inviting you to join the chorus.",
        "A Dunmer gambler invites you to a game of chance, his gold septims glinting as he promises riches—if the dice favor you.",
        "You overhear mercenaries plotting a raid on a nearby bandit camp; their maps are stained with ale and blood.",
        "The barkeep shares a whispered rumor about a hidden treasure in Bleak Falls Barrow, but demands a favor in return.",
        "A serving wench hurriedly presses a note into your hand before disappearing into the kitchen. It speaks of a conspiracy.",
        "A group of traveling minstrels performs a haunting ballad about the Oblivion Crisis.",
        "You find a wall hung with monster trophies—werewolf pelts, giant spider legs, and a troll's skull—each with a tale.",
        "A tipsy scholar insists that the local Jarl is a puppet of the Thalmor. His evidence? A strange tattoo seen after too much Honningbrew mead.",
        "You witness a brawl break out over a game of cards, and the barkeep slips you a healing potion 'just in case.'",
        "A mysterious traveler in a dark cloak offers to trade Dwemer artifacts for any tales of dragon sightings."
    ],
    "forest": [
        "Sunlight dapples the mossy earth as you follow elk tracks past ancient pines and babbling streams.",
        "A sudden hush falls; you spot a circle of standing stones and recall tales of mischievous Spriggans.",
        "You hear faint chanting and discover a coven of witches, their hands raised to the sky in a dark ritual.",
        "A fox darts by, chased by a child with a flower crown—her laughter echoing through the trees.",
        "You find a toppled shrine to Kyne, covered in runes and half-swallowed by the roots of an ancient tree.",
        "A hunter invites you to share his fire and tells of a legendary white stag sacred to Hircine.",
        "You stumble on a ruined cottage, its chimney overgrown with nightshade and its hearth still faintly warm.",
        "Will-o'-the-wisps flicker in a sunlit glade, swirling in intricate patterns as if spelling out a warning.",
        "A sudden rain pelts the canopy, sending you scrambling for shelter under a fallen log.",
        "You follow a songbird to a nest of rare songfinch eggs—a prize for apothecaries, but sacred to local villagers."
    ],
    "plains": [
        "Tall grass sways in endless waves, hiding hares and nesting larks. The sky seems impossibly wide over the Whiterun plains.",
        "You spot a lone mammoth, its massive form outlined against the sunset as it grasps near a stream.",
        "A shepherd greets you, his flock spread over the hills, and shares news of giants sighted near the Pale.",
        "You stumble upon a circle of standing stones, carved with symbols of the Divines and offerings of grain and mead.",
        "A sudden dust devil whirls across your path, and with it, a scrap of a lost Imperial missive bearing the Emperor's seal.",
        "You find an abandoned camp, its fire pit cold and a single septim left behind.",
        "A column of ants carries away crumbs from a sweetroll, a reminder of a recent traveler.",
        "The distant howl of wolves rises on the wind, mingling with the calls of circling hawks.",
        "Wild horses thunder past, their manes streaming and hooves churning up the soft earth.",
        "You find a patch of mountain flowers—rare and said to grant luck if woven into a garland."
    ],
    "cave": [
        "You squeeze through a narrow crevice and emerge into a chamber glittering with amethyst and strange fungi.",
        "A trickle of water echoes, leading you to a pool where blind cavefish dart away from your shadow.",
        "You spot a faded mural painted by ancient Falmer hands, depicting snow elves and forgotten gods.",
        "A cold draft warns of a deeper tunnel where the air hums with an unnatural Dwemer energy.",
        "Scattered bones crunch underfoot—recent, and gnawed as if by something larger than a wolf, perhaps a troll.",
        "A nest of bats stirs, and you duck as they swirl past, their wings beating a frantic rhythm.",
        "You find a pile of discarded mining equipment; among them, a rusted iron sword and a journal describing a doomed expedition for ebony ore.",
        "A tiny, luminescent beetle crawls onto your boot, its shell reflecting shifting colors – a Torchbug.",
        "You hear distant Draugr voices, but when you call out, only the echo answers.",
        "A side passage is blocked by a rockfall, but you glimpse a glint of gold beyond—a lost cache of septims, perhaps?"
    ],
    "ruin": [
        "Crumbling arches frame a courtyard where wildflowers bloom among toppled statues of ancient heroes.",
        "You find a mosaic floor, its tiles faded but still depicting a long-forgotten battle between Nords and Elves.",
        "A hidden alcove contains offerings: septims, dried lavender, and a child’s wooden toy horse.",
        "You hear faint music—a lute's melody drifting from somewhere deeper in the ruins, perhaps a lingering spirit.",
        "An owl blinks at you from a shattered window, feathers dusted with ancient mortar.",
        "You discover a library, its shelves collapsed but a single scroll still intact and sealed with dragon claws.",
        "A spiral staircase leads down into darkness, the air heavy with the scent of damp parchment and decay.",
        "You spot a ghostly warrior who vanishes when you blink, leaving behind only a chill and the whisper of steel.",
        "A sudden breeze scatters leaves across a sunbeam, illuminating faded runes on the wall—a Dragon Shout, perhaps?",
        "You find a silver chalice set atop a stone altar, crusted with dried berries—an offering to a long-forgotten god."
    ],
    "barrow": [
        "The air is cold and thick with the scent of old stone and death. Rows of Draugr sarcophagi line the walls.",
        "You brush past cobwebs to find a mural of armored Nordic warriors ascending to Sovngarde.",
        "A faint blue glow emanates from a crack in the floor—wisp lights, said to guard the slumbering Draugr.",
        "You hear the clatter of bone on bone and freeze; the sound fades, but your heart pounds with dread.",
        "A weathered shield leans against a tomb, inscribed with a family crest you recognize from a local legend of a fallen hero.",
        "You find a rusted lockbox—inside, a faded love letter and a ring of braided silver.",
        "A cold wind extinguishes your torch for a moment, and you sense unseen eyes watching from the darkness.",
        "You spot a tiny door at ankle height, perhaps for offerings to the ancient dead.",
        "You come across a pile of grave goods: septims, carved figurines of the Divines, and a bowl of petrified mammoth cheese.",
        "The ceiling is painted with constellations, some familiar, others lost to the Dragon Cult."
    ],
    "hold": [
        "From a rocky outcrop, you survey the valley—herds of elk, distant lakes, and the glint of snow on the Throat of the World.",
        "A band of Stormcloaks practices swordplay beneath fluttering blue banners, preparing for war against the Empire.",
        "You help a traveler whose cart wheel broke, and she rewards you with a pouch of Elsweyr Fondue.",
        "A local Thane greets you at his campfire and shares news of a giant's recent rampage through a nearby village.",
        "You pass a field of snowberries, their white fruit glistening in the sun.",
        "A pack of wolves circles a lone bull elk, and you watch the drama unfold from a safe distance.",
        "You find a cairn with fresh snowdrops—a memorial to a hero lost in the Great War.",
        "A shepherd’s flute music drifts up the hillside, mingling with the calls of snow hawks.",
        "A sudden blizzard sweeps in, forcing you to seek shelter beneath a rocky overhang.",
        "You discover a hot spring hidden in a hollow, steam rising into the frigid air—a blessing from Mara."
    ],
    "tundra": [
        "The wind howls over the endless snow, and you spot a herd of mammoths lumbering past, their thick fur covered in frost.",
        "A lone sabre cat prowls a frozen riverbank, pausing to drink from a hole in the ice.",
        "You find a cluster of hardy snowdrops poking up through the snow, defying the bitter cold.",
        "A distant aurora shimmers green and violet across the night sky—a sign of magic in the air.",
        "You come across an abandoned hunter's camp, its fire pit choked with snow and its tent collapsed.",
        "The air is so cold your breath crystallizes instantly; you pull your fur cloak tighter around you.",
        "You see a frost troll's tracks and wisely choose another path—the beast is known to be territorial.",
        "A lost Imperial courier stumbles into your camp, desperate for warmth and news of the war.",
        "You discover a half-buried Dragon Mound, its entrance marked with ancient dragon runes.",
        "A flight of snow hawks circles overhead, hunting for unseen prey in the frozen waste."
    ],
    "market": [
        "The air is thick with the scent of spices from Morrowind, roasting meats, and the clamor of merchants hawking their wares.",
        "A juggler performs for a crowd of children, his balls painted with the symbols of the Nine Divines.",
        "A Dunmer merchant offers you a mysterious amulet said to ward off curses—for a hefty price in septims.",
        "You hear a heated argument over a shipment of moon sugar; guards are called, but you slip away unnoticed.",
        "A fortune teller beckons you to her tent, her tarot cards splayed out in patterns foretelling your destiny.",
        "You taste a candied apple, its sweetness offset by a hint of skooma.",
        "A skilled pickpocket tries his luck but is caught by an angry mob and dragged away to the dungeons.",
        "You watch a caged guar from Morrowind on display, its strange cries echoing through the crowd.",
        "An old woman sells hand-woven tapestries, each depicting a scene from the life of Tiber Septim.",
        "You spot a rare book dealer displaying a tome bound in dragon hide, its pages glowing faintly with magic."
    ],
    "inn": [
        "A roaring fire warms the common room, where a bard’s lute music draws smiles from weary travelers.",
        "You sip spiced wine and listen to a Nord warrior recount his battles with the Thalmor.",
        "A pair of adventurers compare scars earned in ancient ruins, their laughter rising above the clinking of mugs.",
        "The innkeeper discreetly asks if you’re seeking honest work—or something a little more… lucrative.",
        "You find a guestbook filled with cryptic signatures and coded messages hinting at a secret society.",
        "A Khajiit cat naps on the hearthrug, opening one eye to watch your every move with feline suspicion.",
        "The aroma of fresh bread draws you to the kitchen, where the cook offers you a taste in exchange for gossip about the Jarl.",
        "You discover a hidden door behind a bookcase, leading to a smuggler’s tunnel.",
        "A mysterious guest in a velvet cloak asks pointed questions about your knowledge of the Dark Brotherhood.",
        "You find a lost gauntlet embroidered with the crest of a noble family, tucked beneath a bench."
    ],
    "desert": [
        "Blinding sunlight reflects off endless dunes, and the heat shimmers on the horizon of Elsweyr.",
        "You find the skeleton of a senche-raht, half-buried by blowing sand and picked clean by carrion birds.",
        "A Khajiit nomad offers you a sip of cactus juice and shares a story of a lost oasis blessed by Jone and Jode.",
        "You stumble across an oasis, its date palms heavy with fruit and its waters icy cool—a gift from the moons.",
        "A sandstorm whips up suddenly, forcing you to seek shelter behind a crumbling statue of a Khajiit god.",
        "At twilight, the desert comes alive with strange calls—jackals, sand cats, and the whispers of the Anequina spirits.",
        "You spot a caravan in the distance, its guar laden with moon sugar and shimmering silks.",
        "A mirage dances before your eyes, promising water and shade that vanish as you approach—a trick of the desert.",
        "You discover ancient Khajiit petroglyphs carved into a red sandstone cliff, depicting the Mane and his protectors.",
        "The night sky is a tapestry of stars, brighter and closer than anywhere else you've traveled—a window to Aetherius."
    ],
    "river": [
        "The river’s song is ever-present, its waters sparkling with sunlight on the banks of Skyrim's White River.",
        "A fisherman waves from his boat and offers you a freshly caught salmon in exchange for a tale of your adventures.",
        "Dragonflies skim the surface, their wings glittering like polished glass.",
        "You find a smooth stone covered in ancient runes—perhaps a marker for a sunken Dwemer ruin?",
        "A family of otters plays in the shallow, sliding over mossy rocks and chasing after silverfish.",
        "You cross a rickety wooden bridge and feel it sway alarmingly beneath your feet, threatening to plunge you into the icy water.",
        "A ferryman offers passage downstream to Riften, his price a handful of septims.",
        "You spot tracks of a giant mudcrab and hear rumors of a monstrous Slaughterfish lurking in the depths.",
        "A willow tree’s roots create a tangle of hiding places for small fish and lost treasures.",
        "You fill your waterskin with icy water and find it refreshes you more than any potion—a gift from the river."
    ],
    "farm": [
        "Golden fields of wheat ripple in the breeze, and the air is thick with the scent of freshly cut hay at Pelagia Farm.",
        "You help a farmer mend a broken fence, earning a wedge of Jarrin Root cheese and a grateful smile.",
        "A scarecrow with a spriggan perched on its shoulder seems to watch your every move with eerie intelligence.",
        "Children chase a runaway cluckshroom through rows of cabbages and leeks.",
        "You stumble on a patch of wild huckleberries, sweet and sun-warmed.",
        "A barn cat presents you with a vole, proud of its hunting prowess.",
        "You hear the rhythmic thud of a millstone grinding wheat into flour at the nearby mill.",
        "The farmer’s wife offers you a cup of warm milk and news of a missing cow.",
        "A weathered wind vane creaks atop a red-tiled roof, always pointing towards the Throat of the World.",
        "You find a patch of blue mountain flowers, rumored to keep away evil spirits and bless the harvest."
    ],
    "village": [
        "Thatched cottages cluster around a well where villagers gather to share news and gossip in Riverwood.",
        "You meet a blacksmith who displays a sword said to be forged from meteoric iron.",
        "Children play tag among stacks of firewood, their laughter ringing across the village green.",
        "An old woman offers you a charm to keep away ill fortune, if you’ll listen to her rambling stories.",
        "You witness a lively harvest festival, with dancers in colorful attire and the scent of roasted pheasant.",
        "A dog leads you to a hidden garden behind the mill, filled with rare herbs used by the village apothecary.",
        "The village priest invites you into the local chapel where candles flicker before the shrine of Arkay.",
        "A group of elders debates the best way to deal with wolves spotted near the sheep pens.",
        "You find a bundle of love letters hidden in a hollow tree, tied with a ribbon.",
        "A traveling tinker sharpens your blade for a song and a flagon of ale."
    ],
    "mine": [
        "The air is thick with dust and the clang of pickaxes echoes through the tunnels of Kolskeggr Mine.",
        "You pass miners singing a Dwarven work song, their faces smudged with soot and grime.",
        "A cart rumbles past, heaped with glittering gold ore and guarded by a surly foreman.",
        "You find a rusty miner's helmet, its crest barely visible beneath the grime.",
        "A small lizard scurries away as you step over a trickle of water flowing through the mine.",
        "You discover a lantern swinging from a nail, its flame flickering in the damp air.",
        "A collapsed shaft blocks your way, but a faint draft hints at a hidden passage beyond.",
        "You overhear a heated argument about someone stealing gold from the mine's cache.",
        "A miner offers to sell you a chunk of raw malachite crystal said to contain magical energy.",
        "You glimpse a shadowy figure flitting just out of sight, deeper in the mine—perhaps a ghost or a Falmer?"
    ],
    "camp": [
        "A ring of tents surrounds a crackling campfire where adventurers trade boasts and share dried venison.",
        "You help pitch a tent and earn a tale about the haunted ruins of Labyrinthian.",
        "A scout returns with news of a dragon sighted near the Throat of the World.",
        "You find a forgotten journal filled with maps and coded entries hinting at a lost treasure.",
        "A healer tends to a sprained ankle and offers you a vial of potent healing salve.",
        "You listen to a tale of forbidden love and a promise to return home after one last perilous quest.",
        "The camp’s cook invites you to taste his famous mammoth stew.",
        "A game of stones and knucklebones draws laughter and friendly wagers around the fire.",
        "A sentry spots a shooting star and insists it’s a sign of good fortune.",
        "You find a pouch of ancient Dwemer coins beneath your sleeping mat."
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

def trigger_random_event(location_tags, player, UI, current_location): # Added current_location as an argument
    """Triggers a random event based on location tags."""
    event = None  # Initialize event to None
    try:
        possible_events = []
        for tag in location_tags:
            if tag in RANDOM_EVENTS:
                possible_events.extend(RANDOM_EVENTS[tag])

        if possible_events and random.random() < 0.6: # Chance to trigger an event, not always
            event = random.choice(possible_events)
            UI.slow_print(event["description"])

            if event["type"] == "item":
                try:
                    from items import Item
                    # Create a placeholder Item object
                    item = Item(
                        name=event["item"],
                        category="misc", # Default category
                        material="common", # Default material
                        weight=1.0,  # Default weight
                        value=10     # Default value
                    )
                    UI.slow_print(f"You receive: {item.name}")
                    if hasattr(player, "inventory") and player.inventory is not None:
                        player.inventory.append(item)
                        # No longer need to manually update carry_weight here, Stats handles it
                    else:
                        UI.slow_print("You have no place to store this item.")
                except ImportError:
                    # Fallback if Item class is unavailable
                    UI.slow_print(f"You receive: {event['item']} (cannot store due to missing inventory system)")
            elif event["type"] == "quest":
                # Generate a quest using the new diversified reward structure
                # Pass player.level and location_tags to generate_reward
                quest_reward_dict = generate_reward(player.level, location_tags)
                
                quest = Quest(
                    title="A Random Opportunity", # Generic title for random quests
                    description=event["quest"],
                    reward=quest_reward_dict, # Pass the reward dictionary
                    level_requirement=player.level,
                    location={"name": current_location['name'], "tags": location_tags}, # Use the passed current_location argument
                    completion_condition="random_event_quest" # Generic completion condition
                )
                UI.slow_print(f"New quest: {quest.description}")
                # Format reward display similarly to look_around_area for consistency
                reward_parts = []
                for r_type, r_value in quest.reward.items():
                    if isinstance(r_value, Item):
                        reward_parts.append(f"{r_value.name} (Item)")
                    else:
                        reward_parts.append(f"{r_value} {r_type.capitalize()}")
                UI.slow_print(f"Reward: {', '.join(reward_parts)}")

                if hasattr(player, "quest_log") and player.quest_log is not None:
                    player.quest_log.add_quest(quest)
                else:
                    UI.slow_print("You have no way to track this quest.")
        # Only print "Nothing unusual happens today" if no event was chosen or found
        elif not event:
            UI.slow_print("Nothing unusual happens today.")
        return event
    except Exception as e:
        traceback.print_exc()
        pass
