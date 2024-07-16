# Overview

This is day 63 assignment.  The goal is to create an application that can help us track the books we read.

The `step-1` folder contains an in-memory implementation of my book list, which goes away when I close the application.

The `step-2` folder contains a SQLAlchemy implementation, which persists data.  This is only a store of a default book.

The `step-3` folder contains an example of the project where we can add and delete books.


# Running
Run this code with a command like this:

```
cd step-1
flask --app main --debug run
```

or

```
cd step-2
flask --app main --debug run
```

# External Links
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

# requirements.txt
make sure you run `pip install -r requirements.txt`

The requirements file may not be up-to-date.

```
pip install Flask-SQLAlchemy
```

# Final Solution

# TODOs

- Add support to delete a book.  At this time we can only add.
