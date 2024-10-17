from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.db"
    app.config["SECRET_KEY"] = "ec9439cfc6c796ae2029594d"

    db.init_app(app)

    app.home_template_folder = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "home/templates"
    )
    app.customer_template_folder = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "customer/templates"
    )
    common_templates_folder = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "common_templates"
    )
    app.jinja_loader.searchpath.append(common_templates_folder)

    from app.home.routes import home_bp
    from app.customer.routes import customer_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(customer_bp)

    return app
