import tkinter

# The request here is to add a logo to the main window with some padding.


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

myimage = tkinter.PhotoImage(file="./logo.png")

mycanvas = tkinter.Canvas(mywindow, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mycanvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image=myimage)
mycanvas.grid(row=0, column=0)

mywindow.mainloop()
