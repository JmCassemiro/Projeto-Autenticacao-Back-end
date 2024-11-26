from flask import Blueprint, redirect, render_template, url_for, request
from app import app
from app.customer.services.signin_form import CustomerSigninForm
from app.customer.services.signup_form import CustomerSignupForm
from app.customer.services.form_validations import (validate_form_on_signup, validade_form_on_signin)
from app.jwt_helper import TokenManager

customer_app = Blueprint("customer", __name__)

@app.route("/customer-signin", methods=["GET", "POST"])
def customer_signin_page():
    token = request.cookies.get('access_token')
    if token and TokenManager.verify_token(token):
        return redirect(url_for("home_page"))

    form = CustomerSigninForm()
    is_form_validated = validade_form_on_signin(form)

    if is_form_validated:
        return redirect(url_for("home_page"))

    return render_template("customer_signin.html", form=form)


@app.route("/customer-signup", methods=["GET", "POST"])
def customer_signup_page():
    token = request.cookies.get('access_token')
    if token and TokenManager.verify_token(token):
        return redirect(url_for("home_page"))

    form = CustomerSignupForm()
    is_form_validated = validate_form_on_signup(form)

    if is_form_validated:
        return redirect(url_for("home_page"))

    return render_template("customer_signup.html", form=form)
