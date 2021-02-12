import numpy as np
import pandas as pd
import pytest

import fintopy as fin
import tests.data as td


@pytest.fixture
def px_df():
    return pd.DataFrame(index=td.dt_idx, columns=td.columns, data=td.px_data)

@pytest.fixture
def ret_df():
    return pd.DataFrame(index=td.dt_idx, columns=td.columns, data=td.ret_data)

@pytest.fixture
def num_df():
    return pd.DataFrame(index=td.int_idx, columns=td.columns, data=td.px_data)

@pytest.fixture
def dupl_df():
    return pd.DataFrame(index=td.dupl_idx, columns=td.columns, data=td.px_data)


def test_log_prices1(px_df):  # Pass
    logdata = np.log(px_df.to_numpy())
    result = px_df.prices.log_prices()
    expected = pd.DataFrame(index=px_df.index, columns=px_df.columns, data=logdata)
    pd.testing.assert_frame_equal(result, expected)

def test_log_prices2(ret_df):  # Fail, negative prices
    with pytest.raises(AttributeError):
        ret_df.prices.log_prices()

def test_log_prices3(num_df):  # Fail, not datetime index
    with pytest.raises(AttributeError):
        num_df.prices.log_prices()

def test_log_prices4(dupl_df):  # Fail, duplicate index
    with pytest.raises(AttributeError):
        dupl_df.prices.log_prices()