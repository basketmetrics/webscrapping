import unittest
from bs4 import BeautifulSoup, Tag
from ws.bs import Soup
import os
from data.boxscore.team import Team
from data.boxscore.game import Game
from data.boxscore.quarters import Quarters


class WSTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://www.espn.com/wnba/boxscore/_/gameId/401736233"
        soup = Soup(url)
        cls.soup = soup.soup
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
        with open(f"{project_root}/files/content.html", "w", encoding="utf-8") as f:
            f.write(cls.soup.prettify())
        cls.id_game = url.split("gameId/")[1]

    @classmethod
    def tearDownClass(cls):
        del cls.soup
        del cls.id_game

    def test_get_soup(self):
        soup = self.soup
        self.assertIsInstance(soup, BeautifulSoup)

    def test_get_header(self):
        soup = self.soup
        # Scores
        left_score = soup.find(class_="Gamestrip__Team relative flex w-100 items-center Gamestrip__Team--left Gamestrip__Team--loser")
        away_result = left_score.find(class_="Gamestrip__Score relative tc w-100 fw-heavy-900 h2 clr-gray-01").text if left_score is not None else None
        if not isinstance(left_score, Tag):
            left_score = soup.find(class_="Gamestrip__Team relative flex w-100 items-center Gamestrip__Team--left Gamestrip__Team--winner")
            away_result = left_score.find(class_="Gamestrip__Score relative tc w-100 fw-heavy-900 h2 clr-gray-01")
            # Obtiene solamente el resultado, obviando cualquier tag o imagen que pueda haber dentro
            away_result = ''.join(away_result.find_all(string=True, recursive=False)).strip()
        right_score = soup.find(class_="Gamestrip__Team relative flex w-100 items-center Gamestrip__Team--right Gamestrip__Team--loser")
        home_result = right_score.find(class_="Gamestrip__Score relative tc w-100 fw-heavy-900 h2 clr-gray-01").text if right_score is not None else None
        if not isinstance(right_score, Tag):
            right_score = soup.find(class_="Gamestrip__Team relative flex w-100 items-center Gamestrip__Team--right Gamestrip__Team--winner")
            home_result = right_score.find(class_="Gamestrip__Score relative tc w-100 fw-heavy-900 h2 clr-gray-01")
            # Obtiene solamente el resultado, obviando cualquier tag o imagen que pueda haber dentro
            home_result = ''.join(home_result.find_all(string=True, recursive=False)).strip()
        center = soup.find(class_="Table Table--align-right").tbody.find_all("tr")
        away_quarters = center[0].find_all("td")
        home_quarters = center[1].find_all("td")
        game = Game(self.id_game)
        game.home_result = home_result
        game.away_result = away_result
        # Quarters
        quarters = Quarters()
        quarters.home_quarters = [q.text for q in home_quarters[1:-1]]
        quarters.away_quarters = [q.text for q in away_quarters[1:-1]]
        game.quarters = quarters
        # Team names
        team_names = soup.find_all(class_="ScoreCell__Truncate Gamestrip__Truncate h4 clr-gray-01")
        home_team = team_names[1]
        away_team = team_names[0]
        game.home_team.name = home_team.a.h2.text
        game.away_team.name = away_team.a.h2.text
        self.assertEqual(game.id_game == self.id_game, True, f"El id game de Game: {game.id_game} no es el de la variable id_game: {self.id_game}")
        self.assertEqual(game.home_result == home_result, True, f"El resultado del equipo de casa: {game.home_result} no es el de la variable home_result: {home_result}")
        self.assertEqual(game.away_result == away_result, True, f"El resultado del equipo visitante: {game.away_result} nos es el de la variable away_result: {away_result}")
        self.assertEqual(game.quarters.home_quarters == [q.text for q in home_quarters[1:-1]], True, f"Los arrays del objeto game.quarters.home_quarters: {game.quarters.home_quarters} y los de la variable home_quarters: {[q.text for q in home_quarters[1:-1]]} son distintos")
        self.assertEqual(game.quarters.away_quarters == [q.text for q in away_quarters[1:-1]], True, f"Los arrays del objeto game.quarters.away_quarters: {game.quarters.away_quarters} y los de la variable home_quarters: {[q.text for q in away_quarters[1:-1]]} son distintos")
        self.assertEqual(game.home_team.name == home_team.a.h2.text, True, f"El nombre del equipo del objeto Team {game.home_team.name} es distinto al del contenido {home_team.a.h2.text}")
        self.assertEqual(game.away_team.name == away_team.a.h2.text, True, f"El nombre del equipo del objeto Team {game.away_team.name} es distinto al del contenido {away_team.a.h2.text}")

    def test_get_boxscore(self):
        soup = self.soup
        div_bx = soup.find(class_="Boxscore Boxscore__ResponsiveWrapper")
        left_div = div_bx.find_all(class_="Wrapper")[0]
        right_div = div_bx.find_all(class_="Wrapper")[1]
        self.assertIsInstance(left_div, Tag)
        self.assertIsInstance(right_div, Tag)

    def test_set_team_data(self):
        soup = self.soup
        div_bx = soup.find(class_="Boxscore Boxscore__ResponsiveWrapper")
        left_div = div_bx.find_all(class_="Wrapper")[0]
        right_div = div_bx.find_all(class_="Wrapper")[1]
        homeTeam = Team()
        awayTeam = Team()
        home_team_name = left_div.find(class_="BoxscoreItem__TeamName h5").text
        away_team_name = right_div.find(class_="BoxscoreItem__TeamName h5").text
        self.assertEqual(home_team_name == "Las Vegas Aces", True, f"El valor devuelto por la variable home_team_name: {home_team_name} no es 'Las Vegas Aces'")
        self.assertEqual(away_team_name == "New York Liberty", True, f"El valor devuelto por la variable away_team_name: {away_team_name} no es 'New York Liberty'")
        homeTeam.name = home_team_name
        awayTeam.name = away_team_name

if __name__ == '__main__':
    unittest.main()
