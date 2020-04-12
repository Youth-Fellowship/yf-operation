"""This module will handle the creation of connection to the mongo server"""
import os

from flask import current_app, g
from flask_pymongo import PyMongo
from dotenv import load_dotenv


load_dotenv()

DB_URI = os.environ.get("MONGODB_URI")


def init_db(app: object) -> object:
    # connect to the db
    current_app.config["MONGO_URI"] = DB_URI
    mongo = PyMongo(app)

    if mongo.db is None:
        raise ConnectionError("Could not connect to the mongodb database")

    # TODO: implement logging here
    print("Database connected!")
    return mongo.db
