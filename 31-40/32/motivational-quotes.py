'''
Here, we read from a file to get a list of quotes.
Next, we print out a random quote.
The goal is to send an email each Monday with a random inspirational quote.
'''

import datetime as dt
import os
import smtplib
import random

QUOTEFILE = "quotes.txt"



def read_quotes():
    quotes = []
    with open(QUOTEFILE) as file:
        for line in file:
            quotes.append(line)
    return quotes

def get_random_quote():
    return random.choice(read_quotes())

def get_day_of_week():
    return dt.datetime.now().weekday()

def run():
    read_quotes()
    today = get_day_of_week()
    if today == 1:
        print (f'Today is the day to send email!')
        send_email(get_random_quote())
    else:
        print (f'Today is not the day to send email!')
        print (f'Today is {today}')
        print (f"Let's give you a quote anyway")
        print (f"{get_random_quote()}")

def send_email(quote):
    my_email = os.environ['EMAIL_ADDRESS']
    password = os.environ['EMAIL_PASSWORD']
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject: Motivational Quote\n\n{quote}')
        

run()
