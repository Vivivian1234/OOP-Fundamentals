from weapons import Weapon, Sword, Bow, Longbow, Shortbow

weapon_list = Weapon

# Creating instances
basic_sword = Sword("Excalibur", 50, "Slashing")
basic_bow = Bow("Hunter's Bow", 30, "Piercing")
longbow = Longbow("Eagle Longbow", 40, "Piercing", 150)
shortbow = Shortbow("Swift Shortbow", 35, "Piercing", 80)

def main():
    while True:
        action = input("This is the weapon recording system. What would you like to do? \n- 1. Add weapon \n- 2. View inventory \n- 3. Search inventory \n- 4. Exit")

        if action == 1:
            weapon_list.add_weapon()
        elif action == 2:
            weapon_list.view_inventory()
        elif action == 3:
            weapon_list.search_inventory()
        elif action == 4:
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")


