import streamlit as st
import requests

@st.cache
def main():
    st.title("Web Scraper")

    # Input field for the URL
    url = st.text_input("Enter the URL to scrape")

    if st.button("Scrape"):
        try:
            response = requests.get(url)

            # Display the scraped content
            st.write("Scraped content:")
            st.write(response.text)

        except requests.RequestException as e:
            st.write("Error occurred:", e)

if __name__ == "__main__":
    main()
