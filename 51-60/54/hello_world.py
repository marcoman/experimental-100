from flask import Flask
app = Flask(__name__)

# This next line will return "__name__" if we run this directly, and not as a library.
# print (__name__)

@app.route('/')
def hello_world():
    return 'Hello World.'


@app.route('/bye')
def bye():
    return 'Goodbye!'

if __name__ == "__main__":
    app.run()

