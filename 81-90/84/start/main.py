
# start by asking people for their names

# define a data structure for our tic-tac-toe
# This all feels like a class:
    # create a method to clear the screen.
    # create a method to let the person add their part.
    # create a method to prompt the user
    # create a method to display the playing area


class PlayingArea:
    board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]

    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        pass

class TicTacToe:
    
    myarena = PlayingArea()
    player1 = ''
    player2 = ''
    gameon = False

    def __init__(self) -> None:
        self.myarena.initialize()
        self.gameon = False

    def display(self):
        print(f' {self.myarena.board[0][0]} | {self.myarena.board[0][1]} | {self.myarena.board[0][2]} ')
        print(f'------------')
        print(f' {self.myarena.board[1][0]} | {self.myarena.board[1][1]} | {self.myarena.board[1][2]} ')
        print(f'------------')
        print(f' {self.myarena.board[2][0]} | {self.myarena.board[2][1]} | {self.myarena.board[2][2]} ')

        # for line in self.myarena.board:
        #     print (''.join(str(l) for l in line))

    def get_player_names(self):
        self.player1 = input("What is the name of the first player (X) ? ")
        self.player2 = input("What is the name of the second player (O) ? ")

    def start_game(self):
        print(f'Player 1 (X) is named {self.player1}')
        print(f'Player 2 (O) is named {self.player2}')
        self.display()


    def prompt_player(self, mark):
        answer = 'n'
        player_name = ''
        if (mark == 'X'):
            player_name = self.player1
        else:
            player_name = self.player2

        while (answer != 'y'):
            try:
                row = int(input(f'\t##{player_name}##, where do you want to place your {mark} as "(row) "? '))
            except ValueError:
                print('Please enter a number')
                continue

            try:            
                col = int(input(f'\t##{player_name}##, where do you want to place your {mark} as "(col) "? '))
            except ValueError:
                print('Please enter a number')
                continue
            
            answer = input(f'You entered row={row}, col={col}.  Is this correct? (y/n) ')
            if (answer == 'y'):
                if (self.is_selection_valid(row,col)):
                    self.commit_answer(row, col, player_name, mark)
                else:
                    print(f'Your selection of ({row}, {col}) is not valid. Please try again.')
                    answer = 'n'
            else:            
                print('Please try again')
                continue

                # except ValueError:

    def is_selection_valid(self, row, col):
        if ((row < 0) or
            (row > 2) or
            (col < 0) or
            (col > 2)
            ):
            print(f'The inputs {row}, {col} are false')
            return False
        # raise Exception('Selection is not valid')
        elif (self.myarena.board[row][col] != '.'):
            print(f'The spot {row}, {col} is already taken')
            return False
        else:
            return True

    def commit_answer(self, row, col, player, mark):
        print (f'\t\t{player} marks {row}, {col} as {mark}')
        self.myarena.board[row][col] = mark
        self.check_winner(player)
        self.display()

    def check_winner(self, player):
        if ((self.myarena.board[0][0] == self.myarena.board[0][1] == self.myarena.board[0][2] != '.') or
            (self.myarena.board[1][0] == self.myarena.board[1][1] == self.myarena.board[1][2] != '.') or
            (self.myarena.board[2][0] == self.myarena.board[2][1] == self.myarena.board[2][2] != '.') or
            
            (self.myarena.board[0][0] == self.myarena.board[1][0] == self.myarena.board[2][0] != '.') or
            (self.myarena.board[0][1] == self.myarena.board[1][1] == self.myarena.board[2][1] != '.') or
            (self.myarena.board[0][2] == self.myarena.board[1][2] == self.myarena.board[2][2] != '.') or

            (self.myarena.board[0][0] == self.myarena.board[1][1] == self.myarena.board[2][2] != '.') or
            (self.myarena.board[0][2] == self.myarena.board[1][1] == self.myarena.board[2][0] != '.')):
            self.gameon = False
            print (f'WINNER. Congratulations {player}')
            self.gameon = False


    def play_game(self):

        self.gameon = True
        self.get_player_names()
        self.start_game()

        mark = 'X'
        counter = 0

        while (self.gameon and counter < 9):
            self.prompt_player(mark)
            if (mark == 'X'):
                mark = 'O'
            else:
                mark = 'X'
            counter += 1
        print ('Game Over')
        self.gameon = False

mygame = TicTacToe()
mygame.play_game()