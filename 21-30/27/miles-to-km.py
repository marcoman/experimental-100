import tkinter as tk

mywindow = tk.Tk()
mywindow.title("Miles to Km Converter")

def convert_mi_to_km():
    miles = float(entry_miles.get())
    km = miles * 1.609
    label_value.config(text=f"{km}")

# label for entry
label_instructions = tk.Label(text="Enter Miles")
label_instructions.grid(row=0, column=0)

# entry
entry_miles = tk.Entry()
entry_miles.grid(row=0, column=1)
print(entry_miles.get())

# is equal to
label_equal_to = tk.Label(text="is equal to")
label_equal_to.grid(row=1, column=0)

# value
label_value = tk.Label(text="0")
label_value.grid(row=1, column=1)

# km label
label_km = tk.Label(text="km")
label_km.grid(row=1, column=2)

# button
button_calculate = tk.Button(text="Calculate", command=convert_mi_to_km)
button_calculate.grid(row=2, column=1)

mywindow.config(padx=30, pady=30)
mywindow.mainloop()

