# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return (
            f"Rectangle Details:\n"
            f"Length: {self.length}, Width: {self.width}\n"
            f"Area: {self.area()}, Perimeter: {self.perimeter()}"
        )


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return (
            f"Circle Details:\n"
            f"Radius: {self.radius}\n"
            f"Area: {self.area()}, Circumference: {self.circumference()}"
        )

rectangle = Rectangle(5, 10)
circle = Circle(5)

print(rectangle)
print(circle)