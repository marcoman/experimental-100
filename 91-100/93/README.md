# Overview

This is the day 93 assignment.

## _From the course:_
Build a custom web scraper to collect data on things that you are interested in.

Using what you have learnt about web scraping, scrape a website for data that you are interested in. Try to build a CSV with the scraped data.

What you scrape is up to you.

Here are some suggestions:

- [NBA Player Stats](https://www.nba.com/stats/)
- [Audible Books and Ratings](https://www.audible.com/search?keywords=book&node=18573211011)
- [Miami House Foreclosure Listing](https://miamidade.realforeclose.com/index.cfm?zaction=AUCTION&Zmethod=PREVIEW&AUCTIONDATE=11/02/2020)
- [Steam Games Data](https://steamdb.info/)
- [Alibaba Products](https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab=)
- [Registered Doctors in Idaho](https://isecure.bom.idaho.gov/BOMPublic/LPRBrowser.aspx)
- [Recipes](https://www.allrecipes.com/)
- [Real Estate](https://www.trulia.com/)
- [Songs](https://soundcloud.com/)
- [Rollercoasters](https://rcdb.com/)
- [Food Nutrition](https://www.nutritionvalue.org/Pasta%2C_enriched%2C_dry_nutritional_value.html)

## My comments:

- Let's see if I can find a website of interest.  Some ideas off the top of my head
  - The prices of AWS EC2 instances in us-east-1
  - All of the DVHL hockey schedules

 Maybe this page:
[AWS EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

See Day 53 for my previous example.

I am reminded that I needed to use the selenium driver to render the javascript-based pages.  Javascript is popular to display tables or extra data, and a regular page request doesn't bring in all the data.


# Running

```
python3 main.py
```

# External Links

- 

# requirements.txt

# TODOs

- instead of cutting-and-pasting the full XPath, and then modifying the format, let's instead use a library to conver the XPath into a format that is convenient to use with Beautiful Soup.
