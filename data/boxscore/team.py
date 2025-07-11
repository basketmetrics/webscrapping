
class Team:
    def __init__(self):
        self.id = None
        self.name = None

    def __del__(self):
        del self.id
        del self.name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = int(id) if id is not None else None

    @id.deleter
    def id(self):
        del self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name