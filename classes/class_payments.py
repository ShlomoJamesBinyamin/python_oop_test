from datetime import datetime
from typing import override, reveal_type
from class_IPayment import IPayment
from log_files.logger import log

class CASH(IPayment):

    @override
    def pay(self, amount: float):
        print(f"Payment of {amount: .2f}$")
        log.info(f"{amount: .2f}$ BY CHASH")

class CREDIT(IPayment):
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    @override
    def pay(self, amount: float):
        if check_card_number(self):
            print(f" Paid: {amount: .2f} By Credit, {self.card_number[-4:]}")
            log.info(f"{amount: .2f} BY CREDIT, {self.card_number[-4:]}")
        else: raise ValueError("Invalid Card Number")

class CHECK(IPayment):
    def __init__(self,bank_code:str, branch_number:str, check_number:str, account_number:str):
        self.bank_code = bank_code
        self.branch_number = branch_number
        self.check_number = check_number
        self.account_number = account_number

    @override
    def pay(self, amount: float):
        if check_check(self):
            print(f"Paid: {amount: .2f} By Check, From Account: {self.account_number[-4:]}")
            log.info(f"{amount: .2f} BY CHECK:\n ACCOUNT: {self.account_number[-4:]}\n BANK: {self.bank_code}|{self.branch_number}\n CHECK: {self.check_number}")
        else: raise ValueError("Invalid Check")


def check_card_number(card):
    """this to validate the card details for real interfaces"""
    try:
        if len(card.card_number) == 16:
            exp_date = datetime.strptime(card.expiration_date, "%m/%y").date()
            if exp_date > datetime.today().date():
                if len(card.cvv) in (3,4):
                    return True
    except ValueError:
        log.error("PAYMENT DENIED: INVALID EXPIRATION DATE")
        return False
    log.error(f"PAYMENT DENIED: INVALID CARD NUMBER")
    return False

def check_check(check):
    """this to verify the check details for real interface"""
    valid_banks = ["10", "11", "12", "04", "20", "31","46","52"]
    if not check.bank_code in valid_banks:
        log.error("PAYMENT DENIED: INVALID BANK CODE")
        return False
    if not (1<= int(check.branch_number) <= 3):
        log.error("PAYMENT DENIED: INVALID BRANCH NUMBER")
        return False
    if len(check.account_number) < 6:
        log.error("PAYMENT DENIED: INVALID ACCOUNT NUMBER")
        return False
    if len(check.check_number) <= 0:
        log.error("PAYMENT DENIED: INVALID CHECK NUMBER")
        return False
    return True

