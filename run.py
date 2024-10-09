from app import app
from app.customer.routes import customer_login_blueprint, customer_register_blueprint
from app.home_route import home_blueprint

app.register_blueprint(customer_login_blueprint, url_prefix="/login_customer")
app.register_blueprint(customer_register_blueprint, url_prefix="/register_customer")
app.register_blueprint(home_blueprint, url_prefix="/home")

if __name__ == '__main__':
    app.run(debug=True)
