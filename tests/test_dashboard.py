from flask import url_for
from tests.helper import TestModel


class DashboardPageTest(TestModel):
    """
    Test for `dashboard.dashboard_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "dashboard.dashboard_page"

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 401)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 200)


class DashboardBackendTest(TestModel):
    """
    Test for `dashboard.dashboard_backend`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "dashboard.dashboard_backend"
        self.post_keyword_data_ok = {
            "type": "keyword",
            "directory_id": "1",
            "keyword": "test_keyword1",
        }
        self.post_keyword_data_bad = {
            "type": "keyword",
            "directory_id": "100",
            "keyword": "test_keyword1",
        }
        self.post_directory_data_ok = {"type": "directory", "value": "test_directory1"}
        self.post_directory_data_bad = {"type": "directory", "value": "test_directory"}

        self.delete_keyword_data_ok = {
            "type": "keyword",
            "directory_id": "1",
            "keyword": "test_keyword",
        }
        self.delete_keyword_data_bad = {
            "type": "keyword",
            "directory_id": "2",
            "keyword": "test_keyword2",
        }
        self.delete_directory_data_ok = {"type": "directory", "id": "1"}
        self.delete_directory_data_bad = {"type": "directory", "id": "100"}

    def post_request(self, data):
        with self.client:
            self.login()
            return self.client.post(url_for(self.route), json=data)

    def delete_request(self, data):
        with self.client:
            self.login()
            return self.client.delete(url_for(self.route), json=data)

    def test_post_ok_keyword(self):
        response = self.post_request(self.post_keyword_data_ok)
        self.assertEqual(response.status_code, 200)

    def test_post_ok_directory(self):
        response = self.post_request(self.post_directory_data_ok)
        self.assertEqual(response.status_code, 200)

    def test_post_bad_keyword(self):
        response = self.post_request(self.post_keyword_data_bad)
        self.assertEqual(response.status_code, 400)

    def test_post_bad_directory(self):
        response = self.post_request(self.post_directory_data_bad)
        self.assertEqual(response.status_code, 400)

    def test_delete_ok_keyword(self):
        response = self.delete_request(self.delete_keyword_data_ok)
        self.assertEqual(response.status_code, 200)

    def test_delete_ok_directory(self):
        response = self.delete_request(self.delete_directory_data_ok)
        self.assertEqual(response.status_code, 200)

    def test_delete_bad_keyword(self):
        response = self.delete_request(self.delete_keyword_data_bad)
        self.assertEqual(response.status_code, 400)

    def test_delete_bad_directory(self):
        response = self.delete_request(self.delete_directory_data_bad)
        self.assertEqual(response.status_code, 400)


class GetDirectoryPageTest(TestModel):
    """
    Test for `dashboard.get_directory_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "dashboard.get_directory_page"

    def get_request(self, directory_name="", login=False):
        with self.client:
            if login:
                self.login()
            return self.client.get(url_for(self.route, directory_name=directory_name))

    def test_get_with_no_auth(self):
        response = self.get_request("test")
        self.assertEqual(response.status_code, 401)

    def test_get_with_auth_404(self):
        response = self.get_request("test", True)
        self.assertEqual(response.status_code, 404)

    def test_get_with_auth(self):
        response = self.get_request("test_directory", True)
        self.assertEqual(response.status_code, 200)
