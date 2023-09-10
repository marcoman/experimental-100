
# Created on Wed Apr  3 15:53:10 2019
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = "~/bin/chromedriver"

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Edge()
driver.get("https://google.com")


# This closes the active tab
#driver.close()

# This quits the entire browser.
#driver.quit()