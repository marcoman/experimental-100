from selenium import webdriver
from selenium.webdriver.common.by import By

WEBSITE = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)

article_count = driver.find_element(By.ID, value="articlecount")
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

print (f'article count is {article_count.text}')


# This quits the entire browser.
driver.quit()
