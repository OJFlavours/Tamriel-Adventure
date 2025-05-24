import random
from enum import Enum
from typing import List, Dict, Optional
from items import Item
from tags import TAGS, FLAVOR_VIGNETTES
from npc import NPC
from stats import Player, Stats
from ui import UI

class ActionType(Enum):
    ATTACK = "attack"
    RANGED_ATTACK = "ranged_attack"
    BLOCK = "block"
    DODGE = "dodge"
    CAST_SPELL = "cast_spell"
    USE_ITEM = "use_item"
    FLEE = "flee"

class MagicSchool(Enum):
    DESTRUCTION = "destruction"
    RESTORATION = "restoration"
    ALTERATION = "alteration"
    CONJURATION = "conjuration"
    ILLUSION = "illusion"
    MYSTICISM = "mysticism"

class StatusEffectType(Enum):
    POISON = "poison"
    PARALYSIS = "paralysis"
    FROST = "frost"
    SHOCK = "shock"
    FIRE = "fire"
    SILENCE = "silence"
    WEAKNESS = "weakness"

class StatusEffect:
    def __init__(self, effect_type: StatusEffectType, duration: int, potency: float, source: str):
        self.effect_type = effect_type
        self.duration = duration
        self.potency = potency
        self.source = source

    def apply(self, target) -> str:
        flavor = {
            StatusEffectType.POISON: f"Venom from {self.source} sears {target.name}'s blood!",
            StatusEffectType.PARALYSIS: f"{target.name} is locked in {self.source}'s paralyzing grip!",
            StatusEffectType.FROST: f"{target.name} trembles under {self.source}'s icy embrace!",
            StatusEffectType.SHOCK: f"{self.source}'s lightning courses through {target.name}!",
            StatusEffectType.FIRE: f"{self.source}'s flames engulf {target.name}!",
            StatusEffectType.SILENCE: f"{self.source} seals {target.name}'s voice, blocking spells!",
            StatusEffectType.WEAKNESS: f"{self.source} drains {target.name}'s vitality!"
        }
        return flavor.get(self.effect_type, "")

class Spell:
    def __init__(self, name: str, school: MagicSchool, mana_cost: int, damage: tuple, skill: str, effect: Optional[StatusEffectType] = None, effect_chance: float = 0.0):
        self.name = name
        self.school = school
        self.mana_cost = mana_cost
        self.damage = damage
        self.skill = skill
        self.effect = effect
        self.effect_chance = effect_chance

SPELLS = {
    "fire_damage": Spell("Fire Damage", MagicSchool.DESTRUCTION, 20, (10, 20), "destruction", StatusEffectType.FIRE, 0.5),
    "frost_damage": Spell("Frost Damage", MagicSchool.DESTRUCTION, 18, (8, 18), "destruction", StatusEffectType.FROST, 0.6),
    "shock_damage": Spell("Shock Damage", MagicSchool.DESTRUCTION, 22, (12, 22), "destruction", StatusEffectType.SHOCK, 0.4),
    "restore_health": Spell("Restore Health", MagicSchool.RESTORATION, 25, (15, 25), "restoration"),
    "fortify_armor": Spell("Fortify Armor", MagicSchool.ALTERATION, 15, (0, 0), "alteration"),
    "charm": Spell("Charm", MagicSchool.ILLUSION, 15, (0, 0), "illusion"),
    "summon_skeleton": Spell("Summon Skeleton", MagicSchool.CONJURATION, 35, (0, 0), "conjuration"),
    "soul_trap": Spell("Soul Trap", MagicSchool.MYSTICISM, 20, (0, 0), "mysticism", StatusEffectType.WEAKNESS, 0.3),
    "paralyze": Spell("Paralyze", MagicSchool.ILLUSION, 30, (0, 0), "illusion", StatusEffectType.PARALYSIS, 0.4)
}

