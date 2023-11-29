from flask import Flask
from functools import wraps
app = Flask(__name__)

# This next line will return "__name__" if we run this directly, and not as a library.
# print (__name__)

# This is my bold decorator

def db(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<b>{func(*args, **kwargs)}</b>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

def dem(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<em>{func(*args, **kwargs)}</em>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

def du(function=None):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = f'<u>{func(*args, **kwargs)}</u>'
            return result
        return wrap
    if function:
        return wrapper(function)
    else:
        return wrapper

@app.route('/')
@db
@du
def hello_world():
    return ('Hello World.')

@app.route('/bye')
@du
def bye():
    return ('Goodbye!')

@app.route('/greet/<name>')
def greet(name):
    return(f"Hello my friend {name}")

@app.route('/<name>')
@dem
@db
@du
def name(name):
    return(f"Hello my best friend, {name}")

if __name__ == "__main__":
    app.run(debug=True)

