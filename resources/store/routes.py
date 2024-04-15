from flask import Flask, request, jsonify, Blueprint
from flask.views import MethodView
from flask_smorest import abort


from . import bp
from schemas import Store_Schema

from models.store_model import Store_Model

@bp.route('/store')
class StoreList(MethodView):

    @bp.arguments(Store_Schema)
    def post(self, store_data):

        try:

            store = Store_Model()
            store.from_dict(store_data)
            store.save_item()
            return{"Item successfully added to store." : f"{store.product_name} added to store"}
        
        except:
            abort(400, message = f"Failed to add {store.product_name} to store.")

    @bp.response(200, Store_Schema(many=True))
    def get(self):
        try:
            return Store_Model.query.all()
        
        except:
            abort(400, message = "Failed to get items from store.")

@bp.route('/store')
class Items(MethodView):

    @bp.response(200, Store_Schema)
    def get(self, id):
        item = Store_Model.query.get(id)

        if item:
            return item
        
        else:
            abort(400, message = "Item not in store.")

    @bp.arguments(Store_Schema)
    @bp.response(200, Store_Schema)
    def put(self, store_data, id):
    
        item = Store_Model.query.get(id)

        if item:
            item.from_dict(store_data)
            item.save_item()
            return item
        
        else:
            abort(400, message = "Item not in store.")


    def delete(self, id):
        item = Store_Model.query.get(id)

        if item:
            item.del_item()

            return {200, "Item has been deleted from store."}