"""This module contains all the API for the hymnal service"""
import pymongo
from flask import Blueprint, current_app, jsonify

bp = Blueprint("hymns", __name__, url_prefix="/hymns")


@bp.route("/", methods=["GET"])
def hymns():
    """get all the hymns in the datastore"""
    # retrieve the database connection from the app instance
    db = current_app.db

    # get all the hymns and arranged according to categories
    hymn_cursor = db.hymns.find({}, projection={'_id': False}).sort([
        ('category', pymongo.ASCENDING),
        ('no', pymongo.ASCENDING)
    ])
    all_hymns = list(hymn_cursor)

    return jsonify(data=all_hymns)
