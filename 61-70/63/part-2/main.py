from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "book-list.db")

Bootstrap5(app)

# This line initializes the database
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self) -> str:
        return f'<Book {self.title}>'
    
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating


with app.app_context():
    db.create_all()

# Create the first record
with app.app_context():
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.5)
    db.session.add(new_book)
    db.session.commit()

class addBook(FlaskForm):
    id = StringField("Book ID", validators=[DataRequired()])
    title = StringField("Book Title", validators=[DataRequired(),
                                                     Length(min=5, max=80)])
    author = StringField("Author", validators=[DataRequired(),
                                               Length(min=5, max=80)])
    rating = StringField("Rating", validators=[DataRequired(),
                                               Length(min=1, max=3)])
    submit = SubmitField("Add Book")

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = addBook()
    if form.validate_on_submit():
        print ("Form Submitted")
        new_book = {
            "title": form.book_title.data,
            "author": form.author.data,
            "rating": form.rating.data
        }
        all_books.append(new_book)
        for book in all_books:
            print (book)
        return redirect(url_for('home'))
    else:
        print ("Form not validated on submit")
        return render_template("add.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
