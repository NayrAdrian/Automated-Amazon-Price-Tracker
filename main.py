import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests

# Load environment variables from .env file
load_dotenv()

# Email credentials and target recipient
EMAIL_ADDRESS = os.environ["MY_EMAIL"]
EMAIL_PASSWORD = os.environ["MY_EMAIL_PASSWORD"]
TARGET_EMAIL = os.environ["MY_TARGET_EMAIL"]

# Custom headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "cross-site",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36",
}

# Target price
TARGET_PRICE = 100.00  # Set your target price

# URL to track
product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Fetch the web page
response = requests.get(product_url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the offscreen price element
product_title = soup.find('span', id='productTitle')
offscreen_price = soup.find('span', class_='aok-offscreen')

# Get the price if the element is found and remove the '$' sign
if product_title and offscreen_price:
    title = product_title.get_text(strip=True)
    price = offscreen_price.getText().strip().replace('$', '')
    current_price = float(price)
    print(f"Current Price: {current_price}")

    # Check if the current price is below the target price
    if current_price < TARGET_PRICE:
        print("Sending email, current price is below the target.")

        # Setup SMTP Connection
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # Secures the connection
            connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Create email content
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = TARGET_EMAIL
            msg['Subject'] = f"Price Alert: {title} Below Target Price!"

            # Create email body with UTF-8 encoding
            body = (
                f"The current price of '{title}' is ${current_price}, which is below your target price of ${TARGET_PRICE}.\n"
                f"Check it out here: {product_url}"
            )
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # Send email
            connection.send_message(msg)
        print("Email sent successfully.")
    else:
        print("Current price is above the target, no email sent")
else:
    print("Title or price not found")
