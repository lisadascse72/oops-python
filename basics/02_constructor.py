# Day 2: OOPs Python – Constructor Example

# Define a class Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Creating objects of Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model 3", 2023)

car1.display_info()  # Output: 2022 Toyota Camry
car2.display_info()  # Output: 2023 Tesla Model 3
