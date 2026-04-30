from classes.class_items import Items
from insert_query import InsertQuery
from select_query import SelectQuery
from create_query import CreateQuery
from log_files.logger import log
from classes.class_customers import Customers


def db_search_customer(first: str, last: str) -> bool:
    query = """
                SELECT FROM customers WHERE first_name = ? AND last_name = ?
                """, (first, last)
    try:
        log.info(f"{__file__},{__name__}\n run query: {query}")
        results = SelectQuery("customers_file").run(query)
        if results: return True

    except Exception as e:
        log.error(f"{__file__},{__name__} error: {e}\n trying: {query}")
    return False


def db_search_item(name: str) -> bool:
    query = """SELECT FROM items WHERE name = ?""",name
    try:
        log.info(f"{__file__},{__name__}\n run query: {query}")
        results = SelectQuery("items_file").run(query)
        if results: return True
    except Exception as e:
        log.error(f"{__file__},{__name__} error: {e}\n trying: {query}")
    return False


def db_retrieve_customer(first: str, last: str) -> Customers | None:
    query = """
    SELECT * FROM customers WHERE first_name = ? AND last_name = ?
    """,(first, last)
    result = None
    try:
        log.info(f"{__file__},{__name__}\n run query: {query}")
        result = SelectQuery("customers_file").run(query)
    except Exception as e:
        log.error(f"{__file__},{__name__} error: {e}\n trying: {query}")
    if not result is None:
        return result
    else:
        return None


def db_retrieve_item(name)-> Items | None:
    query = """SELECT * FROM items WHERE name = ?""",name
    result = None
    try:
        log.info(f"{__file__},{__name__}\n run query: {query}")
        result = SelectQuery("items_file").run(query)
    except Exception as e:
        log.error(f"{__file__},{__name__} error: {e}\n trying: {query}")
    if not result is None:
        return result
    else:
        return None


def db_add_new_customer(first_name_input: str, last_name_input: str, email_input: str, address_input: str) -> bool:
    query = """INSERT INTO customers (first_name, last_name, email, address_input,account_type,discount,favorite_items,gifted)
    VALUES(?,?,?,?,'REG',0,[],?)""",(first_name_input, last_name_input, email_input, address_input,False)
    try:
        log.info(f"{__file__},{__name__}\n run query: {query}")
        InsertQuery("customers_file").run(query)
        return True
    except Exception as e:
        log.error(f"{__file__},{__name__} error: {e}\n trying: {query}")
    return False

