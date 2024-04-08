from flask_wtf import FlaskForm, RecaptchaField

from wtforms import StringField, SelectField, IntegerField, RadioField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo

class register(FlaskForm):
    name = StringField("Your name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Your email address", validators=[DataRequired(), Email(), Length(max=100)])
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


class signin(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me", validators=[Optional()])
