from flask import Flask, request
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

app.config['JWT_SECRET_KEY'] = "please-remember-to-change-me"
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.store_model import Store_Model
from models.cart_model import Cart_Model
from models.user_model import User_Model

from resources.store import bp as store_bp
app.register_blueprint(store_bp)

from resources.cart import bp as cart_bp
app.register_blueprint(cart_bp)

from resources.users import bp as user_bp
app.register_blueprint(user_bp)