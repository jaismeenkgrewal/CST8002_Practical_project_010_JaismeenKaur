

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

    def __init__(self, records):
        self.records = records

    def get_all(self):
        return self.records

    def get_one(self, index):
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def add(self, record):
        self.records.append(record)

    def update(self, index, record):
        if 0 <= index < len(self.records):
            self.records[index] = record

    def delete(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]

    def reload(self, new_records):
        self.records = new_records