from classes.class_IGift import IGift
from log_files.logger import log
class Customers:

    def __init__(self,first_name, last_name, email, delivery_address, account_type, discount, favorite_items, gift):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.account_type = account_type
        self.discount = discount
        self.favorite_items = favorite_items
        self.gifted = gift
        self.saved_payment = None

    def __str__(self):
        return (f"────> Customer Details:\n   id:{self.id}\n   name: {self.first_name} {self.last_name}\n   email: {self.email}\n   address: {self.delivery_address}"
                f"\n   {self.account_type} ({self.discount})\n   gifts: {self.gifted}\n   favorite list: {self.favorite_items}")

    def get_gift(self, gift:IGift):
        self.gifted = gift
        print(f"Hey {self.first_name}! You got a new gift! ")

    def open_gift(self):
        if self.gifted is None:
            print("Sorry, you don't have any gifts")
            return
        self.gifted.open_gift()
        self.gifted = None

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,x):
        self.__id = x
        log.info(f"customer id set to {x}")

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self,x):
        self.__first_name = x
        log.info(f"customer first_name set to {x}")

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self,x):
        self.__last_name = x
        log.info(f"customer last_name set to {x}")

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,x):
        self.__email = x
        log.info(f"customer email set to {x}")

    @property
    def delivery_address(self):
        return self.__delivery_address
    @delivery_address.setter
    def delivery_address(self,x):
        self.__delivery_address = x
        log.info(f"customer delivery_address set to {x}")

    @property
    def account_type(self):
        return self.__account_type
    @account_type.setter
    def account_type(self,x):
        self.__account_type = x
        log.info(f"customer account_type set to {x}")

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self,x):
        self.__discount = x
        log.info(f"customer discount set to {x}")

    @property
    def favorite_items(self):
        return self.__favorite_items
    @favorite_items.setter
    def favorite_items(self,x):
        self.__favorite_items = x
        log.info(f"customer favorite items modified")

    @property
    def gifted(self):
        return self.__gifted
    @gifted.setter
    def gifted(self,x):
        self.__gifted = x
        log.info(f"customer gifted set {x}")

    @property
    def saved_payment(self):
        return self.__saved_payment
    @saved_payment.setter
    def saved_payment(self,x):
        self.__saved_payment = x
        log.info(f"customer saved payment: {x}")


