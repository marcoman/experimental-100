from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import os

mysecret = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = mysecret

class MyForm(FlaskForm):
    email = StringField('email')
    password = StringField('password') 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = MyForm()
    return render_template('login.html', form=form)

@app.route("/success.html", methods=["POST"])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)


