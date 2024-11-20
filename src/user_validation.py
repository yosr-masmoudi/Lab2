import re
 
 
def is_valid_username(username):
    """
    Validates the username:
    - Must not be empty.
    - Must not contain spaces.
    """
    if not username or " " in username:
        return False
    return True
 
 
def is_valid_password(password):
    """
    Validates the password:
    - At least 8 characters.
    - At least one number.
    - At least one letter.
    - At least one special character.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
 
 
def is_valid_email(email):
    """
    Validates the email:
    - Contains @.
    - Contains .
    """
    if "@" not in email or "." not in email:
        return False
    return True