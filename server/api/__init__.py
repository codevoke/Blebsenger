from flask_restful import Api

from .User import User


api = Api(prefix="/api")

for resource in [User]:
    api.add_resource(resource, resource.path)