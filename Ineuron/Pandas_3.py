import pandas as pd
import numpy as np
from pathlib import Path

my_path = Path('C:\\Users\\proy\\OneDrive - Tractor Supply Co\\PRAT_TSC\\MISC\\PYTHON'
               '\\Krish_Naik\\materials\\files\\')
print(my_path)

from numpy.random import randn as rn  # function generate random data
# numpy only understand array or matrix
print(rn(5, 4))

np.random.seed(100)  # by setting seed, for same seed , it will generate same set of random data
r = rn(5, 4)
print(r)

pd.DataFrame(r)  # convert matrix to dataframe

# passing list variable as row and column names

row = ['a', 'b', 'c', 'd', 'e']
column = ['p', 'q', 'r', 's']

pd.DataFrame(r, index=row, columns=column)

df = pd.DataFrame(r, index=row, columns=column)
df[['p']]

df['new'] = df['p'] + df['s']
df
df.drop('p')  # not found in Axis, by default axis = 0
df.drop('a')
df  # again row a will be back
df.drop('a', inplace=True)  # permanently delete row a from dataframe
df

df = df.drop('a')  # my overriding dataframe also we can remove the row a

df.drop('p', axis=1, inplace=True)  # axis 1 means column, axis 0 for row
df

df.loc[['c', 'b']]  # always work on named indexes

df.iloc[[1]]  # integer location: always work on default indexes

# accessing data from an intersection
df.loc[['b', 'c'], ['r']]
df.loc[['b', 'c'], ['r', 's']]

df
df.iloc[[2, 3], [2, 3]]

# using range
df.iloc[0: 3, :]  # will pull 0,1,2 th rows and all columns
df.iloc[::2, 1:3]  # start from 0 till row 1 and columns 1 and 2

# we can have duplicate name in indexes

df.ix[[0]]  # it will understand both default or named indexes
df.ix[::2, ['s']]  # passing default as well as named index

df[df > 1]  # condition on entire data frame

# row and column level filter operation
df.loc[['b','c']] > 0  # boolean result
df[df.loc[['b','c']] > 0]  # actual data result

df[df['r'] > 0]  # apply filter on column level rather the dataframe
df[(df['r'] > 0) & (df['s'] < 0)]
df
df.reset_index(drop=True)  # this will reset all the indexes

l = 'm n o p q'

df[x] = l.split()
