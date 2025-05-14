from shapey import Circle, Rectangle

while True:

    action = input("Choose shape:\n1. Circle\n2. Rectangle\n3. Exit\n")
    
    if action == "1":
        choice = input ("Choose type of calulation:\n1. Perimeter\n2. Area\n3. Volume\n")
        if choice ==  "1":
            print("Circle Perimeter:", Circle.perimeter()) 
        elif choice == "2":
            print("Circle Area:", Circle.area()) 
        elif choice == "3":
            print("Circle Volume:", Circle.volume()) 
    elif action == "2":
        choice = input ("Choose type of calulation:\n1. Perimeter\n2. Area\n3. Volume\n")
        if choice ==  "1":
            print("Rectangle Perimeter:", Rectangle.perimeter()) 
        elif choice == "2":
            print("Rectangle Area:", Rectangle.area()) 
        elif choice == "3":   
            print("Rectangle Volume:", Rectangle.volume())  
    elif action == "3":
        print("\nThank you for using this program.\n")
        break
    else:
        print("\nInvalid input. Please try again.\n")


#----------------------------------------------------------------------------------------------------------------??