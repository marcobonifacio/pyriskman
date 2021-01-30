from typing import List, Set, Tuple, Union
from numpy import ndarray
from pandas import Series


def bloomberg_isins_to_tickers(
  isins: Union(List, Tuple, ndarray, Series)
  ) -> Set
  """
  Formats isin codes for Bloomberg requests (e.g. /ISIN/{isin}) and checks for the correct length of any element (must be 12).
  
  Parameters
  ----------
  isins: list, tuple, 1-d array, Pandas Series
  
  Returns
  -------
  tickers: set
  """
  if isinstance(isins, Series):
    isins = isins.value
    
  for i in isins:
    if len(i) != 12:
      isins.remove(i)
      
  return set([f'/ISIN/{isin}' for isin in isins])
  
  
  def bbg_i2t(
    isins: Union(List, Tuple, ndarray, Series)
    ) -> Set
    """
    Convenience shorthand for function `bloomberg_isins_to_tickers`
    """
    return bloomberg_isins_to_tickers(isins)