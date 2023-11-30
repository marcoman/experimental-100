from functools import wraps
from flask import Flask
import random

app = Flask(__name__)

GIF_DEFAULT = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
GIF_HIGHER = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GIF_LOWER = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

global number
number = random.randint(0, 9)
color = []
n = 100
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

def add_gif2(function):
    def wrapper(*args):
        print(f"You are adding {args[1]}")
        result = '<a href="{args[1]}</a>'
        print(result)
    return wrapper

@add_h2
def write_report(guess):
    output = f"You guessed, {guess}"
    # output += f"<br>and the number is {number}"
    if guess > number:
        output += " and it was too high"
    elif guess < number:
        output += " and it was too low"
    else:
        output += " and it was correct!"
    return (output)

@app.route('/')
@add_h1
def hello_world():
    global number
    number = random.randint(0, 9)
    print (f"Number is {number}")
    return ('Guess a number between 0 and 9.')

@app.route('/<int:guess>')
@add_random_color
def number(guess):
    return(f"{write_report(guess)}")

number = random.randint(0, 9)
print (f"Number is {number}")

if __name__ == "__main__":
    app.run(debug=True)

