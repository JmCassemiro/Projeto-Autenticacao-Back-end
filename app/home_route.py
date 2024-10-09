from flask import render_template, Blueprint

from app import app

home_blueprint = Blueprint("home", __name__, template_folder="templates")
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')