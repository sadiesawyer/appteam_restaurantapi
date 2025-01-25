# appteam_restaurantapi

#Tools
For this project, I decided to use **Flask** as the framework for building the API. I chose Flask because in the case of this project, it is simpler and more lightweight than other frameworks, making it faster and only needing the most essential functionality. For a time crunch like this, I think Flask is the best option because you can get a Flask app up and running with only a few lines of code, and it makes creating REST API endpoints super simple.

I opted to use **Marshmallow** for serialization because it is build to work well with Flask. This way, I didn't have to manually convert both objects to user-readable JSON and it would interpret user input without having to manually parse it. It also has great data validation rules and constraints, ensuring that users send valid data and that bad data doesn't get put in the database.

I chose **SQLAlchemy** for querying the database because it eliminates the need to write raw SQL queries, which can be error prone. It integrates really well with Flask, and it is simple to define an entity and its relationships. I also installed Flask Migrate so that I could update the database using CLI commands more easily.

This was a fun project from the get-go because I was implementing a lot of the database concepts that we have learned this semester in INLS 523 in a hands-on way.

#API Endpoints

Restaurants

1. Add a Restaurant

Endpoint: POST /restaurants

Request Body:

{
  "name": "Restaurant Name",
  "cuisine_type": "Cuisine Type",
  "location": "Location"
}

Response: Returns the created restaurant object.

2. Get All Restaurants

Endpoint: GET /restaurants

Response: List of all restaurants.

3. Get Restaurant by ID

Endpoint: GET /restaurants/<id>

Response: Restaurant details.

4. Search Restaurants by Cuisine Type

Endpoint: GET /restaurants/cuisine/<cuisine_type>

Response: List of restaurants with the given cuisine type.

5. Search Restaurants by Location

Endpoint: GET /restaurants/location/<location>

Response: List of restaurants in the given location.

6. Search Restaurants by Name

Endpoint: GET /restaurants/name-search/<name>

Response: List of restaurants matching the given name.

Reviews

1. Add a Review to a Restaurant

Endpoint: POST /restaurants/<restaurant_id>/reviews

Request Body:

{
  "rating": 4.5,
  "comment": "Great food!",
  "user": "username"
}

Response: The created review object.

2. Get Reviews for a Restaurant

Endpoint: GET /restaurants/<restaurant_id>/reviews

Response: List of reviews for the given restaurant.

3. Get Reviews by User

Endpoint: GET /restaurants/reviews/<user>

Response: List of reviews written by the user.
