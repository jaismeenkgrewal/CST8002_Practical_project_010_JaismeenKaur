"""
Course: CST8002 - Programming Language Research
Assignment: Practical Project 4
Student Name: Jaismeen Kaur
Student Number: 041145316
Section: 010
Professor: Daniel Cormier

File Description:
This file contains the Record model class.
The Record class represents a single row from the dataset
and stores all column values associated with a record.
It provides a structured way to work with dataset data
throughout the application.

References

[1] 	Matplotlib Development Team, "Matplotlib documentation.," Matplotlib, [Online]. Available: https://matplotlib.org/stable/. [Accessed 9 august 2026].
[2] 	Matplotlib Development Team, "Bar(x, height)," Matplotlib, [Online]. Available: https://matplotlib.org/stable/plot_types/basic/bar.html. [Accessed 9 Aug 2026].
[3] 	Python Software Foundation, "Errors and Exceptions," Python Software Foundation, [Online]. Available: https://docs.python.org/3/tutorial/errors.html. [Accessed 9 Aug 2026].



"""

class Record:
    """
    Represents a single dataset record.
    Stores all column values from one row of the CSV file.
    """

    def __init__(self, *columns):
        """
        Initializes a Record object with dynamic column values.

        Parameters:
            *columns: Variable length argument list representing dataset fields.
        """
        self.columns = list(columns)

    def __str__(self):
        """
        Returns a readable string representation of the record.

        Returns:
            str: Pipe-separated string of column values.
        """
        return " | ".join(
            str(c) if c not in ["", None] else "NA"
            for c in self.columns
        )