import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []

    book_elements = soup.find_all('article', class_='product_pod')
    for element in book_elements:
        title = element.find('h3').find('a')['title']
        price = element.find('p', class_='price_color').text.strip()
        availability = element.find('p', class_='instock availability').text.strip()

        book = {
            'title': title,
            'price': price,
            'availability': availability
        }
        books.append(book)

    return books

# Streamlit UI
st.title("Books Scraper")

url = "https://books.toscrape.com/"
if st.button("Scrape"):
    scraped_data = scrape_books(url)
    st.write("Scraped Data:")
    for book in scraped_data:
        st.write(f"Title: {book['title']}")
        st.write(f"Price: {book['price']}")
        st.write(f"Availability: {book['availability']}")
        st.write("---")
