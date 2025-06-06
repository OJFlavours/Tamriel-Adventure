# npc_roles.py

# Define roles that imply noble or commoner status
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess", "court_mage", "advisor"}
COMMONER_ROLES = {
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "stormcloak_supporter", "imperial_citizen", "mage_apprentice", "warrior",
    "thief_lookout", "pickpocket", "guild_rogue", "db_initiate",
    "explorer", "sailor", "dock_worker", "ship_captain_ashore", "fishmonger", "acolyte", "temple_guardian",
    "stall_owner", "shop_assistant", "city_guard", "mine_foreman", "farmer_spouse",
    "server", "cook", "beggar", "elder", "stormcloak_recruiter", "imperial_deserter", "publican", "tavern_staff_server", "mine_owner", "alchemist_merchant", "jarl_advisor", "blacksmith_spouse", "jarl_stormcloak", "merchant_general_goods", "blacksmith", "blacksmith_trainer", "alchemist_apprentice", "untalented_bard", "mage_conjurer_scholar_vampire_expert", "merchant_clothing_tailor_haughty", "merchant_fletcher", "shop_assistant_woodcutter", "merchant_clothing_tailor", "stormcloak_officer", "jarl", "thane", "blacksmith_spouse", "bard_local", "mine_patron"
}

# Define roles that are typically hostile
HOSTILE_ROLES = {
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "vampire", "vampire_thrall", "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thief",
    "draugr", "skeleton", "ghost",
    "bear", "wolf", "spider",
    "dwarven_sphere", "falmer", "chaurus",
    "mage", "cultist", "thalmor_justiciar", "dominion_spy"
}

FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES

def add_fixed_npc(npc_registry, location_id, npc_name, npc_race, npc_role, npc_level):
    """Adds a fixed NPC to a specific location."""
    from npc import NPC  # Import here to avoid circular dependency
    new_npc = NPC(name=npc_name, race=npc_race, role=npc_role, level=npc_level)
    if location_id in npc_registry:
        npc_registry[location_id].append(new_npc)
    else:
        npc_registry[location_id] = [new_npc]

def define_fixed_npcs(npc_registry):
    """Defines and adds fixed NPCs to the registry."""
    # Stormcloak recruiter in Windhelm
    add_fixed_npc(npc_registry=npc_registry, location_id=70, npc_name="Torin Battle-Born", npc_race="Nord", npc_role="stormcloak_recruiter", npc_level=5)

    # Imperial deserter hiding in the wilderness (Eastmarch)
    add_fixed_npc(npc_registry=npc_registry, location_id=7, npc_name="Marcus Varo", npc_race="Imperial", npc_role="imperial_deserter", npc_level=3)

    # Dominion spy gathering information in Riften
    add_fixed_npc(npc_registry=npc_registry, location_id=100, npc_name="Elenwen's Eye", npc_race="Altmer", npc_role="dominion_spy", npc_level=7)

def define_specific_npcs():
    """Defines specific NPCs for the game world."""
    from npc_entities import NPC # Import here to avoid circular dependency

    # Jarls
    jarl_laila_lawgiver = NPC(name="Laila Law-Giver", race="nord", role="jarl", level=25, disposition=60, gold=500)
    jarl_laila_lawgiver.add_tag("location", "governs", "riften")
    jarl_laila_lawgiver.add_tag("political", "affiliation", "empire")

    jarl_korir = NPC(name="Korir", race="nord", role="jarl", level=28, disposition=40, gold=600)
    jarl_korir.add_tag("location", "governs", "winterhold")
    jarl_korir.add_tag("political", "affiliation", "empire")

    # Important Merchants
    birna = NPC(name="Birna", race="nord", role="merchant", level=15, disposition=50, gold=300)
    birna.add_tag("location", "lives_in", "winterhold")
    birna.add_tag("trade", "sells", "general_goods")

    # Guild Leaders (if applicable in 200 4E)
    endrast_direnni = NPC(name="Endrast Direnni", race="altmer", role="mage_guild_leader", level=35, disposition=45, gold=700)
    endrast_direnni.add_tag("location", "lives_in", "winterhold")
    endrast_direnni.add_tag("guild", "leader_of", "college_of_winterhold")

    # Other Influential Figures
    vulwulf_snow_shod = NPC(name="Vulwulf Snow-Shod", race="nord", role="thane", level=22, disposition=55, gold=400)
    vulwulf_snow_shod.add_tag("location", "lives_in", "windhelm")
    vulwulf_snow_shod.add_tag("political", "affiliation", "stormcloak")
    # Adding more specific NPCs for 200 4E

    # Jarls
    jarl_elisif_the_fair = NPC(name="Elisif the Fair", race="nord", role="jarl", level=27, disposition=65, gold=550)
    jarl_elisif_the_fair.add_tag("location", "governs", "solitude")
    jarl_elisif_the_fair.add_tag("political", "affiliation", "empire")

    bryling = NPC(name="Bryling", race="nord", role="merchant", level=18, disposition=52, gold=350)
    bryling.add_tag("location", "lives_in", "solitude")
    bryling.add_tag("trade", "sells", "clothing")

    galmar_stone_fist = NPC(name="Galmar Stone-Fist", race="nord", role="stormcloak_officer", level=30, disposition=48, gold=650)
    galmar_stone_fist.add_tag("location", "lives_in", "windhelm")
    galmar_stone_fist.add_tag("political", "affiliation", "stormcloak")
    # Additional NPCs for 200 4E

    # Jarls
    jarl_vignar_gray_mane = NPC(name="Vignar Gray-Mane", race="nord", role="jarl", level=26, disposition=55, gold=520)
    jarl_vignar_gray_mane.add_tag("location", "governs", "whiterun")
    jarl_vignar_gray_mane.add_tag("political", "affiliation", "neutral")

    # Merchants
    aeri = NPC(name="Aeri", race="wood elf", role="merchant", level=12, disposition=45, gold=250)
    aeri.add_tag("location", "lives_in", "angas_mill")
    aeri.add_tag("location", "region", "the_pale")
    aeri.add_tag("trade", "sells", "wood")

    hroki = NPC(name="Hroki", race="nord", role="blacksmith", level=17, disposition=58, gold=330)
    hroki.add_tag("location", "lives_in", "markarth")
    hroki.add_tag("trade", "sells", "weapons_armor")

    lisbet = NPC(name="Lisbet", race="nord", role="merchant", level=15, disposition=50, gold=300)
    lisbet.add_tag("location", "lives_in", "markarth")
    lisbet.add_tag("trade", "sells", "jewelry")

    return {
        "jarl_laila_lawgiver": jarl_laila_lawgiver,
        "jarl_korir": jarl_korir,
        "birna": birna,
        "endrast_direnni": endrast_direnni,
        "vulwulf_snow_shod": vulwulf_snow_shod,
        "jarl_elisif_the_fair": jarl_elisif_the_fair,
        "bryling": bryling,
        "galmar_stone_fist": galmar_stone_fist,
        "jarl_vignar_gray_mane": jarl_vignar_gray_mane,
        "aeri": aeri,
        "hroki": hroki,
        "lisbet": lisbet,
    }
