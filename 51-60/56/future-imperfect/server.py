from flask import Flask, render_template
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    output = f"Hello World"
    return output

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/single')
def single():
    return render_template('single.html')



# Run the app if we're running standalone
if __name__ == "__main__":
    app.run(debug=True)

