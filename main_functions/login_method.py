from log_files.logger import log, line,notify,failure
from classes.class_customers import Customers
from main_functions import checkers
from db_actions import db_act
from main_functions.config_ import config, io,new_config

def _log_in_method() -> Customers | bool:
    print("—————————————————————————————————————————————"
          f"             WELLCOME BACK !")
    while True:
        print(f"\n{line}| Enter Your Info Or Double Tap 'Enter' To Exit: \n")
        first_name      = input("       First Name:  |").lower()
        last_name       = input("       Last Name:   |").lower()

        if not first_name or not last_name:
            print(f"\n{failure} Failed To Log On, You're Launched Back To The Beginning.")
            log.info("NO NAME ENTERED. EXITING.")
            return False

        if not checkers.check_name(first_name) :
            print(f"{notify}{first_name} Is Not A Valid Name. Try A Real One Please")

        if not checkers.check_name(last_name) :
            print(f"{notify}{last_name} Is Not A Valid Fam Name. Try A Real One Please")

        if checkers.check_name(first_name) and checkers.check_name(last_name):
            try:
                user = db_act.db_retrieve_customer(first_name, last_name)
                if user:

                    log.info("MANAGED TO GET USER FROM DB")
                    new_config(user)
                    with io.open('preferences.ini', 'w', encoding='utf-8') as configfile:
                        config.write(configfile)
                    return user
                else:
                    log.error("FAILED TO SPECIFY USER FROM DB. NONE RETRIEVED")
                    return False
            except Exception as e:
                log.error("FAILED TO GET USER DATA AT LOGIN PaymentMethod\n" + str(e))
                return False
