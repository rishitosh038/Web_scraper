# Web Scraping Using BeautifulSoup

## Project Overview

This project demonstrates how to perform web scraping using Python.

The script:
- Sends an HTTP request to a website
- Parses HTML using BeautifulSoup
- Extracts book titles, prices, and ratings
- Stores extracted data into a CSV file
- Handles missing tags safely
- Follows ethical scraping practices

This project helps understand how data is collected from web sources.

---

## Tools Used

- Python 3.x
- requests library
- beautifulsoup4
- csv module (built-in)
- VS Code

Install required libraries:

pip install requests beautifulsoup4

---

## Website Used

Books to Scrape (a legal practice website for web scraping)

http://books.toscrape.com/

This website is intentionally created for learning and practicing web scraping.

---

## Project Structure

web_scraper.py  
books_data.csv  
README.md  

---

## How to Run the Project

1. Open terminal in project directory
2. Run:

python web_scraper.py

3. The program will:
   - Fetch website HTML
   - Extract book details
   - Save them into books_data.csv

---

## Data Extracted

The script extracts:

- Book Title
- Price
- Rating

Sample CSV Output:

Title, Price, Rating  
A Light in the Attic, £51.77, Three  
Tipping the Velvet, £53.74, One  

---

## Features Implemented

✔ HTTP GET request using requests  
✔ HTML parsing using BeautifulSoup  
✔ Finding tags and attributes  
✔ Extracting text and attribute values  
✔ Handling missing elements safely  
✔ Writing structured data into CSV  
✔ Exception handling for network errors  

---

## Concepts Covered

- What is Web Scraping?
- HTML structure understanding
- Tags, classes, and attributes
- find() vs find_all()
- Nested tag extraction
- File handling in Python
- Exception handling
- Ethical scraping practices

---

## Ethical Scraping Practices Followed

- Used a scrape-friendly website
- No login or private data scraped
- Limited to homepage data only
- No aggressive repeated requests
- Checked robots.txt guidelines

---

## Learning Outcome

After completing this task, you can:

- Extract structured data from web pages
- Parse HTML using BeautifulSoup
- Identify and extract specific tags
- Store scraped data in CSV format
- Handle real-world scraping issues
- Follow ethical scraping standards

---

