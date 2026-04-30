from db_actions import db_act
from main_functions import checkers
from log_files.logger import log


def _sign_in_method():
    print(f"\n\n————————————————————————————————————————————————")
    print(f"                   Hello There!!!")
    print(f"       Pls Enter Your Info, Press Enter To Exist: \n\n")
    kick = False

    while not kick:
        # ——————————————————————————————————————————— Registration Name
        while True:
            first_name_input = str(input("————|First Name:  |")).lower()
            last_name_input = str(input("————|Last Name:   |")).lower()

            if not first_name_input and not last_name_input:
                print(f"\n————|< X > Failed To Register, You're Launched Back To The Beginning.\n\n")
                log.info("No Name Entered. Failed SignIn. Redirecting.")
                return False

            if not checkers.check_name(first_name_input):
                print(f"")
                first_name_input = str(input("————| Pls Enter A Valid Private Name. Or - Press Enter To Exist:  ")).lower()


            elif not checkers.check_name(last_name_input):
                last_name_input = str(input("————| Pls Enter A Valid Private Name. Or - Press Enter To Exist:  ")).lower()

            elif db_act.db_search_customer(first_name_input, last_name_input):
                print(f"Name Is Already Taken. Try Something Different")
                first_name_input = str(input("————|First Name:  |")).lower()
                last_name_input = str(input("————|Last Name:   |")).lower()

            else:
                print(f"\n————|< V > Valid name: '{first_name_input} {last_name_input}'")
                kick = True
                log.info(f"New Customer's Name: {first_name_input} {last_name_input}")
                break


        if kick:  # ———————————————————————————————————Registration Email
            kick = False
            while True:
                email_input = str(input("————|Email:      |")).lower()

                if not checkers.check_email(email_input):
                    print("————|< !!! > Pls Enter A Valid Email  ")

                else:
                    print(f"\n ————|< V > Valid Email: {email_input}")
                    kick = True
                    log.info(f"New Customers's Email: {email_input}")
                    break

        if kick:  # —————————————————————————————————— Registration Address
            kick = False
            print(f"Address Rules: \n————| 1: Between 8 to 30 Characters\n————|2: Must Contain Both Street, City And House Number")
            while True:
                address_input = str(input("————| Physical Delivery Address:   |")).lower()

                if not checkers.check_address(address_input):
                    print("————|< !!! > Pls Enter A Valid Delivery Address   |")

                else:
                    print(f"\n ————|< V > Valid Address. Hope Will Find It Easily...")
                    log.info(f"New Customer's Address: {address_input}")
                    kick = True
                    break

        if kick:
            db_act.add_new_customer(first_name_input, last_name_input,email_input,address_input)
            return True
        kick = False
    return None
