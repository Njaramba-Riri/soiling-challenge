from flask_wtf import FlaskForm
import phonenumbers.util
from wtforms import StringField, IntegerField, TelField, SelectField, RadioField, DecimalRangeField
from wtforms.validators import DataRequired, Optional, Length, NumberRange, ValidationError, InputRequired

import phonenumbers

class featuresForm(FlaskForm):
    gender = RadioField("Select gender", validators=[DataRequired()], choices=[("Male", "Male"), ("Female", "Female")])
    age = IntegerField("Age of the child", validators=[DataRequired(), NumberRange(min=3, max=15)])
    hrs_slept = IntegerField("How many hours slept?", validators=[DataRequired(), NumberRange(min=1, max=15)])
    leep_qty = SelectField("Sleep quality", validators=[DataRequired()],
                           choices=[(" ", "-----Select Option-----"), ("Excellent", "Excellent"),
                                    ("Good", "Good"), ("Concerning", "Concerning")])
    food_taken = SelectField("Main dish", validators=[DataRequired()], 
                             choices=[(" ", "-----Select Option-----"), ("Ugali", "Ugali"), 
                                      ("Meat", "Meat"), ("Rice", "Rice"),
                                      ("Fruits", "Fruits"), ("Veggies", "Veggies"), ("Githeri", "Githeri")])
    food_amount = RadioField("Amout of food taken", validators=[DataRequired()],
                              choices=[("Heavy", "Heavy"), ("Normal", "Normal"), ("Small", "Small")])
    drinks = SelectField("Drinks taken", validators=[DataRequired()],
                         choices=[(" ", "-----Select Option-----"), ("Coffee", "Coffee"), 
                                  ("Tea", "Tea"), ("Porridge", "Porridge"), ("Soft Drink", "Soft Drink"), 
                                  ("Water", "Water")])
    temperatures = IntegerField("Average temperature", validators=[DataRequired(), NumberRange(min=10.0, max=40.0)])
    exercise = RadioField("Involved in any form of execise?", validators=[DataRequired()],
                          choices=[('Yes', "Yes"), ("No", "No")])
    medication = RadioField("Any medication taken?", validators=[DataRequired()],
                             choices=[("Yes", "Yes"), ("No", "No")])
    visit_restroom = RadioField("Visited rest room today?", validators=[DataRequired()],
                                choices=[("Yes", "Yes"), ("No", "No")])
    times_rest = IntegerField("If yes, how many times?", validators=[InputRequired(), NumberRange(min=0, max=10)])
    tel = TelField("Caregiver/parent mobile", validators=[Optional()])
    name = StringField("Name of the child", validators=[Optional()])
    
    
    def validate_tel(form, field):
        try:
            telephone = phonenumbers.parse(field.data)
            if not phonenumbers.is_valid_number(telephone):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError("Invalid phone number.")
                
