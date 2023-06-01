import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = []

        # Find all book elements on the page
        book_elements = soup.find_all('article', class_='product_pod')

        # Extract data from each book element
        for book_element in book_elements:
            title = book_element.h3.a['title']
            price = book_element.find('p', class_='price_color').text
            rating = book_element.find('p', class_='star-rating')['class'][1]
            stock = book_element.find('p', class_='instock availability').text.strip()
            books.append({'Title': title, 'Price': price, 'Rating': rating, 'Stock': stock})

        return books
    else:
        st.error(f"Error: {response.status_code}")

# Streamlit app code
st.title("Book Scraper App")

# Scrape button
if st.button("Scrape"):
    url = "https://books.toscrape.com/"
    data = scrape_website(url)
    if data:
        st.success("Scraping successful!")
        for i, book in enumerate(data[:5], start=1):
            st.write(f"Book {i}")
            st.write(book)
    else:
        st.warning("No data found.")
