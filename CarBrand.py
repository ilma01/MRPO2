import datetime


class CarBrand:
    def __init__(self, name: str, country: str = None, founding_year: datetime.datetime.year = None):
        self.name = name
        self.country = country
        self.founding_year = founding_year

    def get_info(self):
        return {
            "name": self.name,
            "country": self.country,
            "foundation_year": self.founding_year
        }