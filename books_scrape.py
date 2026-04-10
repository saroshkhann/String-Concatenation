from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import requests

stored_data= []

base_url = "https://books.toscrape.com/catalogue/"
URL= "https://books.toscrape.com/"

while True:
    response = requests.get(URL)

    data = response.text

    soup = BeautifulSoup(data, "lxml")

    books = soup.find_all(class_="product_pod")

    for book in books:
        title = book.find("h3").get_text()
        price  = book.find(class_="price_color").get_text()
        new_price = float(price.replace("Â£", ""))

        rating_class = book.find("p")["class"][1]

        rating_map ={
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

        rating = rating_map[rating_class]

        stored_data.append({"title": title, "price": new_price, "rating": rating})
    next_btn = soup.find(class_="next")

    if next_btn:
        next_page = next_btn.find("a")["href"]
        URL = urljoin(URL, next_page)
        print(URL)
    else:
        break


df = pd.DataFrame(stored_data)
df.to_csv("books_scrape.csv", index = False)
