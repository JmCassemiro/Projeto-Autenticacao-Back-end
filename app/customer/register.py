aifrom flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from .model import Customer


class RegisterForm(FlaskForm):
    def validate_username(self, username):
        user = Customer.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Usuário já cadastrado! Utilize outro.')

    def validate_email_address(self, email_address):
        email = Customer.query.filter_by(email_address=email_address.data).first()
        if email:
            raise ValidationError('Email já cadastrado. Utilize outro.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Criar Conta')
