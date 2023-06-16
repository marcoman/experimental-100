'''
Here we test examples of dictionary comprehension
'''
import random

names = ['Bob', 'Angel', 'Jimi', 'Alan', 'Ada']
full_names = ['Bob Martin', 'Angel Harlem', 'Jimi Hendrix', 'Alan Turing',
              'Ada Lovelace']

# create a dict with an assignment of random numbers for each name

names_dict = {name: random.randint(70, 100) for name in names}

print(names_dict)

# I can see from the coursework that PyCharm is pretty good with showing variables with a CLI invocation of python
# I found an interactive CLI for VS Code.  Pretty neat.

high_scores = {name: score for name, score in names_dict.items() if score > 80}
print(high_scores)
