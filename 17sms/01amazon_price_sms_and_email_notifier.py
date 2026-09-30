import requests
from bs4 import BeautifulSoup
import time
import yagmail


sender = 'freek23@gmail.com'
receiver = 'f@vdberg.us'
password = 'rkhy nqbj seom uune' # make a password at https://myaccount.google.com/apppasswords
subject = "New price alert"


# Example function to check the price on Amazon for a specific disposal installation item
def check_amazon_price_disposal_installation():
    url = "https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M"
    response = requests.get(url)
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")
    currency = soup.find("span", class_="a-price-symbol").text
    wholes = soup.find("span", class_="a-price-whole").text
    cents = soup.find("span", class_="a-price-fraction").text
    return f"{currency}{wholes}{cents}"

# Send an email with a price notification
def send_email_notification(price):
    # Implement your email sending logic here
    print(f"Sending email notification: The price is now {price}")
    yag = yagmail.SMTP(user=sender, password=password)
    contents = f"The price is now {price}"
    yag.send(to=receiver, subject=subject, contents=contents)

# check the price continuously
# and send email notifications if the price changes
price = check_amazon_price_disposal_installation()
old_price = ""
while True:
    if price != old_price:
        send_email_notification(price)
    time.sleep(60)  # wait for 60 seconds before checking the price again
    old_price = price
    price = check_amazon_price_disposal_installation()
