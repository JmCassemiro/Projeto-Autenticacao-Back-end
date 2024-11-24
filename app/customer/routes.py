from flask import Blueprint, redirect, render_template, url_for

from app import app
from app.customer.services.signin_form import SigninForm
from app.customer.services.signup_form import SignupForm
from app.customer.services.form_validations import (validade_form_on_signin,
                                                    validate_form_on_signup)

customer_app = Blueprint("customer", __name__)


@app.route("/customer-signin", methods=["GET", "POST"])
def customer_signin_page():
    form = SigninForm()
    is_form_validated = validade_form_on_signin(form)

    if is_form_validated:
      return redirect(url_for("home_page"))

    return render_template("customer_signin.html", form=form)


@app.route("/customer-signup", methods=["GET", "POST"])
def customer_signup_page():
    form = SignupForm()
    is_form_validated = validate_form_on_signup(form)

    if is_form_validated:
      return redirect(url_for("home_page"))

    return render_template("customer_signup.html", form=form)
