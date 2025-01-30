# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests

BASE_URL = "https://ghibliapi-iansedano.vercel.app"

cat_species = []

response = requests.get(BASE_URL + f"/api/species")
species = response.json()
for sp in species:
    if "cat" in {sp["name"].lower()}:
        cat_species.append(sp)

for sp in cat_species:
    response = requests.get(BASE_URL + f"/api/species/{sp['id']}")
    species = response.json()
    print(f"{species['name']}")
    print(f"{species['classification']}")
    print(f"{species['eye_colors']}")
    print(f"{species['hair_colors']}")
    print(f"{species['url']}")
    print("\n")

# import requests

# BASE_URL = "https://ghibliapi-iansedano.vercel.app"

# cat_species = []

# for sp in cat_species:
#     response = requests.get(BASE_URL + f"/api/species")
#     species = response.json()
#     if "cat" in sp["species"].lower():
#         print(f"{sp["name"]}")
#         print(f"{sp["classification"]}")
#         print(f"{sp["eye_colors"]}")
#         print(f"{sp["hair_colors"]}")
#         print(f"{sp["url"]}")
#         print("\n")


