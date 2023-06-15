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
                print ("Ace is 1 or 11")
                if score > 21:
                    print ("Ace is 1")
                    score -= 10
                elif score == 21:
                    print ("Blackjack")
                else:
                    print ("Ace is 11")
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
                print("BUST!")
                keep_playing = False
                playing = False

            elif mycards.calc_score(cards_player) < 21:
                print("Your new score is " + str(mycards.calc_score(cards_player)))

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
        print("DEALER BUST!")
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
    elif player_score <= 21:
        print("Player wins!")
    else:
        print ("Not possible -2 ")
    print("You win!")
