
class Subject:
    def __init__(self, name, year_level, class_code, num_students):
        self.name = name
        self.year_level = year_level
        self.class_code = class_code
        self.num_students = num_students

    def display_details(self):
        print(f"Subject Name: {self.name}")
        print(f"Year Level: {self.year_level}")
        print(f"Class Code: {self.class_code}")
        print(f"Students Enrolled: {self.num_students}")
        print("-" * 30)

# Optional: function to display all subjects in a list
def display_all(subjects):
    if not subjects:
        print("No subjects added yet.")
    else:
        for idx, subject in enumerate(subjects, start=1):
            print(f"Subject {idx}:")
            subject.display_details()

