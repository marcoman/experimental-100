from flask import Flask
app = Flask(__name__)

# This next line will return "__name__" if we run this directly, and not as a library.
# print (__name__)

# This is my bold decorator
def dec_b(function):
    def b():
        return f"<b>{function()}</b>"
    return b

def dec_i(function):
    def i():
        return f"<i>{function()}</i>"
    return i

def dec_u(function):
    def u():
        return f"<u>{function()}</u>"
    return u

@app.route('/')
@dec_b()
@dec_i()
def hello_world():
    return 'Hello World.'


@app.route('/bye')
@dec_i()
@dec_u()
def bye():
    return 'Goodbye!'

@app.route('/greet/<name>')
@dec_i()
def greet(name):
    return(f"Hello my friend {name}")

@app.route('/<name>')
@dec_u()
def name(name):
    return(f"Hello my best friend, {name}")

if __name__ == "__main__":
    app.run(debug=True)

