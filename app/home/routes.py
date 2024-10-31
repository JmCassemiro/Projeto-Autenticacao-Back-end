from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import logout_user

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/")
@home_bp.route("/home")
def home_page():
    return render_template("home.html")


@home_bp.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home.home_page"))
