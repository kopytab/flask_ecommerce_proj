from flask_smorest import Blueprint

bp = Blueprint("cart", __name__, description="routes for cart")

from . import routes