import datetime


class DVD:

    def __init__(self, name: str, ident: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = ident
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, ident: int, name: str, date: str, age_restriction: int):
        day, month_number_as_str, year = date.split('.')

        monthinteger = int(month_number_as_str)
        month = datetime.date(1900, monthinteger, 1).strftime('%B')

        return cls(name, ident, int(year), month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
