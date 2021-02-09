import numpy as np
import pandas as pd
import pytest

import fintopy as fin
import tests.data as td


def test_isins_to_tickers():
    isins_seq = td.isin_codes + ['FAKE']
    isins_array = np.asarray(isins_seq)
    isins_series = pd.Series(isins_seq, index=range(len(isins_seq)))

    # test isins as Sequence
    result = fin.isins_to_tickers(isins_seq)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # tests isins as ndarray
    result = fin.isins_to_tickers(isins_array)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # tests isins as Series
    result = fin.isins_to_tickers(isins_series)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # raises a NotImplementedError
    with pytest.raises(NotImplementedError):
        fin.isins_to_tickers('123')


def test_tickers_to_isins():
    tickers = ['/ISIN/IT1234567890', '/ISIN/DE1234567890']
    tickers_idx = pd.Index(tickers)

    # tests tickers as Index
    result = fin.tickers_to_isins(tickers_idx)
    expected = pd.Index(['IT1234567890', 'DE1234567890'])
    assert result.all() == expected.all()

    # raises a NotImplementedError
    with pytest.raises(NotImplementedError):
        fin.tickers_to_isins(tickers)


def test_dropfield():
    idx = td.px_2lvls_df.columns

    # tests MultiIndex
    result = fin.dropfield(idx)
    expected = pd.Index(td.isin_codes)
    assert result.all() == expected.all()

    # raises a NotImplementedError
    with pytest.raises(NotImplementedError):
        fin.dropfield(pd.Index(td.isin_codes))


def test_xs_list():
    df = td.px_2lvls_multi_df
    
    # tests DataFrame
    result = df.pipe(fin.xs_list)
    expected = [pd.DataFrame(index=td.idx, columns=td.isin_codes, data=[[p[0], p[2]] for p in td.prices]), pd.DataFrame(index=td.idx, columns=td.isin_codes, data=[[p[1], p[3]] for p in td.prices])]
    for n in range(len(result)):
        assert result[n].all().all() == expected[n].all().all()

    # raises a NotImplementedError
    with pytest.raises(NotImplementedError):
        fin.xs_list(pd.DataFrame(index=td.idx, columns=td.bbg_fields, data=[[p[0], p[1]] for p in td.prices]))