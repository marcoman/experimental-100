# Imports
from PIL import Image

MAX_COUNT = 10
# Read an image file.
image = Image.open("ubuntu14.jpg")
color_map = {}
number_pixels = image.width * image.height

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
    for i in range(count):
        if i >= len(sorted_map):
            break
        color = sorted_map[i][0]
        print(f"Color: {get_color(*color)}, Count: {sorted_map[i][1]}, Percentage: {get_percentage(sorted_map[i][1]):.2f}%")


def print_color_map():
    """
    Prints the color map
    """
    sorted_map = generate_sorted_map()
    for color, count in sorted_map:
        print(f"Color: {get_color_code(*color)}, Count: {count}, Percentage: {get_percentage(count):.2f}%")

generate_color_map()
print(f'Size of the map is: {len(color_map)}')
print(f'Number of pixels is {number_pixels}')
sorted_map = generate_sorted_map()
print_top_colors(10)

