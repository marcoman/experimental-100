import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

class Cards:
    suits = ["diamond", "heart", "spade", "club"]
    ranks = [['2', 2],
             ['3', 3],
             ['4', 4],
             ['5', 5],
             ['6', 6],
             ['7', 7],
             ['8', 8],
             ['9', 9],
             ['10', 10],
             ['J', 10],
             ['Q', 10],
             ['K', 10],
             ['A', 11]]
    mydeck = []

    def __init__(self):
        for i in self.suits:
            for j in self.ranks:
                self.mydeck.append([j, i])
        random.shuffle(self.mydeck)

    def print_deck(self):
        print(self.mydeck)

    def print_hello(self):
        print("Hello.  Welcome to the game")
    
    def deal_card(self):
        return self.mydeck.pop()

    def card_status(self, card):
        return (f'{card[0][0]} of {card[1]}')
    
    def print_hand(self, cards):
        myhand = '('
        for i in cards:
            myhand += f'{self.card_status(i)}, '
        return myhand + ')'
    
    def calc_score(self, cards):
        score = 0
        for i in cards:
            rank = i[0][0]
            score += int(i[0][1])
            if rank == 'A':
                # print ("Ace is 1 or 11")
                if score > 21:
                    # print ("Ace is 1")
                    score -= 10
                elif score == 21:
                    print ("Blackjack")
                else:
                    pass
                    # print ("Ace is 11")
        return int (score)
    
    def ace_in_the_hole(self, cards):
        for i in cards:
            if i[0][0] == 'A':
                return True
        return False


mycards = Cards()

cards_dealer = []
cards_player = []

mycards.print_hello()
# mycards.print_deck()

keep_playing = True
playing = False

while keep_playing == True:
    if playing == True:
        print (f'You have {str(len(cards_player))} cards {mycards.print_hand(cards_player)}, score = {mycards.calc_score(cards_player)}.')
        choice = input(f'hit or stay? (h/s) \n')
        if choice == "h":
            newcard = mycards.deal_card()
            print(f'You drew {mycards.card_status(newcard)}.')
            cards_player.append(newcard)
            # print(f'You have {str(len(cards_player))} cards showing {cards_player}.')
            if mycards.calc_score(cards_player) > 21:
                # print("BUST!")
                keep_playing = False
                playing = False

            elif mycards.calc_score(cards_player) < 21:
                # print("Your new score is " + str(mycards.calc_score(cards_player)))
                pass

            elif mycards.calc_score(cards_player) == 21:
                print("Blackjack!")
                keep_playing = False
                playing = False   

            if len(cards_player) == 5:
                print("You win!")
                keep_playing = False
                playing = False
        elif choice == "s":
            print("You stay")
            keep_playing = False
            playing = False
        else:
            print("Invalid input")
    else:

        choice = input("Do you want to play? (y/n)")

        if choice == "y" and playing == False:
            print ('Dealing cards')
            playing = True
            cards_dealer.append(mycards.deal_card())
            cards_player.append(mycards.deal_card())
            cards_dealer.append(mycards.deal_card())
            cards_player.append(mycards.deal_card())
            # print (f'You have {str(len(cards_player))} cards showing {cards_player}.')
        elif choice == "n":
            keep_playing = False
            playing = False
        else:
            print("Invalid input")

while mycards.calc_score(cards_dealer) < 17:
    print (f'Dealer has {str(len(cards_dealer))} cards {mycards.print_hand(cards_dealer)}, score = {mycards.calc_score(cards_dealer)}.')

    newcard = mycards.deal_card()
    print(f'Dealer drew {mycards.card_status(newcard)}.')
    cards_dealer.append(newcard)
    dealer_score = mycards.calc_score(cards_dealer)
    if dealer_score > 21:
        # print("DEALER BUST!")
        keep_playing = False
        playing = False

    elif dealer_score < 21:
        print("Dealer's new score is " + str(dealer_score))

    elif dealer_score == 21:
        print("DEALER Blackjack!")
        keep_playing = False
        playing = False

dealer_score = mycards.calc_score(cards_dealer)
player_score = mycards.calc_score(cards_player)

if dealer_score > player_score:
    if dealer_score > 21:
        print("Dealer BUST!")
        if player_score == 21:
            print("Player wins! Blackjack!")
        elif player_score < 21:
            print("Player wins!")
    elif dealer_score <= 21:
        print("Dealer wins!")
    else:
        print ("Not possible -1 ")

elif dealer_score == player_score:
    if mycards.ace_in_the_hole(cards_dealer) == True:
        print("Dealer wins!")
    elif mycards.ace_in_the_hole(cards_player) == True:
        print("Player wins!")
    else:
        print("Push")

elif dealer_score < player_score:
    if player_score > 21:
        print("Player BUST!")
        if dealer_score == 21:
            print("Dealer wins! Blackjack!")
        elif dealer_score < 21:
            print("Dealer wins!")
    elif player_score == 21:
        print("Player wins - BLACKJACK!")
    elif player_score < 21:
        print("Player wins!")
    else:
        print ("Not possible -2 ")
