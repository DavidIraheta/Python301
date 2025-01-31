# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

class Music:
    def __init__(self, title, artist, album, release_date):
        
        self.title = title
        self.artist = artist
        self.album = album
        self.release_date = release_date

    def get_info(self):
        return f"{self.title} by {self.artist} from the album {self.album} was released on {self.release_date}."

