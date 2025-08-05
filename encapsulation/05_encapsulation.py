# 📄 Question:
# Create a Student class where __name is a private variable. Add:

# set_name() to set the name

# Day 4 OOPs - Q1: Encapsulation using private variable

class Student(object):
    def __init__(self):
        self.__name = None  # private variable

    def set_name(self, name):
        """Set the student name"""
        self.__name = name

    def get_name(self):
        """Get the student name"""
        return self.__name

# Test
s = Student()
s.set_name("Lisa Das")
print("Student Name:", s.get_name())  # Output: Student Name: Lisa Das

