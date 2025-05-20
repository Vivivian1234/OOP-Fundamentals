import datetime

class Person:
    def __init__(self, first_name, surname, dob, subject, email):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.subject = subject
        self.email = email

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.dob.year
        print(f"{self.first_name} {self.surname} is {age} years old.\n")

    def get_details(self):
        print(f"First Name: {self.first_name}\nSurname: {self.surname}\nDOB: {self.dob}\nSubject: {self.subject}\nEmail: {self.email}\n")



# Example of how to create an instance correctly:
dob_example = datetime.datetime(2000, 5, 15)  # Ensure DOB is a datetime object
person = Person("John", "Doe", dob_example, "Math", "john.doe@example.com")

person.get_age()
person.get_details()
