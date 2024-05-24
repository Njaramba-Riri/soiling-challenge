import datetime

from webapp import db
from ..auth.models import User

class Features(db.Model):
    """Defines the database model for storing submitted features."""
    
    __tablename__ = "features"
    
    id =  db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hrs_slept = db.Column(db.Integer, nullable=False)
    sleep_quality = db.Column(db.String(20), nullable=False)
    food_taken = db.Column(db.String(20), nullable=False)
    food_amount = db.Column(db.String(20), nullable=False)
    drink = db.Column(db.String(20), nullable=False)
    temperatures = db.Column(db.Float, nullable=False)
    exercise = db.Column(db.String(5), nullable=False)
    medication = db.Column(db.String(5), nullable=False)
    visit_restroom = db.Column(db.String(5), nullable=False)
    times_visited = db.Column(db.Integer, nullable=False)
    caregiver = db.Column(db.String(30), nullable=True)
    child_name = db.Column(db.String(50), nullable=True)
    predicted = db.Column(db.String(10), nullable=True)
    probability = db.Column(db.Integer, nullable=True)
    time = db.Column(db.String(10), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='features')
    date = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)
    feedback = db.relationship('Feedback', backref='feature', lazy='dynamic')


class Feedback(db.Model):
    """"Defines the database model for storing user feedback"""
    
    __tablename__ = "feedback"
    
    id = db.Column(db.Integer, primary_key=True)
    feed = db.Column(db.Text(), nullable=False)
    features_id = db.Column(db.Integer, db.ForeignKey('features.id'), nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    email = db.Column(db.String(64))
    mobile = db.Column(db.String(20))
    text = db.Column(db.Text())
    
    def __repr__(self) -> str:
        return "<Reminder ''>".format(self.text[:20])
