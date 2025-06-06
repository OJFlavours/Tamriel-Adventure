# npc_roles.py

# This file defines the various roles NPCs can have in the world,
# categorized for use by the NPC generation system.

# Roles that imply a higher social or political standing
NOBLE_ROLES = {
    "noble",
    "jarl",
    "thane",
    "steward",
    "court_wizard",
    "advisor",
    "emperor",          # For specific historical/quest contexts
    "empress",
    "legion_legate",    # High-ranking Imperial officer
    "stormcloak_general"
}

# Roles for common citizens, professionals, and faction members not inherently hostile
COMMONER_ROLES = {
    # Basic Professions
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "alchemist", "fletcher", "lumberjack", "woodcutter", "ferryman", "carriage_driver",
    "pawnbroker", "shopkeeper", "beggar", "elder", "child", "courier", "executioner",

    # Faction-Specific (Non-Hostile)
    "companion",        # Member of the Companions
    "college_mage",     # Member of the College of Winterhold
    "blade",            # Member of the Blades
    "greybeard",        # Master of the Way of the Voice
    "vigilant_of_stendarr",
    "penitus_oculatus", # Emperor's secret service
    "thieves_guild_member",
    "dark_brotherhood_member", # For non-hostile encounters within the sanctuary
    "imperial_soldier",
    "stormcloak_soldier",
    "orc_stronghold_member",

    # Misc Roles
    "mercenary",
    "pilgrim",
    "refugee"
}

# Roles that are typically hostile to the player
HOSTILE_ROLES = {
    # Humanoid Enemies
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "warlock", "conjurer", "illusionist", "pyromancer",
    "vampire", "vampire_thrall", "vampire_lord",
    "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thalmor_justiciar", "thalmor_soldier",
    "silver_hand",      # Werewolf hunters
    "reaver",           # Solstheim bandits
    "cultist",

    # Undead
    "draugr", "draugr_wight", "draugr_scourge", "draugr_deathlord",
    "skeleton", "ghost", "wraith", "dragon_priest",

    # Creatures
    "wolf", "ice_wolf", "bear", "cave_bear", "snow_bear",
    "spider", "frostbite_spider",
    "troll", "frost_troll",
    "hagraven", "spriggan", "wisp", "wispmother", "ice_wraith",
    "giant", "mammoth",

    # Daedra & Constructs
    "dremora",
    "atronach_flame", "atronach_frost", "atronach_storm",
    "dwarven_sphere", "dwarven_spider", "dwarven_centurion",

    # Subterranean
    "falmer", "falmer_shaman", "chaurus", "chaurus_hunter"
}

# Combined set for all non-hostile NPCs, calculated automatically
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES