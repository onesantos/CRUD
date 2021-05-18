from flask import Flask
from app.model.database import db


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=True)
    genre = db.Column(db.String(255), nullable=False)


def init_app(app: Flask):
    db.create_all(app=app)