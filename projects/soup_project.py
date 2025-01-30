#Your Soup() objects should at least be able to:
#take an unlimited number of Ingredient() or Spice() objects during instantiation
#have a .cook() method that returns a search result for a soup recipe using all the added ingredients
#Take the amount of each Ingredient() into account. How can you work that into creating a recipe the user can actually cook?
#Interface with a recipe API instead of concatenating a web search URL. Receive the API response data, format it, and display it as command-line output.
#Create child classes to Soup() that have specific qualities.
 
import requests

class Soup:
    def __init__(self, name, steps, *ingredients):
        self.name = name
        self.steps = steps
        self.ingredients = ingredients
        self.ingredients = {}
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def add_ingredient(self, ingredient):
        
        name, amount = ingredient
        if name in self.ingredients:
            self.ingredients[name] += amount
        else:
            self.ingredients[name] = amount
        return self.ingredients
    
    def remove_ingredient(self, ingredient):

        if ingredient in self.ingredients:
            del self.ingredients[ingredient]
        return self.ingredients
    
    def cook(self, api_key):

        ingredients = "+".join(self.ingredients.keys())
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={ingredients}"

        response = requests.get(url)
        
        if response.status_code == 200:
            recipes = response.json()
        
            if recipes:
                recipes = recipes[0]
                return f"{recipes['title']}\nLink{recipes.get('sourceUrl', 'No URL provided')}"
            else:
                return "No recipes found."
        else:
            return f"Error: Unable to find recipes. Status code: {response.status_code}"

    def get_info(self):
        ingredients_info = ", ".join([f"{amount} {name}" for name, amount in self.ingredients.items()])
        return f"{self.name} is a soup made with {ingredients_info}."

class Spicy_soup(Soup):
    def __init__(self, name, steps, spice_level, *ingredients):
        super().__init__(name, steps, *ingredients)
        self.spice_level = spice_level
    

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} Soup has a spice level of {self.spice_level}."
    
class VeganSoup(Soup):
    def __init__(self, name, *ingredients):
        super().__init__(name, *ingredients)

    def is_vegan(self):
        non_vegan_ingredients = ['meat', 'chicken', 'fish', 'milk', 'egg', 'cheese']
        for ingredient in self.ingredients:
            if any(non_vegan in ingredient.lower() for non_vegan in non_vegan_ingredients):
                return False
        return True

    def get_info(self):
        base_info = super().get_info()
        vegan_status = "vegan" if self.is_vegan() else "not vegan"
        return f"{base_info} This soup is {vegan_status}."
 
if __name__ == "__main__":
    # Initialize a soup
    tomato_soup = Soup("Tomato Soup", "Cook the tomatoes and blend.", ("tomatoes", 3), ("onions", 1), ("garlic", 2))
    print(tomato_soup.get_info())


    print(tomato_soup.cook())

    # Create a spicy soup
    spicy_soup = Spicy_soup("Spicy Tomato Soup", "Cook the tomatoes, add spices.", "Medium", ("tomatoes", 3), ("onions", 1), ("chili flakes", 1))
    print(spicy_soup.get_info())

    # Create a vegan soup
    vegan_soup = VeganSoup("Vegetable Soup", "Boil and simmer the vegetables.", ("Coconut", 2), ("Ginger", 3), ("Celery", 1), ("Kale", 1), ("Zucchini", 1))
    print(vegan_soup.get_info())