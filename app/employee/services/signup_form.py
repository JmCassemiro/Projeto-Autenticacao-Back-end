from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)
from app.employee.model import Employee


class SignupForm(FlaskForm):
    username = StringField(
        label="Nome do Funcionário:", validators=[Length(min=2, max=30), DataRequired()]
    )
    email_address = StringField(
        label="Endereço de Email:", validators=[Email(), DataRequired()]
    )
    employee_id = StringField(
        label="ID do Funcionário:", validators=[Length(min=2, max=30), DataRequired()]
    )
    password = PasswordField(
        label="Senha:", validators=[Length(min=6), DataRequired()]
    )
    confirm_password = PasswordField(
        label="Confirmar Senha:", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")

    def validate_username(self, username_to_check):
        user = Employee.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Usuário já existe.")

    def validate_email_address(self, email_address_to_check):
        email_address = Employee.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email já existe")

    def validate_employee_id(self, employee_id_to_check):
        employee_id = Employee.query.filter_by(
            employee_id=employee_id_to_check.data
        ).first()
        if employee_id:
            raise ValidationError("ID já cadastrado")
