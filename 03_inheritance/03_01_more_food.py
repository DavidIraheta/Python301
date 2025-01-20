# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.
# Edit the .expire() method of your Spice class to include a conditional statement. 
# If the name of your Spice() instance is "salt", then print a message that clarifies that salt never expires

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...poops")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste
    def expire(self):
        """Expires the ingredient item."""
        if self.name == "salt":
            print(f"Salt never expires, it's still good!")
        else:
            print(f"whoops, this {self.name} expired, it's probably still good...")
        self.name = "old " + self.name


    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

c = Ingredient('carrots', 3)
t = Ingredient('tomatoes', 6)
m = Ingredient('milk', 1)
s = Spice('salt', 10)
p = Spice('pepper', 20)

print(c)
print(p)
c.expire()
p.expire()
s.expire()
p.grind()
