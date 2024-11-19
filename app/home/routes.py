from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import logout_user

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("home.html")


@home_bp.route("/logout", methods=["GET", "POST"])
def logout_page():
    logout_user()
    flash("Você foi desconectado!", category="info")
    return redirect(url_for("customer.login_customer_page"))
