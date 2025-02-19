# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.


import requests

# API Endpoints
POKE_URL = "https://pokeapi.co/api/v2/type/ghost"
GHIBLI_URL = "https://ghibliapi-iansedano.vercel.app/api/species"

def get_ghost_pokemon():
    """Fetch Ghost Pokémon from the PokéAPI."""
    response = requests.get(POKE_URL)
    print(f"PokéAPI Response Code: {response.status_code}") 
    if response.status_code == 200:
        data = response.json()
        return [poke["pokemon"]["name"].title() for poke in data["pokemon"]][:5]
    print(f"PokéAPI Response: {response.text}") 
    return []

def get_ghibli_spirits():
    """Fetch Ghibli spirits from the Ghibli API."""
    response = requests.get(GHIBLI_URL)
    print(f"GhibliAPI Response Code: {response.status_code}") 
    if response.status_code == 200:
        data = response.json()
        return [spirit["name"].title() for spirit in data["data"]["species"]][:5]
    print(f"GhibliAPI Response: {response.text}")  
    return []
def create_ghost_crossover_team():
    """Pair ghost Pokémon with Ghibli spirits."""
    pokemon_team = get_ghost_pokemon()
    ghibli_spirits = get_ghibli_spirits()

    if not pokemon_team or not ghibli_spirits:
        return "Could not retrieve data from APIs."

    print("\n**Ghost Crossover Team (Pokémon & Ghibli)**\n")
    for poke, spirit in zip(pokemon_team, ghibli_spirits):
        print(f"- {poke} takes on {spirit}")

create_ghost_crossover_team()