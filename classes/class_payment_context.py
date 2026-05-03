# from class_payments import *
from class_IPayment import IPayment
from log_files.logger import log

class Payment_Method:
    def __init__(self,method:IPayment):
        self.method = method

    @property
    def method(self):
        return self.__method
    @method.setter
    def method(self,method):
        self.__method = method
        log.info(f"Payment_Method SET: {self.method}")

    def execute_payment(self, amount:float):
        """execute payment method"""
        self.method.pay(amount)
        log.info(f"PAYMENT PAID: {self.method}")
