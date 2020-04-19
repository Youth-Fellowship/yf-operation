"""This module contains all the API for the hymnal service"""
import pymongo
from flask import Blueprint, current_app, jsonify, request

bp = Blueprint("hymns", __name__, url_prefix="/hymns")


@bp.route("/", methods=["GET"])
def hymns():
    """get all the hymns in the data store"""
    # retrieve the database connection from the app instance
    db = current_app.db
    hymn_collection = db.hymns
    # trying to avoid using global keyword
    hymn_cursor = [{}]

    # probably a query was attached
    # the query can be extended to fields and values
    category = request.args.get('category')
    if category is not None and category != "":
        category = category.upper()
        query = {"category": category}
        hymn_cursor[0] = hymn_collection.find(query, projection={'_id': False})
    else:
        hymn_cursor[0] = hymn_collection.find({}, projection={'_id': False}).sort([
            ('category', pymongo.ASCENDING),
            ('no', pymongo.ASCENDING)
        ])

    all_hymns = list(hymn_cursor[0])

    return jsonify(hymns=all_hymns)


@bp.route("/categories", methods=["GET"])
def hymns_categories():
    """get all the hymns in the data store"""
    # retrieve the database connection from the app instance
    db = current_app.db
    # get all the ordered hymns categories
    hymn_cursor = db.hymns.distinct('category')
    categories = list(hymn_cursor)

    return jsonify(categories=categories)
