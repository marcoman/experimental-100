# Use this page for reference:

# https://en.wikipedia.org/wiki/Morse_code

# The requirements:
# - Take a text based input
# - Convert it to morse
# - Output the results


import csv

# First, Let's find a text-based morse list
# I found: http://www.csgnetwork.com/morsecodechrtbl.html

# See the file morse.csv for the details

# Next, let's absorb the list into an array.  Stary by reading in the CSV file
morse_dict = []
with open('morse.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        morse_dict.append(row)
        print(', '.join(row))

# Next, let's absorb the list into an array.  Start by reading in the CSV file
# Next, collect input strings from the command-line (gets)
myinput = input("Please enter a string to convert to morse:")
m_array = list(myinput)

# For each letter in the input, render the morse output
res = []
for char in m_array:
    # print(char)
    # lookup the character in the array
    res += [row[1] for row in morse_dict if row[0] == char.upper()]
print (res)
print (' '.join(res))

# Present the information to the user.
# Present the results to the user.
