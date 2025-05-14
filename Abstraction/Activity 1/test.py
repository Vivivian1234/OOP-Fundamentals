from shapey import Circle, Rectangle  # Ensure shapey.py contains correct class definitions

while True:
    action = input("Choose shape:\n1. Circle\n2. Rectangle\n3. Exit\n")

    if action == "1":
        radius = float(input("Enter the radius of the circle: "))  # Prompt user for radius
        circle = Circle(radius)  # Create Circle instance with user input

        choice = input("Choose type of calculation:\n1. Perimeter\n2. Area\n3. Volume\n")
        if choice == "1":
            print("Circle Perimeter:", circle.perimeter())  # Now correctly calls on instance
        elif choice == "2":
            print("Circle Area:", circle.area()) 
        elif choice == "3":
            print("Circles do not have volume!")  # Assuming Circle is 2D
    elif action == "2":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))  # Ask for all parameters
        rectangle = Rectangle(width, height, length)  # Create Rectangle instance

        choice = input("Choose type of calculation:\n1. Perimeter\n2. Area\n3. Volume\n")
        if choice == "1":
            print("Rectangle Perimeter:", rectangle.perimeter())  # Fixed instance method call
        elif choice == "2":
            print("Rectangle Area:", rectangle.area()) 
        elif choice == "3":   
            print("Rectangle Volume:", rectangle.volume())  
    elif action == "3":
        print("\nThank you for using this program.\n")
        break
    else:
        print("\nInvalid input. Please try again.\n")
