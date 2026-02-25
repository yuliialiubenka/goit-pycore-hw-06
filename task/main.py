from colorama import init
from input_parser import parse_input
from handlers import execute_command
from messages import (
    welcome_message,
    goodbye_message,
    prompt_for_command,
)

# Initialize colorama for Windows compatibility
init(autoreset=True)


def main() -> None:
    """
    Main CLI loop for the contact assistant bot.

    Provides an interactive command-line interface for managing contacts.
    Supported commands:
    - hello: Display greeting
    - add <name> <phone>: Add a new contact
    - change <name> <phone>: Update an existing contact's phone
    - phone <name>: Look up a contact's phone number
    - all: Display all contacts in a formatted table
    - close/exit: Terminate the program

    The bot runs in an infinite loop until the user enters "close" or "exit".
    """

    contacts: dict[str, str] = {}

    print(welcome_message())

    while True:
        user_input = input(prompt_for_command())
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(goodbye_message())
            break

        result = execute_command(command, args, contacts)

        if result:  # Only print if there's a result
            print(result)


# For testing purposes
if __name__ == "__main__":
    main()
