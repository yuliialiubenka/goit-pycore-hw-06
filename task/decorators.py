"""
Decorators module for the contact assistant bot.

This module provides reusable decorators for:
- Error handling in command handlers
- Colored output for different message types
- Input validation and argument handling
"""

from functools import wraps
from typing import Callable, Any, Optional
from colorama import Fore, Style
from message_texts import (
    INPUT_ERROR_MISSING_ARGS,
    INPUT_ERROR_CONTACT_NOT_FOUND,
    INPUT_ERROR_ENTER_NAME,
    UNKNOWN_COMMAND,
    INVALID_ARGUMENT_FORMAT,
)


def validate_args(
    required_count: int,
    validators: Optional[dict[int, Callable[[str], bool]]] = None,
    error_messages: Optional[dict[int, str]] = None,
    normalize_args: bool = False,
) -> Callable:
    """
    Decorator to validate command arguments before execution.

    Validates both the number and format of arguments. Can check if arguments
    match expected patterns (e.g., phone numbers contain only digits).

    Args:
        required_count: Minimum number of arguments required.
        validators: Optional dict mapping argument index to validation function.
                   Example: {1: lambda x: x.isdigit()} to check if arg[1] is numeric.
        error_messages: Optional dict mapping argument index to custom error messages.
        normalize_args: When True, combines multi-word name arguments into a single value.

    Returns:
        Decorator function that validates arguments before calling handler.

    Example:
        >>> @validate_args(
        ...     required_count=2,
        ...     validators={1: lambda x: x.isdigit()},
        ...     error_messages={1: "Phone number must contain only digits"}
        ... )
        ... def add_contact(args, contacts):
        ...     name, phone = args
        ...     contacts[name] = phone
        ...     return "Contact added."
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(args: list[str], *other_args: Any, **kwargs: Any) -> str:
            normalized_args = args
            if normalize_args:
                if required_count == 1 and len(args) > 1:
                    normalized_args = [" ".join(args)]
                elif required_count == 2 and len(args) > 2:
                    normalized_args = [" ".join(args[:-1]), args[-1]]

            # Check if we have enough arguments
            if len(normalized_args) < required_count:
                raise ValueError

            # Validate argument formats if validators provided
            if validators:
                for idx, validator in validators.items():
                    if idx < len(normalized_args):
                        if not validator(normalized_args[idx]):
                            if error_messages and idx in error_messages:
                                return error_messages[idx]
                            else:
                                return INVALID_ARGUMENT_FORMAT.format(arg_index=idx + 1)

            return func(normalized_args, *other_args, **kwargs)

        return wrapper

    return decorator


def input_error(func: Callable) -> Callable:
    """
    Decorator to handle input errors in command handler functions.

    Catches common exceptions (ValueError, KeyError, IndexError) and returns
    user-friendly error messages instead of letting the program crash.

    Args:
        func: Function to wrap with error handling.

    Returns:
        Wrapped function that handles exceptions gracefully.

    Example:
        >>> @input_error
        ... def add_contact(args, contacts):
        ...     name, phone = args
        ...     contacts[name] = phone
        ...     return "Contact added."
    """

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError:
            return INPUT_ERROR_MISSING_ARGS
        except KeyError as exc:
            if exc.args and exc.args[0] == "unknown_command":
                return UNKNOWN_COMMAND
            return INPUT_ERROR_CONTACT_NOT_FOUND
        except IndexError:
            return INPUT_ERROR_ENTER_NAME

    return inner


def colored_output(
    success_color: str = Fore.GREEN,
    error_color: str = Fore.RED,
    info_color: str = Fore.BLUE,
) -> Callable:
    """
    Decorator to apply colored formatting to function output.

    Automatically colors the output based on the content or result type.
    Success messages are displayed in green, error messages in red,
    and informational messages in blue by default.

    Args:
        success_color: Color for success messages (default: Fore.GREEN).
        error_color: Color for error messages (default: Fore.RED).
        info_color: Color for informational messages (default: Fore.BLUE).

    Returns:
        Decorator function that wraps the target function.

    Example:
        >>> @colored_output()
        ... def greet():
        ...     return "Hello!"
        >>> greet()  # Will print in green
        "Hello!"
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)

            # Determine color based on message content
            if isinstance(result, str):
                if Style.RESET_ALL in result:
                    return result

                result_lower = result.lower()

                if any(
                    word in result_lower
                    for word in [
                        "error",
                        "not found",
                        "invalid",
                        "give me",
                        "unknown",
                    ]
                ):
                    color = error_color
                elif any(
                    word in result_lower for word in ["added", "updated", "contact"]
                ):
                    color = success_color
                else:
                    color = info_color
            else:
                color = info_color

            return f"{color}{result}{Style.RESET_ALL}"

        return wrapper

    return decorator


def output_formatter(color: str = Fore.WHITE, bold: bool = False) -> Callable:
    """
    Decorator to format function output with specific color and style.

    Applies a specific color and optionally bold style to the function's
    return value. Useful for consistently styling specific types of output.

    Args:
        color: Colorama color code to apply (default: Fore.WHITE).
        bold: Whether to make the text bold using Style.BRIGHT (default: False).

    Returns:
        Decorator function that wraps the target function.

    Example:
        >>> @output_formatter(color=Fore.CYAN, bold=True)
        ... def show_title():
        ...     return "=== Contact List ==="
        >>> show_title()  # Will print in bright cyan
        "=== Contact List ==="
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            style = Style.BRIGHT if bold else ""

            return f"{style}{color}{result}{Style.RESET_ALL}"

        return wrapper

    return decorator
