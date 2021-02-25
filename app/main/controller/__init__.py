from flask import Flask, Blueprint
from flask_restful import Api

from app.main.controller.user_controller import User

user_bp = Blueprint('user', __name__)
user_api = Api(user_bp)

user_api.add_resource(User, '/user')