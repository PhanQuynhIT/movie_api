from flask import Flask
from app.config import Config
from app.extensions import db
from app.routes.movie_routes import movie_bp

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object(Config)

    if testing:
        app.config["TESTING"] = True

    db.init_app(app)

    from app.routes.movie_routes import movie_bp
    app.register_blueprint(movie_bp, url_prefix="/api/movies")

    return app

