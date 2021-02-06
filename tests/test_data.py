import random

import pandas as pd


isin_codes = ['DE1234567890', 'IT1234567890', 'US1234567890']


bbg_fields = ['PX_ASK', 'PX_BID', 'PX_LAST']


one_lvl_cols = pd.Index(isin_codes)
two_lvls_cols = pd.MultiIndex.from_arrays([isin_codes, 3 * list(bbg_fields[2])])
two_lvls_multi_flds_cols = pd.MultiIndex.from_arrays([3 * isin_codes, 3 * bbg_fields])


idx = pd.date_range('2021-01-01', '2021-01-15')