import streamlit as st
import requests
import re

def scrape_website(url):
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Use regular expressions to extract data from the HTML
        pattern = r'<h1>(.*?)</h1>'  # Example pattern: extract text inside <h1> tags
        matches = re.findall(pattern, response.text)
        return matches
    else:
        st.error(f"Error: {response.status_code}")

# Streamlit app code
st.title("Web Scraper App")

# Input URL
url = st.text_input("Enter the URL of the website to scrape")

# Scrape button
if st.button("Scrape"):
    if url:
        data = scrape_website(url)
        if data:
            st.success("Scraping successful!")
            st.write(data)
        else:
            st.warning("No data found.")
    else:
        st.warning("Please enter a URL.")
