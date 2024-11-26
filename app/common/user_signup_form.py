from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class UserSignupForm(FlaskForm):
    username = StringField(
        label="User Name:", validators=[Length(min=2, max=30), DataRequired()]
    )
    email_address = StringField(
        label="Email Address:", validators=[Email(), DataRequired()]
    )
    password = PasswordField(
        label="Password:", validators=[Length(min=6), DataRequired()]
    )
    confirm_password = PasswordField(
        label="Confirm Password:", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")

    def validate_username(self, username_to_check):
        pass

    def validate_email_address(self, email_address_to_check):
        pass
