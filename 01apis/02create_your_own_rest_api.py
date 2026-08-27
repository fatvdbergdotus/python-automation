from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# function to get the currency rate from x-rates.com
def get_currency_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rate = soup.find("span", class_="ccOutputTrail").previous_sibling.text
    return rate

# define the API endpoint documentation
@app.route("/")
def home():
    return "<h1>Currency rate API</h1><p>This site is a prototype API for currency rates. Example usage: /api/v1/usd-eur</p>"

# define the API endpoint for getting the currency rate
# example: http://127.0.0.1:5000/api/v1/usd-eur
@app.route("/api/v1/<in_currency>-<out_currency>")
def api(in_currency, out_currency):
    rate = get_currency_rate(in_currency, out_currency)
    result_dict = [{"from": in_currency, "to": out_currency, "rate": rate}]
    return jsonify(result_dict)

app.run(host="0.0.0.0")