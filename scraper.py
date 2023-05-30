import streamlit as st
import pandas as pd
import numpy as np
import requests

def scrape_books():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(url)
    html = response.text

    # Extracting data using pandas
    dfs = pd.read_html(html)
    books_table = dfs[0]

    # Cleaning up the data
    books_table.columns = books_table.iloc[0]
    books_table = books_table[1:]

    # Selecting relevant columns
    books = books_table[['Title', 'Price']]

    # Adding a random availability column using numpy
    availabilities = ['In Stock', 'Out of Stock']
    books['Availability'] = np.random.choice(availabilities, size=len(books))

    return books

# Streamlit UI
st.title("Books Scraper")

if st.button("Scrape"):
    scraped_data = scrape_books()
    st.write("Scraped Data:")
    st.write(scraped_data)
