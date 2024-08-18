# Overview

This is the day 96 assignment.

## _From the course:_
120 minutes to complete
1,432 student solutions
Build a custom website using an API that you find interesting.

Using what you have learnt about HTTP request and REST APIs, in today's project you will build a website that uses data from a public API.

For example, previously we create a rain alert app using a weather API. We also created an ISS tracker and looking into Bitcoin prices, all using a public API.

Today, you get to work on an API that you find interesting and build a service or website based on that API.

Here are some example APIs from the course

- These appear to work
    - [Brewery Data](https://www.openbrewerydb.org/?ref=public-apis)
    - [Spelling and Grammar Check API](https://www.perfecttense.com/api)
    - [Sound Effects API](https://freesound.org/docs/api/index.html?ref=public-apis)
    - [Lord of the Rings API]()https://the-one-api.dev/
    - [Art Data](https://developers.artsy.net/v2/)
    - [Stock Market Data](https://marketstack.com/)
    - [Barcode Generator/Recognition](https://www.cloudmersive.com/barcode-api?ref=public-apis)

- These do not appear to work
    - [Dictionary API](https://owlbot.info/?ref=public-apis)
    - [ESPN Data](http://www.espn.com/apis/devcenter/io-docs.html?ref=public-apis)
    - [Food Facts API](https://documenter.getpostman.com/view/8470508/SVtN3Wzy)
    - [Harry Potter Data](https://www.potterapi.com/?ref=public-apis)
    - [Elephant Data](https://elephant-api.herokuapp.com/?ref=public-apis)

    - [New York Subway Data](http://nycpulse.herokuapp.com/api)


## My comments:


I appreciate the sample APIs.  I will probably use one of those.
I am using the sound affects API to get a list of sounds, and present their links.  However, I won't download at this time.
This is a proof-of-concept example, where i display a page with a default list, and there are download links to get the files.
I also have a query link that takes you to a page where you can enter a new query string.  This redirects to the main page to show you the files and their download links.
The download is only allowed if you are logged on.

# Running

```bash
flask --app main run
```

# External Links


# requirements.txt


# TODOs

- Add pagination to the screen, to let people see additional pages.
- Consider adding the capability to play the sound in-line.
- reduce the number of rows to make the screen nicer to see.  
- Add additional data, perhaps a link to the license.
- display the page's context, in terms of the search word