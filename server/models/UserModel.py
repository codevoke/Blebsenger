from ._db import db, BaseModel
from ._exceptions import *
from passlib.hash import pbkdf2_sha256


class UserModel(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def get_public_field_list(cls):
        return ["id", "email"]

    def authenticate(self, email, password):
        user = self.query.filter_by(email=email).first()

        if not user:
            raise UserNotFound()

        if not pbkdf2_sha256.verify(password, user.password):
            raise InvalidPassword()

        return user
