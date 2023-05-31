import requests
import re

# Send a GET request to the website
response = requests.get("http://books.toscrape.com/")

# Extract the book containers using regular expressions
book_containers = re.findall(r'<article class="product_pod">(.*?)</article>', response.text, re.DOTALL)

# Iterate over each book container and extract relevant information
for container in book_containers:
    # Extract the title of the book
    title = re.search(r'<h3><a.*?title="(.*?)">', container).group(1)
    
    # Extract the price of the book
    price = re.search(r'<p class="price_color">(.*?)</p>', container).group(1)
    
    # Extract the availability of the book
    availability = re.search(r'<p class="instock availability">(.*?)</p>', container).group(1).strip()
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print("-----------------------")
