from selenium import webdriver
from selenium.webdriver.common.by import By

WEBSITE = "https://www.python.org"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

for event_time in event_times:
    print (f'event time is {event_time.text}')

for event_name in event_names:
    print (f'event is {event_name.text}')

events = {}

for n in range(len(event_times)):
    events[n] = {
        'time' : event_times[n].text,
        'name' : event_names[n].text,
    }

print (events)

# This quits the entire browser.
driver.quit()
