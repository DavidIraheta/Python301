# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    pass

    def __init__(self, name, radius, mass, distance_from_sun, moons):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons
    
    def planet_info(self):
        print(f"Name: {self.name}")
        print(f"Radius: {self.radius}")
        print(f"Mass: {self.mass}")
        print(f"Distance from Sun: {self.distance_from_sun}")
        print(f"Moons: {self.moons}")

planet_1 = Planet("Mercury", 1516, 3.285E23, 57.9, 0)
planet_2 = Planet("Venus", 3760, 4.867E24, 108.2, 0)
planet_3 = Planet("Earth", 3959, 5.972E24, 149.6, 1)
planet_4 = Planet("Mars", 2106, 6.39E23, 227.9, 2)
planet_5 = Planet("Jupiter", 43441, 1.898E27, 778.6, 79)
planet_6 = Planet("Saturn", 36184, 5.683E26, 1433.5, 146)
planet_7 = Planet("Uranus", 15759, 8.681E25, 2872.5, 27)
planet_8 = Planet("Neptune", 15299, 1.024E26, 4495.1, 14)

__str__ = planet_1.planet_info()
__str__ = planet_2.planet_info()
__str__ = planet_3.planet_info()
__str__ = planet_4.planet_info()
__str__ = planet_5.planet_info()
__str__ = planet_6.planet_info()
__str__ = planet_7.planet_info()
__str__ = planet_8.planet_info()

