from classes.class_IOrders import IOrders
from log_files.logger import log, line,arrow,notify,success,failure

class VIPIOrders(IOrders):
    def calc_total_price(self):
        """calculate total price for vip customer"""
        if not self.customer.account_type == "vip":
            log.error("CUSTOMER IS NOT VIP. CANNOT COMPLETE THIS ACTION")
            raise Exception("Customer Not VIP. Cannot Complete This Action.")
        ttl_sum = sum(item.price for item in self.items)
        log.info(f"{line} TOTAL PRICE: {ttl_sum} -> DISCOUNTED:{ttl_sum * (1 - self.customer.discount/100)}\n FOR ACCOUNT: {self.customer.fullname} (ID:{self.customer.id})")
        return ttl_sum * (1 - self.customer.discount/100)


class RegOrder(IOrders):
    def calc_total_price(self):
        """calculate total price for regular customer"""
        log.info(f"{line} TOTAL PRICE: {sum(item.price for item in self.items)}\n FOR ACCOUNT: {self.customer.fullname} (ID:{self.customer.id})")
        return sum(item.price for item in self.items)