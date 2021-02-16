from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    lang = db.Column(db.Text, nullable=False, default="en")
    verify_code = db.Column(db.Text, unique=True, nullable=True)
    status = db.Column(db.Text, nullable=True, default=None)
    # TODO add

    def __init__(self, username, password, email, verify_code, lang):
        self.username = username
        self.password = password
        self.email = email
        self.verify_code = verify_code
        self.lang = lang


class News(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    keyword = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)

    def __init__(self, username, keyword, category):
        self.username = username
        self.keyword = keyword
        self.category = category


class Category(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, username, name):
        self.username = username
        self.name = name
