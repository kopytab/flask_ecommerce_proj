from app import db

class Cart_Model(db.Model):

    __tablename__ = 'cart'

    cart_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey('store.product_id'),nullable = False)

    

    def save_item(self):
        db.session.add(self)
        db.session.commit()

    def del_item(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, store_dict):
        for k, v in store_dict.items():
            setattr(self, k, v)