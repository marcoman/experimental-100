import tkinter as tk
import wonderwords

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


# This is test script 
def test_word_generator():
    print(WordGenerator.generate_word())
    for word in WordGenerator.generate_words(20):
        print(word)
    print(WordGenerator.generate_sentence())

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
        self.characters_typed = 0
        self.total_words = 0
        self.wpm = 0

        # Define the application window and layout
        self.mywindow = tk.Tk()
        self.mywindow.title("Typing Challenge")
        self.mywindow.minsize(width=500, height=500)
        self.mywindow.config(padx=20, pady=20)

        # First row
        self.l_instructions = tk.Label(text="Press 'Start' button to begin")
        self.button = tk.Button(text="Start", command=self.toggle_timer)
        self.l_instructions.grid(row=0, column=0)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        # Second row
        self.l_sample_instructions = tk.Label(text="This is what you type:")
        self.l_sample = tk.Label(text="Test Text")
        self.l_sample_instructions.grid(row=1, column=0, padx=10, pady=10)
        self.l_sample.grid(row=1, column=1, padx=10, pady=10)

        # Third row
        self.l_test_instructions = tk.Label(text="Enter your text here:")
        self.l_test = tk.Label(text="<YOUR INPUT IS SHOWN HERE.")
        self.l_test_instructions.grid(row=2, column=0, padx=10, pady=10)
        self.l_test.grid(row=2, column=1, padx=10, pady=10)

        # Fourth row
        self.l_stats = tk.Label(text=f"Time={self.elapsed_seconds}" + 
                              f"\nWPM={self.wpm}" +
                              f"\nCorrect={self.correct_words}" +
                              f"\nIncorrect={self.incorrect_words}",
                              anchor="w", justify="left"
                              )
        self.l_stats.grid(row=3, column=0)
        pass

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

    def  update_test(self):
        newtext = ''
        for sentence in WordGenerator.generate_sentences(4):
            newtext += sentence + ' '
        self.l_test.config(text=newtext)

    def update_stats(self):
        if self.elapsed_seconds > 0:
            self.wpm = (self.correct_words + self.incorrect_words) / self.elapsed_seconds * 60
        else:
            self.wpm = 0
        self.correct_words = 0
        self.incorrect_words = 0
        self.wpm = 0
        self.l_stats.config(text=f"Time={self.elapsed_seconds}" +
                              f"\nWPM={self.wpm}" +
                              f"\nCorrect={self.correct_words}" +
                              f"\nIncorrect={self.incorrect_words}",
                              anchor="w", justify="left"
                              )

myTypingTest = TypingTest()
myTypingTest.run()
