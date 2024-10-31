from flask import render_template, redirect, url_for, flash, Blueprint
from .model import Customer
from .login import LoginForm
from .register import RegisterForm
from app import db
from flask_login import login_user

customer_bp = Blueprint("customer", __name__, template_folder="templates")


@customer_bp.route("/login_customer", methods=["GET", "POST"])
def login_customer_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Sucesso! Você está logado como: {attempted_user.username}', category='success')
            return redirect(url_for('home.home_page'))
        else:
            flash('Credenciais erradas! Por favor, tente novamente.', category='danger')

    return render_template('login_customer.html', form=form)


@customer_bp.route("/register_customer", methods=["GET", "POST"])
def register_customer_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Customer(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        flash("Usuário criado com sucesso!", category="success")
        return redirect(url_for("home.home_page"))
    if form.errors:
        for err_msg in form.errors.values():
            flash(f"Erro ao criar um usuário: {err_msg}", category="danger")

    return render_template("register_customer.html", form=form)
