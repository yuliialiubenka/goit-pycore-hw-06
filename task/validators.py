"""
Validators module for the contact assistant bot.

This module provides validation functions for different argument types:
- Phone number validation
- Name validation
- General format validators
"""

import re


def is_valid_phone(phone: str) -> bool:
    """
    Validate phone number format.

    Accepts local numbers only (10 digits starting with 0).
    Allows hyphens and parentheses as separators, but no spaces or '+'.

    Args:
        phone: Phone number string without spaces.

    Returns:
        True if phone number is valid, False otherwise.

    Example:
        >>> is_valid_phone("0987654321")
        True
        >>> is_valid_phone("098-765-4321")
        True
        >>> is_valid_phone("+380987654321")  # International is invalid here
        False
        >>> is_valid_phone("098 765-4321")  # Spaces NOT allowed
        False
    """
    if not isinstance(phone, str) or " " in phone:  # Reject if spaces present
        return False

    # Extract only digits
    digits_only = re.sub(r"\D", "", phone)

    # Local format: exactly 10 digits starting with 0, NO '+' allowed
    return len(digits_only) == 10 and digits_only.startswith("0") and "+" not in phone


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
