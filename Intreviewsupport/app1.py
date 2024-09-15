import pandas as pd
 
# Creating 2 pandas Series
ps1 = pd.Series([2, 4, 8, 20, 10, 47, 99])
ps2 = pd.Series([1, 3, 6, 4, 10, 99, 50])
 
print("Series 1:")
print(ps1)
print("nSeries 2:")
print(ps2)
 
# Using Bitwise NOT operator along
# with pandas.isin()
print("nItems of Series 1 not present in Series 2:")
res = ps1[~ps1.isin(ps2)]
print(res)
