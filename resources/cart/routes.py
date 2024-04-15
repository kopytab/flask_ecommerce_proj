from flask import Flask, request, jsonify, Blueprint
from flask.views import MethodView
from flask_smorest import abort


from . import bp
from schemas import Cart_Schema

from models.cart_model import Cart_Model

@bp.route('/cart')
class CartList(MethodView):

    @bp.arguments(Cart_Schema)
    def post(self, cart_data):

        try:

            cart = Cart_Model()
            cart.from_dict(cart_data)
            cart.save_item()
            return{"Item successfully added to cart." : f"{cart.product_id} added to store"}
        
        except:
            abort(400, message = f"Failed to add {cart.product_id} to cart.")

    @bp.response(200, Cart_Schema(many=True))
    def get(self):
        try:
            return Cart_Model.query.all()
        
        except:
            abort(400, message = "Failed to get items from cart.")

@bp.route('/cart')
class Items(MethodView):

    @bp.response(200, Cart_Schema)
    def get(self, id):
        item = Cart_Model.query.get(id)

        if item:
            return item
        
        else:
            abort(400, message = "Item not in cart.")

    @bp.arguments(Cart_Schema)
    @bp.response(200, Cart_Schema)
    def put(self, store_data, id):
    
        item = Cart_Model.query.get(id)

        if item:
            item.from_dict(store_data)
            item.save_item()
            return item
        
        else:
            abort(400, message = "Item not in cart.")


    def delete(self, id):
        item = Cart_Model.query.get(id)

        if item:
            item.del_item()

            return {200, "Item has been deleted from cart."}