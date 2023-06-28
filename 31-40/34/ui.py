'''
This is the user interface for the quiz application.
'''
import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
PADDING = 20
QUESTION_WIDTH = 300
QUESTION_HEIGHT = 250
QUESTION_FONT = ("Arial", 20, "italic")
QUESTION_BACKGROUND = 'white'

class QuizInterface:
    # Today I was reminded how we can delcare the type of the data we supply to a method.
    def __init__(self, quiz_brain: QuizBrain):

        self.quizbrain = quiz_brain

        # Window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # Top row - the score
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Middle -the question
        self.canvas = tk.Canvas(width=QUESTION_WIDTH, height=QUESTION_HEIGHT, bg=QUESTION_BACKGROUND)
        self.question_text = self.canvas.create_text(150, 125, width=QUESTION_WIDTH - 2*PADDING, text="Some Question Text", fill=THEME_COLOR, font=QUESTION_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PADDING)

        # Bottom - the buttons
        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0) 
        self.false_button.grid(row=2, column=1)

        # Now, load up our QuizBrain with data.
        self.get_next_question()

        # Run the program
        self.window.mainloop()

    def true_pressed(self):
        self.give_feedback(self.quizbrain.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quizbrain.check_answer("False"))

    def get_next_question(self):
        question = self.quizbrain.next_question()
        self.canvas.itemconfig(self.question_text, text=question)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.update_score)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quizbrain.score}")
        self.canvas.config(bg=QUESTION_BACKGROUND)
        if self.quizbrain.still_has_questions():
            self.get_next_question()
