from services import app
from flask import render_template, Blueprint

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/register")
def register_page():
    return render_template("register.html")
