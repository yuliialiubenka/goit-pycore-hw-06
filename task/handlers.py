from typing import Callable

from decorators import input_error, colored_output, validate_args
from validators import is_valid_phone, is_valid_name
from messages import (
    hello_message,
    error_unexpected_arguments,
    error_invalid_name_format,
    error_invalid_phone_format,
    no_contacts_found_message,
)


@colored_output()
@input_error
@validate_args(
    required_count=2,
    validators={0: is_valid_name, 1: is_valid_phone},
    error_messages={
        0: error_invalid_name_format(),
        1: error_invalid_phone_format(),
    },
    normalize_args=True,
)
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.

    Creates a new contact entry with the provided name and phone number.
    If a contact with the same name exists, it will be overwritten.

    Args:
        args: List of arguments where args[0] is contact name and args[1] is phone number.
              Must contain at least 2 elements.
        contacts: Dictionary to store contact information with name as key.

    Returns:
        Success message "Contact added."

    Raises:
        ValueError: If insufficient arguments are provided (less than 2).

    Example:
        >>> contacts = {}
        >>> add_contact(["John", "1234567890"], contacts)
        "Contact added."
        >>> contacts
        {"John": "1234567890"}
    """

    name, phone = args
    contacts[name] = phone
    return "Contact added."


@colored_output()
@input_error
@validate_args(
    required_count=2,
    validators={0: is_valid_name, 1: is_valid_phone},
    error_messages={
        0: error_invalid_name_format(),
        1: error_invalid_phone_format(),
    },
    normalize_args=True,
)
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Change phone number for an existing contact.

    Updates the phone number for a contact that already exists in the dictionary.
    Contact must exist before updating.

    Args:
        args: List of arguments where args[0] is contact name and args[1] is new phone number.
              Must contain at least 2 elements.
        contacts: Dictionary containing existing contact information.

    Returns:
        Success message "Contact updated." if contact exists and was updated.

    Raises:
        ValueError: If insufficient arguments provided (less than 2).
        KeyError: If the named contact does not exist in the dictionary.

    Example:
        >>> contacts = {"John": "1234567890"}
        >>> change_contact(["John", "0987654321"], contacts)
        "Contact updated."
        >>> contacts
        {"John": "0987654321"}
    """

    name, phone = args
    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@colored_output()
@input_error
@validate_args(
    required_count=1,
    validators={0: is_valid_name},
    error_messages={0: error_invalid_name_format()},
    normalize_args=True,
)
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Retrieve and return phone number for a specific contact.

    Looks up a contact by name and returns their phone number.

    Args:
        args: List of arguments where args[0] is the contact name to look up.
              Must contain at least 1 element.
        contacts: Dictionary containing contact information.

    Returns:
        The phone number string if contact is found.

    Raises:
        IndexError: If no arguments provided (empty args list).
        KeyError: If the named contact does not exist in the dictionary.

    Example:
        >>> contacts = {"John": "1234567890"}
        >>> show_phone(["John"], contacts)
        "1234567890"
        >>> show_phone(["Jane"], contacts)
        Raises KeyError
    """

    name = args[0]
    return contacts[name]


@colored_output()
@input_error
def show_all(contacts: dict[str, str]) -> str:
    """
    Display all contacts in a formatted table.

    Returns all contacts sorted alphabetically by name with phone numbers
    displayed in a formatted table with aligned columns.

    Args:
        contacts: Dictionary containing contact information with names as keys.

    Returns:
        Formatted table string with header, separator, and contact entries.
        Each line contains name and phone number separated by " | ".
        Returns "No contacts found." if the contacts dictionary is empty.

    Example:
        >>> contacts = {"Alice": "1111111111", "Bob": "2222222222"}
        >>> print(show_all(contacts))
        Name  | Phone
        ----- | -----
        Alice | 1111111111
        Bob   | 2222222222
    """

    if not contacts:
        return no_contacts_found_message()

    # Sort contacts alphabetically by name (case-insensitive)
    sorted_contacts = sorted(contacts.items(), key=lambda item: item[0].lower())

    # Calculate maximum name length for proper alignment
    max_name_len = max(len(name) for name, _ in sorted_contacts)

    # Build table header and separator
    header = f"{'Name'.ljust(max_name_len)} | Phone"
    separator = f"{'-' * max_name_len} | {'-' * 5}"
    lines = [header, separator]

    # Add contact rows
    lines.extend(
        f"{name.ljust(max_name_len)} | {phone}" for name, phone in sorted_contacts
    )

    return "\n".join(lines)


@colored_output()
@input_error
def execute_command(command: str, args: list[str], contacts: dict[str, str]) -> str:
    """
    Execute a command by dispatching to appropriate handler.

    Args:
        command: Command name to execute.
        args: List of arguments for the command.
        contacts: Dictionary of contacts.

    Returns:
        Result string from command execution.

    Raises:
        KeyError: If command is not recognized.
    """
    if not command:  # Empty command
        return ""

    commands: dict[str, tuple[Callable[..., str], str]] = {
        "hello": (hello_message, "none"),
        "add": (add_contact, "args_contacts"),
        "change": (change_contact, "args_contacts"),
        "phone": (show_phone, "args_contacts"),
        "all": (show_all, "contacts"),
    }

    if command in commands:
        handler, mode = commands[command]

        if mode == "none":
            if args:
                return error_unexpected_arguments(command)
            return handler()
        if mode == "contacts":
            if args:
                return error_unexpected_arguments(command)
            return handler(contacts)
        return handler(args, contacts)

    raise KeyError("unknown_command")
