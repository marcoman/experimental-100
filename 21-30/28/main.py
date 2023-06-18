import tkinter as tk
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
ONE_SECOND = 1000

work_count = 1
count = 0
text_check = ""
mytimer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global count
    global text_check
    global work_count

    count = WORK_MIN*60
    work_count = 1
    count = 0
    canvas.itemconfig(text_canvas, text="00:00")

    text_check = ""
    update_check()
    mywindow.after_cancel(mytimer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global work_count
    global count
    if work_count % 2 == 1:
        label_name.config(text="Work", fg=GREEN)
        count = WORK_MIN * 60
    elif work_count % 8 == 0:
        label_name.config(text="Long Break", fg=RED)
        count = LONG_BREAK_MIN * 60
        add_check()
    elif work_count % 2 == 0:
        label_name.config(text="Break", fg=RED)
        count = SHORT_BREAK_MIN * 60
        add_check()
    else:
        print("error")
    work_count += 1
    update_time()
 
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def update_time():
    global mytimer
    global count
    global work_count
    print('update time')
    if count > 0:
        minutes = math.floor(count/60)
        seconds = count %60
        time_text = f"{minutes:02}:{seconds:02}"
        print (time_text)
        canvas.itemconfig(text_canvas, text=time_text)  
        count -= 1
    else:
        start_timer()
    mytimer = mywindow.after(ONE_SECOND, update_time)


# ---------------------------- UI SETUP ------------------------------- #

def add_check():
    global text_check
    text_check += "✔"
    update_check()

def update_check():
    label_check.config(text=text_check, fg=GREEN)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

mywindow = tk.Tk()
mywindow.title("Pomodoro")
mywindow.config(padx=100, pady=50, bg=YELLOW, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

CANVAS_WIDTH = 250
CANVAS_HEIGHT = 250
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
image_tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image=image_tomato)
text_canvas = canvas.create_text(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), text="00:00", fill=GREEN, font=(FONT_NAME, 35))
canvas.grid(column=2, row=1)

label_name = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
button_start = tk.Button(text="Start", fg=RED, bg=YELLOW, font=(FONT_NAME, 15), command=start_timer)
button_reset = tk.Button(text="Reset", fg=RED, bg=YELLOW, font=(FONT_NAME, 15), command=reset_timer)
# button_stop = tk.Button(text="Stop", fg=RED, bg=YELLOW, font=(FONT_NAME, 15), command= reset_timer)
# label_check = tk.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
label_check = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))

label_name.grid(column=2, row=0)
button_start.grid(column=1, row=2)
# button_stop.grid(column=2, row=2)
button_reset.grid(column=3, row=2) 
label_check.grid(column=2, row=3)

# mywindow.after(ONE_SECOND, update_time, 20)


mywindow.mainloop()
