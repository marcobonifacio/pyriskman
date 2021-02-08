import numpy as np
import pandas as pd
import pytest

import fintopy.utils.data as fud
import tests.test_data as td


def test_bbg_i2t():
    isins_seq = td.isin_codes + ['FAKE']
    isins_array = np.asarray(isins_seq)
    isins_series = pd.Series(isins_seq, index=range(len(isins_seq)))

    # test isins as Sequence
    result = fud.bbg_i2t(isins_seq)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # tests isins as ndarray
    result = fud.bbg_i2t(isins_array)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # tests isins as Series
    result = fud.bbg_i2t(isins_series)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890'])
    assert result == expected

    # raises an exception
    with pytest.raises(Exception):
        fud.bbg_i2t('123')


def test_bbg_t2i():
    tickers = ['/ISIN/IT1234567890', '/ISIN/DE1234567890']
    tickers_idx = pd.Index(tickers)

    # tests tickers as Index
    result = fud.bbg_t2i(tickers_idx)
    expected = pd.Index(['IT1234567890', 'DE1234567890'])
    assert result.all() == expected.all()

    # raises an exception
    with pytest.raises(Exception):
        fud.bbg_t2i(tickers)


def test_bloomberg_dropfield():
    idx1 = ['IT1234567890', 'DE1234567890', 'US1234567890']
    idx2 = 3 * ['PX_LAST']
    idx = pd.MultiIndex.from_arrays([idx1, idx2], names=('isin', 'price'))

    # tests MultiIndex
    result = fud.bloomberg_dropfield(idx)
    expected = pd.Index(idx1)
    assert result.all() == expected.all()

    # raises an Exception
    with pytest.raises(Exception):
        fud.bloomberg_dropfield(pd.Index(idx1))


def test_bloomberg_xs():
    col1 = 2 * ['IT1234567890', 'DE1234567890', 'US1234567890']
    col2 = 3 * ['PX_ASK', 'PX_BID']
    col = pd.MultiIndex.from_arrays([col1, col2])
    idx = pd.date_range('2021-01-01', '2021-01-15')
    df = pd.DataFrame(index=idx, columns=col, data=1)
    
    # tests DataFrame
    result = fud.bloomberg_xs(df)
    for r in result:
        r.columns = sorted(r.columns)
    expected = 2 * [pd.DataFrame(index=idx, columns=sorted(set(col1)), data=1)]
    for n in range(len(result)):
        assert result[n].all().all() == expected[n].all().all()

    # raises an Exception (no Multiindex)
    with pytest.raises(Exception):
        fud.bloomberg_xs(pd.DataFrame(index=idx, columns=sorted(set(col1)), data=1))