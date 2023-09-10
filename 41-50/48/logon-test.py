from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WEBSITE = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
# This next line allows us to see the search box.
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)


fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up = driver.find_element(By.CLASS_NAME, value="btn-lg")

fname.send_keys("Marco")
lname.send_keys("Morales")
email.send_keys("mr.marco.a.morales@gmail.com")

# This quits the entire browser.
#driver.quit()
