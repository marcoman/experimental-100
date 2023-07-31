from bs4 import BeautifulSoup
import requests
import re


# <section class="gallery__content-item gallery__content-item--gallery" data-slide-pos="1">
# <div class="gallery__content-item__item-wrapper">
# <div class="static-image">
# <div class="static-image__primary-next gallery__overlay--trigger hide " data-article-gallery-overlay="article-gallery-overlay">
# <img class="gallery-icon" src="/web/20200518073855im_/https://www.empireonline.com/assets-legacy/img/icons/gallery-icon.svg">
# <div class="static-image__primary-next__details">
# <span class="static-image__primary-next__view-gallery">View Gallery</span>
# <span class="static-image__primary-next__image-count">100 photos</span></div>
# <img class="gallery-arrow" src="/web/20200518073855im_/https://www.empireonline.com/assets-legacy/img/icons/gallery-cover-arrow-right.svg"></div>
# <div class="static-image__primary-total">2 of 100</div>
# <picture><source media="(max-width: 439px)" srcset="//web.archive.org/web/20200518073855im_/https://cdn.onebauer.media/one/media/5d2d/d990/853e/7cd6/60cc/fa2e/raging-bull.jpg?quality=50&amp;width=700&amp;ratio=1-1&amp;resizeStyle=aspectfit&amp;format=jpg">
# <img class="landscape" src="//web.archive.org/web/20200518073855im_/https://cdn.onebauer.media/one/media/5d2d/d990/853e/7cd6/60cc/fa2e/raging-bull.jpg?quality=50&amp;width=900&amp;ratio=1-1&amp;resizeStyle=aspectfit&amp;format=jpg" alt="Raging Bull" title="99) Raging Bull">
# </picture></div></div>
# <div class="article-title-description"><div class="article-title-description__text">
# <h3 class="title">99) Raging Bull</h3>
# <div class="descriptionWrapper"><p class="description"><p><strong>1980</strong>
# <br><a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/people/martin-scorsese/">Martin Scorsese</a> and <a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/people/robert-de-niro/">Robert De Niro</a> have together made movies better than their boxing biopic, but it&#39;s hard to argue that any of those movies feature a more jaw-dropping performance than De Niro&#39;s here as self-destructive pugilist Jake La Motta. It also features some of cinema&#39;s best-shot fights; hard to believe that before Scorsese, no director thought to put the camera inside the ring...<br>
# <br><a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/raging-bull/">Read Empire&#39;s review of Raging Bull</a>
# <br><a href="https://web.archive.org/web/20200518073855/https://www.amazon.co.uk/gp/product/B004G8QT2U/ref=as_li_tl?ie=UTF8&amp;tag=baucitnet-21&amp;camp=1634&amp;creative=6738&amp;linkCode=as2&amp;creativeASIN=B004G8QT2U&amp;linkId=b26f7fb5172ea177d53f358d272209a3" rel="nofollow" class="amazon-link">Buy the film now</a>
# <br></p>

# Get a page and load it into a BeautifulSoup object

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webtext = response.text
print (f'Response status code is {response.status_code}')

soup = BeautifulSoup(webtext, "html.parser")
print (f'Title is {soup.title}')

movies_map = {}

title_tags = soup.find_all(name="h3", class_="title")
for title in title_tags:

    title_text = title.text
    try:
        results = re.split(r"[):]", title_text)
        print (f"Results are: {results}")
        movies_map[results[0]] = results[1]
    except:
        print (f'Number is {title_text} and title is None')

# The page has typos we need to work around.  This is why we have exception handling.
# For example, at the time of running this code, the movie at 80 was listed as "15"
# Also, one movie was listed as 12: instead of 12)

for i in range(100):
    try:
        print (f'Movie {i+1} is {movies_map[str(i+1)]}')
    except KeyError:
        print (f'Movie {i+1} is None')
