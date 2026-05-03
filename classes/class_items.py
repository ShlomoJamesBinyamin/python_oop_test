from log_files.logger import log, line,arrow,notify,success,failure
class Items():
    def __init__(self, name, price):
        self.__id = None
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{arrow} Item Details:\n   ID: {self.__id}\n   Name: {self.__name}\n   Price: {self.__price}"

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, x):
        log.info(F"ITEM: {self.name} ID CHANGED TO: {x}")
        self.__id = x

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,x):
        log.info(F"ITEM: {self.name} NAME CHANGED TO: {x}")
        self.__name = x

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,x):
        log.info(F"ITEM: {self.name} PRICE CHANGED TO: {x}")
        self.__price = x
