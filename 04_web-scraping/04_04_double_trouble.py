# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

URL = "https://api.chucknorris.io/jokes/random"
response = requests.get(URL)
chuck_data = response.json()
chuck_joke = chuck_data["value"]
