from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

import os

mysecret = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = mysecret

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Length(min=8), Email(check_deliverability=True)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "marco@marco.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
            # return render_template("success.html")
    return render_template("login.html", form=form)

@app.route("/success", methods=["POST"])
def success():
    return render_template('success.html')

@app.route("/denied", methods=["POST"])
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)


