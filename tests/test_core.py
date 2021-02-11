import pandas as pd
import pytest

from fintopy import TimeSeries

@pytest.fixture()
def sample_df():
    return pd.read_csv('sample_px.csv')


def test_timeseries(sample_df):
    ts = TimeSeries(sample_df)
    assert type(ts) == TimeSeries
    assert type(ts._df) == pd.DataFrame
