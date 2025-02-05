# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import requests
URL = "https://ghibliapi-iansedano.vercel.app"

cat_species = []

species_response = requests.get(URL + "/api/species")
species = species_response.json()

for sp in species["data"]["species"]:
    if "name" in sp and "cat" in sp["name"].lower():
        cat_species.append(sp)


print("\nStudio Ghibli Cats:\n")
if not cat_species:
    print("No cat species found.")
else:
    for sp in cat_species:
        print(f"Name: {sp['name']}")
        print(f"Classification: {sp['classification']}")
        print(f"Eye Colors: {sp['eye_colors']}")
        print(f"Hair Colors: {sp['hair_colors']}")
        print(f"URL: {sp['url']}")
        print("\n")
