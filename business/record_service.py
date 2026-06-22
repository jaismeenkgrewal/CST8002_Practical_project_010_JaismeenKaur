"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 2
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Business Layer of the application.
It manages the in-memory collection of records and performs
CRUD operations including creating, reading, updating,
and deleting records.

References:
[1] Python CSV Documentation - https://docs.python.org/3/library/csv.html
[2] Python UUID Documentation - https://docs.python.org/3/library/uuid.html
[3] Python Unittest Documentation - https://docs.python.org/3/library/unittest.html
[4] Python Documentation - https://docs.python.org/3/
[5] Government of Canada Open Data Portal - https://open.canada.ca
"""

class RecordService:
    """
    Manages the collection of records stored in memory.
    Provides CRUD operations and data reloading functionality.
    """

    def __init__(self, records):
        """
        Initializes the RecordService with a list of records.

        Parameters:
            records (list): Initial list of Record objects.
        """
        self.records = records

    def get_all(self):
        """
        Returns all records currently stored in memory.

        Returns:
            list: The complete list of records.
        """
        return self.records

    def get_one(self, index):
        """
        Retrieves a single record by its index.

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
        Adds a new record to the in-memory list.

        Parameters:
            record (Record): The record to be added.
        """
        self.records.append(record)

    def update(self, index, record):
        """
        Updates an existing record at the specified index.

        Parameters:
            index (int): Position of the record to update.
            record (Record): New record data.
        """
        if 0 <= index < len(self.records):
            self.records[index] = record

    def delete(self, index):
        """
        Deletes a record from the list.

        Parameters:
            index (int): Position of the record to remove.
        """
        if 0 <= index < len(self.records):
            del self.records[index]

    def reload(self, new_records):
        """
        Replaces the current records with newly loaded records.

        Parameters:
            new_records (list): New list of records loaded from the dataset.
        """
        self.records = new_records