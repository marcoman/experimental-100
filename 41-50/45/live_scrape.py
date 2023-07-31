from bs4 import BeautifulSoup
import requests
import json

# Get a page and load it into a BeautifulSoup object

response = requests.get("https://news.ycombinator.com/news")
webtext = response.text
soup = BeautifulSoup(webtext, "html.parser")

#print (f'Title is {soup.title}')

article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.text

span = soup.find(name="span", class_="titleline")
span_title = span.getText()
span_link = span.find('a')['href']
article_upvote = soup.find(name="span", class_="score").getText()

print (f'Article span is [{span}]')
print(f'Article title is {span_title}')
print(f'Article link is {span_link}')
print(f'Article upvote is {article_upvote}')

spans = soup.find_all(name="span", class_="titleline")
for span in spans:
    title = span.text
    links = span.find_all('a')
    for link in links:
        pass


article_texts = []
article_links = []
article_upvotes = []

articles = soup.find_all(name="span", class_="titleline")
for article in articles:
    text = article.text
    article_texts.append(text)
    link = article.find('a')['href']
    article_links.append(link)

article_upvotes = [int((score.getText()).split()[0]) for score in soup.find_all(name="span", class_="score")]

print (article_texts)
print (article_links)
print (article_upvotes)

# now, find the max upvote and get the index of that article
max_upvote = max(article_upvotes)
max_upvote_index = article_upvotes.index(max_upvote)

print (f'The most upvoted article is {article_texts[max_upvote_index]} with {max_upvote} upvotes')