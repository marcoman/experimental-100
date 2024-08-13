# Imports
from PIL import Image

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, NumberRange

from flask import request
from flask import url_for
import os
import os

MAX_COUNT = 10
UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filename = "ubuntu14.jpg"
Bootstrap5(app)

image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")

def get_color_code(red, green, blue):
    """
    Returns a string representation of the RGB color.
    """
    # Convert the RGB values to integers
    red = int(red)
    green = int(green)
    blue = int(blue)
    return f"rgb({red}, {green}, {blue})"
    
def get_color(red, green, blue):
    """
    Returns a string with the color code for HTML output
    """
    return f"#{red:02x}{green:02x}{blue:02x}"

def get_percentage(count):
    """
    Returns the percentage of the total pixels for a given color
    """
    total_pixels = image.width * image.height
    return (count / total_pixels) * 100

def generate_color_map():
    """ 
    Generates a color map for the image
    """
    global color_map
    global image
    # Iterate over the image file for each pixel, and note the color.  Build a map to hold the data
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            if pixel in color_map:
                color_map[pixel] += 1
            else:
                color_map[pixel] = 1

def generate_sorted_map():
    """
    Generates a sorted map based on the color map
    """
    sorted_map = sorted(color_map.items(), key=lambda x: x[1], reverse=True)
    return sorted_map

def print_top_colors(count):
    """
    Returns the top `count` colors from the color map
    """
    sorted_map=generate_sorted_map()
    for i in range(count):
        if i >= len(sorted_map):
            break
        color = sorted_map[i][0]
        print(f"Color: {get_color(*color)}, Count: {sorted_map[i][1]}, Percentage: {get_percentage(sorted_map[i][1]):.2f}%")

def get_top_colors(count):
    """
    Returns an array of color by color code, the count, and the percentage
    """
    sorted_map=generate_sorted_map()
    colors = []
    for i in range(count):
        if i >= len(sorted_map):
            break
        color = sorted_map[i][0]
        colors.append((get_color(*color), 
                      sorted_map[i][1],
                      f'{get_percentage(sorted_map[i][1]):.2f}%'
                    ))
    return colors

def test_cli():
    generate_color_map()
    print(f'Size of the map is: {len(color_map)}')
    print(f'Number of pixels is {number_pixels}')
    # print_top_colors(10)
    mycolors = get_top_colors(10)
    for i in range(len(mycolors)):
        print(mycolors[i])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# test_cli()

# all Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    global color_map
    global number_pixels
    global filename

    # If the user pressed submit, then we have to load a new page.
    if request.method == 'POST':
        print("POST")

        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
    
        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(f"{app.config['UPLOAD_FOLDER']}{filename}"))
            # maybe next time something like this:
            with Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}") as im:
                if im.mode != 'RGB':
                    image = im.convert('RGB')
                else:
                    image = im
                color_map = {}
                number_pixels = image.width * image.height

                # image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")
                # color_map = {}
                # number_pixels = image.width * image.height
                print(f'New File number of pixels in {filename} is {number_pixels}')
                generate_color_map()
                colors = get_top_colors(10)

            return redirect(url_for('home'))
            # return render_template('index.html', colors=colors, image=f"{app.config['UPLOAD_FOLDER']}{filename}")
        
    else:
        with Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}") as im:
            if im.mode != 'RGB':
                image = im.convert('RGB')
            else:
                image = im
            color_map = {}
            number_pixels = image.width * image.height
            print(f'Non-POST.  Number of pixels in {filename} is {number_pixels}')

            # image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")
            number_pixels = image.width * image.height
            print(f'New File number of pixels in {filename} is {number_pixels}')
            generate_color_map()
            colors = get_top_colors(10)

        # image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")
        # color_map = {}
        # number_pixels = image.width * image.height
        # print(f'Non-POST.  Number of pixels in {filename} is {number_pixels}')
        # generate_color_map()
        # colors = get_top_colors(10)
        # #print the colors
        # print(f'Colors are: {colors}')

    return render_template('index.html', colors=colors, image=f"{app.config['UPLOAD_FOLDER']}{filename}")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    global color_map
    global number_pixels
    global image

    if request.method == 'POST':
        print("POST")

        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            print("File is good")
            print(file.filename)
            color_map = {}
            filename = file.filename
            file.save(os.path.join(f"{app.config['UPLOAD_FOLDER']}{filename}"))
            with Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}") as im:
                if im.mode != 'RGB':
                    image = im.convert('RGB')
                else:
                    image = im
                color_map = {}
                number_pixels = image.width * image.height
                print(f'Upload of pixels in {filename} is {number_pixels}')

                # image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")
                # number_pixels = image.width * image.height
                # print(f'New File number of pixels in {filename} is {number_pixels}')
                generate_color_map()
                colors = get_top_colors(10)


            # image = Image.open(f"{app.config['UPLOAD_FOLDER']}{filename}")
            # number_pixels = image.width * image.height
            # print(f'Upload of pixels in {filename} is {number_pixels}')
            # generate_color_map()
            # colors = get_top_colors(10)
            # print(f'Colors are: {colors}')
            # # return redirect(url_for('home'), colors=colors)
            return render_template('index.html', colors=colors, image=f"{app.config['UPLOAD_FOLDER']}{filename}")

    return render_template('upload.html')