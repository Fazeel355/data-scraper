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
            soup = BeautifulSoup(response.content, "html.parser")

            # Scrape data from the website
            # For example, let's scrape all the headlines from an HTML page
            headlines = soup.find_all("h1")

            # Display the scraped data
            st.write("Scraped headlines:")
            for headline in headlines:
                st.write(headline.text)

        except requests.RequestException as e:
            st.write("Error occurred:", e)

if __name__ == "__main__":
    main()
