'''
This file is the assignment where we will translate regular names into NATO letters.  For example, A=Alpha, B=Bravo, etc.
'''
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(f'Student name is {row.student} and score is {row.score}')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv") as file:
    phonetic_data = pandas.read_csv(file)

# This creates a dict with the NATO phonetics.
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}
print(phonetic_dict)

def get_phonetics(word):
    word_list= []
    for letter in word:
        word_list.append(phonetic_dict[letter.upper()])
    return word_list

phonetic_code_word_list = []
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
for (index, row) in student_data_frame.iterrows():
    phonetic_code_word_list.append(get_phonetics(row.student))
print (phonetic_code_word_list)


keep_asking = True
while keep_asking:
    user_input = input("Enter a word: ").upper()
    if user_input == "EXIT":
        keep_asking = False
    else:
        print (get_phonetics(user_input ))