# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import os

class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
    
    def add_ingredient(self, other):
        new_name = self.name + other.name
        new_amount = self.amount + other.amount
        new_unit = self.unit
        return Ingredient(name=new_name, amount=new_amount, unit=new_unit)
    
    def remove_ingredient(self, other):
        new_name = self.name + other.name
        new_amount = self.amount - other.amount
        new_unit = self.unit
        return Ingredient(name=new_name, amount=new_amount, unit=new_unit)
    

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name}"
    
    def get_info(self, name):
        return f"{self.amount} {self.unit} {self.name}"
    