import datetime as dt
from abc import ABC, abstractmethod
from log_files.logger import log

class IOrders(ABC):
    def __init__(self, name, customer, delivery_address, payment_method):
        self.id = None
        self.name = name
        self.delivery_address = delivery_address
        self.items = []
        self.customer = customer
        self.total_price = 0
        self.payment_method = payment_method
        self.date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')
        self.items_to_favorite()


    def __str__(self):
        return f"────> Order: {self.id} | {self.name} | {self.date}\n     price: {self.total_price} ({self.payment_method})\n     by:{self.customer.id}|{self.customer.first_name} {self.customer.last_name}\n     to{self.delivery_address}\n     contains:{self.items}"

    @abstractmethod
    def calc_total_price(self):
        pass

    def add_item(self, item):
        self.items.append(item)

    def items_to_favorite(self):
        existing_items = [item.name for item in self.customer.favorite_items]
        for item in self.items:
            if item.name not in existing_items:
                self.customer.favorite_items.append(item)
        log.info(f"{len(self.customer.favorite_items) - len(existing_items)} Items Added To {self.customer.name} Fav List ")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, x):
        self.__id = x
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        self.__name = x
        pass

    @property
    def delivery_address(self):
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, x):
        self.__delivery_address = x
        pass

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, x: list):
        self.__items = x
        pass

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, x: str):
        self.__payment_method = (x if x == 'cash' else x if x == 'bitcoin' else x if x == 'check' else "None")
        pass

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, ):
        self.__date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')
        pass

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, x):
        self.__customer = x
        pass

    @property
    def total_price(self):
        return self.calc_total_price()

    @total_price.setter
    def total_price(self, x):
        self.__total_price = x
        pass