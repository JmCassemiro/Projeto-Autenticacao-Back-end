from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user

from app import db
from utils.jwt_helper import generate_token

from .login import LoginForm
from .model import CustomerModel
from .register import RegisterForm

customer_bp = Blueprint("customer", __name__, template_folder="templates")


@customer_bp.route("/login_customer", methods=["GET", "POST"])
def login_customer_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = CustomerModel.query.filter_by(username=form.username.data).first()

        if user and user.check_password_correction(form.password.data):
            token = generate_token(user.id)
            response_data = {"message": "Login bem-sucedido!", "token": token}
            print(response_data)
            login_user(user)

            flash(
                f"Login bem-sucedido! Bem-vindo, {user.username}.", category="success"
            )
            return redirect(url_for("home.home_page"))

        flash("Credenciais erradas! Por favor, tente novamente.", category="danger")

    return render_template("login_customer.html", form=form)


@customer_bp.route("/register_customer", methods=["GET", "POST"])
def register_customer_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = CustomerModel(
            username=form.username.data,
            email_address=form.email_address.data,
        )
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso!", category="success")
        return redirect(url_for("home.home_page"))

    for error in form.errors.values():
        flash(f"Erro ao criar um usuário: {error}", category="danger")

    return render_template("register_customer.html", form=form)
