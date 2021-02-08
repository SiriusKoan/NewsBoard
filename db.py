from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    verify_code = db.Column(db.Text, unique=True, nullable=True)
    # TODO add

    def __init__(self, username, password, email, verify_code):
        self.username = username
        self.password = password
        self.email = email
        self.verify_code = verify_code
