**Automated Amazon Price Tracker**

This Python script monitors the price of a specified product on Amazon and sends an email notification when the price falls below a defined target.

**Features**

- Price Monitoring: Tracks the price of a product using its Amazon URL.
- Email Notifications: Sends an alert email if the current price is below the target price.
- Dynamic Price and Title Extraction: Retrieves and processes the product's title and price directly from the Amazon page.
- UTF-8 Support: Handles non-ASCII characters in email content.

**How It Works**

- Environment Variables: Uses a .env file to securely store email credentials and target email addresses.
- Custom Headers: Sends HTTP requests with headers mimicking a real browser for better web scraping results.
- Email Setup: Uses smtplib and email.mime to format and send emails via Gmail's SMTP server.
- Price Comparison: Compares the scraped price with a target price and sends an email alert if the condition is met.

Automation**
You can automate the script execution using PythonAnywhere. PythonAnywhere allows you to set up scheduled tasks to run your script at specified intervals, making it easy to continuously monitor the price without manual intervention.

![1](https://github.com/user-attachments/assets/8052e24f-7d83-4466-a863-0b0354b619f5)

![2](https://github.com/user-attachments/assets/8dd4b121-f3c4-469b-b31d-cb8ef9242a73)

![3](https://github.com/user-attachments/assets/63c2ab8a-4e44-4268-a84d-cfdce6a49d91)
