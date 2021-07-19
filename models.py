# Database models

from . import db # Imports from current package  (website folder)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #  Foreign key references an ID from one column in a database to another, relates databases
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Must pass existing user ID to have access into the database
    # user_id relates User and Note classes

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Relates two classes:
    notes = db.relationship('Note')
