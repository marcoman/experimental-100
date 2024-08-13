# Overview

This is the day 92 assignment.

## _From the course:_
A website that finds the most common colours in an uploaded image.

One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.

https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.

On day 76, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means Googling), build a website where a user can upload an image and you will tell them what are the top 10 most common colours in that image.

This is a good example of this functionality:

http://www.coolphptools.com/color_extract#demo



## My comments:

To me this sounds like a linear operation:

- Open a file
  - Read the file
- For each pixel, identify the color
- Build a list for each of the colors (sounds like a map)
- Sort the map from smallest count to largest.
- Produce the results.

At this time, this application works - but not with PNGs files.  It does work with JPEGs.  I could or should investigate, but I want to move onto the next assignment.


# Running


```bash
flask --app main --debug run
```

# External Links

- 

# requirements.txt

# TODOs

- FIXED.  Figure out why PNGs do not work.  I suspect it is about the way the image details come back differently.  This is what I see:
  - I've seen this before  in Day 85.  
- Convert  the image load code into a method, since it is mostly cut-and-pasted 3 times.
