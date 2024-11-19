import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Config:
    DB_PATH = os.path.join(BASE_DIR, 'utils', 'authentication.db')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get("SECRET_KEY") or "ec9439cfc6c796ae2029594d"

    # Caminhos para os templates
    HOME_TEMPLATE_FOLDER = os.path.join(BASE_DIR, "app/home/templates")
    CUSTOMER_TEMPLATE_FOLDER = os.path.join(BASE_DIR, "app/customer/templates")
    COMMON_TEMPLATES_FOLDER = os.path.join(BASE_DIR, "app/common_templates")