from flask import Blueprint, request, jsonify
from app.models import Movie
from app.extensions import db

movie_bp = Blueprint("movie", __name__)

# GET - Lấy danh sách phim
@movie_bp.route("/", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies]), 200

# POST - Thêm phim mới
@movie_bp.route("/", methods=["POST"])
def add_movie():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Thiếu thông tin tiêu đề"}), 400

    new_movie = Movie(
        title=data["title"],
        director=data.get("director"),
        year=data.get("year")
    )
    db.session.add(new_movie)
    db.session.commit()

    return jsonify(new_movie.to_dict()), 201

# PUT - Cập nhật phim
@movie_bp.route("/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    data = request.get_json()

    movie.title = data.get("title", movie.title)
    movie.director = data.get("director", movie.director)
    movie.year = data.get("year", movie.year)

    db.session.commit()
    return jsonify(movie.to_dict()), 200

# DELETE - Xoá phim
@movie_bp.route("/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Phim đã bị xoá"}), 200
