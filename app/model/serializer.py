from flask import Flask
from flask_marshmallow import Marshmallow
from app.model.tables import Movie

ms = Marshmallow()


def init_app(app: Flask):
    ms.init_app(app=app)


class SerialMovie(ms.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie