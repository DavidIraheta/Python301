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
    
    def __str__(self):
       return (
           f"Planet Details:\n"
           f"Name: {self.name}\n"
           f"Radius: {self.radius} miles\n"
           f"Mass: {self.mass} kg\n"
           f"Distance from Sun: {self.distance_from_sun} million miles\n"
           f"Moons: {self.moons}"
       )

planet_1 = Planet("Mercury", 1516, 3.285E23, 57.9, 0)
planet_2 = Planet("Venus", 3760, 4.867E24, 108.2, 0)
planet_3 = Planet("Earth", 3959, 5.972E24, 149.6, 1)
planet_4 = Planet("Mars", 2106, 6.39E23, 227.9, 2)
planet_5 = Planet("Jupiter", 43441, 1.898E27, 778.6, 79)
planet_6 = Planet("Saturn", 36184, 5.683E26, 1433.5, 146)
planet_7 = Planet("Uranus", 15759, 8.681E25, 2872.5, 27)
planet_8 = Planet("Neptune", 15299, 1.024E26, 4495.1, 14)

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_4)
print(planet_5)
print(planet_6)
print(planet_7)
print(planet_8)


