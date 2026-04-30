from log_files.logger import log
import configparser
import traceback
import io

def config_():
    return configparser.ConfigParser()


def new_config(user):
    config["user_information"] = {
        'saved_id': f'{user.id}' if user.id else None,
        'saved_first_name': f'{user.first_name}' if user.first_name else None,
        'saved_last_name': f'{user.last_name}' if user.last_name else None,
        'saved_email': f'{user.email}' if user.email else None,
        'saved_fav_list': f'{user.favorite_items}' if user.favorite_items else None,
        'saved_delivery_address': f'{user.delivery_address}' if user.delivery_address else None,
        'saved_account_type': f'{user.account_type}' if user.account_type else None,
        'saved_discount': f'{user.discount}' if user.discount else None,
        'saved_favorite_items': f'{user.favorite_items}' if user.favorite_items else None,
        'saved_payments': f'{user.saved_payment}' if user.saved_payment else None,
        'saved_gift': f'{user.gifted}' if user.gifted else None
    }
    print(f"\n————————| New Saved User {user.first_name} {user.last_name}")
    with io.open('preferences.ini', 'w', encoding='utf-8') as configfile: config.write(configfile)


def get_saved_user_info():
    try:
        config.read('preferences.ini')
        first_name   : str = config["user_information"]["saved_first_name"]
        last_name : str = config["user_information"]["saved_last_name"]
        email  : str = config["user_information"]["saved_email"]
        fav_list : str = config["user_information"]["saved_fav_list"]
        delivery_address : str = config["user_information"]["saved_delivery_address"]
        account_type : str = config["user_information"]["saved_account_type"]
        discount : str = config["user_information"]["saved_discount"]
        favorite_items : str = config["user_information"]["saved_favorite_items"]
        payments : str = config["user_information"]["saved_payment"]
        gift : str = config["user_information"]["saved_gift"]
        log.info("read User Information From preferences.ini Successfully")

    except Exception as e:
        print(f"————|< X >: Failed To Load Saved Data: {e}")
        log.error("Failed Extracting Data From preferences.ini :\n"+traceback.format_exc())



config = config_()