from selenium import webdriver
import time

import yagmail
import os

# Extract the stock price and percentual change from the ZSE website using Selenium
def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("disable-infobars")
    options.add_argument("start-minimized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver


# Clean the text to extract only the temperature value
def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(" ")[0])
    return output


# Initiate the driver and wait for the page to load
driver = get_driver()
time.sleep(2)

# Get the stock name from the ZSE website
element = driver.find_element(by="xpath",value='//*[@class="stock-page-left"]')
print("Stock name: "+element.text[0:-3])  # remove the last 3 characters (the stock code)

# Get the stock price and percentual change from the ZSE website (2 different ways to get the same data)
element = driver.find_element(by="xpath",value='//*[@class="stock-value"]')
print("Stock price: "+element.text)

element = driver.find_element(by="xpath",value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[1]')
print("Stock price: "+element.text)

element = driver.find_element(by="xpath",value='//*[@class="stock-trend trend-drop"]')
text = str(clean_text(element.text))
print("Trend: "+text)

element = driver.find_element(by="xpath",value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
text = str(clean_text(element.text))
print("Trend: "+text)