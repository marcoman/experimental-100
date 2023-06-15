
# similar to banker roulette, but we pick somebody to pay the bill.

import random
people = input("Please enter the name of people, separated by commas: ")

peoplelist = people.split(",")

count = len(peoplelist)
myrandom = random.randint(0, count-1)
print (f'The victim is {peoplelist[myrandom]}')
