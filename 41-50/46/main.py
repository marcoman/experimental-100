import requests
from bs4 import BeautifulSoup

URL="https://www.billboard.com/charts/hot-100/"


date = "2000-08-12"
date = input("Enter a date: ")
new_url = URL + date

soup = BeautifulSoup(requests.get(new_url).text, "html.parser")
webpage = soup.prettify()

selected = soup.select(selector='html body div main div div div div div div div ul li ul li h3')
for select in selected:
    song_text = select.getText().strip()
    print(f'Song is [{song_text}]')
