from marshmallow import Schema, fields

class Store_Schema(Schema):

    product_id = fields.Int(dump_only = True)
    product_name = fields.Str(required = True)
    product_description = fields.Str(required = True)
    price = fields.Int(required = True)


class User_Schema(Schema):

    user_id = fields.Int(dump_only = True)
    first_name = fields.Str(required = True)
    last_name = fields.Str(required = True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)

class Cart_Schema(Schema):

    cart_id = fields.Int(dump_only = True)
    user_id = fields.Int(required = True)
    product_id = fields.Int(required = True)