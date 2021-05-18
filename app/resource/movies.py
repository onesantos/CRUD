from flask import Flask, request
from typing import List
from flask_expects_json import expects_json
from app.schema.schema import schema_movie
from app.schema.schema import schema_movie
from app.controller.movies import create_movie
from app.controller.movies import select_all_movies
from app.controller.movies import select_movie_by_name
from app.controller.movies import select_movie_by_year
from app.controller.movies import select_all_unrated_movies
from app.controller.movies import select_all_unrated_movies_filter
from app.controller.movies import update_rate_movie_by_id
from app.controller.movies import select_movie_by_id
from app.controller.movies import delete_movie_by_id


def init_app(app: Flask):
    @app.route("/movies", methods=["POST"])
    @expects_json(schema_movie)
    def res_post_movie():
        return create_movie(movie=request.json)

    @app.route("/movies", methods=["GET"])
    def res_get_movies():
        return select_all_movies()

    @app.route("/movies/<name>", methods=["GET"])
    def res_get_movie_by_name(name):
        return select_movie_by_name(name)

    @app.route("/movies/<int:year>/year", methods=["GET"])
    def res_get_movie_by_year(year):
        return select_movie_by_year(year)

    @app.route("/movies/<int:id>", methods=["GET"])
    def res_get_movie_by_id(id):
        return select_movie_by_id(id)

    @app.route("/movies/unrated", methods=["GET"])
    def res_get_movie_unrated():
        return select_all_unrated_movies()

    @app.route("/movies/unrated", methods=["POST"])
    def res_get_movie_unrated_filter():
        movies = request.json
        if not movies:
            return {"message": "missing data."}, 400
        for movie in movies:
            if type(movie) != str:
                return {"message": "invalid data, objects not is string."}, 400
        return select_all_unrated_movies_filter(movies=movies)

    @app.route("/movies/rate/<int:id>", methods=["PATCH"])
    def res_patch_movie_rate(id):
        data = request.json
        if not data or "rate" not in data or not data["rate"] or type(data["rate"]) != float:
            return {"message": "Invalid data."}, 400
        return update_rate_movie_by_id(id=id, rate=data["rate"])

    @app.route("/movies/<int:id>", methods=["DELETE"])
    def res_delete_movie_rate(id):
        return delete_movie_by_id(id=id)
