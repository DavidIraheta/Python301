# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

response = requests.get(BASE_URL + "/api/species")
species = response.json()

cat_species = []


for sp in species:
    if "cat" in sp["classification"].lower():
        print(sp["name"])
        print(sp["classification"])
        print(sp["eye_colors"])
        print(sp["hair_colors"])
        print(sp["url"])
        print("\n")

# response = requests.get(BASE_URL + "/api/films")

# films = response.json()

# for film in films:
#     print(film["title"])
#     print(film["description"])
#     print(film["director"])
#     print(film["release_date"])
#     print(film["rt_score"])
#     print(film["running_time"])
#     print(film["people"])
#     print(film["species"])
#     print(film["locations"])
#     print(film["vehicles"])
#     print(film["url"])
#     print("\n")


