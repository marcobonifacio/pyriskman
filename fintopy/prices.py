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
        if not (df > 0).all().all():
            raise AttributeError('The DataFrame cannot have negative prices.')
    
    def log_prices(self):
        """Calculates log prices.
        """
        return(self._df.pipe(np.log))
        
    def rebase(self):
        pass
    
    def log_returns(self):
        pass
    
    def pct_returns(self):
        pass
    
    def abs_return(self):
        pass
    
    def annualized_return(self):
        pass
    
    def periodic_returns(self):
        pass
    
    def cagr(self):
        pass
    
    def drawdown(self):
        pass
    
    def max_drawdown(self):
        pass
    
    def comparison_plot(self):
        pass
    
    def drawdown_plot(self):
        pass
