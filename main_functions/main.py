import traceback
from log_files.logger import log
from _log_in_method import _log_in_method, config
from _signin_method import _sign_in_method
from classes.class_customers import Customers
from classes.class_orders import RegOrder,VIPIOrders
from classes.class_items import Items
from classes.class_payment_context import METHOD
from datetime import datetime as dt

def access_junction():
    while True:
        print(f"\n\n\n\n————————————————|Wellcome!")
        print(f"\n\n Press 1 To:    Log In. \n Press 2 To:    Register A New Account.")

        try:
            choice = int(input("————| Your choice:   "))
            if choice == 2:
                 if _sign_in_method():
                    print(f"\n\n\n————————|: Now, Log In Again For Verification\n\n\n")
                    return _log_in_method()
                 else:
                    print(f"\n————|< X > Failed To Register, You're Launched Back To The Beginning.")
                    log.error("User Not Registered. Redirecting.")

            if choice == 1:
                try:
                    user = _log_in_method()

                    if user:
                        print(f"\n————|< V >: Logged In As: {user.first_name} {user.last_name}")
                        config.read('preferences.ini')
                        log.info(f'Logged In: {user}')
                        log.info(f'preferences.ini loaded')
                        return user

                except Exception as e:
                    print(f"————|< X >: Action Denied: {e}")
                    log.error(traceback.print_exc())

            if choice is None or choice == "":
                print(f"\n\n\n————————|<>: Exiting \n\n\n\n\n\n")
                log.info("Exited Access Junction")
                return False

        except ValueError:
            print(f" ————|< X >: Invalid Option Selected. Try Again Or Press Enter To Exit")
            # log.error(traceback.print_exc())
            # return False



if __name__ == '__main__':
    log.info("SOFTWARE START OPERATION")
    user = access_junction()

