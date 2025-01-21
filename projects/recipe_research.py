# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser


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
        pass
    
    def get_info(self):

        url = f"https://en.wikipedia.org/wiki/{self.name}"
        webbrowser.open(url)

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name}"

if __name__ == "__main__":


    ingredient1 = Ingredient("flour", 2, "cups")
    ingredient2 = Ingredient("sugar", 1, "cup")
    ingredient3 = Ingredient("butter", 1, "stick")
    ingredient4 = Ingredient("eggs", 2, "large")
    ingredient1.get_info()
    ingredient2.get_info()
    ingredient3.get_info()
    ingredient4.get_info()

    
