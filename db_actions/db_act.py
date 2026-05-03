import datetime
from tkinter.messagebox import RETRY
from traceback import print_tb

from classes.class_IOrders import IOrders
from classes.class_IPayment import IPayment
from classes.class_items import Items
from insert_query import InsertQuery
from select_query import SelectQuery
from create_query import CreateQuery
from log_files.logger import log, notify, success, failure, arrow, line
from classes.class_customers import Customers


def db_search_customer(first: str|None="", last: str|None="", has_id: str | None="") -> Customers|bool:
    """searches db for customer by fullname or id if mentioned. return true if exists"""
    if first and last:
        log.info(f"{__file__}: {__name__}: TRYING: SEARCH CUSTOMER BY NAME")
        try:
           return db_retrieve_customer(first, last)
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return False

    elif has_id:
        log.info(f"{__file__}: {__name__}: TRYING: SEARCH CUSTOMER BY ID")
        try:
            return db_retrieve_customer(None,None,has_id)
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return False

    else:
        log.error("NO FIRST, LAST NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. Couldn't Find Customer")
        return False


def db_search_item(name: str|None="", has_id:str|None="") -> Items | bool:
    """searches db for item by name or id if mentioned. return true if exists"""
    if has_id:
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ITEM BY ID")
        try:
            return db_retrieve_item(None,has_id)
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return False

    elif name:
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ITEM BY NAME ")
        try:
            return db_retrieve_item(name)
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return False
    else:
        log.error("NO NAME NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. Couldn't Find Item")
        return False


def db_retrieve_customer(first:  str|None = "", last: str|None= "", has_id: str | None="") -> Customers | None:
    """searches db for customer by fullname or id if mentioned. return customer if exists"""
    result = None
    if has_id:
        query = """
            SELECT * FROM customers WHERE id = ?
            """
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE CUSTOMER BY ID ")
        try:
            return SelectQuery("customers_file.db").run(query, (has_id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return None

    elif first and last:
        query = """
            SELECT * FROM customers WHERE first_name = ? AND last_name = ?
            """
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE CUSTOMER BY NAME")
        try:
            return SelectQuery("customers_file.db").run(query, (first, last))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return None

    else:
        log.error("NO FIRST, LAST NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. Couldn't Find Item")
        return None

def db_retrieve_item(name:str|None = "", has_id:str|None = "")-> Items | None:
    """searches db for item by name or id if mentioned. return item if exists"""
    result = None
    if has_id:
        query = """SELECT * FROM items WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE ITEM BY ID ")
        try:
            return SelectQuery("items_file.db").run(query, (has_id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return None

    elif name:
        query = """SELECT * FROM items WHERE name = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE ITEM BY NAME ")
        try:
            return SelectQuery("items_file.db").run(query, (name,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return None
    else:
        log.error("NO NAME NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. No Item Found")
        return None


def db_add_new_customer(first_name_input: str, last_name_input: str, email_input: str, address_input: str, object: Customers | None = "") -> bool:
    """inserting new customer into db"""
    query = """INSERT INTO customers (first_name, last_name, email, address_input,account_type,discount,favorite_items,gifted)
    VALUES(?,?,?,?,'REG',0,[],?)"""
    log.info(f"{__file__},{__name__}\n TRYING: ADD NEW CUSTOMER ")
    try:
        InsertQuery("customers_file.db").run(query,(first_name_input, last_name_input, email_input, address_input,False))
        return True
    except Exception as e:
        log.error(f"{__file__},{__name__} ERROR: {e}")
    return False


def view_items():
    """view items"""
    query = """SELECT * FROM items"""
    log.info(f"{__file__},{__name__}\n TRYING: VIEW ITEMS")
    try:
        result = SelectQuery("items_file.db").run(query)
    except Exception as e:
        log.error(f"{__file__},{__name__} ERROR: {e}")
        return
    if not result is None:
        print(line * 5 + "- ITEMS IN STOCK -" + line * 5)
        for item in result:
            print(item)


def  db_place_order(order : IOrders | None = "",
                    name :str| None ="", delivery_address : str | None ="", items:list|None = "",
                    customer : Customers| None="", payment:IPayment | None="",
                    total:float|None = 0, date :datetime.datetime| None = datetime.datetime.now()) -> bool:
    """sending order to db"""
    if order:
        query = """INSERT INTO orders (order_id, name, delivery_Address, items, customer_id,total_price, payment, date)
        VALUES(?,?,?,?,?,?,?)"""
        log.info(f"{__file__},{__name__}\n TRYING: PLACING ORDER ")
        try:
            InsertQuery('orders_file.db').run(query,(order.name,order.delivery_address,order.items,order.customer.id,order.total_price,order.payment_method,order.date))
            return True
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            return False
    elif name and delivery_address and items and customer and payment:
        query = """INSERT INTO orders (order_id, name, delivery_Address, items, customer, payment, date)
                VALUES(?,?,?,?,?,?,?)"""
        log.info(f"{__file__},{__name__}\n TRYING: PLACING ORDER ")
        try:
            InsertQuery('orders_file.db').run(query,(name,delivery_address,items,customer.id,total,payment,date))
            return True
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            return False
    else: return False


def db_search_order(order : IOrders | None = "", has_id:str|None = "",
                    name :str| None ="", customer : Customers| None="", payment:IPayment | None="",
                    date :datetime.datetime| None = datetime.datetime.now()) -> IOrders|None:
    """searching the db for specific order"""

    if order:
        query = """SELECT * FROM orders WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery("orders_file.db").run(query, (order.id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif has_id:
        query = """SELECT * FROM orders WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery("orders_file.db").run(query, (has_id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif name:
        query = """SELECT * FROM orders WHERE name = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery("orders_file.db").run(query, (name,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif customer and date and payment:
        query = """SELECT * FROM orders WHERE customer_id = ? AND date = ? AND payment_method = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery("orders_file.db").run(query, (customer.id,date,payment))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    else:
        print(f"{notify} Something Went Wrong While Searching For The Order. We'll Try Again Later.")
        log.error(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        return None
    return None




