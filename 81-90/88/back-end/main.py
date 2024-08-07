from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(db.func.random())).scalar()
    print (random_cafe)

    # Return the main page
    # return render_template("index.html")

    # Return a jsonify-ed page with the columns we specify.
    # return jsonify(
    #     # id=random_cafe.id,
    #     name=random_cafe.name,
    #     map_url=random_cafe.map_url,
    #     img_url=random_cafe.img_url,
    #     location=random_cafe.location,
    #     seats=random_cafe.seats,
    #     has_toilet=random_cafe.has_toilet,
    #     has_wifi=random_cafe.has_wifi,
    #     has_sockets=random_cafe.has_sockets,
    #     can_take_calls=random_cafe.can_take_calls,
    #     coffee_price=random_cafe.coffee_price
    #     )

    # Return the jsonify-ed page using our built-in method with dictionary comprehension.
    return jsonify(random_cafe.to_dict())

# HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def get_all_cafe():
    # all_cafes = db.session.execute(db.select(Cafe)).scalars()
    # result = db.session.query(Cafe).all()
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    # return jsonify([cafe.to_dict() for cafe in all_cafes])
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

# HTTP Search

@app.route("/search", methods=["GET"])
def search():
    result = db.session.execute(db.select(Cafe).where(Cafe.location.like(request.args.get("loc"))))
    if result:
        all_cafes = result.scalars().all()
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    print (f"New price is {new_price}")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the price to {new_price}."})
    else:
        return jsonify(error={"Not Found": f"Sorry a cafe with that id {cafe_id} was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "MySEcretKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted cafe with id {cafe_id}."})
        else:
            return jsonify(error={"Not Found": f"Sorry a cafe with that id {cafe_id} was not found in the database."}), 404
    else:
        return jsonify(error={"Not Authorized": "Sorry, that's not allowed. Make sure you have the correct api-key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
