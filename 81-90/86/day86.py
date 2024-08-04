import tkinter as tk
import wonderwords
import math

ONE_SECOND = 1000


class WordGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_word():
        return wonderwords.RandomWord().word(include_parts_of_speech=["nouns"]).lower()
    
    @staticmethod
    def generate_words(num_words):
        return [wonderwords.RandomWord().word(include_parts_of_speech=["nouns"]).lower() for _ in range(num_words)]
    
    @staticmethod
    def generate_sentence():
        return wonderwords.RandomSentence().sentence().lower()
    
    @staticmethod
    def generate_sentences(num_sentences):
        return [wonderwords.RandomSentence().sentence().lower() for _ in range(num_sentences)]

class TypingTest:

    def __init__(self) -> None:
        self.mywords =  WordGenerator.generate_words(200)
        self.mysentences = WordGenerator.generate_sentences(200)

        self.timer_on = False
        self.timer = None

        self.elapsed_seconds = 0
        self.correct_words = 0
        self.incorrect_words = 0
        self.correct_letters = 0
        self.incorrect_letters = 0
        self.characters_typed = []
        self.characters_count = 0
        self.total_words = 0
        self.wpm = 0

        # Define the application window and layout
        self.mywindow = tk.Tk()

        self.mywindow.title("Typing Challenge")
        self.mywindow.minsize(width=500, height=500)
        self.mywindow.config(padx=20, pady=20)

        # First row - The instructions
        self.l_instructions = tk.Label(text="Press 'Start' button to begin")
        self.button = tk.Button(text="Start", command=self.toggle_timer)
        self.l_instructions.grid(row=0, column=0)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        # Second row - The text prompt and button
        self.l_prompt = tk.Label(text="This is what you type:")
        self.l_prompt_example = tk.Label(text="Test Text")
        self.l_prompt.grid(row=1, column=0, padx=10, pady=10)
        self.l_prompt_example.grid(row=1, column=1, padx=10, pady=10)

        # Third row - The text we type in
        self.l_test_instructions = tk.Label(text="Enter your text here:")
        self.l_test = tk.Label(text="<YOUR INPUT IS SHOWN HERE.")
        self.l_test_instructions.grid(row=2, column=0, padx=10, pady=10)
        self.l_test.grid(row=2, column=1, padx=10, pady=10)

        # Fourth row - our running stats
        self.l_stats = tk.Label(text=f"Time={self.elapsed_seconds}" + 
                              f"\nWPM={self.wpm}" +
                              f"\nCorrect={self.correct_words}" +
                              f"\nIncorrect={self.incorrect_words}",
                              anchor="w", justify="left"
                              )
        self.l_stats.grid(row=3, column=0)

        # Accept keyboard input
        self.mywindow.bind('<Key>', self.key_handler)
 
    def run(self):
        self.mywindow.mainloop()

    def toggle_timer(self):
        # IF the timer is not on, turn it on and start the timer
        if not self.timer_on:
            self.start_timer()
        else:
            self.stop_timer()

    def start_timer(self):
        print("Timer started")
        self.timer_on = True
        self.update_test()
        self.update_timer()

    def stop_timer(self):
        print("Timer stopped")
        self.timer_on = False
        self.mywindow.after_cancel(self.timer)

    def update_timer(self):
        if self.timer_on:
            print(f"update time {self.elapsed_seconds}")
            self.elapsed_seconds += 1
            self.update_stats()
            self.timer = self.mywindow.after(ONE_SECOND, self.update_timer)

    def key_handler(self, event):
        # Print the incoming text
        print (event.char, event.keysym, event.keycode)
        # Always increment our keystroke count

        # adjust our list as needed, based on what we type in
        # If event.car is the delete character, let's delete an item from  list named characters_typed
        if ((event.keysym == "Shift_L") or
            (event.keysym == "Shift_R`") or
            (event.keysym == "Control_L") or
            (event.keysym == "Control_R") or
            (event.keysym == "Alt_L") or
            (event.keysym == "Alt_R")):
            pass
        else:
            if event.keysym == "BackSpace":
                self.characters_typed.pop()
            elif event.keycode == 65:
                self.characters_typed.append(' ')
            else:
                self.characters_typed.append(event.char)

            self.characters_count += 1
            self.update_text_displayed()
            self.update_stats()
    
    def update_test(self):
        newtext = ''
        for sentence in WordGenerator.generate_sentences(4):
            newtext += sentence + '\n'
        self.l_prompt_example.config(text=newtext)

    def update_text_displayed(self):
        self.l_test.config(text= ''.join(str(e) for e in self.characters_typed))

    def update_stats(self):
        print ("updating stats")
        self.correct_words = 0
        self.incorrect_words = 0

        correct_letters = 0
        incorrect_letters = 0

        length = min(len(self.l_prompt_example.cget('text')), len(self.l_test.cget('text')))
        for i in range(length):
            if self.l_prompt_example.cget('text')[i] == self.l_test.cget('text')[i]:
                correct_letters += 1
            else:
                incorrect_letters += 1

        for word in self.l_prompt_example.cget('text').split():
            if word in self.l_test.cget('text').split():
                self.correct_words += 1
            else:
                self.incorrect_words += 1

        for l in self.characters_typed:
            if l == ' ':
                self.total_words += 1

        if self.elapsed_seconds > 0:
            self.wpm = (self.correct_words + self.incorrect_words) / self.elapsed_seconds * 60
        else:
            self.wpm = 0
        self.l_stats.config(text=f"Time={self.elapsed_seconds}" +
                              f"\nWPM={self.wpm}" +
                              f"\nCorrect={self.correct_words}" +
                              f"\nIncorrect={self.incorrect_words}",
                              anchor="w", justify="left"
                              )

myTypingTest = TypingTest()
myTypingTest.run()
