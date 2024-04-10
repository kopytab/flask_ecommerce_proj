from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class User_Model(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.column(db.String(50))
    last_name = db.column(db.String(50))
    password_hash = db.Column(db.String, nullable = False)
    

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()

def from_dict(self, user_dict):
        for k , v in user_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))