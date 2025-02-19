# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Cat:
    """Models a cat."""
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def __str__(self):
        return f"{self.name} is {self.color} and is {self.age} years old."
    
    def __repr__(self):
        return f"Cat(name={self.name}, color={self.color}, age={self.age})"
    
    def __add__(self, other):
        new_name = self.name + other.name
        new_age = self.age + other.age
        new_color = self.color + other.color
        return Cat(name=new_name, age=new_age, color=new_color)

class Laptop:
    """Models a laptop."""
    
    def __init__(self, brand, model, year,ram):
        self.brand = brand
        self.model = model
        self.year = year
        self.ram = ram
        
    def __str__(self):
        return f"{self.brand} {self.model} from {self.year} and {self.ram} of ram."
    
    def __repr__(self):
        return f"Laptop(brand={self.brand}, model={self.model}, year={self.year}, ram={self.ram})"

class Fruit:
    """Models a fruit."""
    
    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.price = price
        
    def __str__(self):
        return f"{self.name} is a {self.color} fruit with a {self.taste} taste."
    
    def __repr__(self):
        return f"Fruit(name={self.name}, color={self.color}, taste={self.taste}, price={self.price})"

cat1 = Cat("Murray", 11, "Orange")
cat2 = Cat("Pepper", 1, "Grey/Black")

laptop1 = Laptop("Apple", "MacBook Air","2020", "16gb")
laptop2 = Laptop("Dell", "XPS 13","2021" ,"8gb")

fruit1 = Fruit("Mango", "Yellow", "Sweet", "$3")
fruit2 = Fruit("Apple", "Red", "Tart", "$2")

# Changing attributes
cat1.age += 1  
laptop1.ram = 32  
fruit1.sweetness = 10 

new_cat = cat1 + cat2


print(cat1)
print(cat2)
print(new_cat)  

print(laptop1)
print(laptop2)

print(fruit1)
print(fruit2)