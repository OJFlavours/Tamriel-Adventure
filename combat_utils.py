# combat_utils.py

# --- Complex Interactions ---
class Combo:
    def __init__(self, name, moves, damage_multiplier, stamina_cost):
        self.name = name
        self.moves = moves  # List of move names (e.g., ["attack", "block", "attack"])
        self.damage_multiplier = damage_multiplier
        self.stamina_cost = stamina_cost

    def execute(self, attacker, defender):
        """Executes the combo, applying damage and stamina cost."""
        total_damage = attacker.stats.attack * self.damage_multiplier
        defender.stats.take_damage(total_damage)
        attacker.stats.stamina -= self.stamina_cost
        return f"{attacker.name} executes {self.name} for {total_damage} damage!"

# --- Dynamic Interactions ---
def create_dynamic_interaction(name, condition, effect):
    """Creates a dynamic interaction based on a condition and effect."""
    def dynamic_interaction(attacker, defender):
        if condition(attacker, defender):
            return effect(attacker, defender)
        return None
    dynamic_interaction.__name__ = name  # Set the name of the function
    return dynamic_interaction