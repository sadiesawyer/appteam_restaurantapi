# appteam_restaurantapi

# Tools
For this project, I decided to use **Flask** as the framework for building the API. I chose Flask because in the case of this project, it is simpler and more lightweight than other frameworks, making it faster and only needing the most essential functionality. I also have a decent amount of experience in Flask, so it didn't require to much background reading on documentation and setup. For a time crunch like this, I think Flask is the best option because you can get a Flask app up and running with only a few lines of code, and it makes creating REST API endpoints super simple.

I opted to use **Marshmallow** for serialization because it is build to work well with Flask. This way, I didn't have to manually convert both objects to user-readable JSON and it would interpret user input without having to manually parse it. It also has great data validation rules and constraints, ensuring that users send valid data and that bad data doesn't get put in the database.

I chose **SQLAlchemy** for querying the database because it eliminates the need to write raw SQL queries, which can be error prone. It integrates really well with Flask, and it is simple to define an entity and its relationships. I also installed Flask Migrate so that I could update the database using CLI commands more easily.

This was a fun project from the get-go because I was implementing a lot of the database concepts that we have learned this semester in INLS 523 in a hands-on way.

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


