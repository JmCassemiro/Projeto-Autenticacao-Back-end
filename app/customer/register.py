from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from .model import CustomerModel


class RegisterForm(FlaskForm):
    def validate_username(self, username):
        if CustomerModel.query.filter_by(username=username.data).first():
            raise ValidationError("Usuário já cadastrado! Utilize outro.")

    def validate_email_address(self, email_address):
        if CustomerModel.query.filter_by(email_address=email_address.data).first():
            raise ValidationError("Email já cadastrado. Utilize outro.")

    username = StringField(
        "Nome do Usuário:", validators=[Length(min=2, max=30), DataRequired()]
    )
    email_address = StringField("Email:", validators=[Email(), DataRequired()])
    password = PasswordField("Senha:", validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(
        "Confirmar Senha:", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField("Criar Conta")
