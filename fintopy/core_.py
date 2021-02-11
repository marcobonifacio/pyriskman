from typing import Union
from numpy import log
from pandas import DataFrame, Series


def log_prices(
    prices: Union[DataFrame, Series]
    ) -> Union[DataFrame, Series]:
    """Returns logarithms of prices.

    Args:
        prices: a `Pandas DataFrame` or `Series` of prices.
    
    Returns:
        A `Pandas DataFrame` or `Series` of log prices.

    Raises:
        A `NotImplementedError` if the argument is not a `Pandas DataFrame` or `Series`.
    """
    if isinstance(prices, DataFrame) or isinstance (prices, Series):
        return(prices.pipe(log))
    else:
        raise TypeError(f'The argument must be a Pandas DataFrame or Series, a {type(prices)} was passed.')


def log_returns(
    values: Union[DataFrame, Series],
    kind: str = 'P'
    ) -> Union[DataFrame, Series]:
    """Calculates log returns.

    Args:
        values: a `Pandas DataFrame` or `Series` of prices.
        kind: a string, must be P (default) if `values` are prices or R if they are percent returns. 
    
    Returns:
        A `Pandas DataFrame` or `Series` of log returns.

    Raises:
        A `TypeError` if the argument `values` is not a `Pandas DataFrame` or `Series`.
        A `ValueError` if the argument `kind` is not P or R. 
    """
    if isinstance(values, DataFrame) or isinstance(values, Series):
        if kind == 'P':
            return(values.pipe(log).diff())
        elif kind == 'R':
            return(values.add(1).pipe(log))
        else:
            raise ValueError(f'The kind argument must be P for prices or R for percent returns, instead {kind} was passed.')
    else:
        raise TypeError(f'The values argument must be a Pandas DataFrame or Series, a {type(values)} was passed.')