import datetime
import time
from classes.class_customers import Customers
from classes.class_items import Items
from classes.class_orders import RegOrder, VIPIOrders
from classes.class_gifts import ToyGift, CashGift
from classes.class_payment_context import PaymentMethod
from classes.class_payments import CHECK, CASH, CREDIT,OTHER, check_check,check_card_number
from db_actions import  db_act
from log_files.logger import log, line, notify, success, failure, arrow
from main_functions.checkers import check_name

def get_customer() -> Customers | None:
    """Method to pick a customer"""
    log.info(f"{__file__}: {__name__}: TRYING: GET CUSTOMER")
    choice = None
    while True:
        try:
            choice = str(input(f"{line}| Your Choice: "))
            first, last = choice.lower().split(" ")
            customer = db_act.db_retrieve_customer(first, last)
        except ValueError:
            log.error(f"{__file__}: {__name__}: FAILED FINDING CUSTOMER.")
            print(f"{failure} {choice} Was Not Found")
            return None
        return customer

def get_item() -> Items | None:
    """Method to pick an item"""
    log.info(f"{__file__}: {__name__}: TRYING: PICKING ITEM")
    item = None

    choice = str(input(f"\n{line}| Would You Like To Search For A Certain Item? (y/n) "))
    if choice == "Y" or choice == "y" or choice == "YES" or choice == "yes":
        print(f"{arrow} What Is The Item You're Looking For? ")
        choice = str(input(f"{line}| :"))
        if choice.isalpha() and db_act.db_search_item(choice, None):
            item = db_act.db_retrieve_item(choice, None)
        else:
            print(f"{notify} Item {choice} Was Not Found")

    elif choice == "N" or choice == "n" or choice == "NO" or choice == "no":
        print(f"\n{line}| Here Are All The Items In Stock:")
        db_act.view_items()
        print(f"{arrow} Which Item You Want? ")
        choice = str(input(f"{line}| :"))
        if choice:
            if choice.isnumeric() and db_act.db_search_item(None, choice):
                item = db_act.db_retrieve_item(None, choice)
            elif check_name(choice) and db_act.db_search_item(choice, None):
                item = db_act.db_retrieve_item(choice, None)
            else:
                print(f"{notify} Item {choice} Not Found")


    if not item:
        print(f"{failure} Item {choice} Not Found")
        return None

    log.info(f"FOUND ITEM {choice}")
    print(f"{success}| Selected: {item.name} ")
    return item

def get_message() -> str | None:
    """method to pick a message, None also Valid."""
    log.info(f"{__file__}: {__name__}: TRYING: MESSAGE")
    while True:
        print(f"{line}| You Can Add Any Message You Want To Your Gift, Nothing Also Fine!")
        message = str(input(f"{line}| : "))
        print(f"{line}| Confirm The Message By Only Pressing The Button Enter: ")
        time.sleep(0.2)
        choice = str(input(f"{line}| : "))
        if not choice or choice.isspace() or choice == "":
            return message
        else:
            print(f"{failure} Message Was Canceled. Retrying")

def get_amount() -> int | None:
    """Method to pick an amount"""
    log.info(f"{__file__}: {__name__}: TRYING: GET AMOUNT")
    amount = 0
    print(f"{line}| What Amount Do You Want To Gift? ")
    try:
        amount = float(input(f"{line}| : "))
    except ValueError:
        print(f"{failure} Amount: {amount} Is Not Valid")

    if amount > 0:
        return amount
    return None


def pick_payment(user: Customers) -> PaymentMethod | None:
    """Method to pick a payment"""
    choice = None
    payment = None

    try:
        choice = int(input(f"{line}| Your Choice: "))
        if choice == 1:
            method = CASH()
            payment = PaymentMethod(method)
            user.saved_payment = "cash"
        if choice == 2:
            method = get_credit()
            payment = PaymentMethod(method)
            user.saved_payment = "credit"
        if choice == 3:
            method = get_check()
            payment = PaymentMethod(method)
            user.saved_payment = "check"
        if choice == 4:
            desc = input(f"{line}| Describe Payment Method: ")
            method = OTHER(desc)
            payment = PaymentMethod(method)
            user.saved_payment = "other"
    except ValueError:
        print(f"{notify}| {choice} Is Not A Valid Choice. (Should Be 1, 2 or 3)")

    if payment:
        return payment
    return None

