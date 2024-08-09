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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
db = SQLAlchemy(model_class=Base)
db.init_app(app)
Bootstrap5(app)

# TABLE Configuration
class Todo(db.Model):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


class TodoForm(FlaskForm):
    title = StringField(
        'Todo title',
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    description = StringField(
        'Todo description',
        validators=[DataRequired(), Length(min=2, max=250)]
    )
    submit = SubmitField('Submit')

class HomeForm(FlaskForm):
    title = StringField(
        'Todo title',
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    description = StringField(
        'Todo description',
        validators=[DataRequired(), Length(min=2, max=250)]
    )
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    form = HomeForm()

    if form.validate_on_submit():
        new_todo = Todo(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(new_todo)
        db.session.commit()
    else:
        print("Form not validated")

    result = db.session.execute(db.select(Todo).order_by(Todo.title))
    todos_all = result.scalars().all()
    todos_list=[todo for todo in todos_all]
    print(f'my list is {todos_list}')


    return render_template('index.html', todos=todos_list)


# all Flask routes below
@app.route("/todos")
def todos():
    result = db.session.execute(db.select(Todo).order_by(Todo.title))
    todos_all = result.scalars().all()
    todos_list=[todo for todo in todos_all]
    print(f'my list is {todos_list}')
    return render_template('todos.html', todos=todos_list)

# HTTP DELETE - Delete Record
@app.route("/delete/<int:todo_id>", methods=['GET', 'DELETE'])
def delete(todo_id):
    print(f'Trying to delete {todo_id}')
    todo = db.session.get(Todo, todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        print (f"Successfully deleted cafe with id {todo_id}.")
    else:
        print(f"Sorry a cafe with that id {todo_id} was not found in the database.")

    return redirect(url_for('home'))


# Add a todo to our list
@app.route("/add", methods=["GET", "POST"])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)
