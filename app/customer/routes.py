from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user

from app import app, db
from app.customer.model import Customer
from app.customer.services.signin_form import SigninForm
from app.customer.services.signup_form import SignupForm
from app.jwt_helper import generate_token

customer_app = Blueprint("customer", __name__)


@app.route("/customer-signin", methods=["GET", "POST"])
def customer_signin_page():
    form = SigninForm()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            form.password.data
        ):
            login_user(attempted_user)
            flash(
                f"Sucesso! Autenticado como: {attempted_user.username}",
                category="success",
            )
            token = generate_token(attempted_user.id)
            print({"message": "Login bem-sucedido!", "token": token})
            return redirect(url_for("home_page"))
        else:
            flash(
                "Usuário e senha incorretos! Por favor, tente novamente.",
                category="danger",
            )

    return render_template("customer_signin.html", form=form)


@app.route("/customer-signup", methods=["GET", "POST"])
def customer_signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        user_to_create = Customer(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f"Conta criada com sucesso! Você está autenticado como:  {user_to_create.username}",
            category="success",
        )
        token = generate_token(user_to_create.id)
        print({"message": "Login bem-sucedido!", "token": token})
        return redirect(url_for("home_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Ocorreu um erro ao criar um usuário: {err_msg}", category="danger")

    return render_template("customer_signup.html", form=form)
