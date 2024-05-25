import os 
import logging
import numpy as np
from flask import (Blueprint, flash, jsonify, render_template, 
                   url_for, request, redirect, session, current_app)
from flask_login import login_required


from webapp import db, celery
from .forms import featuresForm
from .models import Features
from ..predict import predict_input, predict_time
from ..notify import nofication

main_blueprint = Blueprint("main", __name__)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

@main_blueprint.route('/')
def index():
    return render_template("main/index.html")

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")

@main_blueprint.route("/predict", methods=['POST', 'GET'])
def predict():
    form = featuresForm()
    if request.method == 'POST' and form.validate_on_submit():
        gender = form.gender.data
        age = form.age.data
        hrs_slept = form.hrs_slept.data
        sleep_qlt = form.leep_qty.data
        food = form.food_taken.data
        food_amt = form.food_amount.data
        drink = form.drinks.data
        temp = form.temperatures.data
        exercise = form.exercise.data
        medication = form.medication.data
        restroom = form.visit_restroom.data
        times_rest = form.times_rest.data
        tel = form.tel.data
        name = form.name.data
        
        features = [gender, age, hrs_slept, sleep_qlt, food, food_amt,
                             drink, temp, exercise, medication, restroom, times_rest]
        
        label, probability = predict_input(features)
        duration = predict_time(features)
        try:
            features = Features(gender=gender, age=age, hrs_slept=hrs_slept, sleep_quality=sleep_qlt,
                                food_taken=food, food_amount=food_amt, drink=drink,
                                temperatures=temp, exercise=exercise, medication=medication,
                                visit_restroom=restroom, times_visited=times_rest, 
                                caregiver=form.tel.data, child_name=form.name.data, 
                                predicted=label, probability=probability, time=duration)
            
            session['time'] = duration            
            if name:
                session['name'] = name
            if tel:
                session['receiver'] = tel
                nofication(current_app, 
                           receiver=tel, 
                           sender=current_app.config['TWILIO_SENDER'], 
                           name=name, time=duration)
                reminder_time = max(duration - 5, 0)
                reminder_notification.apply_async((tel, name, 5), countdown=reminder_time*60)
            db.session.add(features)
            db.session.commit()         
            return redirect(url_for('main.results'))
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error when generating prediction: {e}")
            flash(f"The prediction was not successful, kindly try again", category='warning')
    return render_template("main/predict.html", form=form)

@celery.task()
def reminder_notification(telephone, name, time):
    nofication(current_app, 
               receiver=telephone,
               name=name,
               time=time)

@main_blueprint.route('/thanks')
def results():
    name = session.get('name')
    time = session.get('time')
    tel = session.get('tel')
    return render_template('main/result.html', name=name, duration=time, tel=tel)
        
@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html')


        
