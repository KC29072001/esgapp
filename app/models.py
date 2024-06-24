# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Questionnaire(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True)
#     questions = db.relationship('Question', backref='questionnaire', lazy='dynamic')

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(256))
#     questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))

from . import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    questions = db.relationship('Question', backref='questionnaire', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)
