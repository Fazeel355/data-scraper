import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("http://books.toscrape.com/")
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the book containers on the page
book_containers = soup.find_all('article', class_='product_pod')

# Iterate over each book container and extract relevant information
for container in book_containers:
    # Extract the title of the book
    title = container.h3.a['title']
    
    # Extract the price of the book
    price = container.find('p', class_='price_color').text
    
    # Extract the availability of the book
    availability = container.find('p', class_='instock').text.strip()
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print("-----------------------")
