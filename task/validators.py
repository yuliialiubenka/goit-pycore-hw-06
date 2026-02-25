"""
Validators module for the contact assistant bot.

This module provides validation functions for different argument types:
- Phone number validation
- Name validation
- General format validators
"""


def is_valid_phone(phone: str) -> bool:
    """
    Validate phone number format.

    Checks if phone number contains only digits and optional '+' at the start.
    Length must be between 10 and 15 digits.

    Args:
        phone: Phone number string to validate.

    Returns:
        True if phone number is valid, False otherwise.

    Example:
        >>> is_valid_phone("1234567890")
        True
        >>> is_valid_phone("+380501234567")
        True
        >>> is_valid_phone("123abc")
        False
    """
    # Remove whitespace and allow a single leading '+'
    normalized = phone.strip()

    if normalized.startswith("+"):
        normalized = normalized[1:]

    # Check if remaining characters are digits and length is within bounds
    return normalized.isdigit() and 10 <= len(normalized) <= 15


def is_valid_name(name: str) -> bool:
    """
    Validate contact name format.

    Checks if name contains only letters, spaces, hyphens, and apostrophes.
    No leading/trailing separators and no consecutive separators.
    Minimum length: 2 characters.

    Args:
        name: Name string to validate.

    Returns:
        True if name is valid, False otherwise.

    Example:
        >>> is_valid_name("John")
        True
        >>> is_valid_name("Mary-Jane")
        True
        >>> is_valid_name("O'Brien")
        True
        >>> is_valid_name("123")
        False
    """
    trimmed = name.strip()

    if len(trimmed) < 2:
        return False

    # Allow letters, spaces, hyphens, and apostrophes only
    if not all(c.isalpha() or c in " -'" for c in trimmed):
        return False

    # Reject leading/trailing separators
    if trimmed[0] in " -'" or trimmed[-1] in " -'":
        return False

    # Reject consecutive separators (e.g., double spaces or "--")
    separators = " -'"
    prev_is_sep = False

    for char in trimmed:
        is_sep = char in separators

        if prev_is_sep and is_sep:
            return False

        prev_is_sep = is_sep

    return True
