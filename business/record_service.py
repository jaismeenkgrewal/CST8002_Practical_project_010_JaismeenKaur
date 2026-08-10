"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 3
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Daniel Cormier

File Description:
This file contains the Business Layer of the application.
It manages the in-memory collection of records and performs
CRUD operations including creating, reading, updating,
deleting, reloading, and sorting records by SiteName.

References

[1] 	Matplotlib Development Team, "Matplotlib documentation.," Matplotlib, [Online]. Available: https://matplotlib.org/stable/. [Accessed 9 august 2026].
[2] 	Matplotlib Development Team, "Bar(x, height)," Matplotlib, [Online]. Available: https://matplotlib.org/stable/plot_types/basic/bar.html. [Accessed 9 Aug 2026].
[3] 	Python Software Foundation, "Errors and Exceptions," Python Software Foundation, [Online]. Available: https://docs.python.org/3/tutorial/errors.html. [Accessed 9 Aug 2026].



"""


class RecordService:
    """
    Manages the collection of records stored in memory.

    Provides create, read, update, delete, reload,
    and sorting operations.
    """

    def __init__(self, records):
        """
        Initialize the RecordService with a list of records.

        Parameters:
            records (list): Initial list of Record objects.
        """
        self.records = records

    def get_all(self):
        """
        Return all records currently stored in memory.

        Returns:
            list: The complete list of records.
        """
        return self.records

    def get_one(self, index):
        """
        Retrieve a single record by its index.

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
        Add a new record to the in-memory list.

        Parameters:
            record (Record): The record to be added.
        """
        self.records.append(record)

    def update(self, index, record):
        """
        Update an existing record at the specified index.

        Parameters:
            index (int): Position of the record to update.
            record (Record): New record data.
        """
        if 0 <= index < len(self.records):
            self.records[index] = record

    def delete(self, index):
        """
        Delete a record from the list.

        Parameters:
            index (int): Position of the record to remove.
        """
        if 0 <= index < len(self.records):
            del self.records[index]

    def reload(self, new_records):
        """
        Replace the current records with newly loaded records.

        Parameters:
            new_records (list): Records loaded from the dataset.
        """
        self.records = new_records

    def sort_by_SiteName(self):
        """
        Sort records alphabetically by the SiteName dataset column.

        The sorting is case-insensitive.

        Returns:
            list: Records sorted alphabetically by SiteName.
        """
        self.records.sort(
            key=lambda record: str(record.columns[0]).lower()
        )

        return self.records

    def get_chart_data(self, number_of_records):
        """
        Prepare SiteName and THg values for the vertical bar chart.

        Parameters:
            number_of_records (int): Number of valid records to include.

        Returns:
            tuple: SiteName values and THg values.
        """
        site_names = []
        thg_values = []

        count = 1

        for record in self.records:
            try:
                site_name = str(record.columns[0])
                thg_value = float(record.columns[6])

                chart_label = f"{site_name}#{count}"

                site_names.append(chart_label)
                thg_values.append(thg_value)
                count += 1

                if len(site_names) == number_of_records:
                    break

            except (ValueError, TypeError, IndexError):
                continue

        return site_names, thg_values