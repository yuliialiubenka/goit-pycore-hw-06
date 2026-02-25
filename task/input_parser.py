def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parse user input into a command and its arguments.

    Extracts the first word as the command (converted to lowercase) and
    remaining words as arguments.

    Args:
        user_input: Raw input string from user. If empty, returns empty command and args.

    Returns:
        Tuple of (command, arguments_list). Returns ("", []) if input is empty or None.

    Example:
        >>> parse_input("add John 1234567890")
        ("add", ["John", "1234567890"])
        >>> parse_input("")
        ("", [])
    """

    if not user_input or not user_input.strip():
        return "", []

    cmd, *args = user_input.split()

    return cmd.strip().lower(), args
