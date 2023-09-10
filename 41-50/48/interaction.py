from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WEBSITE = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
# This next line allows us to see the search box.
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)

article_count = driver.find_element(By.ID, value="articlecount")
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

print (f'article count is {article_count.text}')

#article_count.click()

view_source = driver.find_element(By.LINK_TEXT, "View source")
view_source.click()

wiki_name = driver.find_element(By.CLASS_NAME, value='mw-logo-wordmark')
wiki_name.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# This quits the entire browser.
#driver.quit()
