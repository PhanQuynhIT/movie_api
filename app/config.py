# import os

# class Config:
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:2@localhost:5432/moviedb")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
