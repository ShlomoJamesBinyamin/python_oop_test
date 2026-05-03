import datetime as dt
from abc import ABC, abstractmethod
from log_files.logger import log, arrow

class IOrders(ABC):
    def __init__(self, name, customer,items, delivery_address, payment_method):
        self.id = None
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_method = payment_method
        self.date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')
        self.items_to_favorite()


    def __str__(self):
        return f"{arrow} Order: {self.id} | {self.name} | {self.date}\n     Price: {self.total_price} ({self.payment_method})\n     By:{self.customer.id}|{self.customer.fullname}\n     To: {self.delivery_address}\n     Contains:{self.items}"

    @abstractmethod
    def calc_total_price(self):
        pass

    def add_item(self, item):
        """add item to order and user.favourites under conditions"""
        self.items.append(item)
        self.items_to_favorite()

    def items_to_favorite(self):
        """conditions for adding an item to user.favourites"""
        existing_items = {item.name for item in self.customer.favorite_items}
        added = 0
        for item in self.items:
            if item.name not in existing_items:
                self.customer.favorite_items.append(item)
                existing_items.add(item.name)
                added += 1
        log.info(f"{added} ITEMS ADDED TO {self.customer.fullname} FAV LIST. ")

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, x):
        log.info(f"{self.name} ID CHANGED TO: {x}")
        self.__id = x


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, x):
        log.info(f"ORDER NAME CHANGED TO: {x}")
        self.__name = x


    @property
    def delivery_address(self):
        return self.__delivery_address
    @delivery_address.setter
    def delivery_address(self, x):
        self.__delivery_address = x
        log.info(f"ORDER DELIVERY ADDRESS SET TO: {x}")


    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, x: list):
        self.__items = x
        log.info(f"ORDER ITEMS SET")


    @property
    def payment_method(self):
        return self.__payment_method
    @payment_method.setter
    def payment_method(self, x: str):
        self.__payment_method = (x if x == 'cash' else x if x == 'card' else x if x == 'check' else "None")
        log.info(f"ORDER PAYMENT SET TO: {x}")


    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,x ):
        self.__date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')
        log.info(f"ORDER DATE CHANGED TO: {x}")


    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, x):
        self.__customer = x
        log.info(f"ORDER CUSTOMER SET TO: {x}")


    @property
    def total_price(self):
        log.info(f"ORDER TOTAL PRICE CALCULATES")
        return self.calc_total_price()