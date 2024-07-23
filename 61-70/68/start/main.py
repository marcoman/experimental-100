from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask import abort
from django.utils.http import url_has_allowed_host_and_scheme

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Configure login
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB1

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    # Per https://flask-login.readthedocs.io/en/latest/#your-user-class.  I think.
    is_authenticated = True
    is_active = True
    is_anonymous = False

    def get_id(self):
        return str(self.id)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

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
        return redirect(url_for('login', name=name))
    else:
        return render_template("register.html", logged_in=current_user.is_authenticated)
    


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        # Per https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.check_password_hash
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password")
            return redirect(url_for('login'))
    else:
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets', methods=["GET", "POST"])
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name, logged_in=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf', as_attachment=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)
