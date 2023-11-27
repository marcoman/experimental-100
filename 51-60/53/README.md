Capstone Project Program Requirements
As we get closer to the latter part of the course, and as you build up your skills every day, the challenges are going to become more life-like and more challenging. As a developer, you will spend most of your time figuring out how to do things using Google and StackOverflow. It's rare that I come across a new project and already know exactly what code I need to write.

In this capstone project, you will need to apply everything you've learnt about website and web scraping with Beautiful Soup and Selenium to complete the project and fulfil the project requirements. You might also need to do your own research and revision to complete the task.

But first, you need to create a new form in Google Forms.

1. Go to https://docs.google.com/forms/ and create your own form:


2. Add 3 questions to the form, make all questions "short-answer":


3. Click send and copy the link address of the form. You will need to use this in your program.


4. Go to this web address on Zillow and see how the website is structured, this is where you'll be scraping the data from:


Program Requirements:

Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).

Create a list of links for all the listings you scraped. e.g.

Create a list of prices for all the listings you scraped. e.g.

Create a list of addresses for all the listings you scraped. e.g.


Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.


Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.


______________________________________________________________________________________________________________________________________


## HELP
I'll admit I used these resources:

Hints:
https://gist.github.com/TheMuellenator/7e45f9b977e90419146c4a2ee1713087


Solution:
https://gist.github.com/TheMuellenator/1318b1084a74e9b559f9820438b4a931

One thing I tried to figure out was how to select a base object, and then iterate within to find child items.

