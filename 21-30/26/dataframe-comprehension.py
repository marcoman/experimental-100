'''
Here we test some dataframe comprehensions
'''

import pandas as pd
import random

# Create a dictionary of students for later processing
student_dict = {
    'student': ['Marco', 'Beth', 'Xavier', 'Zerlina', 'Claudia', 'Chica', 'Texy', 'Rocky', 'Churro', 'Bla Bla'],
    'score': [random.randint(1, 100) for _ in range(10)],
}


print (f'Dict is: {student_dict}')

# dict operations, show the values of each type
print('keys')
for (key, value) in student_dict.items():
    print(key)

print('values')
for (key, value) in student_dict.items():
    print(value)

print('items')
for (key, value) in student_dict.items():
    print(f'{key} : {value}')

student_df = pd.DataFrame(student_dict)
print (f'DataFrame is: {student_df}')

# let's loop through the dataframe

for (key, value) in student_df.items():
    print(f'key: {key} value: {value}')

# now, loop using the dataframe's iterator
for (index, row) in student_df.iterrows():
    print(f'index: {index} row: {row}')

for (index, row) in student_df.iterrows():
    print(f'index: {index} student: {row["student"]}')
    print(f'index: {index} score: {row["score"]}')

for (index, row) in student_df.iterrows():
    if row.student == 'Marco':
        print(f"Marco's score is {row.score}")
