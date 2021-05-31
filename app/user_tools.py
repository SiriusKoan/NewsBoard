from hashlib import sha256
from flask_login import UserMixin
from . import login_manager
from .db import db, Users


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


def login_auth(username, password):
    hash_password = sha256(bytes(password.encode("utf-8"))).hexdigest()
    if user := Users.query.filter_by(username=username).first():
        if user.password == hash_password:
            sessionUser = User()
            sessionUser.id = user.ID
            return sessionUser
    return False


def register(username, password, email, lang):
    if Users.query.filter_by(username=username).first() is None:
        new_user = Users(
            username=username,
            password=sha256(bytes(password.encode("utf-8"))).hexdigest(),
            email=email,
            lang=lang,
        )
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False
