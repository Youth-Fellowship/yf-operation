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
    hymn_no = request.args.get('hymn_no')

    try:
        hymn_no = int(hymn_no)
    except:
        hymn_no = None

    #  if both category and hymn_no are present in the request query parameters.
    if (category is not None and category != "") and hymn_no is not None:
        query = {"category": category.upper(), "no": hymn_no}
        hymn_cursor[0] = hymn_collection.find(query, projection={'_id': False})
    elif category is not None and category != "":
        query = {"category": category.upper()}
        hymn_cursor[0] = hymn_collection.find(query, projection={'_id': False})
    elif hymn_no is not None:
        query = {"no": hymn_no}
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
