from hashlib import sha256
from re import fullmatch
from ..db import db, Users

def login_auth(username, password):
    hash_password = sha256(bytes(password.encode("utf-8"))).hexdigest()
    user = Users.query.filter_by(username=username).first()
    if user:
        return hash_password == user.password
    return False

def register(username, password, email, lang):
    if (
        fullmatch("[a-zA-Z0-9_-]+", username)
        and Users.query.filter_by(username=username).first() is None
    ):
        new_user = Users(
            username=username,
            password=sha256(bytes(password.encode("utf-8"))).hexdigest(),
            email=email,
            lang=lang,
            verify_code=None,
            status=None,
        )
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False