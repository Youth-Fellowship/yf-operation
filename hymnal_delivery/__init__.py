from flask import Flask, g
from flask_pymongo import PyMongo

from hymns import bp
from db import init_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    with app.app_context():
        # make the db connection
        init_db()

    # register the blueprint
    app.register_blueprint(bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app