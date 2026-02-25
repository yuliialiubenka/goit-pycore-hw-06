"""
Messages module for the contact assistant bot.

This module provides user-friendly message functions with formatting:
- Greeting messages
- Error messages
- Command prompts
"""

from decorators import output_formatter
from colorama import Fore
from message_texts import (
    INVALID_NAME_FORMAT,
    INVALID_PHONE_FORMAT,
    WELCOME_MESSAGE,
    HELLO_MESSAGE,
    GOODBYE_MESSAGE,
    ERROR_UNEXPECTED_ARGUMENTS,
    PROMPT_FOR_ARGUMENT,
    PROMPT_FOR_COMMAND,
    NO_CONTACTS_FOUND,
)


@output_formatter(color=Fore.CYAN, bold=True)
def welcome_message() -> str:
    """Return welcome message for the assistant bot."""
    return WELCOME_MESSAGE


@output_formatter(color=Fore.GREEN)
def hello_message() -> str:
    """Return greeting message."""
    return HELLO_MESSAGE


@output_formatter(color=Fore.CYAN)
def goodbye_message() -> str:
    """Return goodbye message."""
    return GOODBYE_MESSAGE


@output_formatter(color=Fore.RED)
def error_unexpected_arguments(command: str) -> str:
    """Return error message when a command receives unexpected arguments."""
    return ERROR_UNEXPECTED_ARGUMENTS.format(command=command)


@output_formatter(color=Fore.RED)
def error_invalid_name_format() -> str:
    """Return error message for invalid name format."""
    return INVALID_NAME_FORMAT


@output_formatter(color=Fore.RED)
def error_invalid_phone_format() -> str:
    """Return error message for invalid phone format."""
    return INVALID_PHONE_FORMAT


@output_formatter(color=Fore.YELLOW)
def prompt_for_argument(arg_description: str, command: str) -> str:
    """Return prompt message for requesting a specific argument."""
    return PROMPT_FOR_ARGUMENT.format(
        arg_description=arg_description,
        command=command,
    )


@output_formatter(color=Fore.YELLOW)
def prompt_for_command() -> str:
    """Return prompt message for requesting a command."""
    return PROMPT_FOR_COMMAND


@output_formatter(color=Fore.BLUE)
def no_contacts_found_message() -> str:
    """Return message when there are no contacts."""
    return NO_CONTACTS_FOUND
