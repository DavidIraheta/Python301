#Extract the title of each recipe and save it as a variable title.
#Extract the text body of each recipe and save it as a variable recipe.
#Combine the process from the previous lesson and this lesson to access all the information from all recipes.

import requests

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
print(page.text)







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
