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

email_tls = os.environ.get("MAIL_TLS")
email_ssl = os.environ.get("MAIL_SSL")
email_sender = os.environ.get("MAIL_SENDER")
email_password= os.environ.get("MAIL_PASSWORD")
email_receiver = os.environ.get("MAIL_RECEIVER")
email_smtp = os.environ.get("MAIL_SMTP")


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
    with smtplib.SMTP(email_smtp, email_tls) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=email_password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs=email_receiver,
                            msg=f'Subject: Motivational Quote\n\n{quote}')
        

run()
