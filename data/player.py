

class Player:
    def __init__(self):
        self.id = None
        self.long_name = None
        self.number = None
        self.short_name = None

    def __del__(self):
        del self.id
        del self.long_name
        del self.number
        del self.short_name

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
    def long_name(self):
        return self.__long_name

    @long_name.setter
    def long_name(self, ln):
        self.__long_name = ln

    @long_name.deleter
    def long_name(self):
        del self.__long_name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = int(number)

    @number.deleter
    def number(self):
        del self.__number

    @property
    def short_name(self):
        return self.__short_name

    @short_name.setter
    def short_name(self, sn):
        self.__short_name = sn

    @short_name.deleter
    def short_name(self):
        del self.__short_name