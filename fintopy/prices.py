"""Price accessor to `pandas.DataFrame` and `pandas.Series`.
"""

import numpy as np
import pandas as pd


@pd.api.extensions.register_dataframe_accessor('prices')
class PricesDataFrameAccessor:
    """Price accessor to `pandas.DataFrame`.
    """

    def __init__(self, df):
        self._validate(df)
        self._df = df.sort_index()

    @staticmethod
    def _validate(df):
        """Validates a `pandas.DataFrame`.

        Checks if DataFrame Index is a DateTime Index and if it is unique.
        Checks if all the prices are positive.
        """
        if not df.index.inferred_type == 'datetime64':
            raise AttributeError('The DataFrame Index must be a DateTime Index.')
        if not df.index.is_unique:
            raise AttributeError('The DataFrame Index cannot have duplicates.')
        if not df.all().all() >= 0:
            raise AttributeError('The DataFrame cannot have negative prices.')
    
    def log_prices(self):
        """Calculates log prices.
        """
        return(self._df.pipe(np.log))
