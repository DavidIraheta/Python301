# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import requests
from bs4 import BeautifulSoup
import json 
import pytest



#scrape books to scrape from https://books.toscrape.com/ for science fiction books



URL = "https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
book_rating = soup.find_all("p", class_="star-rating")
book_list = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    book_list.append({"title": title, "price": price, "rating": rating})
    print(title, price, book_rating)

with open("books.json", "w") as file:
    json.dump(book_list, file)