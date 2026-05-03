import traceback
from random import choice

from log_files.logger import log, line, arrow,notify,success,failure
from classes.class_customers import Customers
import checkers
from db_actions import db_act
from config_ import config, io,new_config

from classes.class_orders import RegOrder,VIPIOrders
from classes.class_items import Items
from classes.class_payment_context import Payment_Method
from datetime import datetime as dt

def _sign_in_method() -> bool | None:
    print(f"\n\n————————————————————————————————————————————————")
    print(f"                   Hello There!!!")
    print(f"       Pls Enter Your Info, Press Enter To Exist: \n\n")
    kick = False
    first_name, last_name, email,address = None, None, None, None
    while not kick:
        # ——————————————————————————————————————————— Registration Name
        while True:
            first_name = str(input(f"{line}| First Name:  |")).lower()
            last_name = str(input(f"{line}| Last Name:   |")).lower()

            if not first_name and not last_name:
                print(f"\n{failure} Failed To Register, You're Launched Back To The Beginning.\n\n")
                log.info("NO NAME REGISTERED. EXITING.")
                return None

            if not checkers.check_name(first_name):
                print(f"")
                first_name = str(input(f"{line}| Pls Enter A Valid Private Name. Or - Press Enter To Exist:  ")).lower()


            elif not checkers.check_name(last_name):
                last_name = str(input(f"{line}| Pls Enter A Valid Private Name. Or - Press Enter To Exist:  ")).lower()

            elif db_act.db_search_customer(first_name, last_name):
                print(f"Name Is Already Taken. Try Something Different")
                first_name = str(input(f"{line}| First Name:  |")).lower()
                last_name = str(input(f"{line}| Last Name:   |")).lower()

            else:
                print(f"\n{success} Valid name: '{first_name} {last_name}'")
                kick = True
                log.info(f"NEW CUSTOMER'S NAME: {first_name} {last_name}")
                break


        if kick:  # ———————————————————————————————————Registration Email
            kick = False
            email = str(input(f"{line}| Email:      |")).lower()
            while True:

                if not checkers.check_email(email):
                    print(f"{notify} Pls Enter A Valid Email  ")

                else:
                    print(f"\n{success} Valid Email: {email}")
                    kick = True
                    log.info(f"NEW CUSTOMER'S EMAIL: {email}")
                    break
                email = str(input(f"{line}| Email:      |")).lower()


        if kick:  # —————————————————————————————————— Registration Address
            kick = False
            print(f"Address Rules: \n{line}| 1: Between 8 to 30 Characters\n{line}| 2: Must Contain Both Street, City And House Number")
            address = str(input(f"{line}| Physical Delivery Address:   |")).lower()
            while True:

                if not checkers.check_address(address):
                    print(f"{notify} Pls Enter A Valid Delivery Address   |")

                else:
                    print(f"\n{success} Valid Address. Hope Will Find It Easily...")
                    log.info(f"NEW CUSTOMER'S ADDRESS: {address}")
                    kick = True
                    break
                address = str(input(f"{line}| Physical Delivery Address:   |")).lower()


        if kick and first_name and last_name and address and email:
            log.info(f"NEW CUSTOMER'S DATA OBTAINED. REDIRECTING TO db_act")
            db_act.db_add_new_customer(first_name, last_name,email,address)
            return True
        kick = False
    return None


def _log_in_method() -> Customers | bool:
    first_name, last_name, email,address = None, None, None, None
    print(f"\n\n————————————————————————————————————————\n"
          f"        WELLCOME BACK !\n")
    while True:
        print(f"\n{line}| Enter Your Info Or Double Tap 'Enter' To Exit: \n")
        first_name      = input("       First Name:  |").lower()
        last_name       = input("       Last Name:   |").lower()

        if not first_name or not last_name:
            print(f"\n{failure} Failed To Log On, You're Launched Back To The Beginning.\n\n")
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
                log.error("FAILED TO GET USER DATA AT LOGIN Payment_Method\n" + str(e))
                return False

def junction() -> Customers | None:
    choice = None
    user = None

    while True:
        print(f"\n\n\n\n————————————————|Wellcome!")
        print(f"\n\n Press 1 To:    Log In. \n Press 2 To:    Register A New Account.")

        try:
            choice = int(input(f"{line}| Your choice:   "))
        except ValueError:
            print(f" ————|< X >: Invalid Option Selected. Try Again Or Press Enter To Exit")
            # log.error(traceback.print_exc())
            # return False

        if choice is None or choice == "":
            print(f"\n\n\n————————|<>: Exiting \n\n\n\n\n\n")
            log.info("Exited Access Junction")
            return None

        if choice == 1:
            try:
                user = _log_in_method()
            except Exception as e:
                print(f"{failure}: Action Denied: {e}")
                log.error(traceback.print_exc())

            if user:
                print(f"{success}: Logged In As: {user.fullname}")
                config.read('preferences.ini')
                log.info(f'Logged In: {user}')
                log.info(f'preferences.ini loaded')
                return user

        if choice == 2:
            if _sign_in_method():
                print(f"{line}|: Now, Log In Again For Verification\n\n\n")
                return _log_in_method()
            else:
                print(f"\n————|< X > Failed To Register, You're Launched Back To The Beginning.")
                log.error("User Not Registered. Redirecting.")
                return None