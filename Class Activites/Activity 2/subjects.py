class Subject:
    def __init__(self, name, year_level, class_code, num_students):
        self.name = name
        self.year_level = year_level
        self.class_code = class_code
        self.num_students = num_students

class SubjectList:
    def __init__(self):
        self.subjects = []

    def add_subject(self):
        name = input("Enter subject name: ")
        year_level = input("Enter year level: ")
        class_code = input("Enter class code: ")
        num_students = int(input("Enter number of students in the class: "))

        self.subjects.append(Subject(name, year_level, class_code, num_students))
        print("\nSubject added.\n")
        return
    
    def view_subjects(self):
        subject_name = input("What subject would you like to view? ")

        if not self.subjects:
            print("\nNo subjects have been added.\n")
            return

        for subject in self.subjects:
            if subject.name.lower() == subject_name.lower():
                print(f"\nSubject: {subject.name}")
                print(f"Year Level: {subject.year_level}")
                print(f"Class Code: {subject.class_code}")
                print(f"Number of Students: {subject.num_students}\n")
                break
        else:
            print("\nSubject not found. Please try again.\n")

    def print_all_subjects(self):
        if not self.subjects:
            print("\nNo subjects have been added.\n")
            return
        
        print("\nAll Subjects:\n")
        for subject in self.subjects:
            print(f"Subject: {subject.name}\nYear Level: {subject.year_level}\nClass Code: {subject.class_code}\nNumber of Students: {subject.num_students}\n")

subjects_list = SubjectList()

while True:

    action = int(input("What would you like to do? \n- 1. Add subject \n- 2. View a chosen subject from the list \n- 3. View all subjects\n- 4.Exit \n"))
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
        print("\nInvalid input. Please try again.\n")
