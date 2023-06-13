import random

WELCOME_MESSAGE = "Welcome to the Number Guessing Game!"
INSTRUCTIONS = "I'm thinking of a number between 1 and 100."
CHOOSE_NUMBER = "Choose a number between 1 and 100: "
TOO_HIGH = "Too high."
TOO_LOW = "Too low."



def generate_random_number():
    return random.randint(1, 100)

playing = True

print(WELCOME_MESSAGE)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid input")
    playing = False

print(INSTRUCTIONS)

random_number = generate_random_number()

while playing:
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        playing = False
        break

    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input(CHOOSE_NUMBER))
    if guess == random_number:
        print("You got it!")
        playing = False
        break
    elif guess > random_number:
        print(TOO_HIGH)
    else:
        print(TOO_LOW)
    attempts -= 1

