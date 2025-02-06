# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.
import requests
from bs4 import BeautifulSoup


URL = "https://codingnomads.github.io/recipes"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

def get_recipes():
    recipes = []
    for recipe in soup.find_all("h3"):
        recipes.append(recipe.text)
    return recipes
def get_recipes_with_ingredients(ingredients):
    # 2) Use the requests module to fetch the recipe collection from the
    # CodingNomads recipe collection.
    # 3) Create a BeautifulSoup object and pass the content of the
    # CodingNomads recipe collection to the object.
    # 4) Create a list of recipe titles that contain the provided
    # ingredients.
    pass

# 5) Create a CLI that takes a list of ingredients from a user.
# 6) Call the function you created in step 1 with the list of
# ingredients provided by the user.
# 7) Print the list of recipe titles that contain the provided
# ingredients.


if __name__ == "__main__":
    ingredients = input("Enter a list of ingredients separated by commas: ").split(",")
    recipes = get_recipes_with_ingredients(ingredients)
    print(recipes)