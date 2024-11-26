from flask import Blueprint, redirect, render_template, url_for, request
from app import app
from app.employee.services.signin_form import EmployeeSigninForm
from app.employee.services.signup_form import EmployeeSignupForm
from app.employee.services.form_validations import (validate_form_on_signup, validade_form_on_signin)
from app.jwt_helper import TokenManager

employee_app = Blueprint("employee", __name__)

@app.route("/employee-signin", methods=["GET", "POST"])
def employee_signin_page():
    token = request.cookies.get('access_token')
    if token and TokenManager.verify_token(token):
        return redirect(url_for("home_page"))

    form = EmployeeSigninForm()
    is_form_validated = validade_form_on_signin(form)

    if is_form_validated:
        return redirect(url_for("home_page"))

    return render_template("employee_signin.html", form=form)


@app.route("/employee-signup", methods=["GET", "POST"])
def employee_signup_page():
    token = request.cookies.get('access_token')
    if token and TokenManager.verify_token(token):
        return redirect(url_for("home_page"))

    form = EmployeeSignupForm()
    is_form_validated = validate_form_on_signup(form)

    if is_form_validated:
        return redirect(url_for("home_page"))

    return render_template("employee_signup.html", form=form)
