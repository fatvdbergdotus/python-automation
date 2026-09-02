import time
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
    time.sleep(1) # wait for the page to load
    return driver

# Get the login page of the demo webshop and log in
driver = get_driver("https://demowebshop.tricentis.com/login")
element = driver.find_element(by="xpath", value='//*[@class="email"]').send_keys("f@vdberg.us")
element = driver.find_element(by="xpath", value='//*[@class="password"]').send_keys("abcabcabc" + Keys.RETURN)
print(driver.current_url)

# Check if the login was successful by looking for the "Log out" button
element = driver.find_element(by="xpath", value='//*[@class="ico-logout"]')
if element.text == "Log out":
    print("Login successful")

print(20*"-") # separate the outputs

# Print the product titles on the home page after logging in
elements = driver.find_elements(by="xpath", value='//*[@class="product-title"]')
with open("products.txt", "w") as f:
    for element in elements:
        f.write(element.text + "\n")
        print(element.text)

print(20*"-") # separate the outputs

# Prints the user data on the "My account" page after logging in
element = driver.find_element(by="xpath", value='//*[@class="account"]').click()
time.sleep(1)
print(driver.current_url)
element = driver.find_element(by="xpath", value='//*[@name="FirstName"]').get_attribute("value")
print(element)
element = driver.find_element(by="xpath", value='//*[@name="LastName"]').get_attribute("value")
print(element)
element = driver.find_element(by="xpath", value='//*[@name="Email"]').get_attribute("value")
print(element)
time.sleep(1)

print(20*"-") # separate the outputs

# Log out and check if the logout was successful by looking for the "Log in" button
element = driver.find_element(by="xpath", value='//*[@class="ico-logout"]').click()
time.sleep(2)
print(driver.current_url)
element = driver.find_element(by="xpath", value='//*[@class="ico-login"]')
if element.text == "Log in":
    print("Logout successful")