from insert_query import InsertQuery
from select_query import SelectQuery
from create_query import CreateQuery
from log_files.logger import log


def table_customers_create():
    try:
        query = """
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            delivery_address TEXT NOT NULL,
            account_type TEXT NOT NULL,
            discount INTEGER,
            favorite_items TEXT NOT NULL,
            gifted BOOLEAN NOT NULL       
        );
        """
        CreateQuery('customers_file.db').run(query)
        log.info(f"{__file__}: {__name__}: CUSTOMER'S TABLE CREATED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def table_items_create():
    try:
        query = """
                CREATE TABLE IF NOT EXISTS items(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                price INTEGER NOT NULL
            );
            """
        CreateQuery("items_file.db").run(query)
        log.info(f"{__file__}: {__name__}: ITEMS TABLE CREATED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def table_orders_create():
    try:
        query = """
            CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            delivery_address TEXT NOT NULL,
            items LIST NOT NULL,
            customer_id INTEGER NOT NULL,
            total_price INTEGER NOT NULL, 
            payment_method TEXT NOT NULL,
            date TEXT NOT NULL
        );
        """
        CreateQuery("orders_file.db").run(query)
        log.info(f"{__file__}: {__name__}: ORDERS TABLE CREATED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def insert_customer():
    try:
        query = ("""
                INSERT INTO customers(first_name,last_name, email, delivery_address, account_type, discount, favorite_items, gifted)
                VALUES ("sofi",'technologies',"sofi@gmail.com","address1","VIP","0","[1,14]",False)
                """)
        InsertQuery('customers_file.db').run(query)
        log.info(f"{__file__}: {__name__}: CUSTOMER INSERTED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def insert_item():
    try:
        query = ("""
        INSERT INTO items(item_name,price)
        VALUES ("item",1)
        """)
        InsertQuery('items_file.db').run(query)
        log.info(f"{__file__}: {__name__}: ITEM INSERTED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def insert_order():
    try:
        query = ("""
        INSERT INTO orders(name,delivery_address,items,customer_id,total_price,payment_method,date)
        VALUES("order","address","[1,2,3]",3,100,"cash","date")
        """)
        InsertQuery('orders_file.db').run(query)
        log.info(f"{__file__}: {__name__}: ORDER INSERTED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)


def select_customer():
    try:
        query = """
        SELECT * FROM customers
        """
        SelectQuery('customers_file.db').run(query)
        log.info(f"{__file__}: {__name__}: CUSTOMER SELECTED")

    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")

def select_item():
    try:
        query = """
        SELECT * FROM items
        """
        SelectQuery('items_file.db').run(query)
        log.info(f"{__file__}: {__name__}: ITEM SELECTED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
        print(e)

def select_order():
    try:
        query = """
        SELECT * FROM orders
        """
        SelectQuery('orders_file.db').run(query)
        log.info(f"{__file__}: {__name__}: ORDER SELECTED")
    except Exception as e:
        log.error(f"{__file__}: {__name__}: {e}")
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
