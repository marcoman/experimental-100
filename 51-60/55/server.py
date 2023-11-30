from functools import wraps
from flask import Flask
import random

app = Flask(__name__)

GIF_DEFAULT = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
GIF_HIGHER = "https://media1.giphy.com/media/PR3585ZZSvcHO9pa76/giphy.gif"
GIF_LOWER = "https://media4.giphy.com/media/UVsEApdS35zdJitRBd/giphy.gif"
GIF_CORRECT = "https://media2.giphy.com/media/pNpONEEg3pLIQ/giphy.gif"

global number
number = random.randint(0, 9)
color = []
n = 10

# Set up an array with different random numbers
for i in range(n):
    color.append('#%06X' % random.randint(0, 0xFFFFFF))

def add_h1(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<h1>{func(*args, **kwargs)}</h1>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

def add_h2(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<h2>{func(*args, **kwargs)}</h2>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

def add_gif(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = '<a href="{args[1]}"</a>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper


def add_random_color(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<h1 style="color: {random.choice(color)}">{func(*args, **kwargs)}</h1>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

@add_h2
def write_report(guess):
    output = f"You guessed, {guess}"
    # output += f"<br>and the number is {number}"
    if guess > number:
        output += " and it was too high"
        output += '<br>'
        output += f'<img src="{GIF_LOWER}" alt="Guess Lower" >'
    elif guess < number:
        output += " and it was too low"
        output += '<br>'
        output += f'<img src="{GIF_HIGHER}" alt="Guess Higher">'
    else:
        output += " and it was correct!"
        output += '<br>'
        output += f'<img src="{GIF_CORRECT}" alt="Correct!" >'
    return (output)

@app.route('/')
@add_h1
def hello_world():
    global number
    number = random.randint(0, 9)
    print (f"Number is {number}")

    output = 'Guess a number between 0 and 9.'
    output += '<br>'
    output += f'<img src="{GIF_DEFAULT}" alt="Girl in a jacket" width="500" height="600">'
    return output

@app.route('/<int:guess>')
@add_random_color
def number(guess):
    return(f"{write_report(guess)}")

if __name__ == "__main__":
    app.run(debug=True)

