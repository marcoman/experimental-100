from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "book-list.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# This line initializes the database
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# create the table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self) -> str:
        return f'<Book {self.title}>'

# create the schema
with app.app_context():
    db.create_all()

# Create the first record
with app.app_context():
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.5)
    db.session.add(new_book)
    db.session.commit()
