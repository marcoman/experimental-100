import os
import requests
import json

from bs4 import BeautifulSoup

EXER53_GOOGLE_FORM = os.environ.get("EXER53_GOOGLE_FORM")
EXER53_ZILLOW_URL = os.environ.get("EXER53_ZILLOW_URL")
EXER53_ZIP_CODE = os.environ.get("EXER53_ZIP_CODE")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response=requests.get(EXER53_ZILLOW_URL, headers=headers)
#response = requests.get(EXER53_ZILLOW_URL)
webtext = response.text
soup = BeautifulSoup(webtext, "html.parser")

print (f'Title is {soup.title}')

#zpid_9369627 > div > div.StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0.bKpguY.property-card-data > div.StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0.fDSTNn > div > span
#document.querySelector("#zpid_9369627 > div > div.StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0.bKpguY.property-card-data > div.StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0.fDSTNn > div > span")
#//*[@id="zpid_9369627"]/div/div[1]/div[2]/div/span
#/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/ul/li[4]/div/div/article/div/div[1]/div[2]/div/span

# This one is precise.
# Full X-Path
# Price: 
#   /html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/ul/li[2]/div/div/article/div/div[1]/div[2]/div/span
# Address:
#   /html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/ul/li[1]/div/div/article/div/div[1]/a/address
# Link:
#   /html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/ul/li[1]/div/div/article/div/div[2]/div[2]/a/div/picture/img

# selected = soup.select('''
#  html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) div span,
#  html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child a address,
#  html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) a div picture img''')

selected = soup.select('''
 html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) a''')  

#selected = soup.select(selector='html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) div span')
#selected = soup.select(selector='html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child')
for select in selected:
    # Price:  div:nth-of-type(2) div span
    # Address: a address
    # Link: div:nth-of-type(2) a div picture img
    # price = selected.select(selector='div:nth-of-type(2) div span')
    # address = selected.select(selctor='a address')
    # link = selected.select(selector='div:nth-of-type(2) a div picture img')
    # print (price)
    select_text = select.getText()
    select_link = select.get("href")
    print(select_text)
    print(select_link)


soup = BeautifulSoup(webtext, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".property-card-data a") 
# Python list comprehension (covered in Day 26)
all_links = [link["href"] for link in all_link_elements] 
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_elements = soup.select(".property-card-link address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
#all_price_elements = soup.select(".PropertyCardWrapper span")
all_price_elements = soup.select(selector='html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) div span')

all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)
