from . import db 
from werkzeug.security
from . import db 
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
# from . import login_manager
# from datetime import datetime 



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)