from ._db import db, BaseModel
from ._exceptions import *


class DialogModel(BaseModel):
    __tablename__ = "dialog"

    id = db.Column(db.Integer, primary_key=True)
    user_id_1 = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_id_2 = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, user_id_1, user_id_2):
        self.user_id_1 = min(user_id_1, user_id_2)
        self.user_id_2 = max(user_id_1, user_id_2)

    def get_public_field_list(cls):
        return ["id", "user_id", "dialog"]

    @classmethod
    def get_dialogs_by_user_id(cls, user_id):
        dialogs =  cls.query.filter_by(
            (cls.user_id_2 == user_id) | (cls.user_id_1 == user_id)
        ).all()

        if not dialogs:
            raise DialogsNotFound

        return dialogs