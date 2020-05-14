from app import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(120), unique =True, nullable =False)
    username = db.Column(db.String(20), unique =True, nullable =False)
    email = db.Column(db.String(120), unique =True, nullable =False)
    image = db.Column(db.String(120), nullable =False, default='profile.jpeg')
    password = db.Column(db.String(60), nullable =False)

    def __repr__(self):
        return  f"User('{self.name}','{self.username}','{self.email}','{self.image}')"