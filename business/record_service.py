"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 3
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Business Layer of the application.
It manages the in-memory collection of records and performs
CRUD operations including creating, reading, updating,
deleting, reloading, and sorting records by SiteName.

References:
[1] Python Software Foundation, "Sorting Techniques,"
    Python Documentation. [Online]. Available:
    https://docs.python.org/3/howto/sorting.html

[2] Python CSV Documentation.
    https://docs.python.org/3/library/csv.html

[3] Python UUID Documentation.
    https://docs.python.org/3/library/uuid.html

[4] Python Unittest Documentation.
    https://docs.python.org/3/library/unittest.html

[5] Government of Canada Open Data Portal.
    https://open.canada.ca
"""


class RecordService:
    """
    Manages the collection of records stored in memory.

    Provides create, read, update, delete, reload,
    and sorting operations.
    """

    def __init__(self, records):
        """
        Initialize the RecordService with a list of records.

        Parameters:
            records (list): Initial list of Record objects.
        """
        self.records = records

    def get_all(self):
        """
        Return all records currently stored in memory.

        Returns:
            list: The complete list of records.
        """
        return self.records

    def get_one(self, index):
        """
        Retrieve a single record by its index.

        Parameters:
            index (int): Position of the record in the list.

        Returns:
            Record: The requested record if found, otherwise None.
        """
        if 0 <= index < len(self.records):
            return self.records[index]

        return None

    def add(self, record):
        """
        Add a new record to the in-memory list.

        Parameters:
            record (Record): The record to be added.
        """
        self.records.append(record)

    def update(self, index, record):
        """
        Update an existing record at the specified index.

        Parameters:
            index (int): Position of the record to update.
            record (Record): New record data.
        """
        if 0 <= index < len(self.records):
            self.records[index] = record

    def delete(self, index):
        """
        Delete a record from the list.

        Parameters:
            index (int): Position of the record to remove.
        """
        if 0 <= index < len(self.records):
            del self.records[index]

    def reload(self, new_records):
        """
        Replace the current records with newly loaded records.

        Parameters:
            new_records (list): Records loaded from the dataset.
        """
        self.records = new_records

    def sort_by_SiteName(self):
        """
        Sort records alphabetically by the SiteName dataset column.

        The sorting is case-insensitive.

        Returns:
            list: Records sorted alphabetically by SiteName.
        """
        self.records.sort(
            key=lambda record: record.SiteName.lower()
        )

        return self.records