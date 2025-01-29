#Extract the title of each recipe and save it as a variable title.
#Extract the text body of each recipe and save it as a variable recipe.
#Combine the process from the previous lesson and this lesson to access all the information from all recipes.

import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
print(soup.prettify())

author = soup.find("p", class_="author")
print(author.text)
print(author.text.strip("by "))  # OUTPUT: SomethingsBrewin

title = soup.find("h2")
print(title.text)

ingredients = soup.find_all("li")
for ingredient in ingredients:
    print(ingredient.text)
    







# from bs4 import BeautifulSoup

# import requests


# BASE_URL = "https://codingnomads.github.io/recipes/"
# page = requests.get(BASE_URL)

# soup = BeautifulSoup(page.text, 'html.parser')
# links = soup.find_all("a")

# for link in links:
#     print(link["href"])

# print(soup.get_text())
# import pprint
# response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
# pprint.pprint(response.json())

# (type(response.json()))  # OUTPUT: <class 'list'>
# for item in response.json()["data"]["films"]:
#     print(item["running_time"])
#     print(item["title"])
