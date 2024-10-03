from flask import Flask

app = Flask(__name__)

from services.auth_service import routes
