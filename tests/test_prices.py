import pandas as pd
import pytest
from xbbg import blp

import fintopy


@pytest.fixture
def sample_s():
    s = blp.bdh('MSFT US Equity', 'PX_LAST', '2020-06-30', '2021-01-31')
    s.columns = s.columns.droplevel(1)
    s = s.iloc[:, 0]
    return(s)


def test_prices_series_accessor(sample_s):
    # Test validate series - Fail, negative values
    with pytest.raises(ValueError):
        negative_s = sample_s.multiply(-1)
        negative_s.prices.set_frequency()
    # Test validate series - Fail, not datetime index
    with pytest.raises(TypeError):
        int_index_s = sample_s.reindex(range(len(sample_s)))
        int_index_s.prices.set_frequency()    
    # Test validate series - Fail, duplicate index
    with pytest.raises(ValueError):
        dupl_idx = pd.Index([x for x in sample_s.index[:5]] + 
                            [x for x in sample_s.index[:-5]])
        dupl_idx_s = sample_s.reindex(dupl_idx)
        dupl_idx_s.prices.set_frequency()
    # Test set_frequency - Pass
    bweekly = sample_s.prices.set_frequency(freq='BW')
    assert bweekly.index[2] == pd.Timestamp('2020-07-17')
    # Test rebase - Pass
    rebased = sample_s.prices.rebase()
    assert pytest.approx(rebased.iat[1], 0.0001) == 100.584733
    # Test log_returns - Pass
    lrdaily = sample_s.prices.set_frequency().prices.log_returns()
    assert pytest.approx(lrdaily.iat[3], 0.0001) == 0
    # Test pct_returns - Pass
    prweekly = sample_s.prices.set_frequency('BW').prices.pct_returns()
    assert pytest.approx(prweekly.iat[3], 0.0001) == -0.007788
    # Test abs_return - Pass
    assert pytest.approx(sample_s.prices.abs_return(), 0.0001) == 0.145543
    # Test annualized_return - Pass
    assert pytest.approx(sample_s.prices.annualized_return(), 
                         0.0001) == 0.249405
    # Test cagr - Pass
    assert pytest.approx(sample_s.prices.cagr(), 0.0001) == 0.262185
    # Test drawdown - Pass
    dd = sample_s.prices.set_frequency().prices.drawdown(negative=True)
    assert pytest.approx(dd.iat[8], 0.0001) == -0.003033
    # Test max_drawdown - Pass
    maxdd = sample_s.prices.max_drawdown()
    assert pytest.approx(maxdd, 0.0001) == 0.134945
