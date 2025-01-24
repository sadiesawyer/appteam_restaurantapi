from flask import Flask, request, jsonify
from models import db, ma, Restaurant, Review, RestaurantSchema, ReviewSchema
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

#initialize schemas
restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

with app.app_context():
    db.create_all()

#endpoint to add a restaurant to the list
@app.route("/restaurants", methods=["POST"])
def add_restaurant():
    data = request.json
    new_restaurant = Restaurant(
        name=data["name"], 
        cuisine_type=data["cuisine_type"]
    )
    db.session.add(new_restaurant)
    db.session.commit()
    return restaurant_schema.jsonify(new_restaurant)

if __name__ == "__main__":
    app.run(debug=True)