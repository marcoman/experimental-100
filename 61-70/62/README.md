# Overview
This is the folder for Day 62 exercises.  This is an example where the learning is based on what we remember and investigate.

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


# External links
Some of the links I used included:

- https://wtforms.readthedocs.io/en/2.3.x/validators/
This is for the validators, including URL

- https://stackoverflow.com/questions/66624995/how-do-i-find-if-variable-contains-a-string-from-list-of-strings
I wanted to see an example of how to match in HTML.  Plain old code.

- https://bootstrap-flask.readthedocs.io/en/stable/macros/#render-form
Background information on rendering a page, as I was looking for rendering each Field one-by-one.  I then saw I could use `render_form` to create a complete form goverend by Flask-WTForms.

- https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
This link is provided to us in the course materials.

# requirements.txt
make sure you run `pip install -r requirements.txt`

The requirements file may not be up-to-date.

# TODOs

- Let us enter a number into the ratings, and then build logic that automatically converts each number into an emoji/symbol.
- Validate the ratings fields to only permit numbers 1 through 5
