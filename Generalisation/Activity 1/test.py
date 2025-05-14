import datetime


class Person:
    def __init__(self, first_name, surname, dob, gender, email):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.gender = gender
        self.email = email

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.dob.year
        print(f"{self.first_name} {self.surname} is {age} years old.")

    def get_details(self):
        print(f"First Name: {self.first_name}, Surname: {self.surname}, Dob: {self.dob}, Gender: {self.gender}, Email: {self.email}")


class Teacher(Person):
    def __init__(self, first_name, surname, dob, gender, email, staff_id, faculty):
        super().__init__(first_name, surname, dob, gender, email)
        self.staff_id = staff_id
        self.faculty = faculty

    def get_faculty(self):
        print(f"{self.first_name} is part of the {self.faculty} faculty.")

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.staff_id} is a teacher at this school.")

class Student(Person):
    def __init__(self, first_name, surname, dob, gender, email, student_id, year_co, house):
        super().__init__(first_name, surname, dob, gender, email)
        self.student_id = student_id
        self.year_co = year_co
        self.house = house

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.student_id} is a student at this school.")

# Usage
teacher_dob = datetime.date(1985, 6, 15) # Assuming the format for dob is year, month, day
teacher = Teacher("John", "Doe", teacher_dob, "Male", "johndoe@example.com", "T12345", "Mathematics")

student_dob = datetime.date(2005, 8, 20)
student = Student("Alice", "Smith", student_dob, "Female", "alicesmith@example.com", "S12345", 2023, "Red House")

teacher.get_details()
teacher.get_age()
teacher.get_faculty()
teacher.get_id()

student.get_details()
student.get_age()
student.get_id()