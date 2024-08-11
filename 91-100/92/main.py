# Imports
from PIL import Image

# Read an image file.
image = Image.open("ubuntu14.jpg")

# Iterate over the image file for each pixel, and note the color.  Build a map to hold the data
color_map = {}
for x in range(image.width):
    for y in range(image.height):
        pixel = image.getpixel((x, y))
        if pixel in color_map:
            color_map[pixel] += 1
        else:
            color_map[pixel] = 1

# Now, let's print out the color map
for color, count in color_map.items():
    print(f"Color: {color}, Count: {count}")


# Next, print out the color map in a more readable format
for color, count in color_map.items():
    red, green, blue = color
    print(f"Color: {color}, Count: {count}, red: {color[0]}, green: {color[1]}, blue: {color[2]}")

# next, print the color map sorted by most common
sorted_color_map = sorted(color_map.items(), key=lambda x: x[1], reverse=True)
for color, count in sorted_color_map:
    red, green, blue = color
    print(f"Sorted Color: {color}, Count: {count}, red: {color[0]}, green: {color[1]}, blue: {color[2]}")

print(f'Size of the map is: {len(color_map)}')