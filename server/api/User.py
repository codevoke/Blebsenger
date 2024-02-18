from http import HTTPStatus

from flask import request
from flask_restful import Resource

from models import UserModel, UserDataModel, UserNotFound


class User(Resource):
    path = "/user/<int:user_id>"

    def get(self, user_id):
        user = UserModel.get_by_id(user_id)

        if not user:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        user_data_json = UserModel.get_by_id(user_id).json()

        return {"user": user.json().update(user_data_json)}, HTTPStatus.OK
