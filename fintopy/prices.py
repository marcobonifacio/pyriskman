"""Accessor to `pandas.Series` for historical series of financial prices. 
"""

import numpy as np
import pandas as pd


@pd.api.extensions.register_series_accessor('prices')
class PricesSeriesAccessor:
    """Accessor for historical series of financial prices.
    
    Examples:
    >>> s.prices.set_frequency()
    >>> s.prices.rebase()
    >>> s.prices.log_returns()
    """

    def __init__(self, series: pd.Series) -> None:
        self._validate(series)
        self._series = series.sort_index()

    @staticmethod
    def _validate(series: pd.Series) -> None:
        # Validates the price series.
        if series.index.inferred_type != 'datetime64':
            raise TypeError('The series index must be a DateTimeIndex.')
        if not series.index.is_unique:
            raise ValueError('The series index cannot have duplicates.')
        if not (series > 0).all():
            raise ValueError('The series cannot have negative prices.')
        
    def set_frequency(self, freq: str = 'B', method: str = 'pad') -> pd.Series:
        """Modifies / sets the frequency of the series.

        Args:
            freq: The frequency of the new series. Typical values could be 'B' (Business Day), 'BW' (alias for 'W-FRI', Business Week), 'BM' (Business Month), 'BQ' (Business Quarter), 'BY' (Business Year), Defaults to 'B' (Business Day).
            method: Method fo filling the holes in the reindexed series. Can assume values `None` (fills with NaN), 'pad'/'ffill' (fills with previous value), 'backfill'/'bfill' (fills with next value). Defaults to 'pad'.
            
        Returns:
            pd.Series: A series with a modified frequency.
        """              
        if freq == 'BW':
            freq = 'W-FRI'
        return self._series.asfreq(freq, method)
    
    def rebase(self, base: int = 100) -> pd.Series:
        """Rebases the series.

        Args:
            base: The base for the new series. Defaults to 100.

        Returns:
            pd.Series: The rebased series.
        """
        return self._series.divide(self._series.iloc[0]).multiply(base)
    
    def log_returns(self, period: int = 1, dropna: bool = True) -> pd.Series:
        """Calculates logarithmic returns.

        Args:
            period: The calculation period. Defaults to 1.
            dropna: If True, NAs are dropped. Defaults to True.

        Returns:
            pd.Series: The series of returns.
        """
        if dropna:        
            return self._series.apply(np.log).diff(period).dropna()
        else:
            return self._series.apply(np.log).diff(period)
    
    def pct_returns(self, period: int = 1, dropna: bool = True) -> pd.Series:
        """Calculates percentage returns.

        Args:
            period: The calculation period. Defaults to 1.
            dropna: If True, NAs are dropped. Defaults to True.

        Returns:
            pd.Series: The series of returns.
        """        
        if dropna:
            return self._series.pct_change(period).dropna()
        else:
            return self._series.pct_change(period)
    
    def abs_return(self) -> float:
        """Calculates the absolute return over the series.

        Returns:
            float: The absolute return over the series.
        """        
        return self._series.iat(-1) / self._series.iat(0) - 1
    
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
