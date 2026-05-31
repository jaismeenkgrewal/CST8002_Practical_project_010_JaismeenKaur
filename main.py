"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Author: Jaismeen Kaur

References:

[1] Python CSV Documentation
https://docs.python.org/3/library/csv.html

[2] Python Exception Handling
https://docs.python.org/3/tutorial/errors.html
"""

import csv
from record import MercuryRecord

print("Student Name: Jaismeen Kaur")
print()

records = []

try:

    with open(
        "NCP_ArcticMarineEcosystems_Mercury_Concentrations_EN_FR.csv",
        "r",
        encoding="latin1"
    ) as file:

        reader = csv.reader(file)

        # Skip metadata rows
        for i in range(29):
            next(reader)

        # Read first few records
        for row in reader:

            if len(row) < 10:
                break

            record = MercuryRecord(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9]
            )

            records.append(record)

            # Only load first 10 records
            if len(records) == 10:
                break

except FileNotFoundError:
    print("Dataset file not found.")

print("Mercury Dataset Records")
print("-----------------------")

for record in records:

    print(
        record.SiteName,
        record.SiteNumber,
        record.Year,
        record.Latitude,
        record.Longitude,
        record.Water_Column_Depth,
        record.THg,
        record.GEM,
        record.Methylated_Hg,
        record.DMHg
    )