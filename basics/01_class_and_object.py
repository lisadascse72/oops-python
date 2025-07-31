"""
GFG OOPs Python – Day 1
Q1. Write a Python class named `Student` with attributes like `name` and `roll_number`.
    Create an object of the class and print the student's details.
"""

class Student:
    # Constructor to initialize name and roll_number
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    # Method to display student details
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")


# Example usage: creating and using a Student object
if __name__ == "__main__":
    # Creating an instance of Student
    student1 = Student("Lisa Das", "2202041072")
    student2 = Student("addy baddie", "2202041071")

    # Displaying student details
    student1.display_details()
    student2.display_details()
