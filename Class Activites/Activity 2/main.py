from subjects import Subject, List

action = int(input("What would you like to do? \n- 1. Add subject \n- 2. View a chosen subject from the list \n- 3. View all subjects\n- 4.Exit \n"))

while action != 4:
    if action == 1:
        List.add_subject()
    elif action == 2:
        List.view_subject()
    elif action == 3:
        List.print_all_subjects()
    else:
        print("Input not valid. Please try again.\n")
        action = int(input("What would you like to do? \n- 1. Add subject \n- 2. View a chosen subject from the list \n- 3. View all subjects\n- 4.Exit \n"))

print ("\nThank you for using this program.")



