"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 3
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Daniel Cormier

File Description:
This file contains unit tests for the RecordService class.
The tests use Python's unittest framework to verify that
records can be added and sorted alphabetically by SiteName.

References:
[1] Python Software Foundation, "unittest — Unit Testing Framework,"
    Python Documentation. [Online]. Available:
    https://docs.python.org/3/library/unittest.html

[2] Python Software Foundation, "Sorting Techniques,"
    Python Documentation. [Online]. Available:
    https://docs.python.org/3/howto/sorting.html

[3] Python Software Foundation, "Python Documentation."
    [Online]. Available:
    https://docs.python.org/3/

[4] Government of Canada, "Open Data Portal."
    [Online]. Available:
    https://open.canada.ca
"""

import unittest

from business.record_service import RecordService
from model.record import Record


class TestRecordService(unittest.TestCase):
    """
    Unit tests for RecordService business-layer functionality.
    """

    def test_add_record(self):
        """
        Test that a record is added to the in-memory collection.
        """
        service = RecordService([])

        record = Record(
            "Hudson Bay",
            "15",
            "2005",
            "62.138",
            "78.714",
            "0",
            "0.2",
            "33",
            "24.5",
            "1.9"
        )

        service.add(record)

        self.assertEqual(len(service.get_all()), 1)

    def test_sort_by_SiteName(self):
        """
        Test that records are sorted alphabetically by SiteName.
        """
        northwest_record = Record(
            "Northwest Passage",
            "6",
            "2005",
            "75.240",
            "74.982",
            "0",
            "1.3",
            "25.1",
            "15",
            "4.5"
        )

        hudson_record = Record(
            "Hudson Bay",
            "15",
            "2005",
            "62.138",
            "78.714",
            "0",
            "0.2",
            "33",
            "24.5",
            "1.9"
        )

        polynya_record = Record(
            "North Open Polynya",
            "1",
            "2005",
            "76.300",
            "71.407",
            "0",
            "0.1",
            "19.5",
            "21.4",
            "4.7"
        )

        service = RecordService(
            [
                northwest_record,
                polynya_record,
                hudson_record
            ]
        )

        sorted_records = service.sort_by_SiteName()

        self.assertEqual(
            sorted_records[0].columns[0],
            "Hudson Bay"
        )

        self.assertEqual(
            sorted_records[1].columns[0],
            "North Open Polynya"
        )

        self.assertEqual(
            sorted_records[2].columns[0],
            "Northwest Passage"
        )


if __name__ == "__main__":
    unittest.main()