def get_credit() -> CREDIT | None:
    """gets the credit card details"""
    card_number, card_cvv, card_date = None, None, None

    while True:
        while True:
            try:
                card_number = str(input(f"{line}| Credit Card Number: "))

                break
            except ValueError:
                print(f"{notify} {card_number} Is Not A Valid Card Number")

        while True:
            try:
                card_cvv = str(input(f"{line}| Credit CVV: "))
                break
            except ValueError:
                print(f"{notify} {card_cvv} Is Not A Valid CVV")
        while True:
            try:
                card_date = str(input(f"{line}| Credit Card Date: "))
                break
            except ValueError:
                print(f"{notify} {card_date} Is Not A Valid Date")
        if not card_number and not card_cvv and not card_date:
            print(f"{notify} No Data Provided. Redirecting")
            return None
        elif check_card_number(CREDIT(card_number,card_date, card_cvv)):
            return CREDIT(card_number, card_date, card_cvv)
        else:
            print(f"{notify}  something Went Wrong, Lets Try Again")

def get_check() -> CHECK | None:
    """gets the check details"""
    check_number, bank,branch, account = None, None, None,None
    while True:
        while True:
            try:
                check_number = str(input(f"{line}| Check Number: "))
                break
            except ValueError:
                print(f"{notify} {check_number} Is Not A Valid Check Number")
        while True:
            try:
                bank = str(input(f"{line}| Bank Code: "))
                break
            except ValueError:
                print(f"{notify} {bank} Is Not A Valid Bank Code")
        while True:
            try:
                branch = str(input(f"{line}| Branch Number: "))
                break
            except ValueError:
                print(f"{notify} {branch} Is Not A Valid Branch Number")
        while True:
            try:
                account = str(input(f"{line}| Account Number: "))
                break
            except ValueError:
                print(f"{notify} {account} Is Not A Valid Account Number")
        if not check_number and not account and not bank and not branch:
            print(f"{notify} No Data Provided. Redirecting")
            return None
        elif check_check(CHECK(bank, branch, check_number, account)):
            return CHECK(bank, branch, check_number, account)
        else:
            print(f"{notify} something Went Wrong, Lets Try Again")




def gift_toy(user: Customers) -> bool| None:
    """give toy gift method"""
    log.info(f"{__file__}: {__name__}: TRYING: GIFTING TOY.")
    print(f"\n{line}| Let's Gift!\n{line}| Who Would You Like To Gift?")
    while True:
        customer = get_customer()
        if customer:
            print(f"{success} We Found:  {customer.fullname}")
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

        # if customer and customer.gifted:
        #     print(
        #         f"{notify} We're Sorry, But {customer.fullname} Gift List Already Full. Push Them To Open Their Gifts!!")
        #     return False

    while True:
        item = get_item()
        if item:
            print(f"{success} We Found: \n{item}")
            message = get_message()
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

    while True:
        print(f"{line}| Pick Your Payment Method:\n{arrow} For Cash: Press 1\n{arrow} For Credit Card: Press 2\n{arrow} For Check: Press 3\n{arrow} For Other, Press 4")
        payment = pick_payment(user)
        if payment:
            payment.execute_payment(item.price)
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

    if item and customer and payment:
        gift = ToyGift(item, message)
        customer.get_gift(gift)
        log.info(f"GIFT TOY WAS SUCCESSFUL.")
        print(f"{success} We Gifted {customer.fullname} Successfully. You're Awsome!!")
        return True

    print(f"\n{line}| Canceling Your Order. Redirecting.")
    log.info(f"ORDER CANCELLED")
    return None

def gift_money(user: Customers) -> bool | None:
    """give money as a gift"""
    print(f"\n{line}| Let's Gift!\n{line}| Who Would You Like To Gift?")
    message = None
    while True:
        customer = get_customer()
        if customer:
            print(f"{success} We Found:  {customer.fullname}")
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

    while True:
        amount = get_amount()
        if amount:
            print(f"{success} Amount Set TO: {amount}")
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

    while True:
        print(f"{line}| Pick Your Payment Method:\n{arrow} For Cash: Press 1\n{arrow} For Credit Card: Press 2\n{arrow} For Check: Press 3\n{arrow} For Other, Press 4")
        payment = pick_payment(user)
        if payment:
            payment.execute_payment(amount)
            break
        else:
            print(f"{notify} Something Went Wrong")
            print(f"{notify} To Cancel The Gift, Please Paste The Exact Message:")
            print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
            choice = str(input(f"{line}| :"))
            if choice == 'CANCEL ORDER':
                print(f"\n{line}| Canceling Your Order. Redirecting.")
                log.info(f"ORDER CANCELLED")
                return None

    if customer and payment:
        gift = CashGift(amount, message)
        customer.get_gift(gift)
        db_act.db_update_gifts(customer)
        log.info(f"GIFT TOY WAS SUCCESSFUL.")
        print(f"{success} We Gifted {customer.fullname} Successfully. You're Awsome!!")
        return True

    print(f"\n{line}| Canceling Your Order. Redirecting.")
    log.info(f"ORDER CANCELLED")
    return None





