import pandas as pd


isin_codes = ['DE1234567890', 'IT1234567890']


bbg_fields = ['PX_ASK', 'PX_BID']


multi_flds_cols = pd.MultiIndex.from_product([isin_codes, bbg_fields])


idx = pd.date_range('2021-01-01', '2021-01-05')


prices = [
    [6.20, 6.30, 9.18, 9.35],
    [6.05, 6.12, 9.23, 9.37],
    [6.12, 6.18, 9.45, 9.54],
    [5.89, 5.94, 9.36, 9.39],
    [6.01, 6.08, 9.57, 9.63]
    ]


px_2lvls_multi_df = pd.DataFrame(index=idx, columns=multi_flds_cols, data=prices)
px_2lvls_df = px_2lvls_multi_df.loc(axis=1)[:, ['PX_ASK']]
px_1lvl_df = px_2lvls_multi_df.xs('PX_ASK', level=1, axis=1)