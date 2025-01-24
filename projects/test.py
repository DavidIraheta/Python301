import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
print(response.json())