class SysFacade:
    """a facade system that contains all user interface actions in the software"""
    def __init__(self, user: Customers):
        self.user = user

    def create_order(self):
        """orchestrates the ordering action"""
        print(f"\n\n{line*5}MAKE ORDER{line*5}")
        print(f"{notify}| NOTE: You Can Cancel At Any Time By Pressing The Enter Button")
        print(f"\n{line}| Please, Name Your Order (You May Choose Any Name You'd Like!) ")

        cancel_order = False
        order_name = str(input(f"{arrow} :"))
        address = self.user.delivery_address
        customer = self.user
        items =[]
        total = 0

        while True:
            item =  get_item()
            if item:
                items.append(item)
                log.info(f"ADDED ITEM TO ORDER")
                print(f"{success}| {item.name} Was Added To Your Order")
            else:
                break
            print(f"{success}: Let's Pick Another One!\n{notify} To Move Towards Payment, Just Press The Enter Button")

        if len(items) == 0:
            print(f"{notify} No Items In Order. Canceling.")
            log.info(f"{notify} User Canceled Order. EXITING")
            return

        print(f"\n{arrow} Order Details:\nOrder Name: {order_name}\nUser: {customer}\nItems: {items}\nDate: {datetime.datetime.now()}\nOrder Address: {address}")
        print(f"{line}| Choose Payment Method:\n{arrow} 1 : Cash\n{arrow} 2 : Credit\n{arrow} 3 : Check\n{arrow}")

        for item in items:
            total += item.price

        while True:
            print(f"{line}| Pick Your Payment Method:\n{arrow} For Cash: Press 1\n{arrow} For Credit Card: Press 2\n{arrow} For Check: Press 3\n{arrow} For Other, Press 4")
            payment = pick_payment(self.user)
            if payment:
                break
            else:
                print(f"{notify}| No Payment Method Chosen. To Cancel The Order Please Paste The Exact Message:")
                print(f"{line}| 'CANCEL ORDER'\n To Try Again, Please Press The Enter Button")
                choice = str(input(f"{line}| :"))
                if choice == 'CANCEL ORDER':
                    cancel_order = True
                    break

        if cancel_order:
            print(f"\n{line}| Canceling Your Order. Redirecting.")
            log.info(f"ORDER CANCELLED")
            return

        if self.user.account_type == 'vip':
            order = VIPIOrders(order_name,customer,items,address,customer.saved_payment)
            log.info(f"ORDER BUILD SUCCESSFULLY")
            payment.execute_payment(order.total_price)
            log.info(f"ORDER PAYMENT SUCCESSFULLY")
            db_act.db_place_order(order)
            db_act.db_sync_favorites(customer)
            print(f"{success}| {order.name} Was Placed Successfully!")


        if self.user.account_type == 'reg':
            order = RegOrder(order_name,customer,items,address,customer.saved_payment)
            log.info(f"ORDER BUILD SUCCESSFULLY")
            payment.execute_payment(order.total_price)
            log.info(f"ORDER PAYMENT SUCCESSFULLY")
            db_act.db_place_order(order)
            db_act.db_sync_favorites(customer)
            print(f"{success}| {order.name} Was Placed Successfully!")

    def pick_gift(self) :
        """gives a gift from current user to other"""
        log.info(f"GIFTING STARTED")
        print(f"{line}| What would you like to give?\n{arrow} For Any Toy: Press 1\n{arrow} For Money: Press 2\n{arrow} To Cancel: Press The Enter Button")
        choice = None
        try:
            choice = int(input(f"{line}| Your Choice: "))
            if not choice:
                print(f"{notify}| Canceling Gift. Exiting.")
                log.info(f"GIFTING CANCELLED")
                return
        except ValueError:
            print(f"{notify}| {choice} Is Not A Valid Choice.")
        if choice == 1:
            log.info(f"GIFT TOY SELECTED.")
            gift_toy(self.user)
        if choice == 2:
            log.info(f"GIFT MONEY SELECTED.")
            gift_money(self.user)

    def open_gift(self):
        """implements the open_gift function of any customer"""
        self.user.open_gift()

    def view_account(self):
        print(self.user)


    def open_all_gifts(self):
        self.user.open_all_gifts()
        db_act.db_update_gifts(self.user)









