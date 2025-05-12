list = []

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

        print ("\nSubject added.")

    def view_subjects():
        subject = input("")






info = Subject(name, year_level, class_code, num_students)

print(f'\nStudent name: {info.name()}')
print(f'Year Level: {info.year_level()}')
print(f'Class code: {info.class_code()}')
print(f'Number of students: {info.num_students}')

action = int(input("What would you like to do? \n- 1. Add subject \n- 2. View a chosen subject from the list \n- 3. View all subjects\n- 4.Exit \n"))

while action != 4:
    if action = 1:
        list.add_subject()
    elif action = 2:
        list.view_subject()











add_subject_name = input("Add subject: ")
view_chosen_subject = input("View a chosen subject from the list: ")
vie_all_subjects = input("View all subjects: ")