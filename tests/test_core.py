import numpy as np
import pandas as pd
import pytest

import fintopy as fin
import tests.data as td


def test_log_prices():
    df = td.px_1lvl_df
    s = td.px_s
    
    # Tests DataFrame
    result = df.pipe(fin.log_prices)
    expected = pd.DataFrame(index=td.idx, columns=td.isin_codes, data=[[np.log(p[0]), np.log(p[2])] for p in td.prices])
    assert result.all().all() == expected.all().all()
    
    # Tests Series
    result = s.pipe(fin.log_prices)
    expected = pd.Series(index=td.idx, data=[np.log(p[0]) for p in td.prices])
    assert result.all() == expected.all()

    # Raises a TypeError
    with pytest.raises(TypeError):
        fin.log_prices(td.prices)


def test_log_returns():
    df = td.px_1lvl_df
    s = td.px_s
    
    # Tests DataFrame of prices
    result = df.pipe(fin.log_returns)
    expected = pd.DataFrame(index=td.idx, columns=td.isin_codes, data=[[np.log(p[0]), np.log(p[2])] for p in td.prices]).diff()
    assert result.all().all() == expected.all().all()
    
    # Tests DataFrame of returns
    result = df.pct_change().pipe(fin.log_returns, kind='R')
    expected = pd.DataFrame(index=td.idx, columns=td.isin_codes, data=[[np.log(p[0]), np.log(p[2])] for p in td.prices]).diff()
    assert result.all().all() == expected.all().all()

    # Raises a TypeError
    with pytest.raises(TypeError):
        fin.log_returns(td.prices)

    # Raises a ValueError
    with pytest.raises(ValueError):
        df.pct_change().pipe(fin.log_returns, kind='Z')