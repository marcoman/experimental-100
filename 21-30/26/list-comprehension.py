'''
This test file is about list comprehensions

Create a list from an existing list
'''

import random

# consider the case where we take a list of number, and create a new list that scales the first by (for example) 2

first_list = [1, 2, 3, 4, 5]
second_list = [x * 2 for x in first_list]

print (f'First list {first_list}')
print (f'Second list {second_list}')

# experiment some more with list comprehension

# use methods to alter the list
third_list = [x * random.randint(1, 50) for x in first_list]
fourth_list = [x % 5 for x in third_list]

print (f'Third list {third_list}')
print (f'Fourth list {fourth_list}')

# create a list with range, and then test it
fifth_list = [x for x in range(1, 100) if x % 5 == 0]
print (f'Fifth list {fifth_list}')


# filter down to a subset
names = ["Marco", "Beth", "Claudia", "Zerlina", "Xavier"]
short_names = [name for name in names if len(name) < 5]
long_names = [name for name in names if len(name) > 5]
print (f'Short names {short_names}')
print (f'Long names {long_names}')


# square numbers
numbers1 = [x for x in range(1, 20)]
numbers1_squared = [x ** 2 for x in numbers1]
print (f'Numbers1 {numbers1}')
print (f'Numbers1 squared {numbers1_squared}')