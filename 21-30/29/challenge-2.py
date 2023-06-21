import tkinter
import random
import string
from tkinter import messagebox
import pyperclip



# The challenge here is to create screen widgets with the following:
# Website - label & text input
# Username - label & text input
# Password - label and text <output>
# Submit - button


class MyPass():
    CANVAS_HEIGHT = 200
    CANVAS_WIDTH = 200
    PADDING = 20
    WINDOW_HEIGHT = CANVAS_HEIGHT + PADDING * 2
    WINDOW_WIDTH = CANVAS_WIDTH + PADDING * 2
    PASSWORD_LENGTH = 12
    default_username = ''
    newpassword = ''

    def __init__(self):
        # First
        # Create a window, and set the image to the middle, and have padding of 20 around it.

        self.mywindow = tkinter.Tk()
        self.mywindow.title("My Pass")
        self.mywindow.config(padx=100, pady=50, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)

        self.myimage = tkinter.PhotoImage(file="logo.png")

        self.mycanvas = tkinter.Canvas(self.mywindow, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.mycanvas.create_image(int(self.CANVAS_WIDTH/2), int(self.CANVAS_HEIGHT/2), image=self.myimage)
        self.mycanvas.grid(row=0, column=1)

        self.label_website  = tkinter.Label(self.mywindow, text="Website:")
        self.label_username = tkinter.Label(self.mywindow, text="Email/Username:")
        self.label_password = tkinter.Label(self.mywindow, text="Password:")
        self.label_website.grid(row=1, column=0)
        self.label_username.grid(row=2, column=0)
        self.label_password.grid(row=3, column=0)

        self.entry_website = tkinter.Entry(self.mywindow, width=35)
        self.entry_username = tkinter.Entry(self.mywindow, width=35)
        self.entry_password = tkinter.Entry(self.mywindow, width=23)
        self.entry_website.grid(row=1, column=1, columnspan=2)
        self.entry_username.grid(row=2, column=1, columnspan=2)
        self.entry_password.grid(row=3, column=1)

        self.button_generate = tkinter.Button(self.mywindow, text="Generate", command=self.generate_password)
        self.button_submit = tkinter.Button(self.mywindow, text="Submit", command=self.save_to_file)
        self.button_generate.grid(row=3, column=2)
        self.button_submit.grid(row=4, column=1)


    def save_to_file(self):
        '''
        Save the credentials to a file
        '''
        un = self.entry_username.get()
        pw = self.entry_password.get()
        ws = self.entry_website.get()

        if un == '' or pw == '' or ws == '':
            messagebox.showerror(title="Oops!", message="Please fill in all fields")
            return

        myanswer = messagebox.askyesnocancel (title="Correct?", message=f"Are Username: {un}\nPassword: {pw}\nWebsite: {ws} correct?")
        if myanswer == True:
            with open('passwords.txt', 'a') as f:
                f.write(f"{un},{pw},{ws}\n")
            self.default_username = un
            
            self.setup_screen()
        else:
            return



    def load_from_file():
        '''
        Load the credentials from a file
        '''
        with open('passwords.txt', 'r') as f:
            while True:
                myline = f.readline()
                un,pw,ws = myline.split(',')
                print(un,pw,ws)

    def run(self):
        '''
        Run the application
        '''
        self.mywindow.mainloop()

    def setup_screen(self):
        '''
        Setup the screen
        '''
        self.entry_password.delete(0, tkinter.END)
        self.entry_website.delete(0, tkinter.END)
        self.entry_username.delete(0, tkinter.END)
        self.entry_website.insert(0, '')
        self.entry_username.insert(0, self.default_username)
        self.entry_website.focus()

    def generate_password(self):
        '''
        Generate a password
        '''
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.newpassword = ''.join(random.choice(letters) for i in range(self.PASSWORD_LENGTH))
        print (f'newpassword is {self.newpassword}')
        self.entry_password.delete(0, tkinter.END)
        self.entry_password.insert(0, self.newpassword)
        pyperclip.copy(self.newpassword)


myPass = MyPass()
myPass.run()