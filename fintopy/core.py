from pandas import DataFrame, Series

class TimeSeries:

    def __init__(self, df):
        self._df = df

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self, self._df.attr)

    @property
    def df(self):
        return(self._df)

    @df.setter
    def df(self, d):
        if isinstance(d, DataFrame):
            self._df = d
        elif isinstance(d, Series):
            self._df = d.to_frame()
        else:
            raise TypeError('The argument passed to the constructor must be a Pandas DataFrame or Pandas Series')
