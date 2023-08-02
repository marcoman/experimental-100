import requests
from bs4 import BeautifulSoup

URL="https://camelcamelcamel.com/product/B0C93PZTJN"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

webpage = soup.prettify()

# This one is precise.
#/html/body/div[1]/div[3]/div[4]/div/div/div[2]/div[3]/div[1]/div/p/span/span
selected = soup.select(selector='html body div div div div div div div div div p span span')
for select in selected:
    price = select.getText()
    print (price)

# This one is not as precise.
# selected = soup.find_all(name="span", class_="green")
# for select in selected:
#     price = select.getText()
#     print (price)
