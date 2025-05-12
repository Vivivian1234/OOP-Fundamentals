class Subject:
    def __init__(self, name, year_level, class_code, num_students):
        self.name = name
        self.year_level = year_level
        self.class_code = class_code
        self.num_students = num_students

class List:
    def __init__(self):
        self.list = []

    def add_subject(self):
        name = input("Enter subject name: ")
        year_level = input("Enter year level: ")
        class_code = input("Enter class code: ")
        num_students = int(input("Enter number of students in the class: "))

        self.list.append(Subject(name, year_level, class_code, num_students))
        print("\nSubject added.")
        return
    
    def view_subjects(self):
        subject_name = input("What subject would you like to view? ")

        if not self.list:
            print("\nNo subjects have been added.")
            return
        
        elif subject_name not in self.list:
            print ("Subject not found. Please try again.")
            return


        for subject in self.list:
            if subject.name == subject_name:
                print(f"\nSubject: {subject.name}\nYear Level: {subject.year_level}\nClass Code: {subject.class_code}\nNumber of Students: {subject.num_students}")
                return

    def print_all_subjects(self):
        if not self.list:
            print("\nNo subjects have been added.")
            return
        
        print("\nAll Subjects:")
        for subject in self.list:
            print(f"\nSubject: {subject.name}\nYear Level: {subject.year_level}\nClass Code: {subject.class_code}\nNumber of Students: {subject.num_students}")

subjects_list = List()

action = int(input("What would you like to do? \n- 1. Add subject \n- 2. View a chosen subject from the list \n- 3. View all subjects\n- 4.Exit \n"))

while True:
    if action == 1:
        subjects_list.add_subject()
    elif action == 2:
        subjects_list.view_subjects()
    elif action == 3:
        subjects_list.print_all_subjects()
    elif action == 4:
        print("\nThank you for using this program.\n")
        break
    else:
        print("Invalid input. Please try again.")
