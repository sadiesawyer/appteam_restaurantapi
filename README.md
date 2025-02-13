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

# API Endpoints

| HTTP Method | Endpoint | Parameters | Description | Expected Response |
|------------|----------|------------|-------------|--------------------|
| **POST** | `/restaurants` | `name`, `cuisine_type`, `location` (JSON body) | Add a new restaurant to the list. | `201 Created` `{ "id": 1, "name": "Example", "cuisine_type": "Italian", "location": "NYC" }` |
| **GET** | `/restaurants` | None | Fetch all restaurants. | `200 OK` `[ { "id": 1, "name": "Example", "cuisine_type": "Italian", "location": "NYC" }, ... ]` |
| **GET** | `/restaurants/<int:id>` | `id` (path parameter) | Get details for a specific restaurant by ID. | `200 OK` `{ "id": 1, "name": "Example", "cuisine_type": "Italian", "location": "NYC" }` or `404 Not Found` |
| **GET** | `/restaurants/search` | `cuisine_type`, `name`, `location` (query parameters) | Search restaurants by name, cuisine, or location. | `200 OK` `[ { "id": 2, "name": "Pizza Place", "cuisine_type": "Italian", "location": "Chicago" } ]` or `404 Not Found` |
| **POST** | `/restaurants/<int:id>/reviews` | `user`, `comment`, `rating` (JSON body) | Add a review for a specific restaurant. | `201 Created` `{ "review_id": 1, "user": "JohnDoe", "rating": 5, "comment": "Great food!" }` |
| **GET** | `/restaurants/reviews` | `user`, `restaurant_id`, `restaurant_name` (query parameters) | Get reviews by restaurant ID, user, or restaurant name. | `200 OK` `[ { "review_id": 1, "user": "JohnDoe", "rating": 5, "comment": "Great food!" } ]` or `404 Not Found` |
| **GET** | `/restaurants/average-rating/<identifier>` | `restaurant_id` or `restaurant_name` (path parameter) | Get the average rating of a restaurant by ID or name. | `200 OK` `{ "restaurant": "Pizza Place", "average_rating": 4.5 }` or `404 Not Found` |

---

# Running the API

## Prerequisites
Before running the API, ensure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)
- Any additional dependencies specified in `requirements.txt` (if applicable)

## Steps to Run the API

1. **Clone the Repository**  
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**  
   ```bash
   python -m flask run
   ```
   By default, Flask runs the server on `http://127.0.0.1:5000/`.

4. **Testing the API**  
   Use tools like curl in the command line or Postman

   Example cURL request to fetch all restaurants:
   ```bash
   curl http://127.0.0.1:5000/restaurants
   ```

5. **Stopping the Server**  
   Press *CTRL+C* in the terminal to stop the Flask server.

---
```

