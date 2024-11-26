from flask import flash, jsonify, make_response
from flask_login import login_user
from app.employee.model import Employee
from app.jwt_helper import TokenManager
from app import db


def validade_form_on_signin(form):
    if form.validate_on_submit():
        attempted_employee_id = Employee.query.filter_by(
            employee_id=form.employee_id.data
        ).first()
        if attempted_employee_id and attempted_employee_id.check_password_correction(
            form.password.data
        ):
            login_user(attempted_employee_id)
            flash(
                f"Sucesso! Autenticado como: {attempted_employee_id.username}",
                category="success",
            )
            token = TokenManager.generate_token(attempted_employee_id.user_id)
            return True

        flash(
            "Credenciais inválidas! Por favor, tente novamente.",
            category="danger",
        )

        return False


def validate_form_on_signup(form):
    if form.validate_on_submit():
        user_to_create = Employee(
            username=form.username.data,
            email_address=form.email_address.data,
            employee_id=form.employee_id.data,
            password=form.password.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f"Conta criada com sucesso! Você está autenticado como:  {user_to_create.username}",
            category="success",
        )
        token = TokenManager.generate_token(user_to_create.user_id)
        return True

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f"Ocorreu um erro ao criar um funcionário: {err_msg}", category="danger"
            )

            return False
