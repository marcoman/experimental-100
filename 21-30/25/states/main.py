import turtle
import pandas as pd


class US_States(turtle.Turtle):
    IMAGE_PATH = "blank_states_img.gif"
    STATES_PATH = "50_states.csv"
    def __init__(self, name):
        super().__init__()
        self.incorrect_guesses = []
        self.correct_guesses = []
        self.name = name
        self.myscreen = turtle.Screen()
        self.myscreen.addshape(self.IMAGE_PATH)
        self.shape(self.IMAGE_PATH)
        self.cursor = turtle.Turtle()

    def place_text(self, x, y, text):
        self.cursor.penup()
        self.cursor.goto(x, y)
        self.cursor.write(text, move=False)

    def get_mouse_click_coor(self, x, y):
        print(x, y)

    def setup(self):
        self.correct_guesses.clear()
        self.myscreen.onscreenclick(self.get_mouse_click_coor)
        self.states = self.load_states()
        self.states_list = self.states.state.to_list()

    def get_input(self):
        user_answer = self.myscreen.textinput(title="Guess the State", prompt="What's another state's name?")
        return user_answer
    
    def save_game(self):
        df = pd.DataFrame(self.correct_guesses)
        df.to_csv("correct_guesses.csv")
        df = pd.DataFrame(self.incorrect_guesses)
        df.to_csv("incorrect_guesses.csv")
        df = pd.DataFrame(self.states_list)
        df.to_csv("states_list.csv")
        df = pd.DataFrame(self.states)
        df.to_csv("states.csv")

        # missing_states = []
        # for state in self.states_list:
        #     if state not in self.correct_guesses:
        #         missing_states.append(state)

        # This next line should replace the 4 above by utilizing list comprehension
        missing_states = [state for state in self.states_list if state not in self.correct_guesses]

        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")

        print("Game saved")
        print(f'Correct guesses {self.correct_guesses}')
        print(f'Incorrect guesses {self.incorrect_guesses}')
        print(f'Total guesses {len(self.correct_guesses) + len(self.incorrect_guesses)}')

        self.myscreen.bye()
    
    def run_quiz(self):
        self.setup()
        while len(self.correct_guesses) < 50:
            user_answer = str(self.get_input()).title()
            print(f'Guessing {user_answer}')
            if user_answer == "Exit":
                print("Game over")
                print(f'Correct guesses {self.correct_guesses}')
                print(f'Incorrect guesses {self.incorrect_guesses}')
                print(f'Total guesses {len(self.correct_guesses) + len(self.incorrect_guesses)}')
                break
            else:
                if user_answer in self.states_list:
                    if user_answer not in self.correct_guesses:
                        print("Correct!")
                        state_info = self.states[self.states.state == user_answer]
                        self.place_text(x= int(state_info.x),
                                        y = int(state_info.y),
                                        text = user_answer)
                        self.correct_guesses.append(user_answer)
                    else:
                        print("Already guessed")
                else:
                    print("Not a valid state")
                    self.incorrect_guesses.append(user_answer)
            print(f'guess count {len(self.correct_guesses)} {len(self.incorrect_guesses)}')

        self.save_game()


    def initialize_game(self):
        self.correct_guesses.clear()
        self.incorrect_guesses.clear()

    def load_states(self):
        with open(self.STATES_PATH) as f:
            df = pd.read_csv(f)
        return df

mystates = US_States("USA! USA! USA!")
mystates.setup()
mystates.run_quiz()

mystates.myscreen.mainloop()
#mystates.myscreen.exitonclick()