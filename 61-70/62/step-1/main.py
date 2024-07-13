from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, NumberRange

import requests
from flask import request
import csv
from flask import url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField(
        'Cafe name',
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    location = StringField(
        'Map link',
        validators=[DataRequired(), URL(require_tld=False, message='Invalid URL')]
    )
    open_time = StringField(
        'Opening Time',
        validators=[DataRequired()]
    )
    close_time = StringField(
        'Closing Time',
        validators=[DataRequired()]
    )
    wifi_rating = StringField(
        'Wifi Rating',
        validators=[DataRequired(), Length(min=0, max=10)]
        # TODO: Figure out how to use NumberRange
    )
    coffee_rating = StringField(
        'Coffee Rating',
        validators=[DataRequired(), Length(min=0, max=10)]
    )
    power_rating = StringField(
        'Power Rating',
        validators=[DataRequired(), Length(min=0, max=10)]
    )
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        print('Form validated')
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        # TOOD: use an emoji instead of a rating number.
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as data_file:
            data_file.write(f"{form.name.data},"
                            f"{form.location.data},"
                            f"{form.open_time.data},"
                            f"{form.close_time.data},"
                            f"{form.coffee_rating.data},"
                            f"{form.wifi_rating.data},"
                            f"{form.power_rating.data}\n")
        return redirect(url_for('cafes'))
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
