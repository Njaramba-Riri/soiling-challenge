from flask import Blueprint, flash, render_template, url_for, request, redirect
from flask_login import login_user, logout_user

from webapp import db

from .forms import register, signin
from .models import User

auth_blueprint = Blueprint("auth", __name__,
                           url_prefix="/auth")


@auth_blueprint.route("/register", methods=['GET', 'POST'])
def signup():
    form = register()
    if request.method == 'POST' and form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        except Exception as e:
            db.session.rollback()
            flash("Account not created, kindly try again", category="warning")
    return render_template("auth/register.html", form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = signin()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Welcome, login successful.")
            return redirect(url_for("main.index"))
        flash("Invalid credentials, try again.", category="warning")
    return render_template("/auth/login.html", form=form)


@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
