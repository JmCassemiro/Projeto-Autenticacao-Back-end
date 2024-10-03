from services import app
from services.auth_service.routes import auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)
