from bs4 import BeautifulSoup as bs4
import lxml


def  get_html(filename):
    with open(filename, 'r') as f:
        response = f.read()
    return response

def  parse(html):
    soup = bs4(html, 'html.parser')
    body = soup.body
    print (body)
    h1 = body.h1
    print (h1)
    print (body.p)

    print('********************')
    print (f'##TITLE is {soup.title}')
    print (f'##TITLE name is {soup.title.name}')
    print (f'##TITLE text is {soup.title.text}')
    print (f'##TITLE parent is {soup.title.parent}')
    print (f'##TITLE parent name is {soup.title.parent.name}')
    print (f'##TITLE parent parent is {soup.title.parent.parent}')
    print (f'##TITLE parent parent name is {soup.title.parent.parent.name}')


    print('********************')
    print(soup.prettify())

    print('********************')
    print("All Anchor Tags")
    all_anchor_tags = soup.find_all(name ="a")
    print(all_anchor_tags)

    all_paragraph_tags = soup.find_all(name='p')
    print(all_paragraph_tags)

    print('********************anchor')
    for tag in all_anchor_tags:
        print(tag.getText())
        print(tag.get("href"))

    print('********************')
    myheading = soup.find(id='name')
    print(myheading )
    print(myheading.getText())

    print('********************')
    section_heading = soup.find(name='h3', class_='heading')
    print(section_heading)
    print(section_heading.getText())
    print(section_heading.get('class'))
    print(section_heading.name)

    print('********************')
    selected = soup.select_one(selector='#url')
    print(selected)

    # This next line looks for an "a" tag inside a "p" tag
    selected = soup.select_one(selector='p a')
    print(selected)

    selected = soup.select_one(selector='#name')
    print(selected)

    selected = soup.select(selector=".heading")
    print(selected)


parse(get_html('website.html'))

