from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TelField, SelectField, RadioField, DecimalRangeField
from wtforms.validators import DataRequired, Optional, Length, NumberRange

class featuresForm(FlaskForm):
    gender = RadioField("Select Gender", validators=[DataRequired()], choices=[("Male", "Male"), ("Female", "Female")])
    age = IntegerField("Age of the child", validators=[DataRequired()])
    hrs_slept = IntegerField("How many hours slept?", validators=[DataRequired()])
    leep_qty = SelectField("Sleep quality", validators=[DataRequired()],
                           choices=[(" ", "-----Select Option-----"), ("Excellent", "Excellent"),
                                    ("Good", "Good"), ("Concerning", "Concerning"), 
                                    ("Worse", "Worse"), ("Worst", "Worst")])
    food_taken = SelectField("Food taken", validators=[DataRequired()], 
                             choices=[(" ", "-----Select Option-----"), ("Ugali", "Ugali"), 
                                      ("Chapati", "Chapati"), ("Meat", "Meat"), ("Rice", "Rice"),
                                      ("Fruits", "Fruits"), ("Veggies", "Veggies"), ("Snacks", "Snacks")])
    food_amount = RadioField("Amout of food taken", validators=[DataRequired()],
                              choices=[("Heavy", "Heavy"), ("Normal", "Normal"), ("Small", "Small")])
    drinks = SelectField("Drinks taken", validators=[DataRequired()],
                         choices=[(" ", "-----Select Option-----"), ("Coffee", "Coffee"), 
                                  ("Tea", "Tea"), ("Porridge", "Porridge"), ("Soft Drink", "Soft Drink"), 
                                  ("Milk", "Milk"), ("Water", "Water")])
    temperatures = DecimalRangeField("Average temperature", validators=[DataRequired(), NumberRange(min=10.0, max=40.0)])
    execises = RadioField("Involved in any form of execise?", validators=[DataRequired()],
                          choices=[('Yes', "Yes"), ("No", "No")])
    medication = RadioField("Any medication taken?", validators=[DataRequired()],
                             choices=[("Yes", "Yes"), ("No", "No")])
    visit_restroom = RadioField("Visited rest room today?", validators=[DataRequired()],
                                choices=[("Yes", "Yes"), ("No", "No")])
    times_rest = IntegerField("If yes, how many times?", validators=[DataRequired(), Length(min=0, max=10)])
    tel = TelField("Caregiver/parent mobile", validators=[Optional()])
    
