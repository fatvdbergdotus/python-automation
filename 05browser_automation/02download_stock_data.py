import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

# Extract a webpage
def get_driver(url):
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new") # disable the browser window from opening
    options.add_argument("disable-infobars")
    options.add_argument("start-minimized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1) # wait for the page to load
    print(driver.current_url)
    return driver

# Get the stock values from Yahoo Finance for Microsoft (MSFT) and the last 3 months of data
driver = get_driver("https://finance.yahoo.com/quote/MSFT/history/?period1=1780404264&period2=1788351631")

# Deal with the consent pop-up
print(driver.find_element(By.TAG_NAME, "body").text)
input("Press ENTER...")

# Get the stock values
elements = driver.find_elements(by="xpath", value='//*[@class="yf-u4m6f0"]')

# Write the stock values to a text file and print them to the console
with open("stock_data.csv", "w") as file:
    for element in elements[3:]: # skip the first element, which is the header
        if len(element.text) > 40:
            content = element.text.replace(",", "").replace(" ", ",").replace(",", " ", 2) + "\n"
            file.write(content)
            print(content, end="")

print (20*"-") # separate the outputs

# Read the stock values from the text file and convert them to a pandas DataFrame
df = pd.read_csv("stock_data.csv", header=None, names=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
print(df)