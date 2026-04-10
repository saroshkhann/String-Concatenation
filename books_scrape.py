from bs4 import BeautifulSoup
import pandas as pd
import requests

stored_data= []


URL= "https://books.toscrape.com/"

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

df = pd.DataFrame(stored_data)

df.to_csv("books_scrape.csv", index = False)
