from bs4 import BeautifulSoup
import requests

# Fetch the web page
response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the price elements
whole_price = soup.find('span', class_='a-price-whole')
fraction_price = soup.find('span', class_='a-price-fraction')

# Combine whole price and fraction price, if both are found
if whole_price and fraction_price:
    price = whole_price.getText() + fraction_price.getText()
    print(f"Price: ${price}")
else:
    print("Price not found")
