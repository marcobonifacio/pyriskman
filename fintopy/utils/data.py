from typing import List, Set, Tuple, Union
from numpy import ndarray
from pandas import DataFrame, Index, MultiIndex, Series


def bloomberg_isins_to_tickers(
    isins: Union[List, Tuple, ndarray, Series]
    ) -> Set:
    """Formats isin codes for Bloomberg requests.
    
    Checks the correct length of any element of the sequence and returns a set formatted for Bloomberg requests (e.g. /ISIN/{isin}).

    Args:
        isins: a sequence containing the ISINs to be formatted. 
  
    Returns:
        A set of formatted ISINs.
    
    Raises:
        An exception if the argument is not a sequence, a numpy array or a Pandas Series.
    """
    if isinstance(isins, Series):
        isins = list(isins.values)
    elif isinstance(isins, ndarray):
        isins = list(isins)
    elif isinstance(isins, List) or isinstance(isins, Tuple):
        pass
    else:
        raise Exception('The argument must be a sequence, a numpy array or a Pandas Series.')
    
    for i in isins:
        if len(i) != 12:
            isins.remove(i)
      
    return set([f'/ISIN/{isin}' for isin in isins])
  
  
def bbg_i2t(
    isins: Union[List, Tuple, ndarray, Series]
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
    
    Raises:
        An exception if the argument is not a Pandas Index.
    """
    if isinstance(tickers, Index):
        return Index([ticker[6:] for ticker in tickers])
    else:
        raise Exception('The argument must be a Pandas Index.')
  
  
def bbg_t2i(tickers: Index) -> Index:
    """Convenience shorthand for function `bloomberg_tickers_to_isins`.
    """
    return bloomberg_tickers_to_isins(tickers)


def bloomberg_dropfield(
    columns: MultiIndex) -> Index:
    """Drops the inner level from a Pandas two-level MultiIndex.
    
    Useful for Bloomberg historical request with only one field.
  
    Args:
        columns: A two-level Pandas MultiIndex returned by Bloomberg.
  
    Returns:
        A Pandas Index.
    
    Raises:
        An exception if the argument is not a two-level Pandas MultiIndex.
    """
    if isinstance(columns, MultiIndex) and columns.nlevels == 2:
        return columns.droplevel(1)
    else:
        raise Exception('The argument must be a two-level Pandas MultiIndex.')
    
    
def bloomberg_xs(df: DataFrame) -> List[DataFrame]:
    """Returns a cross-section of a Bloomberg request.

    Args:
        df: a Pandas DataFrame returned by Bloomberg with a two-level MultiIndex as columns.
    
    Returns:
        A list of Pandas Dataframes.

    Raises:
        An exception if the argument is not a Pandas DataFrame nor it has a two-level MultiIndex as columns.
    """
    if isinstance(df, DataFrame) and df.columns.nlevels == 2:
        out = []
        for l in df.columns.levels[1]:
            out.append(df.xs(l, level=1, axis=1))
        return(out)
    else:
        raise Exception('The argument must be a Pandas Dataframe with a two-level MultiIndex as columns.')