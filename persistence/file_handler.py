"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 3
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Persistence Layer of the application.
It reads the actual tabular records from the CSV dataset,
creates Record objects, and saves records to a new CSV file
using a UUID-generated filename.

References:
[1] Python Software Foundation, "csv — CSV File Reading and Writing,"
    Python Documentation. [Online]. Available:
    https://docs.python.org/3/library/csv.html

[2] Python Software Foundation, "uuid — UUID Objects,"
    Python Documentation. [Online]. Available:
    https://docs.python.org/3/library/uuid.html

[3] Python Software Foundation, "Python Documentation."
    [Online]. Available:
    https://docs.python.org/3/

[4] Government of Canada, "Open Data Portal."
    [Online]. Available:
    https://open.canada.ca
"""

import csv
import uuid

from model.record import Record


class FileHandler:
    """
    Handles CSV file input and output operations.
    """

    COLUMN_NAMES = [
        "SiteName",
        "SiteNumber",
        "Year",
        "Latitude",
        "Longitude",
        "Water_Column_Depth",
        "THg",
        "GEM",
        "Methylated_Hg",
        "DMHg"
    ]

    def load_file(self, filename):
        """
        Load up to 100 actual dataset records from the CSV file.

        Metadata rows are ignored. Reading begins after the
        actual dataset header row is found. Data dictionary
        rows are also ignored.

        Parameters:
            filename (str): Path to the original CSV dataset.

        Returns:
            list: List of Record objects.
        """
        records = []
        header_found = False

        try:
            with open(
                filename,
                "r",
                newline="",
                encoding="cp1252"
            ) as file:

                reader = csv.reader(file)

                for row in reader:

                    # Ignore completely empty rows.
                    if not row:
                        continue

                    # Remove extra spaces from every column.
                    cleaned_row = [
                        column.strip()
                        for column in row
                    ]

                    # Find the actual dataset header.
                    if not header_found:
                        SiteName = cleaned_row[0]

                        if SiteName == "SiteName":
                            header_found = True

                        # Ignore metadata rows and the header row.
                        continue

                    # Ignore rows containing only blank values.
                    if all(column == "" for column in cleaned_row):
                        continue

                    # Ignore rows that do not contain all 10 columns.
                    if len(cleaned_row) < len(self.COLUMN_NAMES):
                        continue

                    # Use exactly the required 10 dataset columns.
                    cleaned_row = cleaned_row[:len(self.COLUMN_NAMES)]

                    # Use exact dataset column names as variables.
                    SiteName = cleaned_row[0]
                    SiteNumber = cleaned_row[1]
                    Year = cleaned_row[2]
                    Latitude = cleaned_row[3]
                    Longitude = cleaned_row[4]
                    Water_Column_Depth = cleaned_row[5]
                    THg = cleaned_row[6]
                    GEM = cleaned_row[7]
                    Methylated_Hg = cleaned_row[8]
                    DMHg = cleaned_row[9]

                    # Only actual data rows have numeric SiteNumber and Year.
                    # This removes the data dictionary rows at the end.
                    if not SiteNumber.isdigit() or not Year.isdigit():
                        continue

                    record = Record(
                        SiteName,
                        SiteNumber,
                        Year,
                        Latitude,
                        Longitude,
                        Water_Column_Depth,
                        THg,
                        GEM,
                        Methylated_Hg,
                        DMHg
                    )

                    records.append(record)

                    # Load a maximum of 100 actual records.
                    if len(records) >= 100:
                        break

                if not header_found:
                    print(
                        "Error: The SiteName dataset header "
                        "was not found."
                    )
                else:
                    print(
                        f"{len(records)} dataset records loaded."
                    )

        except FileNotFoundError:
            print("File not found:", filename)

        except PermissionError:
            print("Permission denied while reading:", filename)

        except Exception as error:
            print("Error reading file:", error)

        return records

    def save_file(self, records):
        """
        Save records to a CSV file using a UUID filename.

        Parameters:
            records (list): Record objects to save.
        """
        filename = f"{uuid.uuid4()}.csv"

        try:
            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                # Save the required dataset column names.
                writer.writerow(self.COLUMN_NAMES)

                # Save each record's 10 column values.
                for record in records:
                    writer.writerow(record.columns)

            print("Records saved successfully.")
            print("Saved as:", filename)

        except PermissionError:
            print("Permission denied while saving:", filename)

        except Exception as error:
            print("Error saving file:", error)