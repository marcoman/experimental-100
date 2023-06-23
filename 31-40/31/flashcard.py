import tkinter
import random
import pandas as pd

class FlashCard:
    BACKGROUND_COLOR = "#B1DDC6"  
    PADDING = 50
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 800
    CANVAS_HEIGHT = 526
    CANVAS_WIDTH = 800
    TEXT1_FORMAT = ('Arial', 40, 'italic')
    TEXT2_FORMAT = ('Arial', 60, 'bold')

    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    WHITE = '#ffffff'
    BLACK = '#000000'

    TEXT1_X = 400-160
    TEXT1_Y = 150
    TEXT2_X = 400-150
    TEXT2_Y = 300

    SLEEP_TIMER = 3000

    mode = 'French'

    def __init__(self):
        super().__init__()
        self.count_right = 0
        self.count_wrong = 0
        self.words_known = []
        self.words_unknown = []
        self.word = None
        self.mywindow = tkinter.Tk()
        self.mywindow.title("Flash Card")
        self.mywindow.config(padx=self.PADDING, pady=self.PADDING, height=self.WINDOW_HEIGHT, width=self.WINDOW_WIDTH, bg=self.BACKGROUND_COLOR)
        self.mywindow.resizable(False, False)

        self.myimage_front = tkinter.PhotoImage(file="./images/card_front.png")
        self.myimage_back = tkinter.PhotoImage(file="./images/card_back.png")
        
        self.mycanvas = tkinter.Canvas(self.mywindow, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.mycanvas_image = self.mycanvas.create_image(int(self.CANVAS_WIDTH/2), int(self.CANVAS_HEIGHT/2), image=self.myimage_front)
        self.mycanvas.config(bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.mycanvas.grid(row=0, column=0, columnspan=2)
        self.mycanvas.create_text(self.CANVAS_WIDTH/2, 150, 
                                  text="French", font=self.TEXT1_FORMAT, fill=self.BLACK, tags='Language')
        self.mycanvas.create_text(self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2, 
                                  text="Word", font=self.TEXT2_FORMAT, fill=self.BLACK, tags='Word')

        self.wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
        self.right_image = tkinter.PhotoImage(file="./images/right.png")
        self.wrong_button = tkinter.Button(self.mywindow, image=self.wrong_image, 
                                           highlightthickness=0, command=self.wrong_button_clicked)  
        self.right_button = tkinter.Button(self.mywindow, image=self.right_image, 
                                           highlightthickness=0, command=self.right_button_clicked)  
        self.wrong_button.grid(row=1, column=0)
        self.right_button.grid(row=1, column=1)

        self.save_button = tkinter.Button(self.mywindow, text="Save", command=self.save_words)
        self.save_button.grid(row=2, column=1)

    def run(self):
        self.read_words()
        self.display_word()
        self.mywindow.mainloop()

    def set_random_word(self):
        self.random_word = random.choice(list(self.words_unknown))
        self.f_word = self.random_word['French']
        self.e_word = self.random_word['English']
    
    def display_word(self):
        if self.mode == 'French':
            self.set_random_word()
            self.mycanvas.itemconfig(self.mycanvas.find_withtag("Language"), text=self.mode, fill=self.BLACK)
            self.mycanvas.itemconfig(self.mycanvas.find_withtag("Word"), text=self.f_word, fill=self.BLACK)
            self.mode = 'English'
            self.mytimer = self.mywindow.after(self.SLEEP_TIMER, self.display_word)
            self.mycanvas.itemconfig(self.mycanvas_image, image=self.myimage_front)
        else:
            self.mycanvas.itemconfig(self.mycanvas.find_withtag("Language"), text=self.mode, fill=self.WHITE)
            self.mycanvas.itemconfig(self.mycanvas.find_withtag("Word"), text=self.e_word, fill=self.WHITE)
            self.mode = 'French'
            self.mycanvas.itemconfig(self.mycanvas_image, image=self.myimage_back)

        
    def read_words(self):
        try:
            with open("./data/unknown.csv") as f:
                panda_data = pd.read_csv(f)
                self.words_dict = panda_data.to_dict()
                self.words_unknown = panda_data.to_dict(orient='records')
                print (self.words_unknown)
            with open("./data/known.csv") as f:
                panda_data = pd.read_csv(f)
                self.words_dict = panda_data.to_dict()
                self.words_known = panda_data.to_dict(orient='records')
                print (self.words_known)
                
        except FileNotFoundError:
            print("starting from scratch")

            try:
                with open("./data/french_words.csv") as f:
                    panda_data = pd.read_csv(f)
                    self.words_dict = panda_data.to_dict()
                    self.words_unknown = panda_data.to_dict(orient='records')
                    print (self.words_unknown)
                    self.words_known = []
                    self.save_words
            except FileNotFoundError:
                print("No initial file.  Need to quit")
        else:
            pass



    def wrong_button_clicked(self):
        self.mywindow.after_cancel(self.mytimer)
        self.count_wrong += 1
        print(self.count_wrong)
        self.add_word_to_list(self.words_unknown)
        self.display_word()

    def right_button_clicked(self):
        self.mywindow.after_cancel(self.mytimer)
        self.count_right += 1
        print(self.count_right)
        self.add_word_to_list(self.words_known)
        self.remove_from_unknown()
        self.mode = 'French'
        self.display_word()

    def add_word_to_list(self, mylist):
        mylist.append(self.random_word)

    def remove_from_unknown(self):
        # remove word from l ist
        self.words_unknown.remove(self.random_word)


    def save_words(self):
        with open("./data/known.csv", 'w') as f:
            panda_data = pd.DataFrame(self.words_known)
            panda_data.to_csv(f, index=False)

        with open("./data/unknown.csv", 'w') as f:
            panda_data = pd.DataFrame(self.words_unknown)
            panda_data.to_csv(f, index=False)

myflash = FlashCard()
myflash.run()

