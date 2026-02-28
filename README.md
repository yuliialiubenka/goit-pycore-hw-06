# Python Core Homework 06

Solution for Python Core homework assignment, module 6.
This project contains a CLI contact assistant bot and address book models with OOP architecture.

## Quick Start

### 1. Activate Virtual Environment

**Windows:**

```bash
.venv/Scripts/activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the CLI Bot

```bash
python task/main.py
```

### 4. Run Tests

```bash
python test_address_book_package.py
```

## Overview

### CLI Contact Assistant Bot

Interactive console application for contact management with input validation and error handling.

**Technologies:**

- Modular architecture (separate modules for handlers, validators, messages)
- Decorators for error handling and output formatting
- `colorama` for colored terminal messages
- Validation for names and phones (local 10 digits format)
- Dictionary-based contact storage

**Available Commands:**

- `hello` — greeting
- `add <name> <phone>` — add contact with phone number
- `change <name> <phone>` — change existing phone number
- `phone <name>` — show phone number for contact
- `all` — show all contacts
- `close` / `exit` — exit program

**Phone Format:**

- Accepts: `0501234567`, `050-123-4567`, `(050)123-4567`
- Must be 10 digits starting with 0
- No spaces or international prefix allowed

**Usage Examples:**

```bash
python task/main.py

# In interactive mode:
>>> add John 0501234567
>>> phone John
>>> change John 0509876543
>>> all
>>> close
```

### Address Book Models

OOP-based address book implementation in `task/models/` package with proper encapsulation and validation.

**Architecture:**

- **Field** — base class for all fields
- **Name** — name field with validation (min 2 chars, letters only)
- **Phone** — phone field with validation and normalization
- **Record** — contact record managing name and multiple phones
- **AddressBook** — main container inheriting from `UserDict`
- **Custom Exceptions** — hierarchy for error handling

**Key Features:**

- ✅ Type hints throughout all code
- ✅ Custom exception hierarchy (`AddressBookError`, `FieldError`, `RecordError`)
- ✅ Phone normalization (flexible input → 10 digits storage)
- ✅ Name validation (letters, spaces, hyphens, apostrophes)
- ✅ Centralized error messages in constants
- ✅ Full inheritance chain (Field → Name/Phone)

**Test File:**

Run [test_address_book_package.py](test_address_book_package.py) to see the implementation matching homework requirements:

```bash
python test_address_book_package.py
```

## Project Structure

```
goit-pycore-hw-06/
├── task/
│   ├── models/                # Address book models package
│   │   ├── __init__.py        # Package exports
│   │   ├── address_book.py    # AddressBook class
│   │   ├── exceptions.py      # Custom exceptions hierarchy
│   │   ├── field.py           # Base Field class
│   │   ├── name.py            # Name field with validation
│   │   ├── phone.py           # Phone field with validation
│   │   └── record.py          # Record class
│   ├── decorators.py          # Error handling decorators
│   ├── handlers.py            # Command handlers (add, change, etc.)
│   ├── input_parser.py        # Command parsing logic
│   ├── main.py                # CLI bot entry point
│   ├── message_texts.py       # Centralized message constants
│   ├── messages.py            # Message formatting utilities
│   └── validators.py          # Input validation functions
├── test_address_book_package.py  # Demo test from homework
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

## Models Package API

### Importing Models

```python
from task.models import AddressBook, Record, Name, Phone
from task.models import InvalidNameError, InvalidPhoneError, PhoneNotFoundError
```

### Usage Example

```python
# Create address book
book = AddressBook()

# Create record with name validation
john = Record("John")

# Add phones with validation and normalization
john.add_phone("050-123-4567")  # Stored as: 0501234567
john.add_phone("0509999999")

# Add to book
book.add_record(john)

# Find record
found = book.find("John")
print(found)  # Contact name: John, phones: 0501234567; 0509999999

# Edit phone
john.edit_phone("0501234567", "0501111111")

# Find specific phone
phone = john.find_phone("0509999999")  # Returns: "0509999999"

# Delete record
book.delete("John")
```

## Exception Hierarchy

```
AddressBookError (base)
├── FieldError
│   ├── InvalidNameError
│   └── InvalidPhoneError
└── RecordError
    └── PhoneNotFoundError
```

## Technologies and Concepts

- **Python 3.12+** — modern version with type hints support
- **OOP** — inheritance (Field → Name/Phone), encapsulation, custom exceptions
- **Type Hints** — comprehensive type annotations (`str | None`, `list[Phone]`, etc.)
- **Custom Exceptions** — exception hierarchy for clear error handling
- **Decorators** — for error handling and output formatting
- **colorama** — colored terminal output
- **re (regular expressions)** — for validation and text parsing
- **UserDict** — proper dictionary inheritance for AddressBook
- **Package Structure** — modular organization with `__init__.py` exports
- **Validation** — two-layer (CLI input + model level)
- **Data Normalization** — flexible phone input formats normalized to storage format

## Validation Rules

### Phone Numbers

- **Format:** Local 10-digit numbers only
- **Must start with:** 0
- **Accepted input:** `0501234567`, `050-123-4567`, `(050)123-4567`
- **Not allowed:** spaces, international prefix (`+380`)
- **Storage:** Normalized to 10 digits (`0501234567`)

### Names

- **Min length:** 2 characters
- **Allowed:** letters, spaces, hyphens, apostrophes
- **Not allowed:** numbers, special symbols
- **Examples:** `John`, `Mary-Jane`, `O'Brien`

## Requirements

See [requirements.txt](requirements.txt) for full dependency list:

- `colorama>=0.4.6` — colored terminal output
