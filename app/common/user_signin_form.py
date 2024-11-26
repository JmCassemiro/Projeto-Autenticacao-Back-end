from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired


class UserSigninForm(FlaskForm):
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Entrar")