class Combat:
    def __init__(self, player: Player, enemies: List[NPC], location: Dict):
        self.player = player
        self.player.combat = self
        self.enemies = [enemy for enemy in enemies if enemy.is_alive()]
        self.location = location
        self.turn = 0
        self.environmental_modifiers = self._calculate_environmental_modifiers()
        self.status_effects: Dict[str, List[StatusEffect]] = {player.name: [], **{enemy.name: [] for enemy in enemies}}
        self.summoned_allies: List[NPC] = []

    def _calculate_environmental_modifiers(self) -> Dict:
        modifiers = {"hit_chance": 1.0, "damage": 1.0, "fatigue_cost": 1.0, "magicka_cost": 1.0, "regen_rate": 1.0}
        for tag in self.location.get("tags", []):
            if tag == "snowy":
                modifiers["hit_chance"] *= 0.9
                modifiers["fatigue_cost"] *= 1.2
                modifiers["regen_rate"] *= 0.8
            elif tag == "cavern":
                modifiers["hit_chance"] *= 0.95
                modifiers["damage"] *= 1.1
            elif tag == "swamp":
                modifiers["fatigue_cost"] *= 1.3
                modifiers["hit_chance"] *= 0.85
                modifiers["regen_rate"] *= 0.7
            elif tag == "mountain":
                modifiers["fatigue_cost"] *= 1.15
                modifiers["magicka_cost"] *= 1.1
            elif tag == "forest":
                modifiers["hit_chance"] *= 0.9
            elif tag == "ruin":
                modifiers["magicka_cost"] *= 0.9
        return modifiers

    def _get_flavor_text(self, action: ActionType, attacker, target, success: bool = True, extra: Dict = None) -> str:
        weapon = next((item for item in attacker.equipment if item.category == "weapon"), None)
        weapon_name = weapon.name.lower() if weapon else "fist"
        spell_name = extra.get("spell").name if extra and "spell" in extra else ""
        base_flavor = {
            ActionType.ATTACK: f"{attacker.name} slashes with their {weapon_name} at {target.name}",
            ActionType.RANGED_ATTACK: f"{attacker.name} looses an arrow from their {weapon_name} at {target.name}",
            ActionType.BLOCK: f"{attacker.name} raises their shield to fend off {target.name}",
            ActionType.DODGE: f"{attacker.name} dances away from {target.name}'s strike",
            ActionType.CAST_SPELL: f"{attacker.name} unleashes {spell_name} upon {target.name}",
            ActionType.USE_ITEM: f"{attacker.name} quaffs a potion",
            ActionType.FLEE: f"{attacker.name} seeks to escape {target.name}"
        }
        flavor = base_flavor.get(action, "")
        if not success:
            flavor += ", but the blow misses!" if action in [ActionType.ATTACK, ActionType.RANGED_ATTACK, ActionType.CAST_SPELL] else ", but fails!"
        vignettes = [FLAVOR_VIGNETTES[tag] for tag in self.location.get("tags", []) if tag in FLAVOR_VIGNETTES]
        vignettes = [v if isinstance(v, str) else random.choice(v) for v in vignettes]
        if vignettes and random.random() < 0.4:
            flavor += f" as {random.choice(vignettes).lower()}"
        return flavor

    def _apply_status_effects(self, target) -> List[str]:
        messages = []
        active_effects = self.status_effects.get(target.name, [])
        for effect in active_effects[:]:
            effect.duration -= 1
            resistance = {
                StatusEffectType.POISON: target.stats.poison_resist,
                StatusEffectType.PARALYSIS: target.stats.magic_resist,
                StatusEffectType.FROST: target.stats.frost_resist,
                StatusEffectType.SHOCK: target.stats.shock_resist,
                StatusEffectType.FIRE: target.stats.fire_resist,
                StatusEffectType.SILENCE: target.stats.magic_resist,
                StatusEffectType.WEAKNESS: target.stats.magic_resist
            }.get(effect.effect_type, 0)
            potency = effect.potency * (1 - resistance / 100)

            if effect.effect_type == StatusEffectType.POISON:
                damage = int(potency * 5)
                target.stats.take_damage(damage, "poison")
                messages.append(f"{target.name} writhes, taking {damage} poison damage.")
            elif effect.effect_type == StatusEffectType.PARALYSIS:
                messages.append(f"{target.name} is paralyzed, struggling to move!")
            elif effect.effect_type == StatusEffectType.FROST:
                target.stats.speed = max(10, target.stats.speed - int(potency * 10))
                messages.append(f"{target.name}'s limbs stiffen in the frost's grip.")
            elif effect.effect_type == StatusEffectType.SHOCK:
                target.stats.current_magicka = max(0, target.stats.current_magicka - int(potency * 15))
                messages.append(f"Shock drains {target.name}'s magicka.")
            elif effect.effect_type == StatusEffectType.FIRE:
                damage = int(potency * 6)
                target.stats.take_damage(damage, "fire")
                messages.append(f"{target.name} burns, taking {damage} fire damage.")
            elif effect.effect_type == StatusEffectType.SILENCE:
                messages.append(f"{target.name} is silenced, unable to weave spells!")
            elif effect.effect_type == StatusEffectType.WEAKNESS:
                target.stats.strength = max(10, target.stats.strength - int(potency * 10))
                target.stats.update_combat_stats()
                messages.append(f"{target.name}'s strength wanes under weakness.")
            if effect.duration <= 0:
                active_effects.remove(effect)
        return messages

    def _calculate_damage(self, attacker, defender, action: ActionType, extra: Dict) -> tuple:
        skill_value = 15
        skill_name = ""
        weapon = next((item for item in attacker.equipment if item.category == "weapon"), None)

        if action == ActionType.ATTACK:
            if weapon:
                skill_name = "blade" if weapon.name in ["Sword", "Dagger"] else "blunt" if weapon.name in ["Axe", "Mace"] else "hand_to_hand"
                skill_value = attacker.skills.get(skill_name, 15)
            else:
                skill_name = "hand_to_hand"  # Use hand_to_hand skill for unarmed
                skill_value = attacker.skills.get(skill_name, 15)
        elif action == ActionType.RANGED_ATTACK:
            if weapon:
                skill_name = "marksman"
                skill_value = attacker.skills.get(skill_name, 15)
            else:
                #No weapon, cannot perform ranged attack
                return 0, None, False, "physical"

        elif action == ActionType.CAST_SPELL:
            skill_name = extra.get("spell").skill
            skill_value = attacker.skills.get(skill_name, 15)

        if not attacker.stats.roll_to_hit(skill_value, defender.stats):
            return 0, None, False, "physical"

        damage = 0
        effect = None
        damage_type = "physical"
        if action in [ActionType.ATTACK, ActionType.RANGED_ATTACK]:
            if weapon and weapon.durability > 0:
                damage = random.randint(weapon.base_damage[0], weapon.base_damage[1]) * (1 + skill_value / 100)
                material_mod = {"ebony": 1.3, "daedric": 1.4, "dwemer": 1.2}.get(weapon.material.lower(), 1.0)
                damage *= material_mod
                if weapon.enchantment in [e.value for e in StatusEffectType] and random.random() < 0.3:
                    effect = StatusEffect(StatusEffectType(weapon.enchantment), 3, 1.0, weapon.name)
                    damage_type = weapon.enchantment if weapon.enchantment in ["fire", "frost", "shock", "poison"] else "physical"
                weapon.damage_item(5)
            else:
                damage = random.randint(attacker.stats.weapon_damage_min, attacker.stats.weapon_damage_max)
                skill_value = attacker.skills.get("hand_to_hand", 15)
                damage *= (1 + skill_value / 100)
        elif action == ActionType.CAST_SPELL and "spell" in extra:
            spell = extra["spell"]
            if not attacker.stats.roll_spell_success(skill_value):
                UI.slow_print(f"{attacker.name}'s spell fizzles!")
                return 0, None, False, "magical"
            damage = random.randint(spell.damage[0], spell.damage[1]) * (1 + skill_value / 100)
            if spell.effect and random.random() < spell.effect_chance:
                effect = StatusEffect(spell.effect, 3, 1.0, spell.name)
            damage_type = spell.effect.value if spell.effect in [StatusEffectType.FIRE, StatusEffectType.FROST, StatusEffectType.SHOCK] else "magical"

        if attacker.stats.roll_critical():
            damage *= attacker.stats.critical_multiplier
            UI.slow_print(f"{attacker.name} lands a critical strike!")

        damage = int(damage * self.environmental_modifiers["damage"])
        return damage, effect, True, damage_type

    def _npc_choose_action(self, npc: NPC) -> tuple:
        if StatusEffectType.PARALYSIS in [e.effect_type for e in self.status_effects[npc.name]] and random.random() < 0.7:
            return None, {}
        if StatusEffectType.SILENCE in [e.effect_type for e in self.status_effects[npc.name]]:
            spell_actions = []
        else:
            spell_actions = [ActionType.CAST_SPELL]

        if npc.alignment == "hostile":
            if npc.role_tag in ["mage", "necromancer"] and npc.stats.current_magicka >= 20 and random.random() < 0.6:
                spell = random.choice([s for s in SPELLS.values() if s.school in [MagicSchool.DESTRUCTION, MagicSchool.ILLUSION, MagicSchool.MYSTICISM]])
                return ActionType.CAST_SPELL, {"spell": spell}
            elif npc.role_tag in ["bandit", "warrior"] and any(item.name == "Bow" for item in npc.equipment) and random.random() < 0.4:
                return ActionType.RANGED_ATTACK, {}
            elif npc.role_tag == "thief":
                return random.choice([ActionType.ATTACK, ActionType.DODGE]), {}
            return ActionType.ATTACK, {}
        elif npc.role_tag == "healer" and npc.stats.current_magicka >= 25 and npc.stats.current_health < npc.stats.max_health * 0.5:
            return ActionType.CAST_SPELL, {"spell": SPELLS["restore_health"]}
        if npc.stats.current_health < npc.stats.max_health * 0.3 and random.random() < 0.5:
            return ActionType.FLEE, {}
        return ActionType.ATTACK, {}

    def player_turn(self) -> bool:
        UI.slow_print("\nYour turn:")
        print(f"Health: {self.player.stats.current_health}/{self.player.stats.max_health}, Magicka: {self.player.stats.current_magicka}/{self.player.stats.max_magicka}, Fatigue: {self.player.stats.current_fatigue}/{self.player.stats.max_fatigue}")
        print("Choose action:")
        print("1) Attack  2) Cast Spell  3) Use Item  4) Flee")
        choice = input("> ").strip()
        if choice == "1":
            target = self.enemies[0]
            dmg, effect, hit, dmgtype = self._calculate_damage(self.player, target, ActionType.ATTACK, {})
            UI.slow_print(self._get_flavor_text(ActionType.ATTACK, self.player, target, hit))
            if hit and dmg > 0:
                target.stats.take_damage(dmg, dmgtype)
                if effect:
                    self.status_effects[target.name].append(effect)
                    UI.slow_print(effect.apply(target))
                UI.slow_print(f"You deal {dmg} {dmgtype} damage to {target.name}.")
            else:
                UI.slow_print(f"Your blow misses {target.name}!")
            return True
        elif choice == "2":
            UI.slow_print("Which spell?")
            for i, key in enumerate(SPELLS, 1):
                print(f"{i}) {SPELLS[key].name}")
            sel = input("> ").strip()
            if not sel.isdigit() or int(sel) < 1 or int(sel) > len(SPELLS):
                UI.slow_print("No spell cast.")
                return True
            spell = list(SPELLS.values())[int(sel)-1]
            if not self.player.stats.consume_magicka(spell.mana_cost):
                UI.slow_print("Not enough magicka!")
                return True
            target = self.enemies[0]
            dmg, effect, hit, dmgtype = self._calculate_damage(self.player, target, ActionType.CAST_SPELL, {"spell": spell})
            UI.slow_print(self._get_flavor_text(ActionType.CAST_SPELL, self.player, target, hit, {"spell": spell}))
            if hit and dmg > 0:
                target.stats.take_damage(dmg, dmgtype)
                if effect:
                    self.status_effects[target.name].append(effect)
                    UI.slow_print(effect.apply(target))
                UI.slow_print(f"You deal {dmg} {dmgtype} damage to {target.name}.")
            else:
                UI.slow_print(f"Your spell misses {target.name}!")
            return True
        elif choice == "3":
            UI.slow_print("Not implemented yet.")
            return True
        elif choice == "4":
            UI.slow_print("You attempt to flee!")
            return False
        else:
            UI.slow_print("Invalid action.")
            return True

    def npc_turn(self, npc: NPC) -> bool:
        action, extra = self._npc_choose_action(npc)
        if action is None:
            UI.slow_print(f"{npc.name} is unable to act!")
            return True
        target = self.player
        if action == ActionType.FLEE:
            UI.slow_print(f"{npc.name} flees!")
            self.enemies.remove(npc)
            return False
        dmg, effect, hit, dmgtype = self._calculate_damage(npc, target, action, extra)
        UI.slow_print(self._get_flavor_text(action, npc, target, hit, extra))
        if hit and dmg > 0:
            target.stats.take_damage(dmg, dmgtype)
            if effect:
                self.status_effects[target.name].append(effect)
                UI.slow_print(effect.apply(target))
            UI.slow_print(f"{npc.name} deals {dmg} {dmgtype} damage to {target.name}.")
        else:
            UI.slow_print(f"{npc.name}'s blow misses {target.name}!")
        return True

    def run(self):  # Added the run method
        UI.slow_print(f"Entering combat at {self.location['name']}!")
        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.slow_print(f"\n--- Turn {self.turn} ---")
            # Apply status effects
            messages = self._apply_status_effects(self.player)
            for msg in messages:
                UI.slow_print(msg)
            for enemy in self.enemies:
                messages = self._apply_status_effects(enemy)
                for msg in messages:
                    UI.slow_print(msg)

            # Player turn
            if not self.player_turn():
                break

            # Check if any enemies died
            self.enemies = [enemy for enemy in self.enemies if enemy.stats.is_alive()]

            # Enemy turns
            for enemy in self.enemies[:]:  # Iterate over a copy to allow removal during loop
                if not self.npc_turn(enemy):
                    break

            # Check if player died or enemies are all defeated
            if not self.player.stats.is_alive():
                UI.slow_print("You have been defeated!")
                break
            if not self.enemies:
                UI.slow_print("You have defeated all your enemies!")
                break

        # Cleanup after combat
        self.player.combat = None
        UI.slow_print("Combat ends.")