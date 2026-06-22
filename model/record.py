"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 2
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda


File Description:
This file contains the Record model class.
The Record class represents a single row from the dataset
and stores all column values associated with a record.
It provides a structured way to work with dataset data
throughout the application.

References:
[1] Python CSV Documentation - https://docs.python.org/3/library/csv.html
[2] Python UUID Documentation - https://docs.python.org/3/library/uuid.html
[3] Python Unittest Documentation - https://docs.python.org/3/library/unittest.html
[4] Python Documentation - https://docs.python.org/3/
[5] Government of Canada Open Data Portal - https://open.canada.ca
"""

class Record:

    def __init__(self, *columns):
        self.columns = list(columns)

    def __str__(self):
        return " | ".join(
            str(c) if c not in ["", None] else "NA"
            for c in self.columns
        )