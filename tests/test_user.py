from tests.helper import TestModel


class LoginPageTest(TestModel):
    """
    Test for `user.login_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "user.login_page"

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 200)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"dashboard" in response.data)

    def test_post_ok(self):
        response = self.post_request(self.login_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"dashboard" in response.data)

    def test_post_bad(self):
        response = self.post_request({"username": "test", "password": "bad"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"login" in response.data)


class LogoutPageTest(TestModel):
    """
    Test for `user.logout_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "user.logout_page"

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 401)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"/" in response.data)


class RegisterPageTest(TestModel):
    """
    Test for `user.register_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "user.register_page"
        self.register_data = {
            "username": "test2",
            "password": "test2test2",
            "repeat_password": "test2test2",
            "email": "test2@test2.com",
            "language": "en",
        }
        self.register_data_bad = {
            "username": "test3",
            "password": "test3",
            "repeat_password": "test3",
            "email": "test3@test3.com",
            "language": "en",
        }
        self.register_data_bad_2 = {
            "username": "test",
            "password": "testtest",
            "repeat_password": "testtest",
            "email": "test3@test3.com",
            "language": "en",
        }

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 200)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"dashboard" in response.data)

    def test_post_ok(self):
        response = self.post_request(self.register_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"login" in response.data)

    def test_post_bad_too_short_password(self):
        response = self.post_request(self.register_data_bad)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"register" in response.data)

    def test_post_bad_duplicate_user(self):
        response = self.post_request(self.register_data_bad_2)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"register" in response.data)


class UserSettingPageTest(TestModel):
    """
    Test for `user.user_setting_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "user.user_setting_page"
        self.setting_data = {"password": "", "email": "test@test.com", "lang": "en"}
        self.setting_data_bad = {
            "password": "short",
            "email": "test@test.com",
            "lang": "en",
        }

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 401)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 200)

    def test_post_ok(self):
        response = self.post_request(self.setting_data, True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"dashboard" in response.data)

    def test_post_bad_too_short_password(self):
        response = self.post_request(self.setting_data_bad, True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"user_setting" in response.data)
