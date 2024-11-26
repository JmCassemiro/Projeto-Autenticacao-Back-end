from app.common.user_signin_form import UserSigninForm
from wtforms import StringField
from wtforms.validators import DataRequired


class EmployeeSigninForm(UserSigninForm):
    employee_id = StringField("ID:", validators=[DataRequired()])
