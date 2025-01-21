#Your Soup() objects should at least be able to:
#take an unlimited number of Ingredient() or Spice() objects during instantiation
#have a .cook() method that returns a search result for a soup recipe using all the added ingredients
#Take the amount of each Ingredient() into account. How can you work that into creating a recipe the user can actually cook?
#Interface with a recipe API instead of concatenating a web search URL. Receive the API response data, format it, and display it as command-line output.
#Create child classes to Soup() that have specific qualities.


class Soup:
    def __init__(self, name, steps, *ingredients):
        self.name = name
        self.steps = steps
        self.ingredients = ingredients
        self.ingredients = list(ingredients)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self.ingredients

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        return self.ingredients

    def get_info(self):
        print(f"{self.name} is a delicious soup that is made with {self.ingredients} and is made by following these steps: {self.steps}")


