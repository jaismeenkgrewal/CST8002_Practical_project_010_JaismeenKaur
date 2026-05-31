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

class MercuryRecord:
    """
    Represents one record from the mercury dataset.
    """

    def __init__(self,
                 SiteName,
                 SiteNumber,
                 Year,
                 Latitude,
                 Longitude,
                 Water_Column_Depth,
                 THg,
                 GEM,
                 Methylated_Hg,
                 DMHg):

        self.SiteName = SiteName
        self.SiteNumber = SiteNumber
        self.Year = Year
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Water_Column_Depth = Water_Column_Depth
        self.THg = THg
        self.GEM = GEM
        self.Methylated_Hg = Methylated_Hg
        self.DMHg = DMHg