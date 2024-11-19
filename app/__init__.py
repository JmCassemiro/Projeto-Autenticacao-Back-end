from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from utils.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    db.init_app(app)

    app.home_template_folder = Config.HOME_TEMPLATE_FOLDER
    app.customer_template_folder = Config.CUSTOMER_TEMPLATE_FOLDER
    common_templates_folder = Config.COMMON_TEMPLATES_FOLDER
    app.jinja_loader.searchpath.append(common_templates_folder)

    from app.customer.routes import customer_bp
    from app.home.routes import home_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(customer_bp)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "customer.login_customer_page"
    login_manager.login_message_category = "info"

    from app.customer.model import CustomerModel

    @login_manager.user_loader
    def load_user(user_id):
        return CustomerModel.query.get(int(user_id))

    return app
