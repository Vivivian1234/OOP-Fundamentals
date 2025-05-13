from create_character import CharacterList

character_list = CharacterList()

def main():
    while True:
        action = input("This is the character data record system. What would you like to do? \n- 1. Add character information \n- 2. Level up a character's attribute \n- 3. Exit \n")

        if action == "1":
            character_list.add_character()
        elif action == "2":
            character_list.level_up()
        elif action == "3":
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()
