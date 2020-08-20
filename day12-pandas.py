# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  8 11:31:28 2020

# @author: kudevara
# """
# # mixed datatypes effective handling
# # [0] [1] - unlike this we can do customized indexing
# # handling missing data
# # In-consistant / unstructured data - effective handling
# # data processed via pandas will help in => to load DB / Data analysis sw fwd
# # time & non-time based data hadling
# # Pandas (1) Series is 1-dim (2) DataFrame is n-dim
# # dictionary's keys can be used as indices


# import pandas as pd
# import numpy as np

# # gd = pd.Series([87,100,97])
# # print(gd)

# # print(pd.Series(98.6, range(3)))

# # gd = pd.Series([87,100,98], index=['A', 'B', 'C']) 
# # # make sure index is immutable
# # # same no. of values

# # hw = pd.Series(['And', 'Ball', 'Cat'])
# # hw.str.contains('a')


# # 5  random gen 60 - 100 temp
# # arr -> series 
# # find avg / min / max
# # descriptive stats

# # temps = np.random.randint(60, 100, 5)
# # temperatures = pd.Series(temps)

# # print(temperatures.min())
# # print(temperatures.max())
# # print(temperatures.mean())
# # print(temperatures.describe())


# # for multi Dim => use DataFrame
# # custome row / col indices 
# # each col in DataFrame is a Series
# # multiple datatypes in a col

# gd_dict = {
#         'Ram' : [100,99,98],
#         'Raheem' : [97,96,95],
#         'Raavan' : [94,93,92],
#         'Curian' : [91,90,89],
#         'Sam' : [88, 87, 86]
#     }

# gd = pd.DataFrame(gd_dict)

# gd.index=['T1', 'T2', 'T3']



# gd = pd.Series([87,100,98], index=['A', 'B', 'C'])

# gd
# Out[9]: 
# A     87
# B    100
# C     98
# dtype: int64

# gd = pd.Series([87,100,98], index=['A', 'B', 'C', 'D'])
# Traceback (most recent call last):

#   File "<ipython-input-10-8e0e11364aae>", line 1, in <module>
#     gd = pd.Series([87,100,98], index=['A', 'B', 'C', 'D'])

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/series.py", line 292, in __init__
#     f"Length of passed values is {len(data)}, "

# ValueError: Length of passed values is 3, index implies 4.


# gd
# Out[11]: 
# A     87
# B    100
# C     98
# dtype: int64







# gd['B']
# Out[12]: 100

# gd.B
# Out[13]: 100

# gd.key
# Traceback (most recent call last):

#   File "<ipython-input-14-ca88fb8b6444>", line 1, in <module>
#     gd.key

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 5274, in __getattr__
#     return object.__getattribute__(self, name)

# AttributeError: 'Series' object has no attribute 'key'


# gd.values
# Out[15]: array([ 87, 100,  98])

# gd.keys
# Out[16]: 
# <bound method Series.keys of A     87
# B    100
# C     98
# dtype: int64>













# hw = pd.Series('And', 'Ball', 'Cat')
# Traceback (most recent call last):

#   File "<ipython-input-17-3ce0c83159bf>", line 1, in <module>
#     hw = pd.Series('And', 'Ball', 'Cat')

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/series.py", line 215, in __init__
#     index = ensure_index(index)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 5358, in ensure_index
#     return Index(index_like)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 422, in __new__
#     raise cls._scalar_data_error(data)

# TypeError: Index(...) must be called with a collection of some kind, 'Ball' was passed


# hw = pd.Series(['And', 'Ball', 'Cat'])

# hw
# Out[19]: 
# 0     And
# 1    Ball
# 2     Cat
# dtype: object

# hw.str.contains('a')
# Out[20]: 
# 0    False
# 1     True
# 2     True
# dtype: bool

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')

# temps
# Out[22]: array([90, 61, 98, 92, 73])

# temperatures
# Out[23]: 
# 0    90
# 1    61
# 2    98
# 3    92
# 4    73
# dtype: int64

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')
# 67
# 93
# 79.4

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')
# 65
# 95
# 82.0
# count     5.000000
# mean     82.000000
# std      12.186058
# min      65.000000
# 25%      76.000000
# 50%      82.000000
# 75%      92.000000
# max      95.000000
# dtype: float64

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')

# gd_dict
# Out[27]: 
# {'Ram': [100, 99, 98],
#  'Raheem': [97, 96, 95],
#  'Raavan': [94, 93, 92],
#  'Curian': [91, 90, 89],
#  'Sam': [88, 87, 86]}

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')

# gd
# Out[29]: 
#    Ram  Raheem  Raavan  Curian  Sam
# 0  100      97      94      91   88
# 1   99      96      93      90   87
# 2   98      95      92      89   86

# gd['Raheem']
# Out[30]: 
# 0    97
# 1    96
# 2    95
# Name: Raheem, dtype: int64

# gd.Raheem
# Out[31]: 
# 0    97
# 1    96
# 2    95
# Name: Raheem, dtype: int64

# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')
# Traceback (most recent call last):

#   File "/Users/kudevara/Desktop/python-tutoring/day12-pandas.py", line 63, in <module>
#     gd.index('T1', 'T2', 'T3')

# TypeError: 'RangeIndex' object is not callable


# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')
# Traceback (most recent call last):

#   File "/Users/kudevara/Desktop/python-tutoring/day12-pandas.py", line 63, in <module>
#     gd.index['T1', 'T2', 'T3']

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 708, in __getitem__
#     return super().__getitem__(key)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 3941, in __getitem__
#     result = getitem(key)

# IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices


