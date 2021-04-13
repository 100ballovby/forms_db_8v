# Database models
from app import db


class User(db.Model):
    """Класс для пользователя сайта"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(256))