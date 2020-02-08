"""This module contains all the API for the hymnal service"""
from flask import Blueprint, g, current_app, jsonify


bp = Blueprint("hymns", __name__, url_prefix="/hymns")


@bp.route("/", methods=["GET"])
def all_hymns():
    db = current_app.db
    song = db.hymns.find_one({"no": 12})
    return song["title"]
