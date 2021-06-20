import unittest
import hashlib
from os import getenv
import RandomUsers as ru
from flask_script import Manager
from app import create_app
from app.db import Users, Keywords, Directories, db

app = create_app(getenv("env"))
manager = Manager(app)


class DirectoryModel(ru.UserModel):
    def __init__(self, user_id, name, instance=Directories) -> None:
        self.info = dict()
        self.user_id = user_id
        self.name = name
        self.instance = instance

    def generate(self):
        self.info["name"] = self.name.generate()
        self.info["user_id"] = self.user_id
        return self.instance(**self.info)


class KeywordModel(ru.UserModel):
    def __init__(self, directory_id, value, instance=Keywords) -> None:
        self.info = dict()
        self.directory_id = directory_id
        self.value = value
        self.instance = instance

    def generate(self):
        self.info["directory_id"] = self.directory_id
        self.info["value"] = self.value.generate()
        return self.instance(**self.info)


@manager.command
def run_test():
    print("Start testing.")
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@manager.command
def test_data():
    print("Generating user test data...")
    username = ru.Username()
    password = ru.Password(hash=lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest())
    email = ru.Email()
    user_model = ru.UserModel(
        username=username,
        password=password,
        email=email,
        information={"lang": "en"},
        instance=Users,
    )
    users = user_model.bulk_generate()
    for user in users:
        db.session.add(user)
        db.session.commit()
    print("Complete.")

    print("Generating directories test data...")
    name = ru.Username()
    directory_model = DirectoryModel(name=name, user_id=1)
    directories = directory_model.bulk_generate()
    for directory in directories:
        db.session.add(directory)
        db.session.commit()
    print("Complete.")

    print("Generating keywords test data...")
    keyword_model = KeywordModel(directory_id=1, value=name)
    keywords = keyword_model.bulk_generate()
    for keyword in keywords:
        db.session.add(keyword)
        db.session.commit()
    print("Complete.")


if __name__ == "__main__":
    manager.run()
