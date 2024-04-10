from app import db


class Store_Model(db.Model):

    __tablename__ = 'store'

    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.column(db.String(50))
    product_description = db.column(db.String(100))
    price = db.column(db.Integer)

    def save_item(self):
        db.session.add(self)
        db.session.commit()

    def del_item(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, store_dict):
        for k, v in store_dict.items():
            setattr(self, k, v)