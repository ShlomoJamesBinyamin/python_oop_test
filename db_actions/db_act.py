import datetime
import json

from classes.class_IOrders import IOrders
from classes.class_orders import VIPIOrders, RegOrder
from classes.class_IPayment import IPayment
from classes.class_items import Items
from classes.class_gifts import ToyGift, CashGift
from classes.class_customers import Customers
from log_files.logger import log, notify, failure, line
from db_actions.write_query import WriteQuery
from db_actions.select_query import SelectQuery


db = "sys_db_file.db"

def db_search_customer(first: str|None="", last: str|None="", has_id: str | None="") -> Customers|bool:
    """searches db for customer by fullname or id if mentioned. return true if exists"""
    return db_retrieve_customer(first, last, has_id) is not None


def db_search_item(name: str|None="", has_id:str|None="") -> Items | bool:
    """searches db for item by name or id if mentioned. return true if exists"""
    return db_retrieve_item(name, has_id) is not None


def db_retrieve_customer(first:  str|None = "", last: str|None= "", has_id: str | None="") -> Customers | None:
    """searches db for customer by fullname or id if mentioned. return customer if exists"""
    if has_id:
        query = """
            SELECT * FROM customers WHERE id = ?
            """
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE CUSTOMER BY ID ")
        try:
            result =  SelectQuery(db).run(query, (has_id,))
            if result and len(result) > 0:
                return row_to_customer(result[0])
        except Exception as e:
            log.error(f"ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return None

    elif first and last:
        query = """
            SELECT * FROM customers WHERE first_name = ? AND last_name = ?
            """
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE CUSTOMER BY NAME")
        try:
            result = SelectQuery(db).run(query, (first, last))
            if result and len(result) > 0:
                return row_to_customer(result[0])
        except Exception as e:
            log.error(f"ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Customer Found")
            return None

    else:
        log.error("NO FIRST, LAST NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. Couldn't Find Item")
        return None


def db_retrieve_item(name:str|None = "", has_id:str|None = "")-> Items | None:
    """searches db for item by name or id if mentioned. return item if exists"""
    if has_id:
        query = """SELECT * FROM items WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE ITEM BY ID ")
        try:
            result = SelectQuery(db).run(query, (has_id,))
            if result and len(result) > 0:
                return row_to_item(result[0])
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return None

    elif name:
        query = """SELECT * FROM items WHERE name = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: RETRIEVE ITEM BY NAME ")
        try:
            result = SelectQuery(db).run(query, (name,))
            if result and len(result) > 0:
                return row_to_item(result[0])
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
            print(f"{failure} Sorry, An Error Occurred. No Item Found")
            return None
    else:
        log.error("NO NAME NOR ID WERE GIVEN.")
        print(f"{failure} Sorry, The Given Data Was Broken. No Item Found")
        return None


def db_add_new_customer(first_name_input: str, last_name_input: str, email_input: str, address_input: str) -> bool:
    """inserting new customer into db"""
    query = """INSERT INTO customers (first_name, last_name, email, delivery_address,
               account_type, discount, gifted)
               VALUES(?,?,?,?,'reg',0,'[]')"""
    try:
        WriteQuery(db).run(query, (first_name_input, last_name_input, email_input, address_input))
        return True
    except Exception as e:
        log.error(f"{__file__},{__name__} ERROR: {e}")
    return False


def view_items():
    """view items"""
    query = """SELECT * FROM items"""
    log.info(f"{__file__},{__name__}\n TRYING: VIEW ITEMS")
    try:
        result = SelectQuery(db).run(query)
    except Exception as e:
        log.error(f"{__file__},{__name__} ERROR: {e}")
        return
    if not result is None:
        print(line * 5 + "- ITEMS IN STOCK -" + line * 5)
        for item in result:
            print(item)


def db_place_order(order: IOrders) -> bool:
    """write order to db"""
    query = """
        INSERT INTO orders (name, delivery_address, items, customer_id, total_price, payment_method, date)
        VALUES (?,?,?,?,?,?,?)
    """
    try:
        items_json = json.dumps([item.id for item in order.items])  # [1, 4, 7]
        WriteQuery(db).run(query, (
            order.name,
            order.delivery_address,
            items_json,              # stored as "[1, 4, 7]"
            order.customer.id,
            order.total_price,
            order.payment_method,
            order.date
        ))
        log.info(f"ORDER PLACED: {order.name}")
        return True
    except Exception as e:
        log.error(f"ORDER INSERT FAILED: {e}")
        return False


def db_search_order(order : IOrders | None = "", has_id:str|None = "",
                    name :str| None ="", customer : Customers| None="", payment:IPayment | None="",
                    date :datetime.datetime| None = datetime.datetime.now()) -> IOrders|None:
    """searching the db for specific order"""

    if order:
        query = """SELECT * FROM orders WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery(db).run(query, (order.id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif has_id:
        query = """SELECT * FROM orders WHERE id = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery(db).run(query, (has_id,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif name:
        query = """SELECT * FROM orders WHERE name = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery(db).run(query, (name,))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    elif customer and date and payment:
        query = """SELECT * FROM orders WHERE customer_id = ? AND date = ? AND payment_method = ?"""
        log.info(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        try:
            return SelectQuery(db).run(query, (customer.id,date,payment))
        except Exception as e:
            log.error(f"{__file__},{__name__} ERROR: {e}")
    else:
        print(f"{notify} Something Went Wrong While Searching For The Order. We'll Try Again Later.")
        log.error(f"{__file__},{__name__}\n TRYING: SEARCH ORDER ")
        return None
    return None

def row_to_customer(row: tuple) -> Customers | None:
    """maps the row tuple to Customers object"""
    if not row:
        return None
    try:
        customer = Customers(
            first_name       = row[1],
            last_name        = row[2],
            email            = row[3],
            delivery_address = row[4],
            account_type     = row[5],
            discount         = row[6],
            favorite_items   = []
        )
        customer.id = row[0]
        customer.favorite_items = db_load_favorites(customer)

        if row[7] and row[7].strip():
            gifts_raw = json.loads(row[7])
            for g in gifts_raw:
                if g["type"] == "cash":
                    customer.gifted.append(CashGift(g["amount"], g.get("message")))
                elif g["type"] == "toy":
                    customer.gifted.append(ToyGift(g["item"], g.get("message")))

        log.info(f"ROW MAPPED TO CUSTOMER: {customer.fullname}")
        return customer

    except Exception as e:
        log.error(f"ROW TO CUSTOMER FAILED: {e}")
        return None


def row_to_item(row: tuple) -> Items | None:
    """ maps the row tuple to Items object"""
    if not row:
        return None
    try:
        item = Items(
            name  = row[1],
            price = row[2]
        )
        item.id = row[0]
        log.info(f"ROW MAPPED TO ITEM: {item.name} (ID:{item.id})")
        return item
    except Exception as e:
        log.error(f"ROW TO ITEM FAILED: {e}")
        return None


def row_to_order(row: tuple, customer: Customers) -> IOrders | None:
    items_ids = json.loads(row[3])
    items = [db_retrieve_item(has_id=i) for i in items_ids]
    order_type = row[8]
    if order_type == 'vip':
        order = VIPIOrders(row[1], customer, items, row[2], row[6])
    else:
        order = RegOrder(row[1], customer, items, row[2], row[6])
    order.id = row[0]
    return order


def db_update_gifts(customer: Customers) -> bool:
    """serialize gift list and save to db"""
    gifts_data = []
    for gift in customer.gifted:
        if isinstance(gift, CashGift):
            gifts_data.append({"type": "cash", "amount": gift.amount, "message": gift.message})
        elif isinstance(gift, ToyGift):
            gifts_data.append({"type": "toy", "item": gift.item, "message": gift.message})
    gifts_json = json.dumps(gifts_data)

    query = "UPDATE customers SET gifted = ? WHERE id = ?"
    try:
        WriteQuery(db).run(query, (gifts_json, customer.id))
        return True
    except Exception as e:
        log.error(f"GIFT UPDATE FAILED: {e}")
        return False


def db_sync_favorites(customer: Customers) -> bool:
    """sync customer's favorite_items list to junction table"""
    # clear existing then re-insert
    delete_query = "DELETE FROM customer_favorites WHERE customer_id = ?"
    insert_query = "INSERT OR IGNORE INTO customer_favorites (customer_id, item_id) VALUES (?,?)"
    try:
        WriteQuery(db).run(delete_query, (customer.id,))
        for item in customer.favorite_items:
            if item.id:
                WriteQuery(db).run(insert_query, (customer.id, item.id))
        log.info(f"FAVORITES SYNCED FOR {customer.fullname}")
        return True
    except Exception as e:
        log.error(f"FAVORITES SYNC FAILED: {e}")
        return False


def db_load_favorites(customer: Customers) -> list:
    """load favorite items from junction table"""
    query = """
        SELECT items.id, items.name, items.price
        FROM customer_favorites
        JOIN items ON customer_favorites.item_id = items.id
        WHERE customer_favorites.customer_id = ?
    """
    result = SelectQuery(db).run(query, (customer.id,))
    items = []
    if result:
        for row in result:
            item = Items(row[1], row[2])
            item.id = row[0]
            items.append(item)
    return items