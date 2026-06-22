"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 2
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Persistence Layer of the application.
It is responsible for reading records from a CSV dataset,
creating Record objects, and saving records back to a new
CSV file using a UUID-generated filename.

References:
[1] Python CSV Documentation - https://docs.python.org/3/library/csv.html
[2] Python UUID Documentation - https://docs.python.org/3/library/uuid.html
[3] Python Unittest Documentation - https://docs.python.org/3/library/unittest.html
[4] Python Documentation - https://docs.python.org/3/
[5] Government of Canada Open Data Portal - https://open.canada.ca
"""

import csv
import uuid
from model.record import Record


class FileHandler:
    """
    Handles file input and output operations for CSV data.
    Responsible for loading dataset into memory and saving records
    back to a new CSV file.
    """

    def load_file(self, filename):
        """
        Loads records from a CSV file into memory.

        Parameters:
            filename (str): Path to the input CSV file.

        Returns:
            list: A list of Record objects loaded from the file.
        """
        records = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                first = True

                for row in reader:

                    # skip header
                    if first:
                        first = False
                        continue

                    # skip empty rows
                    if not row:
                        continue

                    # limit to 100 records
                    if len(records) >= 100:
                        break

                    # convert row to Record object
                    record = Record(*row)
                    records.append(record)

        except FileNotFoundError:
            print("File not found:", filename)

        except Exception as e:
            print("Error reading file:", e)

        return records

    def save_file(self, records):
        """
        Saves in-memory records to a new CSV file using a UUID filename.

        Parameters:
            records (list): List of Record objects to save.

        Returns:
            None
        """
        filename = str(uuid.uuid4()) + ".csv"

        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                for r in records:
                    writer.writerow(r.__dict__.values())

            print("Saved as:", filename)

        except Exception as e:
            print("Error saving file:", e)