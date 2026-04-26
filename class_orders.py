import datetime as dt

class Orders:
    def __init__(self, name, customer_id, delivery_address, payment_method):
        self.id = None
        self.name = name
        self.delivery_address = delivery_address
        self.items = []
        self.customer_id = customer_id
        self.total_price = None
        self.payment_method = payment_method
        self.date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')

    def __str__(self):
        return f"────> Order: {self.id} | {self.name} | {self.date}\n     price: {self.ttl_price} ({self.payment_method})\n     by:{self.customer_id}\n     to{self.delivery_address}\n     contains:{self.items}"

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
    def items(self, x:list):
        self.__items = x
        pass

    @property
    def payment_method(self):
        return self.__payment_method
    @payment_method.setter
    def payment_method(self, x:str):
        self.__payment_method = (x if x =='cash' else x if x == 'bitcoin' else x if x == 'check' else "None")
        pass

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,):
        self.__date = dt.datetime.now().strftime('%Y|%m|%d %I:%M:%S %p')
        pass

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, x):
        self.__customer_id = x
        pass

    @property
    def total_price(self):
        return self.__total_price
    @total_price.setter
    def total_price(self,x):
        self.__total_price = x
        pass


