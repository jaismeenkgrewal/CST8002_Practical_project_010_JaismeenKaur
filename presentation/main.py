"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 3
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Presentation Layer of the application.
It provides a console-based user interface that allows users
to display, add, update, delete, save, reload, and sort
dataset records.

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

import os

from persistence.file_handler import FileHandler
from business.record_service import RecordService
from model.record import Record


def display_menu():
    """
    Display the application title, programmer name,
    and available menu options.
    """

    print("\n============================================")
    print("CST8002 PRACTICAL PROJECT 3")
    print("Program by JAISMEEN KAUR")
    print("============================================")
    print("1. Display Records")
    print("2. Add Record")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Save Records to UUID File")
    print("6. Reload Original Dataset")
    print("7. Sort Records by SiteName")
    print("0. Exit")
    print("============================================")


def main():
    """
    Run the application and connect the Presentation,
    Business, Model, and Persistence layers.
    """

    # Find the main project directory.
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Create a safe path to the original CSV dataset.
    FILE_PATH = os.path.join(
        BASE_DIR,
        "..",
        "NCP_ArcticMarineEcosystems_Mercury_Concentrations_EN_FR.csv"
    )

    # Create the Persistence Layer object.
    file_handler = FileHandler()

    # Load records from the original CSV file.
    records = file_handler.load_file(FILE_PATH)

    # Create the Business Layer object.
    service = RecordService(records)

    while True:

        display_menu()

        choice = input("Enter choice: ").strip()

        # =========================
        # DISPLAY ALL RECORDS
        # =========================
        if choice == "1":

            print("\n--- ALL RECORDS ---")

            all_records = service.get_all()

            if len(all_records) == 0:
                print("No records are currently available.")
            else:
                for index, record in enumerate(all_records):
                    print(index, record)

        # =========================
        # ADD A RECORD
        # =========================
        elif choice == "2":

            print("\n--- ADD RECORD ---")

            col1 = input("Enter col1: ")
            col2 = input("Enter col2: ")

            new_record = Record(col1, col2)

            service.add(new_record)

            print("Record added successfully.")

        # =========================
        # UPDATE A RECORD
        # =========================
        elif choice == "3":

            print("\n--- UPDATE RECORD ---")

            try:
                index = int(input("Enter index to update: "))

                existing_record = service.get_one(index)

                if existing_record is None:
                    print("Record was not found.")
                else:
                    col1 = input("Enter new col1: ")
                    col2 = input("Enter new col2: ")

                    updated_record = Record(col1, col2)

                    service.update(index, updated_record)

                    print("Record updated successfully.")

            except ValueError:
                print("Invalid index. Please enter a whole number.")

        # =========================
        # DELETE A RECORD
        # =========================
        elif choice == "4":

            print("\n--- DELETE RECORD ---")

            try:
                index = int(input("Enter index to delete: "))

                existing_record = service.get_one(index)

                if existing_record is None:
                    print("Record was not found.")
                else:
                    service.delete(index)
                    print("Record deleted successfully.")

            except ValueError:
                print("Invalid index. Please enter a whole number.")

        # =========================
        # SAVE TO UUID FILE
        # =========================
        elif choice == "5":

            print("\n--- SAVE RECORDS ---")

            file_handler.save_file(service.get_all())

        # =========================
        # RELOAD ORIGINAL DATA
        # =========================
        elif choice == "6":

            print("\n--- RELOAD DATASET ---")

            records = file_handler.load_file(FILE_PATH)

            service.reload(records)

            print("Original dataset reloaded successfully.")

        # =========================
        # SORT BY SITENAME
        # =========================
        elif choice == "7":

            print("\n--- SORT RECORDS BY SITENAME ---")

            sorted_records = service.sort_by_SiteName()

            print("Records sorted alphabetically by SiteName.")

            for index, record in enumerate(sorted_records):
                print(index, record)

        # =========================
        # EXIT APPLICATION
        # =========================
        elif choice == "0":

            print("\nExiting program...")
            print("Program by JAISMEEN KAUR")
            break

        # =========================
        # INVALID MENU OPTION
        # =========================
        else:

            print("Invalid option. Please enter a number from 0 to 7.")


if __name__ == "__main__":
    main()