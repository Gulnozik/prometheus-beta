import re

def validate_email(email):
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    
    # Remove leading/trailing whitespace
    email = email.strip()
    
    # Regular expression for email validation
    # Follows RFC 5322 standard with some practical constraints
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the regex pattern
    return bool(re.match(email_regex, email))