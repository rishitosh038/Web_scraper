import requests
from bs4 import BeautifulSoup
import csv


def scrape_books():
    url = "http://books.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        print("Website fetched successfully")

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Ranting"])

            for book in books:
                # Extract title
                title_tag = book.h3.a 
                title = title_tag["title"] if title_tag else "No Title"

                # Extract price
                price_tag = book.find("p", class_="price_color")
                price = price_tag.text if price_tag else "No Price"

                # Extract rating
                rating_tag = book.find("p", class_="star-rating")
                rating = rating_tag["class"][1] if rating_tag else "No Rating"

                writer.writerow([title, price, rating])
            
        print("Data saved to books_data.csv")
    
    except requests.exceptions.RequestException as e:
        print("Failed to fetch website")
        print("Error:", e)

def main():
    print("=== WEB SCRAPER USING BEAUTIFULSOUP ===")
    scrape_books()

if __name__ == "__main__":
    main()