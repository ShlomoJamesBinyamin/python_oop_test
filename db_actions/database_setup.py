from db_actions.write_query import WriteQuery
from db_actions.select_query import SelectQuery
from db_actions.create_query import CreateQuery
from log_files.logger import log

db = "sys_db_file.db"

def setup_database():
    """run once on first launch to build all tables"""
    table_items_create()
    table_customers_create()
    table_orders_create()
    table_favorites_create()
    log.info("DATABASE SETUP COMPLETE")


def table_customers_create():
    query = """
        CREATE TABLE IF NOT EXISTS customers (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name          TEXT    NOT NULL,
            last_name           TEXT    NOT NULL,
            email               TEXT    NOT NULL UNIQUE,
            delivery_address    TEXT    NOT NULL,
            account_type        TEXT    NOT NULL DEFAULT 'reg',
            discount            REAL             DEFAULT 0,
            gifted              TEXT             DEFAULT '[]'  
        );
    """
    try:
        CreateQuery(db).run(query)
        log.info("TABLE customers CREATED")
    except Exception as e:
        log.error(f"TABLE customers FAILED: {e}")


def table_items_create():
    query = """
        CREATE TABLE IF NOT EXISTS items (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            price       REAL    NOT NULL        
        );
    """
    try:
        CreateQuery(db).run(query)
        log.info("TABLE items CREATED")
    except Exception as e:
        log.error(f"TABLE items FAILED: {e}")


def table_orders_create():
    query = """
        CREATE TABLE IF NOT EXISTS orders (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            name                TEXT    NOT NULL,
            delivery_address    TEXT    NOT NULL,
            items               TEXT    NOT NULL DEFAULT '[]',
            customer_id         INTEGER NOT NULL,
            total_price         REAL    NOT NULL,
            payment_method      TEXT    NOT NULL,
            date                TEXT    NOT NULL,
            order_type          TEXT    NOT NULL DEFAULT 'reg',
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
    """
    try:
        CreateQuery(db).run(query)
        log.info("TABLE orders CREATED")
    except Exception as e:
        log.error(f"TABLE orders FAILED: {e}")

def table_favorites_create():
    query = """
        CREATE TABLE IF NOT EXISTS customer_favorites (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            item_id     INTEGER NOT NULL,
            UNIQUE(customer_id, item_id),           -- no duplicates
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (item_id)     REFERENCES items(id)
        );
    """
    try:
        CreateQuery(db).run(query)
        log.info("TABLE customer_favorites CREATED")
    except Exception as e:
        log.error(f"TABLE customer_favorites FAILED: {e}")
        

# def insert_customer():
#     try:
#         query = ("""
#                 INSERT INTO customers(first_name,last_name, email, delivery_address, account_type, discount, favorite_items, gifted)
#                 VALUES ("sofi",'technologies',"sofi@gmail.com","address1","VIP","0","[1,14]",False)
#                 """)
#         WriteQuery(db).run(query)
#         log.info(f"CUSTOMER INSERTED")
#     except Exception as e:
#         log.error(f" CUSTOMER INSERTION FAILED: {e}")
#         print(e)

def insert_item():
    try:
        query = ("""
        INSERT INTO items(item_name,price)
        VALUES ("item",1)
        """)
        WriteQuery(db).run(query)
        log.info(f" ITEM INSERTED")
    except Exception as e:
        log.error(f" ITEM INSERTION FAILED: {e}")
        print(e)

def insert_order():
    try:
        query = ("""
        INSERT INTO orders(name,delivery_address,items,customer_id,total_price,payment_method,date)
        VALUES("order","address","[1,2,3]",3,100,"cash","date")
        """)
        WriteQuery(db).run(query)
        log.info(f" ORDER INSERTED")
    except Exception as e:
        log.error(f"ORDER INSERTION FAILED: {e}")
        print(e)


def select_customer():
    try:
        query = """
        SELECT * FROM customers
        """
        SelectQuery(db).run(query)
        log.info(f" CUSTOMER SELECTED")

    except Exception as e:
        log.error(f"CUSTOMER SELECTION FAILED: {e}")

def select_item():
    try:
        query = """
        SELECT * FROM items
        """
        SelectQuery(db).run(query)
        log.info(f" ITEM SELECTED")
    except Exception as e:
        log.error(f"ITEM SELECTION FAILED: {e}")
        print(e)

def select_order():
    try:
        query = """
        SELECT * FROM orders
        """
        SelectQuery(db).run(query)
        log.info(f" ORDER SELECTED")
    except Exception as e:
        log.error(f"ORDER SELECTION FAILED {e}")
        print(e)


# table_customers_create()
# table_items_create()
# table_orders_create()
# insert_customer()
# select_customer()
# insert_item()
# select_item()
# insert_order()
# select_order()
