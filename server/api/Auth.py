from http import HTTPStatus

from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models import UserModel, UserDataModel, UserNotFound


class Auth(Resource):
    path = "/auth"

    def post(self):
        args = request.json

        try:
            user = UserModel.auth(args["email"], args["password"])
        except UserNotFound:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        return {"access_token": create_access_token(identity=user.id)}, HTTPStatus.OK