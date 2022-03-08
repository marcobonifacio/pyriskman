import datetime as dt


class Datum:
    
    def __init__(self, date: dt.datetime, value: float):
        self.date = self._validate_date(date)
        self.value = self._validate_value(value)

    def _validate_date(self, date):
        pass
    
    def _validate_value(self, value):
        try:
            return float(value)
        except ValueError:
            print('Error: value must be a float number')
