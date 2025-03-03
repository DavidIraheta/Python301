#write a python script that fetches data from " https://jsonplaceholder.typicode.com/posts/1" and prints the post 

import requests 
from pprint import pprint

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
pprint(response.json())
r = response.json()
title = r['title']
print(title)












