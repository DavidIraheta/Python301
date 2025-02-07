# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup
import json 

#scrape books to scrape from https://books.toscrape.com/ for science fiction books

URL = "https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
book_list = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    book_list.append({"title": title, "price": price, "rating": rating})
    print(title, price, rating)

with open("books.json", "w") as file:
    json.dump(book_list, file)

print()

