# This is my TODO app.
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompt.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Bootstrap5(app)

# TABLE Configuration
class Prompt(db.Model):
    __tablename__ = "prompts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    text: Mapped[str] = mapped_column(String(16384), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


# all Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')
