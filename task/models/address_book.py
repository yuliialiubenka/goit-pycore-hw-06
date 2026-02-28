"""AddressBook class for storing and managing contact records."""

from collections import UserDict

from .record import Record


class AddressBook(UserDict):
    """Class for storing records and managing contacts."""

    def add_record(self, record: Record) -> None:
        """Add a record to the address book."""

        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name."""

        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by name."""

        if name in self.data:
            del self.data[name]
