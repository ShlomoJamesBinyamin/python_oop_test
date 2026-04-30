from class_IGift import IGift
from class_items import Items
from log_files.logger import log

class ToyGift(IGift):
    def __init__(self, item:Items, message):
        self.item = item.name
        self.message = message

    def __str__(self):
        if self.message:
            return f"Gift Includes: {self.item}\n And A Message: {self.message}"
        return f"Gift Includes: {self.item}"

    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
        print(self)

class CashGift(IGift):
    def __init__(self, amount:float, message):
        self.amount = amount
        self.message = message

    def __str__(self):
        if self.message:
            return f"Gift Includes: {self.amount}\n And A Message: {self.message}"
        return f"Gift Includes: {self.amount}"

    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
        print(self)

