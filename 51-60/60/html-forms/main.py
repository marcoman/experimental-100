from flask import Flask
from flask import render_template
import requests
from flask import request

app = Flask(__name__)

# Read json file
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

@app.route('/')
def home():
    return render_template('index.html')

# Accept the name and password via post into the file submit.html
@app.route('/submit.html', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['password']
    return render_template('submit.html', name=name, password=password)

if __name__ == "__main__":
    app.run(debug=True)
