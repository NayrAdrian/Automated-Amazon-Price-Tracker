from bs4 import BeautifulSoup
import requests

# Fetch the web page
response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the offscreen price element
offscreen_price = soup.find('span', class_='aok-offscreen')

# Get the price if the element is found
if offscreen_price:
    price = offscreen_price.getText().strip()
    print(f"Price: {price}")
else:
    print("Price not found")
