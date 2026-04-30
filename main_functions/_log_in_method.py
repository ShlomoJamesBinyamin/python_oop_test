from classes.class_customers import Customers
from main_functions import checkers
from log_files.logger import log
from db_actions import db_act
from config_ import config, io,new_config


def _log_in_method() -> Customers | bool:
    print(f"\n\n————————————————————————————————————————\n"
          f"        WELLCOME BACK !\n")
    while True:
        print(f"\n————| Enter Your Info Or Double Tap 'Enter' To Exit: \n")
        first_name_input      = input("       First Name:  |").lower()
        last_name_input       = input("       Last Name:   |").lower()

        if not first_name_input or not last_name_input:
            print(f"\n————|< X > Failed To Log On, You're Launched Back To The Beginning.\n\n")
            log.info("No Name Entered. Failed Login. Redirecting.")
            return False

        if not checkers.check_name(first_name_input) :
            print(f"{first_name_input} Is Not A Valid Name. Try A Real One Please")

        if not checkers.check_name(last_name_input) :
            print(f"{last_name_input} Is Not A Valid Fam Name. Try A Real One Please")

        if checkers.check_name(first_name_input) and checkers.check_name(last_name_input):
            try:
                user = db_act.db_retrieve_customer(first_name_input, last_name_input)
                if user:
                    log.info("Managed To Get User From DB")
                    # config["user_information"] =
                    new_config(user)
                    with io.open('preferences.ini', 'w', encoding='utf-8') as configfile:
                        config.write(configfile)
                    return user
                else:
                    log.error("Failed To Specify Customer. None Retrieved.")
                    return False
            except Exception as e:
                log.error("Failed To Get User Data At Login DB Reading Method\n" + str(e))
                return False



