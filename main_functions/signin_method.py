from log_files.logger import log, line,notify,success,failure
from main_functions import checkers
from db_actions import db_act


def _sign_in_method() -> bool | None:
    print("—————————————————————————————————————————————————————————")
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