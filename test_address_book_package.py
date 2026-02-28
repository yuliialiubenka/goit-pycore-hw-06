"""
Test address book implementation from refactored package.
This script runs the example from the homework assignment using the new package structure.
"""

from task.models import AddressBook, Record


def main():
    # Creating a new address book
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_phone("0501234567")
    john_record.add_phone("0505555555")

    # Adding John's record to the address book
    book.add_record(john_record)

    # Creating and adding a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("0987654321")
    book.add_record(jane_record)

    # Displaying all records in the book
    print("All records in the book:")
    for name, record in book.data.items():
        print(f"{name}: {record}")

    print("\n" + "=" * 50 + "\n")

    # Finding and editing John's phone number
    john = book.find("John")
    john.edit_phone("0501234567", "0111222333")

    print("After editing John's phone:")
    print(john)  # Output: Contact name: John, phones: 0111222333; 0505555555

    print("\n" + "=" * 50 + "\n")

    # Searching for a specific phone number in John's record
    found_phone = john.find_phone("0505555555")
    print(f"{john.name}: {found_phone}")  # Output: John: 0505555555

    print("\n" + "=" * 50 + "\n")

    # Deleting Jane's record
    book.delete("Jane")

    print("After deleting Jane:")
    for name, record in book.data.items():
        print(f"{name}: {record}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
