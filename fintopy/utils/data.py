def bloomberg_isins_to_tickers(isins):
    """ 
    Returns a set of ISINs formatted for Bloomberg API requests (e.g. /ISIN/{isin}).
    
    Parameters
    ----------
    isins: listlike, tuple, 1-d array
    
    Returns
    -------
    tickers: set
    """
    return set([f'/ISIN/{isin}' for isin in isins])


def bbg_i2t(isins):
    """
    Convenience shorthand for bloomberg_isin_to_tickers.
    """
    return(bloomberg_isins_to_tickers(isins))
