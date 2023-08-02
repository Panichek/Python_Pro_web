from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class User(db.Model,
           UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String(150))
    password = db.Column(db.String(250))

