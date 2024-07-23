from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB1

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8), name=name)
        db.session.add(new_user)
        db.session.commit()
        print (f'The name is {name}')
        return redirect(url_for('secrets', name=name))
    else:
        return render_template("register.html")
    


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password")
            return redirect(url_for('login'))
    else:
        return render_template("login.html")


@app.route('/secrets', methods=["GET", "POST"])
def secrets():
    name = request.args.get('name')
    print (f'Name received is {name}')

    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