# runfile('/Users/kudevara/Desktop/python-tutoring/day12-pandas.py', wdir='/Users/kudevara/Desktop/python-tutoring')

# gd
# Out[35]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T2   99      96      93      90   87
# T3   98      95      92      89   86

# gd.T1
# Traceback (most recent call last):

#   File "<ipython-input-36-1520a9024939>", line 1, in <module>
#     gd.T1

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 5274, in __getattr__
#     return object.__getattribute__(self, name)

# AttributeError: 'DataFrame' object has no attribute 'T1'


# gd('T1')
# Traceback (most recent call last):

#   File "<ipython-input-37-0faabacb39d0>", line 1, in <module>
#     gd('T1')

# TypeError: 'DataFrame' object is not callable


# gd.('T1')
#   File "<ipython-input-38-e03a13ebef72>", line 1
#     gd.('T1')
#        ^
# SyntaxError: invalid syntax


# gd.loc('T1')
# Traceback (most recent call last):

#   File "<ipython-input-39-8be1195f3672>", line 1, in <module>
#     gd.loc('T1')

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py", line 577, in __call__
#     axis = self.obj._get_axis_number(axis)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 407, in _get_axis_number
#     raise ValueError(f"No axis named {axis} for object type {cls}")

# ValueError: No axis named T1 for object type <class 'pandas.core.frame.DataFrame'>


# gd.loc['T1']
# Out[40]: 
# Ram       100
# Raheem     97
# Raavan     94
# Curian     91
# Sam        88
# Name: T1, dtype: int64

# gd.loc['T1':'T2']
# Out[41]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T2   99      96      93      90   87

# gd.iloc[0:2]
# Out[42]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T2   99      96      93      90   87

# gd.iloc[0:2]
# Out[43]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T2   99      96      93      90   87

# gd.iloc[['T1', 'T3']]
# Traceback (most recent call last):

#   File "<ipython-input-44-a1fdae59465b>", line 1, in <module>
#     gd.iloc[['T1', 'T3']]

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py", line 1767, in __getitem__
#     return self._getitem_axis(maybe_callable, axis=axis)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py", line 2128, in _getitem_axis
#     return self._get_list_axis(key, axis=axis)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py", line 2110, in _get_list_axis
#     return self.obj._take_with_is_copy(key, axis=axis)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 3409, in _take_with_is_copy
#     result = self.take(indices=indices, axis=axis, **kwargs)

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py", line 3395, in take
#     indices, axis=self._get_block_manager_axis(axis), verify=True

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/pandas/core/internals/managers.py", line 1381, in take
#     else np.asanyarray(indexer, dtype="int64")

#   File "/Users/kudevara/opt/anaconda3/lib/python3.7/site-packages/numpy/core/_asarray.py", line 138, in asanyarray
#     return array(a, dtype, copy=False, order=order, subok=True)

# ValueError: invalid literal for int() with base 10: 'T1'


# gd.loc[['T1', 'T3']]
# Out[45]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T3   98      95      92      89   86

# gd.iloc[[0,2]]
# Out[46]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T3   98      95      92      89   86

# gd.loc['T1':'T2', ['Ram', 'Raheem']]
# Out[47]: 
#     Ram  Raheem
# T1  100      97
# T2   99      96

# gd.iloc[[0:2],[2, 4]]
#   File "<ipython-input-48-d639cd2d8394>", line 1
#     gd.iloc[[0:2],[2, 4]]
#               ^
# SyntaxError: invalid syntax


# gd.iloc[[0,2],[2, 4]]
# Out[49]: 
#     Raavan  Sam
# T1      94   88
# T3      92   86

# gd.iloc[[0,2],0:3]
# Out[50]: 
#     Ram  Raheem  Raavan
# T1  100      97      94
# T3   98      95      92

# gd.iloc[[0,2],:]
# Out[51]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94      91   88
# T3   98      95      92      89   86

# gd.iloc[0:2,0:3]
# Out[52]: 
#     Ram  Raheem  Raavan
# T1  100      97      94
# T2   99      96      93

# gd.iloc[:,0:3]
# Out[53]: 
#     Ram  Raheem  Raavan
# T1  100      97      94
# T2   99      96      93
# T3   98      95      92

# gd[gd > = 90]
#   File "<ipython-input-54-5f9970c0a92e>", line 1
#     gd[gd > = 90]
#             ^
# SyntaxError: invalid syntax


# gd[gd >= 90]
# Out[55]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94    91.0  NaN
# T2   99      96      93    90.0  NaN
# T3   98      95      92     NaN  NaN

# gd[gd < 90]
# Out[56]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  NaN     NaN     NaN     NaN   88
# T2  NaN     NaN     NaN     NaN   87
# T3  NaN     NaN     NaN    89.0   86

# gd[(gd>=80) & (gd > 90)]
# Out[57]: 
#     Ram  Raheem  Raavan  Curian  Sam
# T1  100      97      94    91.0  NaN
# T2   99      96      93     NaN  NaN
# T3   98      95      92     NaN  NaN

import pandas as pd


# gd_dict = {
#         'Ram' : [100,99,98],
#         'Raheem' : [97,96,95],
#         'Raavan' : [94,93,92],
#         'Raavan' : [94,93,92],
#         'Curian' : [91,90,89],
#         'Sam' : [88, 87, 86],
#         'Sam' : [88, 87, 86]
#     }

# gd = pd.DataFrame(gd_dict)

temp = {
        'Mon' : [88, 89],
        'Tue' : [78,65],
        'Wed' : [77,89],
        'Thr' : [67,65],
        'Fri' : [78,87]
        
        }
temperature = pd.DataFrame(temp, ['Low', 'High'])














