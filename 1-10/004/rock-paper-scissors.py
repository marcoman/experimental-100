import random

# Rock Paper Scissors


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

mychoice = int(input('What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if (mychoice < 0 or mychoice > 2):
    print('Invalid input')
elif mychoice  == 0:
    print(rock)
elif  mychoice == 1:
    print(paper)
elif mychoice == 2:
    print(scissors)

outcomes = ["rock", "paper", "scissors"]

botchoice =  random.randint(0,2)

print(f'Computer chose {outcomes[botchoice]}') 

if botchoice == 0:
    print(rock)
    if mychoice == 0:
        print('Draw')
    elif mychoice == 1:
        print('You win')
    elif mychoice == 2:
        print('You lose')
elif botchoice == 1:
    print(paper)
    if mychoice == 0:
        print('You lose')
    elif mychoice == 1:
        print('Draw')
    elif mychoice == 2:
        print('You win')
elif botchoice == 2:
    print(scissors)
    if mychoice == 0:
        print('You win')
    elif mychoice == 1:
        print('You lose')
    elif mychoice == 2:
        print('Draw')

