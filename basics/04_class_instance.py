# Day 4: Class vs Instance Variables
# Question: Create a Student class with a class variable (college)
# and instance variables (name, roll_no). Demonstrate their behavior.


class student:
    college = "VSSUT"

    def _init_(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"name:{self.name}, Roll no: {self.roll_no}, college: {student.college}")    

student1 = student("Lisa Das", "2202041072")
student2 = student("Aditya singh", "2202041044")        

print("before updation of class variable:")
student1.display()
student2.display()

student.college = "VSSUT"

print("\nAfter updating class variables")
student1.display()
student.display()