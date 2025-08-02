# Day 3: Inheritance and Method Overriding
# Question: Inherit Person → Employee and override show() method.

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

# Derived class
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # Reuse Person constructor
        self.emp_id = emp_id

    # Overriding the show method
    def show(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}")

# Creating objects
person1 = Person("Ananya")
employee1 = Employee("Lisa", 1072)

# Output demonstration
person1.show()       # Output: Name: Ananya
employee1.show()     # Output: Name: Lisa, Employee ID: 1072
