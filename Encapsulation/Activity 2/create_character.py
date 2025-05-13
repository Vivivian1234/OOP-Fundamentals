
class CreateCharacter:
    def __init__(self, name, strength, dexterity, constitution, intellect, wisdom):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellect = intellect
        self.wisdom = wisdom

class CharacterList:
    def __init__(self):
        self.characters = []

    def add_character(self):
        name = input("Enter character's name: ")
        name = name.lower().capitalize()
        strength = int(input("Enter character strength: "))
        dexterity = int(input("Enter character dexterity: "))
        constitution = int(input("Enter character constitution: "))
        intellect = int(input("Enter character intellect: "))
        wisdom = int(input("Enter character wisdom: "))

        self.characters.append(CreateCharacter(name, strength, dexterity, constitution, intellect, wisdom))
        print("\nCharacter information added.\n")
        return

    def level_up(self):
        if not self.characters:
            print("\nNo characters have been added.\n")
            return

        print("Characters available: ")
        for char in self.characters:
            print(f"- {char.name}")

        character_name = input("Which character would you like to level up?\n")
        character_name = character_name.lower().capitalize()

        for character in self.characters:
            if character.name == character_name: 
                stat = input(f'\nWhich attribute would you like to improve by 2 levels? Options: \n- strength ({character.strength})\n- dexterity ({character.dexterity}) \n- constitution ({character.constitution})\n- intellect ({character.intellect})\n- wisdom ({character.wisdom})\n').lower()

                if stat == "strength":
                    character.strength += 2
                    print("\nStrength increased by 2 levels.")
                    print(f'Strength = {character.strength}\n')
                elif stat == "dexterity":
                    character.dexterity += 2
                    print("\nDexterity increased by 2 levels.")
                    print(f'Dexterity = {character.dexterity}\n')
                elif stat == "constitution":
                    character.constitution += 2
                    print("\nConstitution increased by 2 levels.")
                    print(f'Constitution = {character.constitution}\n')
                elif stat == "intellect":
                    character.intellect += 2
                    print("\nIntellect increased by 2 levels.")
                    print(f'Intellect = {character.intellect}\n')
                elif stat == "wisdom":
                    character.wisdom += 2
                    print("\nWisdom increased by 2 levels.")
                    print(f'Wisdom = {character.wisdom}\n')
                else:
                    print(f"{stat} is not a valid attribute.")

                print(f"Updated character info for {character.name}:\n")
                print(f"Strength: {character.strength}")
                print(f"Dexterity: {character.dexterity}")
                print(f"Constitution: {character.constitution}")
                print(f"Intellect: {character.intellect}")
                print(f"Wisdom: {character.wisdom}\n")

                return 

        print("\nCharacter not found. Please try again.\n")


character_list = CharacterList()