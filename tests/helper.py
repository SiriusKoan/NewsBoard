from hashlib import sha256
import unittest
from flask import url_for
import RandomUsers as ru
from app import create_app
from app.db import db, Users, Directories, Keywords


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.login_data = {"username": "test", "password": "test"}
        db.drop_all()
        generate_test_data()

    def tearDown(self) -> None:
        if self.app_context is not None:
            self.app_context.pop()
        db.drop_all()

    def login(self):
        return self.client.post(url_for("user.login_page"), data=self.login_data)

    def get_request(self, login=False):
        with self.client:
            if login:
                self.login()
            return self.client.get(url_for(self.route))

    def post_request(self, data, login=False):
        with self.client:
            if login:
                self.login()
            return self.client.post(url_for(self.route), data=data)


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


def generate_test_data():
    db.create_all()

    db.session.add(
        Users(
            username="test",
            password=sha256(bytes("test".encode("utf-8"))).hexdigest(),
            email="test@test.com",
            lang="en",
        )
    )
    db.session.commit()

    name = ru.Username()
    directory_model = DirectoryModel(name=name, user_id=1)
    directories = directory_model.bulk_generate(n=10)
    for directory in directories:
        db.session.add(directory)
        db.session.commit()

    keyword_model = KeywordModel(directory_id=1, value=name)
    keywords = keyword_model.bulk_generate(n=10)
    for keyword in keywords:
        db.session.add(keyword)
        db.session.commit()
