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

def test_rebase(sample_s):  # Pass
    result = sample_s.prices.rebase(base=200)
    assert pytest.approx(result.iat[1], 0.0001) == 200.192919

