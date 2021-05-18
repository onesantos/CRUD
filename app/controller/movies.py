from app.model.tables import Movie
from app.model.tables import db
from app.model.serializer import SerialMovie
from sqlalchemy import func


serial_movie = SerialMovie()
serial_movie_many = SerialMovie(many=True)


def check_movie(name: str, year: int) -> bool:
    movie = Movie.query.filter_by(name=name, year=year).first()
    return True if movie else False


def create_movie(movie: dict):
    if check_movie(name=movie["name"], year=movie["year"]):
        return {"message": "Movie exists."}, 400
    mov = Movie(**movie)
    db.session.add(mov)
    db.session.commit()
    db.session.flush()
    return {"message": "Movie created", "movie": serial_movie.dump(mov)}, 201


def select_all_movies() -> list:
    movies = Movie.query.all()
    movies_dict = serial_movie_many.dump(movies)
    return {"movies": movies_dict}


def select_movie_by_name(name: str) -> dict:
    movie = Movie.query.filter(func.lower(Movie.nome) == func.lower(name)).first()
    return serial_movie.dump(movie)


def select_movie_by_id(id: int) -> dict:
    movie = Movie.query.filter_by(id=id).first()
    return serial_movie.dump(movie)


def select_movie_by_year(year: str) -> list:
    movies = Movie.query.filter_by(ano=year).all()
    return {"movies": serial_movie_many.dump(movies)}


def select_all_unrated_movies() -> list:
    movies = Movie.query.filter_by(rate=None).all()
    return {"movies": serial_movie_many.dump(movies)}


def select_all_unrated_movies_filter(movies: list) -> dict:
    movies = Movie.query.filter(Movie.name.in_(movies), Movie.rate == None).first()
    return serial_movie.dump(movies)


def update_rate_movie_by_id(id: int, rate: float):
    movie = Movie.query.filter_by(id=id, rate=None).first()
    if not movie:
        return {"message": "The movie has already been rated."}, 400
    db.session.query(Movie).filter_by(id=id).update({"rate": rate})
    db.session.commit()
    db.session.flush()
    return {"message": "Movie updated.", "movie": serial_movie.dump(movie)}


def delete_movie_by_id(id):
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        return {"message": "Movie not exists."}, 400
    db.session.delete(movie)
    db.session.commit()
    return {"message": "Movie deleted."}
