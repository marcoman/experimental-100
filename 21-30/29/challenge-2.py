import tkinter

# The challenge here is to create screen widgets with the following:
# Website - label & text input
# Username - label & text input
# Password - label and text <output>
# Submit - button


CANVAS_HEIGHT = 200
CANVAS_WIDTH = 200
PADDING = 20
WINDOW_HEIGHT = CANVAS_HEIGHT + PADDING * 2
WINDOW_WIDTH = CANVAS_WIDTH + PADDING * 2

# First
# Create a window, and set the image to the middle, and have padding of 20 around it.

mywindow = tkinter.Tk()
mywindow.title("My Pass")
mywindow.config(padx=100, pady=50, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

myimage = tkinter.PhotoImage(file="logo.png")

mycanvas = tkinter.Canvas(mywindow, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mycanvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image=myimage)
mycanvas.grid(row=0, column=1)

label_website  = tkinter.Label(mywindow, text="Website:")
label_username = tkinter.Label(mywindow, text="Email/Username:")
label_password = tkinter.Label(mywindow, text="Password:")
label_website.grid(row=1, column=0)
label_username.grid(row=2, column=0)
label_password.grid(row=3, column=0)

entry_website = tkinter.Entry(mywindow, width=35)
entry_username = tkinter.Entry(mywindow, width=35)
entry_password = tkinter.Entry(mywindow, width=23)
entry_website.grid(row=1, column=1, columnspan=2)
entry_username.grid(row=2, column=1, columnspan=2)
entry_password.grid(row=3, column=1)

button_generate = tkinter.Button(mywindow, text="Generate")
button_submit = tkinter.Button(mywindow, text="Submit")
button_generate.grid(row=3, column=2)
button_submit.grid(row=4, column=1)

def save_to_file():
    '''
    Save the credentials to a file
    '''
    pass

def load_from_file():
    '''
    Load the credentials from a file
    '''
    pass


mywindow.mainloop()
