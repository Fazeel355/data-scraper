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
            books.append({'Title': title, 'Price': price})

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
        for book in data:
            st.write(book)
    else:
        st.warning("No data found.")
