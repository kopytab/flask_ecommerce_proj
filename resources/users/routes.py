from flask import Flask, request, jsonify, Blueprint
from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


from . import bp
from schemas import User_Schema

from models.user_model import User_Model


@bp.route('/user')
class UserList(MethodView):
    
    @bp.response(200, User_Schema(many=True))
    def get(self):
        return User_Model.query.all()

    
    @bp.arguments(User_Schema)
    @bp.response(201, User_Schema)
    def post(self, data):
        try:
            user = User_Model()
            user.from_dict(data)
            user.save_user()
            return user
        except:
            return abort(400, message = "Email already in use, please enter another one.")

@bp.route('/user/<int:id>')
class User(MethodView):
    
    @jwt_required() 
    @bp.response(200,User_Schema)
    def get(self, id):
        user = User_Model.query.get(id)
        if user:
            return user
        else:
            abort(400, message="not a valid user")


    @bp.arguments(User_Schema)
    @bp.response(200, User_Schema)
    def put(self, data, id):
        user = User_Model.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user()
            return user
        else:
            abort(400, message="not a valid user")          


    def delete(self, id):
        user = User_Model.query.get(id)
        if user:
            user.del_user()
            return { "message": "user has been deleted"}, 200
        abort(400, message="not a valid user")

@bp.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response
        

@bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
