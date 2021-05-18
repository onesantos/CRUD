from flask import Flask


def init_app(app: Flask):
    @app.errorhandler(400)
    def bad_request(e):
        return {"message": e.description}
