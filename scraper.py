import streamlit as st
import requests
from bs4 import BeautifulSoup

# Create a function to scrape the website
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the desired data from the website
    # Modify this part according to the structure of the website
    data = soup.find('div', class_='product_price')
    
    return data

# Create the Streamlit web app
def main():
    # Set the page title
    st.title("Website Scraper")
    
    # Get the user input URL
    url = st.text_input("Enter the URL to scrape")
    
    # Check if the URL is provided
    if url:
        # Add a button to start scraping
        if st.button("Scrape"):
            # Call the scrape_website function
            scraped_data = scrape_website(url)
            
            # Display the scraped data
            st.write(scraped_data)

# Run the app
if __name__ == "__main__":
    main()
