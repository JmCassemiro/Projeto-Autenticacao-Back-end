from app import db
from app.common.user_model import UserModel


class Employee(UserModel):
    __tablename__ = "employees"

    matricula = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, username, email_address, password, matricula):
        super().__init__(username, email_address, password)
        self.matricula = matricula
