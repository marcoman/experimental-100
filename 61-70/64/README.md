# Overview

This is day 64 assignment.  The goal is to create an application that allows us to manage our most favorite movies.

The `part-1` folder contains the application that displays two sample movies.  I included a hidden `/init` page to setup the database with 2 records.  This allows me to work with the same pages without having to rebuild new applications each time (see Day 63 and Day 62).



# Running
We need an account on TMDB and a key (https://www.themoviedb.org/settings/api) to let us do the complete assignment.

Once setup, I enabled my API key and Read Access Token with:

```
export TMDB_API_KEY=<approximately 20 characters>
export TMDB_API_READ_ACCESS_KEY=<approximately 240 characters>
```
This lets me look up the keys in Python, without having to check anything in.

Run this code with a command like this:

```
cd part-1
flask --app main --debug run
```

# External Links
- I used the following link to test TMDB with my private key.
https://developers.themoviedb.org/3/search/search-movies


# requirements.txt
make sure you run `pip install -r requirements.txt`

The requirements file may not be up-to-date.

```
pip install Flask-SQLAlchemy
```

# Final Solution

# TODOs

