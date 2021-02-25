import pandas as pd
import pytest
from xbbg import blp

import fintopy


@pytest.fixture
def sample_s():
    s = blp.bdh('MSFT US Equity', 'PX_LAST', '2021-01-01', '2021-01-31')
    s.columns = s.columns.droplevel(1)
    s = s.iloc[:, 0]
    return(s)


def test_validate1(sample_s):  # Fail, negative prices
    with pytest.raises(ValueError):
        sample_s = sample_s.multiply(-1) 
        sample_s.prices.rebase()

def test_validate2(sample_s):  # Fail, not datetime index
    with pytest.raises(TypeError):
        sample_s = sample_s.reindex(range(len(sample_s)))
        sample_s.prices.rebase()

def test_validate3(sample_s):  # Fail, duplicate index
    with pytest.raises(ValueError):
        idx = pd.Index([x for x in sample_s.index[:5]] + 
                       [x for x in sample_s.index[:-5]])
        sample_s = sample_s.reindex(idx)
        sample_s.prices.rebase()

def test_set_frequency(sample_s):  # Pass
    result = sample_s.prices.set_frequency(freq='BW')
    assert result.index[2] == pd.Timestamp('2021-01-22')

def test_rebase(sample_s):  # Pass
    result = sample_s.prices.rebase(base=200)
    assert pytest.approx(result.iat[1], 0.0001) == 200.1929

def test_log_returns(sample_s):  # Pass
    result = sample_s.prices.log_returns()
    assert pytest.approx(result.iat[3], 0.0001) == 0.006074

def test_pct_returns(sample_s):  # Pass
    result = sample_s.prices.pct_returns()
    assert pytest.approx(result.iat[3], 0.0001) == 0.006093

def test_abs_return(sample_s):  # Pass
    result = sample_s.prices.abs_return()
    assert pytest.approx(result, 0.0001) == 0.065552

def test_annualized_return(sample_s):  # Pass
    result = sample_s.prices.annualized_return()
    assert pytest.approx(result, 0.0001) == 0.957057

def test_cagr(sample_s):  # Pass
    result = sample_s.prices.cagr()
    assert pytest.approx(result, 0.0001) == 1.526906

def test_drawdown(sample_s):  # Pass
    result = sample_s.prices.drawdown()
    print(result)
    assert pytest.approx(result.iat[8], 0.0001) == 0.030052

def test_max_drawdown(sample_s):  # Pass
    result = sample_s.prices.max_drawdown()
    print(result)
    assert pytest.approx(result, 0.0001) == 0.031736