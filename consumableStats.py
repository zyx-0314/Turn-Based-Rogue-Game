class ConsumableStats():
  def PotionsStats(potionName):
    if (potionName == "Cleance"):
      return {
        "name": "Cleance",
        "description": "Cleanse all Status Effects",
        "effect": "cleance",
        "value": 0,
        "turn": 0,
      }
    
    if (potionName == "Flare Potion"):
      return {
        "name": "Flare Potion",
        "description": "Boost +10 Strength",
        "effect": "boost_attack",
        "value": 10,
        "turn": 4,
      }

    if (potionName == "Max Heal Potion"):
      return {
        "name": "Max Heal Potion",
        "description": "Heal 100 HP",
        "effect": "heal",
        "value": 100,
        "turn": 0,
      }

    if (potionName == "Trinket Heal Potion"):
      return {
        "name": "Trinket Heal Potion",
        "description": "Heal 25 HP",
        "effect": "heal",
        "value": 25,
        "turn": 0,
      }

    if (potionName == "Trinket Flare Potion"):
      return {
        "name": "Trinket Flare Potion",
        "description": "Boost +5 Strength",
        "effect": "boost_attack",
        "value": 5,
        "turn": 1,
      }
