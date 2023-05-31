import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
    books_section = soup.find('div', class_='col-md-8')

  
    products = books_section.find_all('div', class_='col-md-4')

    
    for product in products:
        name = product.find('h3').text.strip()
        price = product.find('h4').text.strip()
        st.write(f"Name: {name}, Price: {price}")
        st.write("---")


def main():
    st.title("Data Scraper App")
    st.write("Enter the URL of the website to scrape:")
    url = st.text_input("URL", value="https://www.scrapethissite.com/")

    if st.button("Scrape"):
        if url:
            scrape_website(url)
        else:
            st.warning("Please enter a URL.")


if __name__ == "__main__":
    main()
