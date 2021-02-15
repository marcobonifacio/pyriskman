import pandas as pd
import pytest

import fintopy
import tests.data as td


@pytest.fixture
def px_series():
    return pd.Series(index=td.dt_idx, data=[p[0] for p in td.px_data])

@pytest.fixture
def ret_series():
    return pd.Series(index=td.dt_idx, data=[r[0] for r in td.ret_data])

@pytest.fixture
def num_series():
    return pd.Series(index=td.int_idx, data=[p[0] for p in td.px_data])

@pytest.fixture
def dupl_series():
    return pd.Series(index=td.dupl_idx, data=[p[0] for p in td.px_data])


def test_validate1(ret_series):  # Fail, negative prices
    with pytest.raises(ValueError):
        ret_series.prices.rebase()

def test_validate2(num_series):  # Fail, not datetime index
    with pytest.raises(TypeError):
        num_series.prices.rebase()

def test_validate3(dupl_series):  # Fail, duplicate index
    with pytest.raises(ValueError):
        dupl_series.prices.rebase()

def test_rebase(px_series):  # Pass
    data = [100 * p[0] for p in td.px_data]
    result = px_series.prices.rebase(base=345)
    expected = pd.Series(index=px_series.index, data=data)
    pd.testing.assert_series_equal(result, expected)

