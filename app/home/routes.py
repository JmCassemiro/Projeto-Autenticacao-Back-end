from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import logout_user

from app import app

home_app = Blueprint("home_app", __name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("Você foi desconectado.", category="info")
    return redirect(url_for("home_page"))
