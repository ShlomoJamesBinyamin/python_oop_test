import re
from log_files.logger import log
# ———————————————————————————————————Name————————————————————————————————————————————
def check_name(input_str: str) -> bool:
    """validates the name for a real person name."""
    input_str = input_str.strip()
    log.info(f"CHECKING NAME CONTEXT FOR {input_str}")
    return 2 <= len(input_str) <= 12 and \
        all(char.isalpha() or char in "-' " for char in input_str)

# ——————————————————————————————————Address—————————————————————————————————————————
def check_address(address:str) -> bool:
    """checks the address context."""
    log.info(f"CHECKING ADDRESS CONTEXT FOR {address}")
    return 8 <= len(address) <= 30 and \
        not all(char.isdigit() or char.isspace() for char in address)

# ———————————————————————————————————Email———————————————————————————————————————————
def check_email(email: str) -> bool:
    """checks the email context."""
    log.info(f"CHECKING EMAIL CONTEXT FOR {email}")
    valid_tlds = ["com", "org", "net", "edu", "gov", "mil", "int", "biz", "info", "pro", "name", "museum", "asia", "cat", "coop", "jobs", "mobi", "tel", "travel", "xxx"]
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.match(pattern, email)
    if not match: return False
    domain_extension = email.split("@")[1].split(".")[-1].lower()
    return domain_extension in valid_tlds

# ————————————————————————————————————————————————————————————————————————————————————