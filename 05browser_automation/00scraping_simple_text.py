from asyncio import sleep
from selenium import webdriver

# Extract a webpage
def get_driver(url):
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # disable the browser window from opening
    options.add_argument("disable-infobars")
    options.add_argument("start-minimized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(1) # wait for the page to load
    return driver


# Get the headlines from the CNN website
driver = get_driver("https://www.cnn.com")
elements = driver.find_elements(by="xpath",value='//*[@class="container__headline-text"]')
for element in elements:
    print(element.text)

print("--------------------------------------------------") # separate the two outputs

# Get the average world temperature now
while True:
    driver = get_driver("https://www.theworldcounts.com/challenges/climate-change/global-warming/average-global-temperature")
    temperature_element = driver.find_element(by="xpath", value='//*[@class="counter-ticker is-size-2-mobile"]')
    print("Average World Temperature: " + temperature_element.text)
