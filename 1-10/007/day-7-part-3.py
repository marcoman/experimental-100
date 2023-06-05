#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

number_errors = 0
while number_errors < 5 and '_' in display:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    guessed_correctly = False
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter
            guessed_correctly = True
    if guessed_correctly is False:
        print(f'You did not guess correctly, {5-number_errors-1} tries left')
        number_errors += 1
    else:
        print(f'You guessed correctly')
    print(display)

if number_errors < 5:
    print(
        f'Congratulations, you correctly guess {chosen_word} with {5 - number_errors -1 } guesses remaining'
    )
else:
    print(f'Sorry, you did not guess {chosen_word}')
