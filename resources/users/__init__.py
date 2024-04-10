from flask_smorest import Blueprint

bp = Blueprint("users", __name__, description="routes for users")

from . import routes