import random
import os

import art
import game_data

class Game:
    
    GREETING = "Welcome to the higher/lower game"
    LOGO = art.logo
    VS = art.vs
    ACCOUNT_A_TEXT = "Compare A: "
    ACCOUNT_B_TEXT = "Compare B: "
    SCORE_TEXT = "Score: "
    WIN_TEXT = "You win!"
    LOSE_TEXT = "You lose!"
    GAME_OVER_TEXT = "Game over!"
    GAME_OVER_SCORE_TEXT = "Your final score was: "

    def __init__(self):
        self.score = 0
        self.game_over = False
        self.account_a = self.get_random_account()
        self.account_b = self.get_random_account()

    def get_account_a(self):
        return self.account_a

    def get_account_b(self):
        return self.account_b

    def get_score(self):
        return self.score

    def is_game_over(self):
        return self.game_over

    def set_account_a(self, account):
        self.account_a = account

    def set_account_b(self, account):
        self.account_b = account

    def set_score(self, score):
        self.score = score

    def set_game_over(self, game_over):
        self.game_over = game_over

    def get_account_data(self, account):
        return account['name'], account['description'], account['country']

    def get_account_name(self, account):
        return account['name']
    
    def get_random_account(self):
        """Get data from random account"""
        return random.choice(game_data.data)
    
    def print_account_data(self, account):
        print (f"{account['name']} from {account['country']} has {account['follower_count']} followers and is a {account['description']}")
    
    def print_welcome(self):
        print (self.LOGO)
        print (self.GREETING)

    def is_correct (self, answer):
        avalue = self.get_account_a()['follower_count']
        bvalue = self.get_account_b()['follower_count']

        # print (f'a is {avalue}, b is {bvalue}')
        if answer == 'A' and avalue > bvalue:
            return True
        elif answer == 'B' and bvalue > avalue:
            return True
        else:
            return False

    def play_game(self):
        playing = True
        self.print_welcome()

        while playing:
            # show the first with data

            self.print_account_data(self.account_a)
            # Show the second
            print (f'Who has more followers?  \n\tA: {self.get_account_name(self.account_a)} or  B: {self.get_account_name(self.account_b)}?')

            # get the answer from the user
            answer = input("Type 'A' or 'B': ").upper()

            # check if the answer is correct
            if self.is_correct(answer):
                # increase the score
                self.score += 1
                print (f'Correct! Current score: {self.score}')
                # reallocate accounts
                self.account_a = self.account_b
                # get a new account
                self.account_b = self.get_random_account()
            else:
                # end the game
                playing = False
                print (f'Incorrect! Current score: {self.score}')
                print (self.GAME_OVER_TEXT)
                print (self.GAME_OVER_SCORE_TEXT, self.score)
            

mygame = Game()
mygame.play_game()
    
