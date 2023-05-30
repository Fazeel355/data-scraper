import streamlit as st
import requests

def scrape_books(url):
    response = requests.get(url)
    books = response.json()['books']
    return books

# Streamlit UI
st.title("Books Scraper")

url = "https://books.toscrape.com/catalogue/category/books_1/index.json"
if st.button("Scrape"):
    scraped_data = scrape_books(url)
    st.write("Scraped Data:")
    for book in scraped_data:
        st.write(f"Title: {book['title']}")
        st.write(f"Price: {book['price']}")
        st.write(f"Availability: {book['availability']}")
        st.write("---")
