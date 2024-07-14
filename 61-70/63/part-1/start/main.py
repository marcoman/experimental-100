from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length

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

all_books = [
     {
        "title": "Harry Potter",
        "author": "J. K. Rowling",
        "rating": 9,
    }
]
class addBook(FlaskForm):
    book_title = StringField("Book Title", validators=[DataRequired(),
                                                     Length(min=5, max=80)])
    author = StringField("Author", validators=[DataRequired(),
                                               Length(min=5, max=80)])
    rating = StringField("Rating", validators=[DataRequired(),
                                               Length(min=1, max=3)])
    submit = SubmitField("Add Book")

@app.route('/')
def home():
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
