# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5


import requests

BASE_URL = "https://pokeapi.co/api/v2/"

golem = requests.get(BASE_URL + "pokemon/golem")
golem_data = golem.json()
toxicroak = requests.get(BASE_URL + "pokemon/toxicroak")
toxicroak_data = toxicroak.json()
hydreigon = requests.get(BASE_URL + "pokemon/hydreigon")
hydreigon_data = hydreigon.json()
houndoom = requests.get(BASE_URL + "pokemon/houndoom")
houndoom_data = houndoom.json()
crawdaunt = requests.get(BASE_URL + "pokemon/crawdaunt")
crawdaunt_data = crawdaunt.json()
celebi = requests.get(BASE_URL + "pokemon/celebi")
celebi_data = celebi.json()


pokemon = ["Golem", "Toxicroak", "Hydreigon", "Houndoom", "Crawdaunt", "Celebi"]

for poke in pokemon:
    response = requests.get(BASE_URL + f"pokemon/{poke.lower()}")
    data = response.json()
    print(f"{data['name']} ({data['id']})")
    print("Types:")
    for type_ in data["types"]:
        print(f"  - {type_['type']['name']}")
    print("\n")
