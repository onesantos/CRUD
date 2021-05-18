from flask import Flask
from app.config import config
from app.model import database
from app.model import tables
from app.resource import movies
from app.errors import errors


def create_app():
    app = Flask(__name__)
    config.init_app(app=app)
    database.init_app(app=app)
    tables.init_app(app=app)
    errors.init_app(app=app)
    movies.init_app(app=app)

    return app
