class PlayerStat():
  Samurai = {
      "name": "Samurai",
      "folder": "samurai",
      "max_hp": 100,
      "strength": 10,
      "accuracy": 85,
      "critChance": 10,
      "critDamage": 1.3,
      "bag": [
        {
          "name": 'Max Heal Potion',
          'quantity': 2,
        },{
          "name": 'Trinket Flare Potion',
          'quantity': 3,
        },{
          "name": 'Wind Potion',
          'quantity': 1,
        }
      ]
    }

  Archer = {
      "name": "Archer",
      "folder": "archer",
      "max_hp": 80,
      "strength": 15,
      "accuracy": 90,
      "critChance": 20,
      "critDamage": 2,
      "bag": [
        {
          "name": 'Max Heal Potion',
          'quantity': 2,
        },{
          "name": 'Trinket Flare Potion',
          'quantity': 3,
        },{
          "name": 'Wind Potion',
          'quantity': 1,
        }
      ]
    }

class MonsterStat():
  SoldierSkeleton = {
      "name": "Soldier Skeleton",
      "folder": "soldierSkeleton",
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
      "max_hp": 180,
      "strength": 10,
      "accuracy": 85,
      "critChance": 20,
      "critDamage": 2,
      "drop": "Trinket Heal Potion",
      "gold": 12
    }