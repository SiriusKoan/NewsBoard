from tests.helper import TestModel


class IndexPageTest(TestModel):
    """
    Test for `main.index_page`
    """

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.route = "main.index_page"

    def test_get_with_no_auth(self):
        response = self.get_request()
        self.assertEqual(response.status_code, 200)

    def test_get_with_auth(self):
        response = self.get_request(True)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(b"dashboard" in response.data)
