
# Created on Wed Apr  3 15:53:10 2019
from selenium import webdriver
from selenium.webdriver.common.by import By

WEBSITE = "https://www.amazon.com/Ducky-Classic-Hotswap-Mechanical-Keyboard/dp/B09Y2GNJ88"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = "~/bin/chromedriver"

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Edge()
driver.get(WEBSITE)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print (f"The price is {price_dollar.text}.{price_cents.text}")

# This closes the active tab
#driver.close()

# This quits the entire browser.
driver.quit()

