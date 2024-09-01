import re
from typing import Tuple


def validate_phone_number(phone_number: str) -> Tuple[bool, str]:
    if len(phone_number) != 11:
        message = "Invalid phone number: Phone number must be 11 digits"
        return False, message
    elif not phone_number.isdigit():
        message = "Invalid phone number: Phone number must be digits"
        return False, message
    elif phone_number[0] != "0":
        message = "Invalid phone number: Phone number must start with 0"
        return False, message
    else:
        message = "Phone number is valid"
        return True, message


def validate_email(email:str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$'
    return re.match(pattern, email) is not None