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
        
        

    def __str__(self):
        return f"{self.amount} {self.unit} {self.name}"
    
    def get_info(self, name):
        return f"{self.amount} {self.unit} {self.name}"
    

    class Ingredients:
    def __init__(self, ingredients):
        """
        Initialize the Ingredients class with a list of ingredients.
        
        Args:
            ingredients (list): A list of ingredient names as strings.
        """
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        """
        Add a single ingredient to the list.
        
        Args:
            ingredient (str): The ingredient to add.
        """
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        """
        Remove an ingredient from the list if it exists.
        
        Args:
            ingredient (str): The ingredient to remove.
        """
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def generate_search_url(self, base_url="https://www.google.com/search?q="):
        """
        Generate a search URL to look for recipes using the available ingredients.
        
        Args:
            base_url (str): The base URL for the search engine or recipe site.
        
        Returns:
            str: A URL string that can be used to search for recipes.
        """
        query = "+".join(self.ingredients) + "+recipe"
        return f"{base_url}{query}"

# Example usage
if __name__ == "__main__":
    # Initialize with a few ingredients
    ingredients = Ingredients(["chicken", "garlic", "onion", "tomato"])
    
    # Add an ingredient
    ingredients.add_ingredient("basil")
    
    # Remove an ingredient
    ingredients.remove_ingredient("onion")
    
    # Generate a search URL
    search_url = ingredients.generate_search_url()
    print("Search URL:", search_url)
