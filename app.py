from flask import Flask, request, jsonify
from models import db, ma, Restaurant, Review, RestaurantSchema, ReviewSchema
from flask_migrate import Migrate
from sqlalchemy import func
from datetime import datetime, timezone


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
    print("Received JSON:", data)

    if not data or "name" not in data or "cuisine_type" not in data or "location" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_restaurant = Restaurant(
        name=data["name"], 
        cuisine_type=data["cuisine_type"],
        location=data["location"]
    )
    db.session.add(new_restaurant)
    db.session.commit()
    return restaurant_schema.jsonify(new_restaurant)


#endpoint to get all restaurants

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    all_restaurants = Restaurant.query.all()
    return restaurants_schema.jsonify(all_restaurants)


#endpoint to search a restaurant by ID

@app.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return restaurant_schema.jsonify(restaurant)

#search by cuisine type
@app.route("/restaurants/cuisine/<string:cuisine_type>", methods=["GET"])
def get_restaurants_by_cuisine(cuisine_type):
    restaurants = Restaurant.query.filter(Restaurant.cuisine_type.ilike(f"%{cuisine_type}%")).all()
    if not restaurants:
        return jsonify({"message": "No restaurants found with this cuisine type."}), 404
    
    return restaurants_schema.jsonify(restaurants)

#search by location
@app.route("/restaurants/location/<path:location>", methods=["GET"])
def get_restaurants_by_location(location):
    restaurants = Restaurant.query.filter(func.lower(Restaurant.location) == func.lower(location)).all()
    return restaurants_schema.jsonify(restaurants)


#add a review to a restaurant
@app.route("/restaurants/<int:restaurant_id>/reviews", methods=["POST"])
def add_review(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    
    rating = request.json.get("rating")
    comment = request.json.get("comment", "")
    user = request.json.get("user")
    timestamp = request.json.get("timestamp", datetime.now(timezone.utc)) 
    

    if rating is None:
        return jsonify({"error": "Rating is required"}), 400
    
    new_review = Review(
        rating=rating, 
        comment=comment, 
        restaurant_id=restaurant.id,
        user=user,
        timestamp=timestamp  
    )

    db.session.add(new_review)
    db.session.commit()

    return review_schema.jsonify(new_review), 201

if __name__ == "__main__":
    app.run(debug=True)