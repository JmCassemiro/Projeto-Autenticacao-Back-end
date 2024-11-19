from flask_login import UserMixin

from app import bcrypt, db


class Customer:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    def __repr__(self):
        return self.username


class CustomerModel(db.Model, UserMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)

    def __init__(self, username, email_address, password_hash=None):
        self.username = username
        self.email_address = email_address
        self.password_hash = password_hash or ""

    def __repr__(self):
        return f"<Customer {self.username}>"

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode(
            "utf-8"
        )

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email_address=email).first()
