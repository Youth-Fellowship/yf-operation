"""This module will handle the creation of connection to the mongo server"""
from flask import current_app, g
from flask_pymongo import PyMongo


def init_db(app: object) -> object:
    # connect to the db
    current_app.config["MONGO_URI"] = "mongodb://localhost:27017/yf_church_db"
    mongo = PyMongo(app)

    if mongo.db is None:
        raise ConnectionError("Could not connect to the mongodb database")

    # TODO: implement logging here
    print("Database connected!")
    return mongo.db


# initialize the database connection
# db = init_db(current_app)
