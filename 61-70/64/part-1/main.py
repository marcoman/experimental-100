import urllib.parse
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import DataRequired
from wtforms.validators import Length
import requests
import os
import urllib

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# Specify the working directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "movie.db")
Bootstrap5(app)

TMDB_API_KEY = os.environ['TMDB_API_KEY']
TMDB_API_READ_REQUEST = os.environ['TMDB_API_READ_REQUEST']
TMDB_URL="https://api.themoviedb.org/3/search"
TMDB_HEADERS = {"Authorization": f"Bearer {TMDB_API_READ_REQUEST}"}

# CREATE DB
# This line initializes the database
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
# initialize the app with the extension
db.init_app(app)
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

class AddMovieSimple(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Find Movie")

class addMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Movie Year", validators=[DataRequired()])
    description = StringField("Movie Description", validators=[DataRequired(),
                                                     Length(min=5, max=500)])
    rating = StringField("Movie Rating", validators=[DataRequired()])
    ranking = StringField("Movie Ranking", validators=[DataRequired()])
    review = StringField("Movie Review", validators=[DataRequired(),
                                                     Length(min=5, max=500)])
    img_url = StringField("Movie Image URL", validators=[DataRequired()])

    submit = SubmitField("Add Movie")

class editMovie(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired(),
                                                     Length(min=5, max=500)])
    submit = SubmitField("Done")


@app.route("/init")
def init():
    # Create the first entry
    with app.app_context():
        print ("ADDING MOVIE")
        movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Thriller about a guy pinned down in a phone booth by a sniper",
            rating=7.2,
            ranking=10,
            review="Neato movie",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )

        second_movie = Movie(
            title="Avatar The Way of Water",
            year=2022,
            description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
            rating=7.3,
            ranking=9,
            review="I liked the water.",
            img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        )        

        db.session.add(movie)
        db.session.add(second_movie)
        db.session.commit()

    return redirect(url_for('home'))

@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    print (all_movies)
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = editMovie()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        print ("Form Submitted")
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print ("Form not validated on submit")
        return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieSimple()
    if form.validate_on_submit():
        movie_title = form.title.data
        print (f"Searching for the title {movie_title}")
        safe_string = urllib.parse.quote_plus(movie_title)
        print (f"SAFE STRING is '{safe_string}'")
        query_url = f'{TMDB_URL}/movie?query={safe_string}&include_adult=false&language=en-US&page=1'
        print (f"Query URL is '{query_url}'")

        response = requests.get(url=query_url,
                                headers=TMDB_HEADERS)
        data = response.json()
        print ("Response is:")
        print (data)
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/addMovie", methods=["GET", "POST"])
def addMovie():
    form = AddMovieSimple()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            year=int(form.year.data),
            description=form.description.data,
            rating=float(form.rating.data),
            ranking=int(form.ranking.data),
            review=form.review.data,
            img_url=form.img_url.data
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)