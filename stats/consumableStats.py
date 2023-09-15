class ConsumableStats():
  def PotionsStats(potionName):
    if (potionName == "Cleanse Potion"):
      return {
        "name": "Cleanse Potion",
        "description": "Cleanse all Status Effects",
        "effect": "cleance",
        "value": 0,
        "type": "potions",
        "turn": 0,
      }

    if (potionName == "Crit Potion"):
      return {
        "name": "Crit Potion",
        "description": "Boost +10 Crit Damage",
        "effect": "boost_critDamage",
        "value": 3,
        "type": "potions",
        "turn": 5,
      }

    if (potionName == "Crit Strike Potion"):
      return {
        "name": "Crit Strike Potion",
        "description": "Boost +10 Crit Chance",
        "effect": "boost_critChance",
        "value": 50,
        "type": "potions",
        "turn": 5,
      }
    
    if (potionName == "Flare Potion"):
      return {
        "name": "Flare Potion",
        "description": "Boost +10 Strength",
        "effect": "boost_attack",
        "value": 10,
        "type": "potions",
        "turn": 5,
      }

    if (potionName == "Max Heal Potion"):
      return {
        "name": "Max Heal Potion",
        "description": "Heal 100 HP",
        "effect": "heal",
        "value": 30,
        "type": "potions",
        "turn": 0,
      }

    if (potionName == "Trinket Heal Potion"):
      return {
        "name": "Trinket Heal Potion",
        "description": "Heal 25 HP",
        "effect": "heal",
        "value": 10,
        "type": "potions",
        "turn": 0,
      }

    if (potionName == "Trinket Flare Potion"):
      return {
        "name": "Trinket Flare Potion",
        "description": "Boost +5 Strength",
        "effect": "boost_attack",
        "value": 5,
        "type": "potions",
        "turn": 2,
      }
    
    if (potionName == "Trinket Wind Potion"):
      return {
        "name": "Trinket Wind Potion",
        "description": "Boost +5 Accuracy",
        "effect": "boost_accuracy",
        "value": 5,
        "type": "potions",
        "turn": 3,
      }
    
    if (potionName == "Wind Potion"):
      return {
        "name": "Wind Potion",
        "description": "Boost +10 Accuracy",
        "effect": "boost_accuracy",
        "value": 10,
        "type": "potions",
        "turn": 5,
      }
    
    if (potionName == "Trinket Crit Potion"):
      return {
        "name": "Trinket Crit Potion",
        "description": "Boost +5 Crit Damage",
        "effect": "boost_critDamage",
        "value": 5,
        "type": "potions",
        "turn": 2,
      }

    if (potionName == "Trinket Crit Strike Potion"):
      return {
        "name": "Trinket Crit Strike Potion",
        "description": "Boost +5 Crit Chance",
        "effect": "boost_critChance",
        "value": 30,
        "type": "potions",
        "turn": 2,
      }
