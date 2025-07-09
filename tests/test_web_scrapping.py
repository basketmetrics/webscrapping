import unittest

from bs4 import BeautifulSoup

from ws.bs import Soup
import os

class WSTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        soup = Soup("https://www.espn.com/wnba/boxscore/_/gameId/401736233")
        cls.soup = soup.soup
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
        print(project_root)
        with open(f"{project_root}/files/content.html", "w", encoding="utf-8") as f:
            f.write(cls.soup.prettify())

    @classmethod
    def tearDownClass(cls):
        del cls.soup

    def test_get_soup(self):
        soup = self.soup
        self.assertIsInstance(soup, BeautifulSoup)

if __name__ == '__main__':
    unittest.main()
