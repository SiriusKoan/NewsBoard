from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    lang = db.Column(db.Text, nullable=False, default="en")
    directories = db.relationship("Directories")
    # for verification
    verify_code = db.Column(db.Text, unique=True, nullable=True, default=None)
    status = db.Column(db.Text, nullable=True, default=None)

    def __init__(self, username, password, email, lang):
        self.username = username
        self.password = password
        self.email = email
        self.lang = lang


class Keywords(db.Model):
    __tablename__ = "keywords"
    ID = db.Column(db.Integer, primary_key=True)
    directory_id = db.Column(db.Integer, db.ForeignKey("directories.ID"), nullable=False)
    value = db.Column(db.Text, nullable=False)

    def __init__(self, directory_id, value):
        self.directory_id = directory_id
        self.value = value


class Directories(db.Model):
    __tablename__ = "directories"
    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.ID"), nullable=False)
    name = db.Column(db.Text, nullable=False)
    keywords = db.relationship("Keywords")

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
