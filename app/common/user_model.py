import random
import bcrypt
from flask_login import UserMixin

from app import db


class UserModel(db.Model, UserMixin):
    __abstract__ = True
    user_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email_address = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email_address, password):
        self.user_id = self.generate_random_id()
        self.username = username
        self.email_address = email_address
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.hashpw(
            plain_text_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password_correction(self, attempted_password):
        return bcrypt.checkpw(
            attempted_password.encode("utf-8"), self.password_hash.encode("utf-8")
        )

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.user_id)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email_address=email).first()

    def generate_random_id(self):
        return random.randint(1000000000, 9999999999)
