import numpy as np
import pandas as pd
import pytest

import fintopy.utils.data as fud


def test_bbg_i2t():
    isins_seq = ['IT1234567890', 'DE1234567890', 'US1234567890', 'FAKE']
    isins_array = np.asarray(isins_seq)
    isins_series = pd.Series(isins_seq, index=range(len(isins_seq)))

    # test isins as Sequence
    result = fud.bbg_i2t(isins_seq)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890',
     '/ISIN/US1234567890'])
    assert result == expected

    # test isins as ndarray
    result = fud.bbg_i2t(isins_array)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890',
     '/ISIN/US1234567890'])
    assert result == expected

    # test isins as Series
    result = fud.bbg_i2t(isins_series)
    expected = set(['/ISIN/IT1234567890', '/ISIN/DE1234567890',
     '/ISIN/US1234567890'])
    assert result == expected

    # raises an exception
    with pytest.raises(Exception):
        fud.bbg_i2t('123')


def test_bbg_t2i():
    tickers = ['/ISIN/IT1234567890', '/ISIN/DE1234567890',
     '/ISIN/US1234567890']
    tickers_idx = pd.Index(tickers)

    # test tickers as Index
    result = fud.bbg_t2i(tickers_idx)
    expected = pd.Index(['IT1234567890', 'DE1234567890', 'US1234567890'])
    assert result.all() == expected.all()

    # raises an exception
    with pytest.raises(Exception):
        fud.bbg_t2i(tickers)


def test_bloomberg_dropfield():
    idx1 = ['IT1234567890', 'DE1234567890', 'US1234567890']
    idx2 = 3 * ['PX_LAST']
    idx = pd.MultiIndex.from_arrays([idx1, idx2], names=('isin', 'price'))

    # test MultiIndex
    result = fud.bloomberg_dropfield(idx)
    expected = pd.Index(idx1)
    assert result.all() == expected.all()

    # raises an Exception
    with pytest.raises(Exception):
        fud.bloomberg_dropfield(pd.Index(idx1))