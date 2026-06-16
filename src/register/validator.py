from email_validator import validate_email, EmailNotValidError
import re


def email_validator(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
    
def validate_user(username):

    pattern = r'^[A-Za-z0-9_]+$'
    if not re.match(pattern, username):
        raise ValueError("username can only contain letters, numbers, and underscores")


def validate_data(data):

    if not data.get("username"):
        raise ValueError("username required")
    
    if len(data.get("username", "")) < 3:
        raise ValueError("username must be at least 3 characters long")
    
    validate_user(data.get("username"))

    if not data.get("email"):
        raise ValueError("email required")
    
    if not email_validator(data.get("email")):
        raise ValueError("email is not valid")

    if data.get("age", 0) < 18:
        raise ValueError("age must be 18+")

    return True