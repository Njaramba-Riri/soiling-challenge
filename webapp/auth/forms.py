from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm, RecaptchaField

from wtforms import StringField, SelectField, IntegerField, RadioField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Optional, Length, EqualTo, ValidationError

from .models import User

class register(FlaskForm):
    name = StringField("Your name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Your email address", validators=[DataRequired(), Length(max=100)])
    username = StringField("Preffered username", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm = PasswordField("Confirm password", validators=[DataRequired(),
                                                          EqualTo('password', "Both password and conmfirm password must match.")])
    patient = RadioField("Do you live with an austic child?", validators=[DataRequired()],
                          choices=[("Yes", "Yes"), ("No", "No")])
    relation = SelectField("How are you related to the child?", validators=[DataRequired()],
                           choices=[(" ", "-----Select from Options-----"), ("Parent", "Parent"),
                                    ("Sibling", "Sibling"), ("Guardian", "Guardian"), 
                                    ("Caregiver", "Caregiver")])
    soiling = SelectField("Does the child have soiling challenges?", validators=[DataRequired()],
                          choices=[(" ", "-----Select from Options-----"), 
                                   ("Yes", "Yes"), ("No", "No")])
    age = IntegerField("Age of the child", validators=[DataRequired()])
    # captcha = RecaptchaField("Confirm you are not a robot", validators=[DataRequired()])
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already exists, log-in instead.")
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("That username is already taken, try another one.")

class signin(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me", validators=[Optional()])
    
    def validate(self, extra_validators=None) -> bool:
        check_validate = super(signin, self).validate(extra_validators)
        if not check_validate:
            return False
        
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append("User with such username does not exist.")
            return False
        
        if not user.check_password(self.password.data):
            self.password.errors.append("Invalid credentials, try again!.")
            return False
        return True
        
