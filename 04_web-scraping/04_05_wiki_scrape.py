# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

URL = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# Extract all the links on the page
links = soup.find_all("a", href=True)
# Filter out navigation links
filtered_links = [link["href"] for link in links if link["href"].startswith("/wiki/") and ":" not in link["href"]]
# Follow one of the links that lead to another Wikipedia article
# I chose the first link
first_link = filtered_links[0]
response = requests.get("https://en.wikipedia.org" + first_link)
soup = BeautifulSoup(response.text, "html.parser")
# Extract the text content from that article
text_content = soup.get_text()
# Save it to a local text file

print(text_content)

with open("web_scraping.txt", "w") as file:
    file.write(text_content)

# Use RegExp to find all numbers in the text
# numbers = re.findall(r"\d+", text_content)
# print(numbers)

# Output:

