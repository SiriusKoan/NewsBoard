import unittest
from flask.helpers import url_for
from flask_login import login_user
from app import create_app
from app.db import db
from app.user_tools import login_auth
from helper import generate_test_data


class IndexPageTest(unittest.TestCase):
    """
    Test for `main.index_page`.
    """

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
        #db.drop_all()

    def login(self):
        return self.client.post(url_for("user.login_page"), data=self.login_data)

    def get_request(self, login=False):
        with self.client:
            if login:
                self.login()
            return self.client.get(url_for("main.index_page"))

    def test_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 200)

    def test_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 302)
