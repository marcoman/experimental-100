import tkinter as tk
from PIL import Image, ImageTk, ImageFont, ImageDraw
from pathlib import Path
import sys

from tkinter import filedialog


# Start by creating a window with a layout for title, the button to upload an image, a label to show the current path, and an image display
class PictureWatermark:

    # setup the class 
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.title("Watermark challenge")
        self.mywindow.minsize(width=500, height=500)
        self.mywindow.config(padx=20, pady=20)

        self.label = tk.Label(text="No file selected")
        self.label.grid(column=0, row=0)

        self.button = tk.Button(text="Select image", command=self.select_image)
        self.button.grid(column=1, row=1)

        self.button = tk.Button(text="Add Watermark", command=self.add_watermark)
        self.button.grid(column=1, row=2)

        self.canvas = tk.Canvas()
        self.canvas.grid(column=0, row=2)
        self.filename = ''

        # self.myimage = tk.PhotoImage(file="./card_front.png")
        # self.myimage = tk.PhotoImage(file="./ubuntu14.jpg")
        self.myimage = ImageTk.PhotoImage(Image.open("./ubuntu14.jpg"))
        self.canvas.config(width=self.myimage.width(), height=self.myimage.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.myimage)

        self.counter = 0

    def run(self):
        self.mywindow.mainloop()

    def select_image(self):
        print("pressed button")
        self.counter += 1
        self.label.config(text=self.counter)
        self.filename = filedialog.askopenfilename(
            filetypes={
                ("image files", "*.jpg;*.png;*.gif"),
                ("all files", "*.*")
            },
            initialdir="./"

        )
        print(f'Selected {self.filename}')
        if self.filename:
            self.display_image(self.filename)

    def display_image(self, filename):
        self.myimage = ImageTk.PhotoImage(Image.open(filename))
        self.filename = filename
        self.canvas.config(width=self.myimage.width(), height=self.myimage.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.myimage)


    def add_watermark(self):
        print("add watermark")
        with Image.open(self.filename) as im:
            if im.mode != 'RGB':
                rgb_im = im.convert('RGB')
            else:
                rgb_im = im
            watermark_text = "Marco Watermark"
            text_position = (50,50)
            font = ImageFont.load_default()
            draw = ImageDraw.Draw(rgb_im)
            draw.text(text = watermark_text, 
                    xy=text_position,
                    fill=(255, 255, 255),
                    font=font)
            rgb_im.save("watermarked_image.jpg")
        self.display_image("watermarked_image.jpg")

myPicture = PictureWatermark()
myPicture.run()
