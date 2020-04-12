from flask import Flask

from hymns import bp
from db import init_db



def create_app():
    # create and configure the app
    app: Flask = Flask(__name__)

    # create database connection
    with app.app_context():
        # make the db connection to have access to the db instance
        # in the API blueprint.
        # I haven't figured a better way yet
        app.db = init_db(app)

    # register the blueprint
    app.register_blueprint(bp)

    return app


# create the app
app = create_app()
