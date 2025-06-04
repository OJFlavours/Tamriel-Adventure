exploration_events = [
  {
    "id": "hidden_cave_discovery",
    "location_id": "eastmarch_01",
    "description": "You discover a hidden cave entrance.",
    "triggers": [
      {
        "type": "skill_check",
        "skill": "perception",
        "threshold": 15
      }
    ],
    "challenges": [
      {
        "type": "puzzle",
        "description": "Solve a riddle to open the cave entrance."
      }
    ],
    "rewards": [
      {
        "type": "item",
        "item_id": "healing_potion",
        "quantity": 3
      },
      {
        "type": "experience",
        "amount": 100
      }
    ],
    "error_message": "You fail to find anything of interest."
  },
  {
    "id": "wandering_merchant_encounter",
    "location_id": "whiterun_01",
    "description": "You encounter a wandering merchant.",
    "triggers": [
      {
        "type": "random",
        "probability": 0.2
      }
    ],
    "challenges": [],
    "rewards": [
      {
        "type": "access",
        "area_id": "merchant_inventory"
      }
    ],
    "error_message": "The merchant is not interested in trading with you."
  },
  {
    "id": "ancient_ruin_exploration",
    "location_id": "winterhold_01",
    "description": "You stumble upon an ancient ruin.",
    "triggers": [
      {
        "type": "location_visited",
        "location_id": "winterhold_01"
      }
    ],
    "challenges": [
      {
        "type": "trap",
        "description": "Avoid a pressure plate trap."
      },
      {
        "type": "combat",
        "enemy_id": "skeleton",
        "quantity": 2
      }
    ],
    "rewards": [
      {
        "type": "item",
        "item_id": "ancient_sword",
        "quantity": 1
      },
      {
        "type": "experience",
        "amount": 200
      }
    ],
    "error_message": "The ruins are too dangerous to explore."
  }
]