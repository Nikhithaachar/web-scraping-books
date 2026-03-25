import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

# Loop through pages (1 to 50)
for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()

        data.append([name, price, availability])

# Create DataFrame
df = pd.DataFrame(data, columns=["Book_Name", "Price", "Availability"])

# Clean data
df['Price'] = df['Price'].str.replace('[^0-9.]', '', regex=True).astype(float)
df['Availability'] = df['Availability'].str.strip()

# Save file
df.to_csv("Project33.csv", index=False)

print("All pages scraped successfully ✅")
print(df)