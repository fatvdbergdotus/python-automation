from bs4 import BeautifulSoup
import requests

currencies = ["USD", "EUR", "GBP", "JPY"]
extended_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]

# Get the exchange rate URL for a currency pair
def get_exchange_rate_url(from_currency, to_currency):
    return f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1"

# Retrieve the exchange rate from the webpage given a URL
def retrieve_exchange_rate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    rate_element = soup.find("span", class_="ccOutputRslt")
    if rate_element:
        return rate_element.text.split()[0]  # Get the numeric part of the rate
    else:
        return None

# Loop through the currency pairs and print the exchange rates
for from_currency in currencies:
    for to_currency in currencies:
        if from_currency != to_currency:
            url = get_exchange_rate_url(from_currency, to_currency)
            rate = retrieve_exchange_rate(url)
            if rate:
                print(f"1 {from_currency} = {rate} {to_currency}")
            else:
                print(f"Could not find exchange rate for {from_currency} to {to_currency}")
        else:
            print(f"1 {from_currency} = 1 {to_currency}")