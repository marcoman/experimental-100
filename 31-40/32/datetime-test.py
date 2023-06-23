'''
Here, we do some tests with the datetime module.
'''

import datetime as dt

# print the time in full detail.
now = dt.datetime.now()
print(f'The current time is now {now}')

# Let's extract different fields from the time.

year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print (f"The year is {year} and it's type is {type(year)}")
print (f"The month is {month} and it's type is {type(month)}")
print (f"The day is {day} and it's type is {type(day)}")
print (f"The day of the week is {day_of_week} and it's type is {type(day_of_week)}")