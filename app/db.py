from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    lang = db.Column(db.Text, nullable=False, default="en")
    # for verification
    verify_code = db.Column(db.Text, unique=True, nullable=True)
    status = db.Column(db.Text, nullable=True, default=None)
    directories = db.relationship("Directories")

    def __init__(self, username, password, email, lang, verify_code, status):
        self.username = username
        self.password = password
        self.email = email
        self.lang = lang
        self.verify_code = verify_code
        self.status = status


class Keywords(db.Model):
    __tablename__ = "keywords"
    ID = db.Column(db.Integer, primary_key=True)
    directory_id = db.Column(db.Integer, db.ForeignKey("directories.ID"), nullable=False)
    keyword = db.Column(db.Text, nullable=False)

    def __init__(self, directory_id, keyword):
        self.directory_id = directory_id
        self.keyword = keyword


class Directories(db.Model):
    __tablename__ = "directories"
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.ID"), nullable=False)
    name = db.Column(db.Text, nullable=False)
    keywords = db.relationship("Keywords")

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
