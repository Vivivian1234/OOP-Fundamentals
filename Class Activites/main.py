from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character = Player("Hugo", "Vampire", "Phantom Thief", 15, 200)

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapon_character = Weapon("Ludwig", "Scythe", random.randint(12, 15))

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140

enemy_character_ = Enemy("Lycaon", "Wolf Thiren", random.randint(15, 18), random.randint(80, 140))

# TODO: Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
print("\n=== Weapon ===")
print(f"Name: {weapon_character.name}")
print(f"Category: {weapon_character.category}")
print(f"Damage: {weapon_character.damage}")

# TODO: Print the enemy character details
print("\n=== Enemy ===")
print(f"Name: {enemy_character_.name}")
print(f"Race: {enemy_character_.race}")
print(f"Damage: {enemy_character_.damage}")
print(f"Health: {enemy_character_.health}")
