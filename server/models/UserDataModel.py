from ._db import db, BaseModel


class UserDataModel(BaseModel):
    __tablename__ = "user_data"

    user_id =   db.Column(db.Integer, db.ForeignKey("user.id"))
    nickname =  db.Column(db.String(25), unique=True, nullable=False)
    ful_name =  db.Column(db.String(100), nullable=False)
    age =       db.Column(db.Integer)
    last_seen = db.Column(db.String)

    def get_public_field_list(cls):
        return ["nickname", "ful_name", "age", "last_seen"]
