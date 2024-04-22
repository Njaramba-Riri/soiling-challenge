from datetime import datetime

from webapp import db
from . import bcrypt

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    joined = db.Column(db.DateTime(), default=datetime.now)
    last_seen = db.Column(db.DateTime(), default=datetime.now)
    
    def __repr__(self) -> str:
        return f"<User> : {self.name}"
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
        
    def ping(self):
        self.last_seen = datetime.now()
        db.session.add(self)
        
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)
