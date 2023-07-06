import os
import requests
import json
import datetime


STOCK = "DE"
COMPANY_NAME = "Deere"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
DEMO_ENDPOINT = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DE&apikey=demo'
DAILY_ENDPOINT = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={apikey}'.format(symbol=STOCK, apikey=os.environ.get('ALPHAVANTAGE_API_KEY'))

YESTERDAY : datetime.date
DAY_BEFORE_YESTERDAY : datetime.date

## STEP 1: Use https://www.alphavantage.co/documentation/#daily

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

response = requests.get(DAILY_ENDPOINT)
print (f'URL is: {DAILY_ENDPOINT}')
print (response.status_code)
# print (response.json())


# We only want the dates from yesterdy, and the day before.
today = datetime.datetime.now().strftime("%Y-%m-%d")

def get_yesterdays():
    global YESTERDAY
    global DAY_BEFORE_YESTERDAY
    YESTERDAY = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    DAY_BEFORE_YESTERDAY = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")

    return YESTERDAY, DAY_BEFORE_YESTERDAY

def get_yesterday_weather():
    # Now get the data for the two days of interest
    data_yesterday = response.json()['Time Series (Daily)'][YESTERDAY]
    data_yesterday_before = response.json()['Time Series (Daily)'][DAY_BEFORE_YESTERDAY]

    print(f'Yesterday data is {data_yesterday}')
    print(f'Yesterday-yesterday data is {data_yesterday_before}')

get_yesterdays()
print (f'Yesterday is {YESTERDAY}')
print (f'Day before yesterday is {DAY_BEFORE_YESTERDAY}')

# get_yesterday_weather()

NEWS_ENDPOINT = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={DAY_BEFORE_YESTERDAY}&sortBy=popularity&apiKey={os.environ.get("NEWS_API_KEY")}'
print (f'URL is: {NEWS_ENDPOINT}')


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

response = requests.get(NEWS_ENDPOINT)
print (response.status_code)
# print (response.json())
# 


for article in response.json()['articles'][:3]:
    print(f"Title: {article['title']}")
    print(f"Article: {article['description']}")
    print(f"Brief: ")

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

# For this section, I'm omitting sending messages from my check-in code.  


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

