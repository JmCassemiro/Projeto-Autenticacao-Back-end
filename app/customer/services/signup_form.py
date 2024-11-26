from app.common.user_signup_form import UserSignupForm
from app.customer.model import Customer
from wtforms.validators import ValidationError


class CustomerSignupForm(UserSignupForm):
    def validate_username(self, username_to_check):
        user = Customer.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Usuário já cadastrado.")

    def validate_email_address(self, email_address_to_check):
        email_address = Customer.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email já cadastrado.")
