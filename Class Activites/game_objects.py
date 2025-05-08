class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race
        self.cls = cls        # Store the player's class
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

# Create a specific player instance
player = Player("Hugo", "Vampire", "Phantom Thief", 15, 200)

class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

# Create a weapon instance
weapon = Weapon("Ludwig", "Scythe", 13)

class Enemy:
    def __init__(self, name, race, damage, health):
        self.name = name
        self.race = race
        self.damage = damage
        self.health = health

# Create an enemy instance
enemy = Enemy("Lycaon", "Wolf Thiren", 14, 190)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from game_objects import Player, Weapon, Enemy
import random

# === Step 1: Create 4 characters ===
characters = [
    Player('Hugo', 'Vampire', 'Phantom Thief', 15, 200),
    Player('Lycaon', 'Wolf Thiren', 'Servant', 14, 190),
    Player('Vivian', 'Banshee', 'Seer', 11, 210),
    Player('Wise', 'Huan', 'Proxy', 3, 450)
]


# === Step 2: Create 4 weapons ===
weapons = [
    Weapon('Scythe', 'Melee', random.randint(12, 15)),
    Weapon('Boots', 'Stealth', random.randint(12, 15)),
    Weapon('Umbrella', 'Magic', random.randint(12, 15)),
    Weapon('Laser', 'Ranged', random.randint(12, 15))
]

# === Step 3: Define selection function ===
def choose_character():
    print("\nChoose your character:")
    for i, c in enumerate(characters, 1):
        print(f"{i}. {c.name} - {c.race} {c.cls}")

    while True:
        try:
            choice = int(input("Enter number (1-4): "))
            if 1 <= choice <= 4:
                selected = characters[choice - 1]
                print(f"\nYou selected: {selected.name}, the {selected.race} {selected.cls}")
                return selected
            else:
                print("Invalid number. Choose a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_weapon():
    print("\nChoose your weapon:")
    for i, w in enumerate(weapons, 1):
        print(f"{i}. {w.name} ({w.category}) - Damage: {w.damage}")

    while True:
        try:
            choice = int(input("Enter number (1-4): "))
            if 1 <= choice <= 4:
                selected = weapons[choice - 1]
                print(f"\nYou selected: {selected.name} - {selected.category} (Damage: {selected.damage})")
                return selected
            else:
                print("Invalid number. Choose a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# === Step 4: Run selection functions ===
player_character = choose_character()
player_weapon = choose_weapon()

# === Step 5: Create random enemy ===
enemy = Enemy('Exaltist', 'Sage', random.randint(15, 18), random.randint(80, 140))

# === Step 6: Print all info ===
print("\n=== Player Character ===")
print(f"Name: {player_character.name}")
print(f"Race: {player_character.race}")
print(f"Class: {player_character.cls}")
print(f"Attack: {player_character.atk}")
print(f"Health: {player_character.health}")

print("\n=== Weapon ===")
print(f"Name: {player_weapon.name}")
print(f"Category: {player_weapon.category}")
print(f"Damage: {player_weapon.damage}")

print("\n=== Enemy ===")
print(f"Name: {enemy.name}")
print(f"Race: {enemy.race}")
print(f"Damage: {enemy.damage}")
print(f"Health: {enemy.health}")

