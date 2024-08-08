from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, NumberRange

#from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

import requests
from flask import request
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Bootstrap5(app)

with app.app_context():
    db.create_all()

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class CafeForm(FlaskForm):
    name = StringField(
        'Cafe name',
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    map_url = StringField(
        'Map link',
        validators=[DataRequired(), URL(require_tld=False, message='Invalid URL')]
    )
    img_url = StringField(
        'Image link',
        validators=[DataRequired(), URL(require_tld=False, message='Invalid URL')]
    )
    location = StringField(
        'Location',
        validators=[DataRequired(), Length(min=2, max=250)]
    )
    seats = StringField(
        'Seats',
        validators=[DataRequired()]
    )
    has_toilet = StringField(
        'Toilet Availability',
        validators=[DataRequired()]
    )
    has_wifi = StringField(
        'Wifi Availability',
        validators=[DataRequired()]
    )
    has_sockets = StringField(
        'Sockets Availability',
        validators=[DataRequired()]
    )
    can_take_calls = StringField(
        'Can Take Calls',
        validators=[DataRequired()]
    )
    coffee_price = StringField(
        'Coffee Price',
        validators=[DataRequired()]
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
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    else:
        return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    mylist=[cafe for cafe in all_cafes]
    print(f'my list is {mylist}')
    return render_template('cafes.html', cafes=mylist)

@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(db.func.random())).scalar()
    print (random_cafe)
    return render_template('cafe.html', cafe=random_cafe)


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        print (f"Successfully deleted cafe with id {cafe_id}.")
    else:
        print(f"Sorry a cafe with that id {cafe_id} was not found in the database.")


if __name__ == '__main__':
    app.run(debug=True)
