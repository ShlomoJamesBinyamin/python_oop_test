from classes.class_IGift import IGift
from log_files.logger import log, line,arrow,notify,success,failure

class Customers:

    def __init__(self,first_name, last_name, email, delivery_address, account_type, discount, favorite_items, gift:IGift):
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
        return (f"{arrow} Customer Details:\n   id:{self.id}\n   name: {self.fullname}\n   email: {self.email}\n   address: {self.delivery_address}"
                f"\n   {self.account_type} ({self.discount})\n   gifts: {self.gifted}\n   favorite list: {self.favorite_items}")

    def get_gift(self, gift:IGift):
        """announce that customer was given a gift"""
        self.gifted = gift
        print(f"{line}Hey {self.first_name}! You got a new gift! ")
        log.info(f"CUSTOMER{self.fullname} WAS GIFTED: {gift}")

    def open_gift(self):
        """show the gift and reset gifted to none"""
        if self.gifted is None:
            print(f"{notify} Oops! It Seems Like You Don't Have Any Gifts")
            return
        self.gifted.open_gift()
        self.gifted = None
        log.info(f"{self.fullname} OPENED IT'S GIFT")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,x):
        log.info(f"{self.fullname}'S ID SET TO: {x}")
        self.__id = x


    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self,x:str):
        log.info(f"{self.fullname}'S FIRST NAME SET TO: {x}")
        self.__first_name = x.lower()


    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self,x:str):
        log.info(f"{self.fullname}'S LAST NAME SET TO: {x}")
        self.__last_name = x.lower()


    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,x:str):
        log.info(f"{self.fullname}'S EMAIL SET TO: {x}")
        self.__email = x.lower()


    @property
    def delivery_address(self):
        return self.__delivery_address
    @delivery_address.setter
    def delivery_address(self,x:str):
        log.info(f"{self.fullname}'S ADDRESS SET TO: {x}")
        self.__delivery_address = x.lower()


    @property
    def account_type(self):
        return self.__account_type
    @account_type.setter
    def account_type(self,x:str):
        self.__account_type = x.lower() if x == "vip" else "reg"
        log.info(f"{self.fullname} TYPE SET TO: {x}")


    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self,x):
        if not self.account_type == "vip":
            print(f"Customer Cannot Have VIP Discount.")
            return
        self.__discount = x
        log.info(f"{self.fullname}'S VIP DISCOUNT SET TO: {x}")


    @property
    def favorite_items(self):
        return self.__favorite_items
    @favorite_items.setter
    def favorite_items(self,x):
        self.__favorite_items = x
        log.info(f"{self.fullname}'S ITEMS LIST MODIFIED")


    @property
    def gifted(self):
        return self.__gifted
    @gifted.setter
    def gifted(self,x):
        self.__gifted = x
        log.info(f"{self.fullname} WAS GIFTER {x}")


    @property
    def saved_payment(self):
        return self.__saved_payment
    @saved_payment.setter
    def saved_payment(self,x):
        self.__saved_payment = x
        log.info(f"{self.fullname} SAVED PAYMENT Payment_Method: {x}")


