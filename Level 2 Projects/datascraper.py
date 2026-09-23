"""
Task 2: Data Scraper
---------------------
Scrapes quotes (author + text) from https://quotes.toscrape.com,
a site built specifically for practicing scraping, and saves the
results to a CSV file.

Objectives covered:
1. Use `requests` to retrieve web page content.
2. Parse the HTML using BeautifulSoup.
3. Extract specific data (quote text + author).
4. Save the scraped data into a CSV file.
"""

import csv
import requests
from bs4 import BeautifulSoup

# 1. Retrieve the web page content
URL = "https://quotes.toscrape.com"
response = requests.get(URL)
response.raise_for_status()  # stop early if the request failed (e.g. 404/500)

# 2. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract specific data
# Each quote on the page lives inside <div class="quote">...</div>
quote_blocks = soup.find_all("div", class_="quote")

scraped_data = []
for block in quote_blocks:
    text = block.find("span", class_="text").get_text(strip=True)
    author = block.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]
    scraped_data.append({
        "author": author,
        "quote": text,
        "tags": ", ".join(tags)
    })

# 4. Save the scraped data into a CSV file
output_file = "quotes.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["author", "quote", "tags"])
    writer.writeheader()
    writer.writerows(scraped_data)

print(f"Scraped {len(scraped_data)} quotes and saved them to {output_file}")