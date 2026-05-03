from class_IGift import IGift
from class_items import Items
from log_files.logger import log, line,arrow,notify,success,failure

class ToyGift(IGift):
    def __init__(self, item:Items, message):
        self.item = item.name
        self.message = message

    def __str__(self):
        if self.message:
            return f"{arrow} Gift Includes - \n {self.item}\n Message: {self.message}"
        return f"{arrow} Gift Includes -\n {self.item}"

    def open_gift(self):
        """show the toy gift details"""
        print("Congratulations! you got a new gift! Enjoy!")
        print(self)

class CashGift(IGift):
    def __init__(self, amount:float, message):
        self.amount = amount
        self.message = message

    def __str__(self):
        if self.message:
            return f"{arrow} Gift Includes -\n {self.amount}\n Message: {self.message}"
        return f"{arrow} Gift Includes -\n {self.amount}"

    def open_gift(self):
        """show the cash gift details"""
        print("Congratulations! you got a new gift! Enjoy!")
        print(self)

