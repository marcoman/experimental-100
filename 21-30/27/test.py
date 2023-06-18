'''
Simple tests for today
'''

# See https://docs.python.org/3/library/tkinter.html
import tkinter
import time

LABEL_FONT = ('Arial', 20, 'bold')


window = tkinter.Tk()
window.title = "Test program"
window.minsize(500,500)

mylabel = tkinter.Label(text="Marco", font=LABEL_FONT)
mylabel.pack(side="left")


mylabel["text"] = "new text"
mylabel.config(text="new text2")

_miles = 20

def convert_mi_to_km(miles=10):
    mylabel["text"] = str(miles * 1.6)
    _miles += 5
    # return (float(miles * 1.6))

def convert_km_to_mi(kms):
    return (float(kms / 1.6))

def button_click():
    update_label_from_input()

# button = tkinter.Button(text="Click me", command=button_click)
# button = tkinter.Button(text="Click me", command=lambda:convert_mi_to_km(_miles))
button = tkinter.Button(text="Click me", command=lambda:update_label_from_input())
button.pack(side='right')


def update_label_from_input():
    mylabel["text"] = input_text.get()

input_text = tkinter.StringVar()
input = tkinter.Entry(window, name="input screen", width=50, textvariable=input_text)
input.pack(side='bottom')
input.focus()

multiline_text = tkinter.Text(window, height=10, width=50)
multiline_text.pack(side='bottom')

spinbox = tkinter.Spinbox(window, values=(1,2,3,4,5))
spinbox.pack(side='left')

radio = tkinter.Radiobutton(window, text="radio button", value=1)
radio.pack(side='bottom')

scale = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL)
scale.pack(side='bottom')


window.mainloop()

