from log_files.logger import log, line, arrow,success,failure
from classes.class_customers import Customers
from main_functions.signin_method import _sign_in_method
from main_functions.login_method import _log_in_method
from main_functions.config_ import config

def junction() -> Customers | None:
    choice = None
    user = None

    while True:
        print(f"\n\n\n\n————————————————|Wellcome!")
        print(f"\n\n Press 1 To:    Log In. \n Press 2 To:    Register A New Account.")

        try:
            choice = int(input(f"{line}| Your choice:"))
        except ValueError:
            print(f"{failure}: Invalid Option Selected. Try Again Or Press Enter To Exit")
            log.error(f"{__file__}: {__name__}: VALUE ERROR")
            # log.error(traceback.print_exc())
            # return False

        if choice is None or choice == "":
            print(f"\n\n\n{arrow}: Exiting \n\n\n\n\n\n")
            log.info("EXITING ACCESS JUNCTION")
            return None

        if choice == 1:
            try:
                user = _log_in_method()
            except Exception as e:
                print(f"{failure}: Action Denied:")
                log.error(f"{__file__}: {__name__}: {e} ")

            if user:
                print(f"{success}: Logged In As: {user.fullname}")
                config.read('preferences.ini')
                log.info(f'Logged In: {user}')
                log.info(f'preferences.ini loaded')
                return user

        if choice == 2 :
            if _sign_in_method():
                print(f"{line}|: Now, Log In Again For Verification\n")
                return _log_in_method()
            else:
                print(f"\n————|< X > Failed To Register, You're Launched Back To The Beginning.")
                log.error("User Not Registered. Redirecting.")
                return None