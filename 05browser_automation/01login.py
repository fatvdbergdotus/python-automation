from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    sleep(1) # wait for the page to load
    return driver

driver = get_driver("https://demowebshop.tricentis.com/login")
element = driver.find_element(by="xpath", value='//*[@class="email"]').send_keys("f@vdberg.us")
element = driver.find_element(by="xpath", value='//*[@class="password"]').send_keys("abcabcabc" + Keys.RETURN)
print(driver.current_url)