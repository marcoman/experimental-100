from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreateItemForm, RegisterForm, LoginForm, CommentForm

import json
import stripe
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Read the strip api key from the environment variable STRIPE_SECRET_KEY
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Configure login
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

def calculate_order_amount(items):
    cart_items = db.session.query(Cart).filter_by(user_id=current_user.id).all()
    print (f"Number of cart items is {len(cart_items)}")
    total_price = sum(item.price * item.quantity for item in cart_items)
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    # return 1400
    return total_price
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

def logged_in_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

# CONFIGURE TABLES
class StoreItem(db.Model):
    __tablename__ = "store_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)

    is_authenticated = True
    is_active = True
    is_anonymous = False

    def get_id(self):
        return str(self.id)

# This is the cart class, to store our "add to cart" items
class Cart(db.Model):
    __tablename__ = "cart"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    
    def get_id(self):
        return str(self.id)

with app.app_context():
    db.create_all()

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print ("RegisterForm submitted")
        if User.query.filter_by(email=form.email.data).first():
            print("User already exists")
            flash(category="error",
                  message="User already exists")
            return render_template('register.html', form=form)
        else:
            print("New user")
            new_user = User(
                email=form.email.data,
                password=generate_password_hash(form.password.data, 
                                                method='pbkdf2:sha256', 
                                                salt_length=8),
                name=form.name.data
            )
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
            return redirect(url_for('login'))
    else:
        print ("Form not submitted")
        return render_template("register.html", form=form, current_user=current_user)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print ("LoginForm submitted")
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return render_template("index.html", logged_in=True)
            # return redirect(url_for('get_all_items', logged_in=current_user.is_authenticated))
        else:
            flash(message="Invalid email or password, please try again.",
                  category='error')
            return redirect(url_for('login', logged_in=False))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout',  methods=["GET", "POST"])
@logged_in_only
def logout():
    logout_user()
    return redirect(url_for('get_all_items'))


@app.route('/')
def get_all_items():
    result = db.session.execute(db.select(StoreItem))
    items = result.scalars().all()
    return render_template("index.html", all_items=items, logged_in=current_user.is_authenticated, current_user=current_user)

@app.route("/item/<int:item_id>")
def show_item(item_id):
    requested_item = db.get_or_404(StoreItem, item_id)
    return render_template("item.html", item=requested_item)

@app.route("/new-item", methods=["GET", "POST"])
@admin_only
def add_new_item():
    form = CreateItemForm()
    if form.validate_on_submit():
        new_post = StoreItem(
            title=form.title.data,
            subtitle=form.subtitle.data,
            img_url=form.img_url.data,
            price=form.price.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_items"))
    return render_template("make-item.html", form=form)

@app.route("/edit-item/<int:item_id>", methods=["GET", "POST"])
@admin_only
def edit_item(item_id):
    item = db.get_or_404(StoreItem, item_id)
    edit_form = CreatePostForm(
        title=item.title,
        subtitle=item.subtitle,
        img_url=item.img_url,
    )
    if edit_form.validate_on_submit():
        item.title = edit_form.title.data
        item.subtitle = edit_form.subtitle.data
        item.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_item", item_id=item.id))
    return render_template("make-item.html", form=edit_form, is_edit=True)

@app.route("/delete/<int:item_id>")
@admin_only
def delete_item(post_id):
    item_to_delete = db.get_or_404(StoreItem, item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_items'))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/add-to-cart/<int:item_id>", methods=["GET", "POST"])
@logged_in_only
def add_to_cart(item_id):
    item_to_add = db.get_or_404(StoreItem, item_id)
    new_cart_item = Cart(
        user_id=current_user.id,
        item_id=item_to_add.id,
        quantity=1,
        price=item_to_add.price,
        title=item_to_add.title,
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return redirect(url_for('get_all_items'))

@app.route("/cart")
@logged_in_only
def show_cart():
    cart_items = db.session.query(Cart).filter_by(user_id=current_user.id).all()
    print (f"Number of cart items is {len(cart_items)}")
    total_price = sum(item.price * item.quantity for item in cart_items)
    print (f"Total price is {total_price}")
    return render_template("cart.html", cart_items=cart_items, total_price=total_price, logged_in=current_user.is_authenticated)

@app.route("/buy-now", methods=["GET", "POST"])
@logged_in_only
def buy_now():
    cart_items = db.session.query(Cart).filter_by(user_id=current_user.id).all()
    for item in cart_items:
        print(f"Buying {item.quantity} of {item.title} for {item.price} each")
    # db.session.commit()
    return render_template("success.html", cart_items=cart_items)

# To do this right, we'll have to follow the instructions at https://docs.stripe.com/payments/quickstart
# I'm stopping now, since I need to move on.
@app.route('/create-payment', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == "__main__":
    app.run(debug=True, port=5002)

