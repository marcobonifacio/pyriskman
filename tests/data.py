import pandas as pd

# DateTimeIndex
dt_idx = pd.date_range('2021-01-01', periods=5)

# Duplicate index
dupl_idx = pd.to_datetime(['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-03'])

# Numeric index
int_idx = [0, 1, 2, 3, 4]

# Categorical index
cat_idx = ['A', 'B', 'C', 'D', 'E']

# Columns
columns = ['Stock1', 'Stock2']

# Prices data
px_data = [
    [3.45, 7.89],
    [3.42, 7.96],
    [3.18, 7.34],
    [2.76, 6.84],
    [2.91, 6.84]
    ]

# Returns data
ret_data = [
    [0.02, -0.03],
    [0.16, 1.25],
    [-0.35, -1.13],
    [0.89, 0.09],
    [0.15, 0.00],
]