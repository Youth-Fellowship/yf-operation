"""This module contains all the API for the hymnal service"""
from flask import Blueprint, g


bp = Blueprint("hymns", __name__, url_prefix="/hymns")


@bp.route("/", methods=["GET"])
def all_hymns():
    return "I will get all the hymns"
