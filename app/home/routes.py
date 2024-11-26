from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import logout_user

from app import app
from app.jwt_helper import TokenManager

home_app = Blueprint("home_app", __name__)


from flask import Blueprint, redirect, render_template, url_for, request
from app import app

@app.route("/")
@app.route("/home")
def home_page():
    # token = request.cookies.get('access_token')

    # if not token or not TokenManager.verify_token(token):
    #     return redirect(url_for("customer_signin_page"))

    return render_template("home.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("Você foi desconectado.", category="info")
    return redirect(url_for("home_page"))
