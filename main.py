from db_actions.database_setup import setup_database
from main_functions.access_junction import junction
from classes.class_sysfacade import SysFacade
from log_files.logger import log, line, arrow, notify

def main_menu(main_faced: SysFacade):
    commands = {
        1: ("Create Order",       main_facade.create_order),
        2: ("Pick A Gift",        main_facade.pick_gift),
        3: ("Open My Gift",       main_facade.open_gift),
        4: ("View My Account",    lambda: print(main_facade.user)),
        0: ("Exit",               None)
    }
    while True:
        print(f"\n{line*3} MAIN MENU {line*3}")
        for k, (label, _) in commands.items():
            print(f"{arrow} {k}: {label}")
        try:
            choice = int(input(f"{line}| Your Choice: "))
            if choice == 0:
                log.info("USER EXITED")
                break
            if choice in commands:
                commands[choice][1]()
            else:
                print(f"{notify} Invalid Choice")
        except ValueError:
            print(f"{notify} Please Enter A Number")

if __name__ == '__main__':
    log.info("SOFTWARE START")
    setup_database()              # create tables if first run
    user = junction()             # login or register
    if user:
        main_facade = SysFacade(user)
        main_menu(main_facade)
    log.info("SOFTWARE END")