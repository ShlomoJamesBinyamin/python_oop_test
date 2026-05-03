from classes.class_customers import Customers
from log_files.logger import log, line, notify, success, failure, arrow
import configparser
import io
from db_actions import db_act


def config_():
    return configparser.ConfigParser()


def new_config(user):
    """establishing new preferences for new user"""
    config["user_information"] = {
        'saved_id'        : f'{user.id}' if user.id else None,
        'saved_first_name': f'{user.first_name}' if user.first_name else None,
        'saved_last_name' : f'{user.last_name}' if user.last_name else None
    }
    print(f"\n{line}| New Saved User {user.full_name}")
    with io.open('preferences.ini', 'w', encoding='utf-8') as configfile: config.write(configfile)
    log.info("SET NEW USER PREFERENCES")


def get_saved_user_info() -> Customers | None:
    """retrieving exists preferences"""
    try:
        config.read('preferences.ini')
        has_id                 = config['user_information']['saved_id']
        first_name   : str     = config["user_information"]["saved_first_name"]
        last_name : str        = config["user_information"]["saved_last_name"]
        log.info("read User Information From preferences.ini Successfully")
        return db_act.db_retrieve_customer(first_name, last_name,has_id)

    except Exception as e:
        print(f"{failure}: Failed To Load Saved Data: {e}")
        log.error("FAILED EXTRACTING DATA FROM preferences.ini")
        return None




config = config_()