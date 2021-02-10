from typing import List, Set, Tuple, Union
from numpy import ndarray
from pandas import DataFrame, Index, MultiIndex, Series


def isins_to_tickers(
    isins: Union[List, Tuple, ndarray, Series]
    ) -> Set:
    """Formats isin codes for Bloomberg requests.
    
    Checks the correct length of any element of the sequence and returns a set formatted for Bloomberg requests (e.g. /ISIN/{isin}).

    Args:
        isins: a sequence containing the ISINs to be formatted. 
  
    Returns:
        A set of formatted ISINs.
    
    Raises:
        A `TypeError` if the argument is not a sequence, a `numpy array` or a `Pandas Series`.
    """
    if isinstance(isins, Series):
        isins = list(isins.values)
    elif isinstance(isins, ndarray):
        isins = list(isins)
    elif isinstance(isins, List) or isinstance(isins, Tuple):
        pass
    else:
        raise TypeError(f'The argument must be a sequence, a numpy array or a Pandas Series, a {type(isins)} was passed.')
    
    for i in isins:
        if len(i) != 12:
            isins.remove(i)
      
    return set([f'/ISIN/{isin}' for isin in isins])
  
  
def tickers_to_isins(tickers: Index) -> Index:
    """Deletes Bloomberg request format from ISIN codes.
    
    Args:
        tickers: A `Pandas Index` (index or columns) returned by Bloomberg.
  
    Returns:
        An unformatted `Pandas Index`.
    
    Raises:
        A `TypeError` if the argument is not a `Pandas Index`.
    """
    if isinstance(tickers, Index):
        return Index([ticker[6:] for ticker in tickers])
    else:
        raise TypeError(f'The argument must be a Pandas Index, a {type(tickers)} was passed.')
  
  
def dropfield(columns: MultiIndex) -> Index:
    """Drops the inner level from a two-level `Pandas MultiIndex`.
    
    Useful to flatten columns of Bloomberg historical request with only one field.
  
    Args:
        columns: A two-level `Pandas MultiIndex` returned by Bloomberg.
  
    Returns:
        A `Pandas Index`.
    
    Raises:
        A `TypeError` if the argument is not a two-level `Pandas MultiIndex`.
    """
    if isinstance(columns, MultiIndex) and columns.nlevels == 2:
        return columns.droplevel(1)
    else:
        raise TypeError(f'The argument must be a two-level Pandas MultiIndex, a {type(columns)} was passed.')
    
    
def xs_list(df: DataFrame) -> List[DataFrame]:
    """Returns a cross-section of a Bloomberg request.

    Args:
        df: a `Pandas DataFrame` returned by Bloomberg with a two-level `MultiIndex` as columns.
    
    Returns:
        A list of `Pandas DataFrames`.

    Raises:
        A `TypeError` if the argument is not a `Pandas DataFrame` nor it has a two-level `MultiIndex` as columns.
    """
    if isinstance(df, DataFrame) and df.columns.nlevels == 2:
        out = []
        for l in df.columns.levels[1]:
            out.append(df.xs(l, level=1, axis=1))
        return(out)
    else:
        raise TypeError('The argument must be a Pandas Dataframe with a two-level MultiIndex as columns.')