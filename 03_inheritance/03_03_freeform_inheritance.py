# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle:
    """Models a Vehicle."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Truck(Vehicle):
    """Models a Truck."""
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with a {self.bed_size} bed."

class Motorcycle(Vehicle):
    """Models a Motorcycle."""
    def __init__(self, make, model, year, style, engine):
        super().__init__(make, model, year)
        self.style = style
        self.engine = engine

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.style}."

class DirtBike(Motorcycle):
    """Models a Dirt Bike."""
    def __init__(self, make, model, year, style, engine):
        super().__init__(make, model, year, style, engine)
        

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.style} with a {self.engine} engine."

class Car(Vehicle):
    """Models a Car."""
    def __init__(self, make, model, year, style):
        super().__init__(make, model, year)
        self.style = style

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.style}."

v = Vehicle('Ford', 'F150', 2021)
t = Truck('Chevy', 'Silverado', 2021, 'short')
m = Motorcycle('Harley', 'Davidson', 2021, 'Cruiser', 'V-Twin')
d = DirtBike('KTM', '450', 2021, 'Enduro', 'Single Cylinder')
c = Car('Toyota', 'Camry', 2021, 'Sedan')

print(v)
print(t)
print(m)
print(d)
print(c)




