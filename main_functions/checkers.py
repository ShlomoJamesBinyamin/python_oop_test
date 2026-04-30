import re

# ———————————————————————————————————Name————————————————————————————————————————————
def check_name(input_str: str) -> bool:
    """
    validates the name for a real person name.
    """
    input_str = input_str.strip()
    return 2 <= len(input_str) <= 12 and \
            [not char.isdigit() or not char == '_' or not char.isspace() for char in input_str]
# ——————————————————————————————————Address—————————————————————————————————————————
def check_address(address:str) -> bool:
    """
    checks the address context.
    """
    return 8 <= len(address) <= 30 and \
        not all(char.isdigit() or char.isspace for char in address)

# ———————————————————————————————————Email———————————————————————————————————————————
def check_email(email: str) -> bool:
        valid_tlds = ["com", "org", "net", "edu", "gov", "mil", "int", "biz", "info", "pro", "name", "museum", "asia", "cat", "coop", "jobs", "mobi", "tel", "travel", "xxx"]
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email): return False
        domain = email.split("@")[1]
        domain_extension = domain.split(".")[-1].lower()
        return bool(re.match(pattern, email)) and domain_extension in valid_tlds


# ————————————————————————————————————————————————————————————————————————————————————