from flask import render_template, Blueprint

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/")
@home_bp.route("/home")
def home_page():
    return render_template("home.html")
