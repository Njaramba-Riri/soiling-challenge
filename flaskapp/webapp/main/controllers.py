from flask import Blueprint, flash, jsonify, render_template, url_for, request

from .forms import featuresForm

main_blueprint = Blueprint("main", __name__)


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
        flash("Your predictions are being generated", category="info")
    return render_template("main/predict.html", form=form)
