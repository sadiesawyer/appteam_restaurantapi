from flask import Flask, request, jsonify
from models import db, ma, Restaurant, Review, RestaurantSchema, ReviewSchema
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

