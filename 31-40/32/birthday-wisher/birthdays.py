import datetime as dt
import csv
import pandas as pd
import os
import random

class Birthdays:

    BIRTHDAYS_FILE = "birthdays.csv"
    LETTERS_DIRECTORY = 'letter_templates'

    def __init__(self):
        self.birthdays = None
        self.letters = []

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def load_letters(self):
        # open a file
        # read the items in as letters
        # create a data structure to hold the letters
        print(f'reading from {self.LETTERS_DIRECTORY}')
        filelist = [f for f in os.listdir(self.LETTERS_DIRECTORY) if os.path.isfile(os.path.join(self.LETTERS_DIRECTORY, f))]
        print(f'list of files is: {filelist}')

        for f in filelist:
            print(f'opening file {f}')
            with open (os.path.join(self.LETTERS_DIRECTORY, f), "r") as f:
                letter = f.read()
                self.letters.append(letter)
    
    def load_birthdays(self):
        # open a file
        # read the items in as letters
        # create a data structure to hold the letters
        print(f'reading from {self.BIRTHDAYS_FILE}')
        with open (self.BIRTHDAYS_FILE, "r") as f:
            # read the items in as letters
            # create a data structure to hold the letters
            self.birthdays = pd.read_csv(f, header=0)
    
    def find_birthdays_today(self):
        td = dt.datetime.now()

        today = self.birthdays[(self.birthdays['year'] == td.year) & 
                               (self.birthdays['month'] == td.month) & 
                               (self.birthdays['day'] == td.day)]

        return today

    def send_letter(self, name):
        # get the letter
        # send the letter
        letter = random.choice(self.letters)
        newletter = str(letter).replace('[NAME]', name).replace('Angela', 'Marco')
        print(newletter)

    def run(self):
        # run the program
        self.load_letters()
        # print (self.letters)

        self.load_birthdays()
        # print (self.birthdays)

        birthdays_today = self.find_birthdays_today()
        print (birthdays_today)

        bd_today = birthdays_today.to_dict('records')
        print (bd_today)
        for bd in bd_today:
            print (f'Sending birthday letter to {bd["name"]}')
            self.send_letter(bd["name"])

        
