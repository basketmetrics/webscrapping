from data.boxscore.team import Team
from data.boxscore.quarters import Quarters

class Game:
    def __init__(self, id_game):
        self.away_team = Team()     # Objeto Team Visitante
        self.home_team = Team()     # Objeto Team local
        self.quarters = Quarters()  # Objeto Quarters
        self.id_game = id_game
        self.away_result = None
        self.home_result = None

    def __del__(self):
        del self.away_result
        del self.away_team
        del self.home_result
        del self.home_team

    @property
    def id_game(self):
        return self.__id_game

    @id_game.setter
    def id_game(self, id):
        self.__id_game = id

    @id_game.deleter
    def id_game(self):
        del self.__id_game

    @property
    def away_result(self):
        return self.__away_result

    @away_result.setter
    def away_result(self, ar):
        self.__away_result = ar

    @away_result.deleter
    def away_result(self):
        del self.__away_result

    @property
    def away_team(self):
        return self.__away_team

    @away_team.setter
    def away_team(self, at):
        self.__away_team = at

    @away_team.deleter
    def away_team(self):
        del self.__away_team

    @property
    def home_result(self):
        return self.__home_result

    @home_result.setter
    def home_result(self, hr):
        self.__home_result = hr

    @home_result.deleter
    def home_result(self):
        del self.__home_result

    @property
    def home_team(self):
        return self.__home_team

    @home_team.setter
    def home_team(self, lt):
        self.__home_team = lt

    @home_team.deleter
    def home_team(self):
        del self.__home_team

    @property
    def quarters(self):
        return self.__quarters

    @quarters.setter
    def quarters(self, q):
        self.__quarters = q

    @quarters.deleter
    def quarters(self):
        del self.__quarters