from flask import Blueprint, flash, render_template, url_for, request

from .forms import register, signin

auth_blueprint = Blueprint("auth", __name__,
                           url_prefix="/auth")


@auth_blueprint.route("/register", methods=['GET', 'POST'])
def signup():
    form = register()
    if request.method == 'POST' and form.validate_on_submit():
        flash("Welcome to WeLove, kindly log in", category="info")
        
    return render_template("auth/register.html", form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = signin()
    if request.method == 'POST' and form.validate_on_submit():
        flash("Welcome, login successful.")
    
    return render_template("/auth/login.html", form=form)
