class Items():
    def __init__(self, name, price):
        self.__id = None
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"────> item details:\n   id: {self.__id}\n   name: {self.__name}\n   price: {self.__price}"

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, x):
        self.__id = x

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,x):
        self.__name = x

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,x):
        self.__price = x
