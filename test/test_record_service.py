"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 2
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains unit tests for the RecordService class.
The tests are implemented using Python's unittest framework
and verify that business layer functionality behaves correctly.

References:
[1] Python CSV Documentation - https://docs.python.org/3/library/csv.html
[2] Python UUID Documentation - https://docs.python.org/3/library/uuid.html
[3] Python Unittest Documentation - https://docs.python.org/3/library/unittest.html
[4] Python Documentation - https://docs.python.org/3/
[5] Government of Canada Open Data Portal - https://open.canada.ca
"""

import unittest
from business.record_service import RecordService
from model.record import Record


class TestRecordService(unittest.TestCase):
    """
    Unit test class for validating RecordService functionality.
    """

    def test_add_record(self):
        """
        Tests whether a record is correctly added to the service.

        This test creates an empty RecordService, adds one Record,
        and verifies that the size of the internal list increases to 1.
        """
        service = RecordService([])

        r = Record("Test", "Data", "Extra")
        service.add(r)

        self.assertEqual(len(service.get_all()), 1)


if __name__ == "__main__":
    unittest.main()