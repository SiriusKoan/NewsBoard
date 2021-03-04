import unittest
from news_tools import Google

class NewsToolsTest(unittest.TestCase):
    def setUp(self):
        self.search_engine = Google()
    def tearDown(self):
        pass
    def test_Google(self):
        news = self.search_engine.get_news('nba', 'zh_TW')
        self.assertTrue(len(news) == 4)
        self.assertTrue(len(news[0]) == 4)
        self.assertTrue(all(all(j) for j in (list(news[i].values()) for i in range(4))))