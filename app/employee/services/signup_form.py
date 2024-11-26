from wtforms import StringField
from app.common.user_signup_form import UserSignupForm
from app.employee.model import Employee
from wtforms.validators import ValidationError
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length, ValidationError


class EmployeeSignupForm(UserSignupForm):
    employee_id = StringField(
        label="ID do Funcionário:", validators=[Length(min=2, max=30), DataRequired()]
    )

    def validate_username(self, username_to_check):
        user = Employee.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Usuário já existe.")

    def validate_email_address(self, email_address_to_check):
        email_address = Employee.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError("Email já existe.")

    def validate_employee_id(self, employee_id_to_check):
        employee_id = Employee.query.filter_by(
            employee_id=employee_id_to_check.data
        ).first()
        if employee_id:
            raise ValidationError("ID já cadastrado")
