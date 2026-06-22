"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 2
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Stanley Pieda

File Description:
This file contains the Presentation Layer of the application.
It provides a console-based user interface that allows users
to interact with the system. Users can display, add, update,
delete, save, and reload dataset records.

References:
[1] Python CSV Documentation - https://docs.python.org/3/library/csv.html
[2] Python UUID Documentation - https://docs.python.org/3/library/uuid.html
[3] Python Unittest Documentation - https://docs.python.org/3/library/unittest.html
[4] Python Documentation - https://docs.python.org/3/
[5] Government of Canada Open Data Portal - https://open.canada.ca
"""

from persistence.file_handler import FileHandler
from business.record_service import RecordService
from model.record import Record
import os


def main():
    """
    Entry point of the application.
    Handles user interaction and connects Presentation,
    Business, and Persistence layers.
    """

    print("Program by JAISMEEN KAUR")

    # =========================
    # SAFE FILE PATH SETUP
    # =========================
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    FILE_PATH = os.path.join(
        BASE_DIR,
        "..",
        "NCP_ArcticMarineEcosystems_Mercury_Concentrations_EN_FR.csv"
    )

    # =========================
    # LOAD DATA (PERSISTENCE LAYER)
    # =========================
    file_handler = FileHandler()
    records = file_handler.load_file(FILE_PATH)

    # =========================
    # BUSINESS LAYER
    # =========================
    service = RecordService(records)

    while True:

        print("\n======================")
        print("1. Display Records")
        print("2. Add Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Save Records (UUID)")
        print("6. Reload Data")
        print("0. Exit")
        print("======================")

        choice = input("Enter choice: ")

        # =========================
        # DISPLAY RECORDS
        # =========================
        if choice == "1":
            print("\n--- RECORDS ---")
            for i, r in enumerate(service.get_all()):
                print(i, r)

        # =========================
        # ADD RECORD
        # =========================
        elif choice == "2":
            col1 = input("Enter col1: ")
            col2 = input("Enter col2: ")
            service.add(Record(col1, col2))
            print("Record added successfully.")

        # =========================
        # UPDATE RECORD
        # =========================
        elif choice == "3":
            index = int(input("Enter index to update: "))
            col1 = input("New col1: ")
            col2 = input("New col2: ")
            service.update(index, Record(col1, col2))
            print("Record updated successfully.")

        # =========================
        # DELETE RECORD
        # =========================
        elif choice == "4":
            index = int(input("Enter index to delete: "))
            service.delete(index)
            print("Record deleted successfully.")

        # =========================
        # SAVE DATA (UUID FILE)
        # =========================
        elif choice == "5":
            file_handler.save_file(service.get_all())

        # =========================
        # RELOAD DATA
        # =========================
        elif choice == "6":
            records = file_handler.load_file(FILE_PATH)
            service.reload(records)
            print("Data reloaded successfully.")

        # =========================
        # EXIT APPLICATION
        # =========================
        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()