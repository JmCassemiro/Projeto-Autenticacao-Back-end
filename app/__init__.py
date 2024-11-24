from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = Config.SECRET_KEY

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "customer_signin_page"
login_manager.login_message_category = "info"

from .customer.routes import customer_app
from .employee.routes import employee_app
from .home.routes import home_app

app.register_blueprint(customer_app)
app.register_blueprint(employee_app)
app.register_blueprint(home_app)

from .customer.model import Customer
from .employee.model import Employee
from .employee.model import Employee


@login_manager.user_loader
def load_user(user_id):
    try:
        customer = Customer.query.get(int(user_id))
        if customer:
            return customer

        employee = Employee.query.get(int(user_id))
        if employee:
            return employee

        return None

    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None
