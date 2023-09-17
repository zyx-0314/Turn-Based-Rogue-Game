class PlayerStat():
  bag = [
        {
          "name": "Max Heal Potion",
          "description": "Heal 100 HP",
          "file_icon": "max_heal_potion",
          "effect": ["heal"],
          "value": 30,
          "type": "potions",
          "turn": 0,
          "quantity": 2
        },{
          "name": "Trinket Heal Potion",
          "description": "Heal 25 HP",
          "file_icon": "trinket_heal_potion",
          "effect": ["heal"],
          "value": 10,
          "type": "potions",
          "turn": 0,
          "quantity": 5
        },{
          "name": "Crit Potion",
          "description": "Boost +10 Crit Damage",
          "file_icon": "crit_potion",
          "effect": ["boost_critDamage"],
          "value": 3,
          "type": "potions",
          "turn": 5,
          "quantity": 1
        },{
          "name": "Trinket Crit Potion",
          "description": "Boost +5 Crit Damage",
          "file_icon": "trinket_crit_potion",
          "effect": ["boost_critDamage"],
          "value": 5,
          "type": "potions",
          "turn": 2,
          "quantity": 3
        },{
          "name": "Flare Potion",
          "description": "Boost +10 Strength",
          "file_icon": "flare_potion",
          "effect": ["boost_attack"],
          "value": 10,
          "type": "potions",
          "turn": 5,
          "quantity": 1
        },{
          "name": "Trinket Flare Potion",
          "description": "Boost +5 Strength",
          "file_icon": "trinket_flare_potion",
          "effect": ["boost_attack"],
          "value": 5,
          "type": "potions",
          "turn": 2,
          "quantity": 3
        },{
          "name": "Wind Potion",
          "description": "Boost +10 Accuracy",
          "file_icon": "wind_potion",
          "effect": ["boost_accuracy"],
          "value": 10,
          "type": "potions",
          "turn": 5,
          "quantity": 2
        },{
          "name": "Trinket Wind Potion",
          "description": "Boost +5 Accuracy",
          "file_icon": "trinket_wind_potion",
          "effect": ["boost_accuracy"],
          "value": 5,
          "type": "potions",
          "turn": 3,
          "quantity": 5
        },{
          "name": "Crit Strike Potion",
          "description": "Boost +10 Crit Chance",
          "file_icon": "crit_strike_potion",
          "effect": ["boost_critChance"],
          "value": 50,
          "type": "potions",
          "turn": 5,
          "quantity": 1
        },{
          "name": "Trinket Crit Strike Potion",
          "description": "Boost +5 Crit Chance",
          "file_icon": "trinket_crit_strike_potion",
          "effect": ["boost_critChance"],
          "value": 30,
          "type": "potions",
          "turn": 2,
          "quantity": 3
        }
      ]

  Samurai = {
      "name": "Samurai",
      "folder": "samurai",
      "weapon": "sword",
      "max_hp": 100,
      "strength": 10,
      "accuracy": 85,
      "critChance": 10,
      "critDamage": 1.3,
      "bag": bag,
      "gold": 100,
      "skill": [
        {
          "name": "Charge Energy",
          "file_icon": "charge_energy",
          "description": "Charge Energy to boost your next attack",
          "effect": ["boost_accuracy", "boost_attack"],
          "value": 5,
          "type": "skills",
          "turn": 2,
        }
      ]
    }

  Archer = {
      "name": "Archer",
      "folder": "archer",
      "weapon": "bow",
      "max_hp": 80,
      "strength": 15,
      "accuracy": 90,
      "critChance": 20,
      "critDamage": 2,
      "bag": bag,
      "gold": 100,
      "skill": [
        {
          "name": "Full Draw",
          "file_icon": "full_draw",
          "description": "Charge Draw to boost your next attack",
          "effect": ["boost_accuracy", "boost_attack"],
          "value": 0,
          "type": "skills",
          "turn": 1,
        }
      ]
    }

  
class MonsterStat():
  SoldierSkeleton = {
      "name": "Soldier Skeleton",
      "folder": "soldierSkeleton",
      "weapon": "sword",
      "max_hp": 200,
      "strength": 6,
      "accuracy": 80,
      "critChance": 10,
      "critDamage": 1.3,
      "drop": "Trinket Heal Potion",
      "gold": 10
    }

  SpearmanSkeleton = {
      "name": "Spearman Skeleton",
      "folder": "spearmanSkeleton",
      "weapon": "spear",
      "max_hp": 180,
      "strength": 10,
      "accuracy": 85,
      "critChance": 20,
      "critDamage": 2,
      "drop": "Trinket Heal Potion",
      "gold": 12
    }

  ArcherSkeleton = {
      "name": "Archer Skeleton",
      "folder": "archerSkeleton",
      "weapon": "bow",
      "max_hp": 150,
      "strength": 15,
      "accuracy": 90,
      "critChance": 30,
      "critDamage": 2.5,
      "drop": "Trinket Heal Potion",
      "gold": 15
    }