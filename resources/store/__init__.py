from flask_smorest import Blueprint

bp = Blueprint("store", __name__, description="routes for store")

from . import routes