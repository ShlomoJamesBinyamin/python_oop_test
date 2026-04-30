from classes.class_IOrders import IOrders
from log_files.logger import log

class VIPIOrders(IOrders):
    def calc_total_price(self):
        if not self.customer.account_type == "VIP":
            log.error("Customer is not VIP. Cannot complete this action.")
            raise Exception("Customer is not VIP. Cannot complete this action.")
        ttl_sum = sum(item.price for item in self.items)
        log.info(f"TOTAL PRICE: {ttl_sum} -> DISCOUNTED:{ttl_sum * (1 - self.customer.discount/100)}\n FOR ACCOUNT: {self.customer.id}")
        return ttl_sum * (1 - self.customer.discount/100)


class RegOrder(IOrders):
    def calc_total_price(self):
        log.info(f"TOTAL PRICE: {sum(item.price for item in self.items)}\n FOR ACCOUNT: {self.customer.id}")
        return sum(item.price for item in self.items)