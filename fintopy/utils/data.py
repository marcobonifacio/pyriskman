from typing import List, Set, Tuple, Union
from numpy import ndarray
from pandas import DataFrame, Index, MultiIndex, Series


def bloomberg_isins_to_tickers(
    isins: Union(List, Tuple, ndarray, Series)
    ) -> Set:
    """Formats isin codes for Bloomberg requests.
    
    Checks the correct length of any element of the sequence and returns a set formatted for Bloomberg requests (e.g. /ISIN/{isin}).

    Args:
        isins: a sequence containing the ISINs to be formatted. 
  
    Returns:
        A set of formatted ISINs.
    """
    if isinstance(isins, Series):
        isins = isins.value
    
    for i in isins:
        if len(i) != 12:
            isins.remove(i)
      
    return set([f'/ISIN/{isin}' for isin in isins])
  
  
def bbg_i2t(
    isins: Union(List, Tuple, ndarray, Series)
    ) -> Set:
    """Convenience shorthand for function `bloomberg_isins_to_tickers`.
    """
    return bloomberg_isins_to_tickers(isins)
    
    
def bloomberg_tickers_to_isins(
    tickers: Index) -> Index:
    """Deletes Bloomberg request format from ISIN codes.
    
    Args:
        tickers: A Pandas Index (index or columns) returned by Bloomberg.
  
    Returns:
        An unformatted Pandas Index. 
    """
    return Index([ticker[6:] for ticker in tickers])
  
  
def bbg_t2i(tickers: Index) -> Index:
    """Convenience shorthand for function `bloomberg_tickers_to_isins`.
    """
    return bloomberg_tickers_to_isins(tickers)


def bloomberg_dropfield(
    columns: MultiIndex) -> Index:
    """Drops the inner level from a Pandas two-level MultiIndex.
    
    Useful for Bloomberg historical request with only one field.
  
    Args:
        columns: A Pandas two-level MultiIndex returned by Bloomberg.
  
    Returns:
        A Pandas Index
    """
    return columns.droplevel[1]