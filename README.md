# appteam_restaurantapi
# Overview
This Restaurant Rating API is a REST API designed to manage restaurant listings, reviews, and ratings. Users can retrieve restaurant details, search for restaurants based on various criteria, submit reviews, and fetch average ratings. I created this for my interview for Backend developer for App Team Carolina.

# Features
- Retrieve all restaurant listings
- Search for restaurants by name, cuisine type, or location
- Add new restaurants
- Submit and retrieve reviews for restaurants
- Get average rating for a specific restaurant

# Tools
For this project, I decided to use **Flask** as the framework for building the API. I chose Flask because in the case of this project, it is simpler and more lightweight than other frameworks, making it faster and only needing the most essential functionality. I also have a decent amount of experience in Flask, so it didn't require to much background reading on documentation and setup. For a time crunch like this, I think Flask is the best option because you can get a Flask app up and running with only a few lines of code, and it makes creating REST API endpoints super simple.

I opted to use **Marshmallow** for serialization because it is build to work well with Flask. This way, I didn't have to manually convert both objects to user-readable JSON and it would interpret user input without having to manually parse it. It also has great data validation rules and constraints, ensuring that users send valid data and that bad data doesn't get put in the database. In the future, I would probably want to implement some security in user input to avoid SQL injections 

I chose **SQLAlchemy** for querying the database because it eliminates the need to write raw SQL queries, which can be error prone. It integrates really well with Flask, and it is simple to define an entity and its relationships. I also installed Flask Migrate so that I could update the database using CLI commands more easily. That was something I ran into trouble with, though.

I also used **Postman** to test my endpoints at the suggestion of the team, which was a new tool I haven't tried before! In previous projects, I built a simple frontend to test or used the terminal and local host. I found that Postman made it really simple and much easier to debug, so I will definitely be using that in the future.

This was a fun project from the get-go because I was implementing a lot of the database concepts that we have learned this semester in INLS 523 as abstract topics in a hands-on way.

## Endpoints Documentation

### Restaurants

#### Add a Restaurant
- **Endpoint**: `/restaurants`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "string",
    "cuisine_type": "string",
    "location": "string"
  }
  ```
- **Response**: Created restaurant details (JSON).

#### Get All Restaurants
- **Endpoint**: `/restaurants`
- **Method**: `GET`
- **Response**: List of all restaurants (JSON).

#### Get Restaurant by ID
- **Endpoint**: `/restaurants/<int:id>`
- **Method**: `GET`
- **Response**: Restaurant details (JSON).

#### Search Restaurants by Name, Cuisine, or Location
- 
- **Response**: List of matching restaurants (JSON).

---

### Reviews

#### Add a Review
- **Endpoint**: `/restaurants/<int:restaurant_id>/reviews`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "rating": "float",
    "comment": "string",
    "user": "string",
    "timestamp": "datetime (optional)"
  }
  ```
- **Response**: Created review details (JSON).

#### Get Reviews for a Restaurant
- **Endpoint**: `/restaurants/<int:restaurant_id>/reviews`
- **Method**: `GET`
- **Response**: List of reviews for the restaurant (JSON).

#### Get Reviews by User
- **Endpoint**: `/restaurants/reviews/<path:user>`
- **Method**: `GET`
- **Response**: List of reviews by the user (JSON).


