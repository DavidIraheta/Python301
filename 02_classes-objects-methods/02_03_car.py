# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def __str__(self):
        return f"Model: {self.model}, Year: {self.year}, Max Speed: {self.max_speed}"
        # return f"{self.model} ({self.year}) - {self.max_speed} km/h"
       
    def add (self, other):
        new_model = self.model + other.model
        new_year = self.year + other.year
        new_max_speed = self.max_speed + other.max_speed
        return Car(model=new_model, year=new_year, max_speed=new_max_speed)

car1 = Car("Toyota Corolla", 2021, 120)
car2 = Car("Honda Civic", 2020, 130)
car3 = Car("Ford Mustang", 2019, 150)
    
print(car1)
print(car2)
print(car3)

