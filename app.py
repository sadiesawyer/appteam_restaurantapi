from flask import Flask, request, jsonify, render_template
from models import db, ma, Restaurant, Review, RestaurantSchema, ReviewSchema
from flask_migrate import Migrate
from sqlalchemy import func
from datetime import datetime, timezone
from flask_cors import CORS 


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

CORS(app)
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

@app.route("/")
def home():
    return render_template("index.html") 

#endpoint to add a restaurant to the list
"""{
  "name": "Juju",
  "cuisine_type": "Asian",
  "location": "Durham"
}
"""
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

#updated search function ex. /restaurants/search?cuisine_type=American&location=Chapel+hill
@app.route("/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name")
    cuisine_type = request.args.get("cuisine_type")
    location = request.args.get("location")

    query = Restaurant.query

    if name:
        query = query.filter(func.lower(Restaurant.name).contains(func.lower(name)))
    if cuisine_type:
        query = query.filter(func.lower(Restaurant.cuisine_type).contains(func.lower(cuisine_type)))
    if location:
        query = query.filter(func.lower(Restaurant.location).contains(func.lower(location)))

    restaurants = query.all()
    return restaurants_schema.jsonify(restaurants)

#add a review to a restaurant

"""{
  "user": "Alice",
  "rating": 5,
  "comment": "Amazing sushi! Definitely coming back."
}
"""
###
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

@app.route("/restaurants/reviews", methods=["GET"])
def get_reviews():
    query_type = request.args.get("type")  
    
    if query_type == 'id':
        restaurant_id = request.args.get("restaurant_id")
        reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
        return reviews_schema.jsonify(reviews)
    
    elif query_type == 'user':
        user = request.args.get("user")
        reviews = Review.query.filter(func.lower(Review.user) == func.lower(user)).all()
        return reviews_schema.jsonify(reviews)
    
    elif query_type == 'name':
        name = request.args.get("name")
        restaurant = Restaurant.query.filter(func.lower(Restaurant.name) == func.lower(name)).first()
        if not restaurant:
            return jsonify({"message": "Restaurant not found."}), 404
        reviews = Review.query.filter_by(restaurant_id=restaurant.id).all()
        return reviews_schema.jsonify(reviews)
    
    return jsonify({"message": "Invalid query type."}), 400

    
   

@app.route("/restaurants/average-rating/<path:identifier>", methods=["GET"])
def get_average_rating(identifier):
    if identifier.isdigit():
        restaurant = Restaurant.query.get(int(identifier))
    else:
        restaurant = Restaurant.query.filter(func.lower(Restaurant.name) == func.lower(identifier)).first()

    if not restaurant:
        return jsonify({"message": "Restaurant not found."}), 404

    average_rating = db.session.query(func.avg(Review.rating)).filter(Review.restaurant_id == restaurant.id).scalar()

    if average_rating is not None:
        return jsonify({"restaurant": restaurant.name, "average_rating": average_rating}), 200
    else:
        return jsonify({"message": "No reviews found for this restaurant."}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)