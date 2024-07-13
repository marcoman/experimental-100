This is the folder for Day 62 exercises.

This project is an exercise of day 61 and day 60 exercises.

The goal is to display a list of cafes, and allow people to enter a new cafe.

The tricks in this project include:

- Construct a useful clas nanmed `CafeForm` in (`main.py`)[step-1/main.py] to define what we seek, and the data validation.
- Render URLs with an appropriate `<a href>` link, and that required us to do a string match for the letters `https` when we iterate over an array.  See the logic in (`cafes.html`)[step-1/static/cafes.html]
- Write a CSV when we have a valid set of data from the form.  See the definition of `add_cafe` in (`main.py`)[step-1/main.py]

# Running

Run this code with a command like this:

```
cd step-1
flask --app main --debug run
```

Navigate to the hidden "add cafe" page by modifying the url to `/add`

# Final solution
I copied the final solution as `solution`. and copied the files as-is from the project source.


Happy testing.