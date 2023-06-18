import tkinter as tk

newtext = "New Text"

mywindow = tk.Tk()
mywindow.title("Widget Challenge")
mywindow.minsize(width=500, height=500)

def update_label(newtext):
    label.config(text=newtext)

label = tk.Label(text="Hello World")
label.grid(column=0, row=0)
label.config(padx=20, pady=20)
button = tk.Button(text="Click me")
button.grid(column=1, row=1)

entry = tk.Entry()
entry.insert(tk.END, "Starting Text")
entry.grid(column=4, row=3)
print(entry.get())

newbutton = tk.Button(text="New Button", command= lambda: update_label(newtext))
newbutton.grid(column=2, row=0)

mywindow.config(padx=20, pady=20)

mywindow.mainloop()
