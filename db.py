"""This module will handle the creation of connection to the mongo server"""
from flask import current_app, g
from flask_pymongo import PyMongo


def init_db():
    # connect to the db
    current_app.config["MONGO_URI"] = "mongodb://localhost:27017/churchdb"
    mongo = PyMongo(current_app)
    # add the db connection to global variable
    g.db = mongo.db
    return g.db