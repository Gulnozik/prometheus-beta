import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test various valid email addresses."""
    valid_emails = [
        "user@example.com",
        "user.name@example.com",
        "user+tag@example.com",
        "user-name@example.co.uk",
        "user123@example-domain.com",
        "first.last@example.org"
    ]
    
    for email in valid_emails:
        assert validate_email(email) is True, f"Failed to validate {email}"

def test_invalid_emails():
    """Test various invalid email addresses."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # Missing @ symbol
        "invalid@email",  # Missing domain extension
        "invalid@.com",  # Missing domain name
        "@example.com",  # Missing local part
        "user@example",  # Missing top-level domain
        "user@.com",  # Invalid domain
        "user name@example.com",  # Spaces not allowed
        "user@example..com"  # Consecutive dots not allowed
    ]
    
    for email in invalid_emails:
        assert validate_email(email) is False, f"Should not validate {email}"

def test_edge_cases():
    """Test edge cases and type validation."""
    # Test whitespace handling
    assert validate_email("  user@example.com  ") is True
    
    # Test type checking
    with pytest.raises(TypeError):
        validate_email(123)
    
    with pytest.raises(TypeError):
        validate_email(None)

def test_case_sensitivity():
    """Test that email validation is case-insensitive for local part."""
    assert validate_email("USER@EXAMPLE.COM") is True
    assert validate_email("User@Example.Com") is True