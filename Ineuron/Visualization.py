# a data scientist will not use a dashboarding tool every time, so will use below libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from numpy.random import randn, randint, uniform, sample
pd.DataFrame(randn(1000))
# changing date as indexes for 1000 records
df = pd.DataFrame(randn(1000), index=pd.date_range('2019-06-07', periods=1000), columns=['value'])
df
ts = pd.Series(randn(1000), index=pd.date_range('2019-06-07', periods=1000))
ts
# draw a graph

df.plot()  # x axis- indexes and y axis- values. by default line graph/plot.

# iris is an open source dataset and has data about flower. can be downloaded from google or
# use it from seaborn library where its already available

iris = sns.load_dataset('iris')
iris  # it has 4 columns along with a label column or class field named species
ax = iris.plot(figsize=(15, 8), title='iris dataset')  # figsize is the window size of the graph
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

df = iris.drop(['species'], axis=1)  # dropping a column from dataset
df
df.iloc[0]  # extracting 0th row
df.iloc[0].plot(kind='bar')  # bar graph, indexes in x axis and value in y axis

titanic = sns.load_dataset('titanic')
titanic.head()
titanic['pclass'].plot(kind='bar')  # bar graph against pclass series

df = pd.DataFrame(randn(10, 4), columns=['a', 'b', 'c', 'd'])
df.head(10)
df.plot.bar()  # another way to get bar graph from dataframe
df.plot.barh()  # bar graph horizontal

iris.head()
iris['sepal_length'].plot.hist()  # histogram- show data in bars
# and each bar groups numbers into ranges and shows frequency.

iris.plot.hist()  # histogram for entire data set where we are seeing some overlap in data
# to avoid the overlap, we use stacked option
iris.plot(kind='hist', stacked=True)

iris
iris.plot.scatter(x='sepal_length', y='petal_length')  # scatter plot or graph
iris.plot.scatter(x='sepal_length', y='petal_length', c='sepal_width')
# c stands for color that color code is based on value.
df = iris
df.plot.scatter(x='sepal_length', y='petal_length', label='length')
# combining multiple graphs
ax = df.plot.scatter(x='sepal_length', y='petal_length', label='length')
df.plot.scatter(x='sepal_width', y='petal_width', label='width', ax=ax, color='r')

df.plot.hexbin(x='sepal_width', y='petal_width', gridsize=5, label='width', color='r')
# giving hexagonal shaped instead of circle

df = iris.drop(['species'], axis=1)
d = df.iloc[0]
d
d.plot.pie(figsize=(10, 10))  # pie chart where summing of total value of that row
# and then percentage of each columns

d = df.head(3).T  # Transpose the first 3 rows
d
d.plot.pie(subplots=True, figsize=(15, 15))  # for each column it will create a pie plot
d.plot.pie(subplots=True, figsize=(20, 20), fontsize=20, autopct='%.2f')  # autopct will show percentage

# scatter matrix to show every relationship to every columns and columns are normalized or not
from pandas.plotting import scatter_matrix
df
scatter_matrix(df, figsize=(8, 8), color='r')  # by default the diagonal matrix will be histogram
# here diagonal axis has the data comnication with same data. for e.g. sepal length with sepal length.
# the curve or data pattern should be like bell curve to be normalized perfectly.

scatter_matrix(df, figsize=(8, 8), color='r', diagonal='kde')
# diagonal changed to kde(kernel density estimation) from hist

df.plot(subplots=True)
df.plot(subplots=True, sharex=False, layout=(2, 3), figsize=(16, 8))
plt.tight_layout()

# plotly and cufflinks
from plotly.offline import iplot
import plotly as py
import plotly.tools as tls
import cufflinks as cf
from pylab import *

py.offline.init_notebook_mode(connected=True)
print(py.__version__)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
df.head()
df.iplot()  # interactive mode, with hovering mouse will see the values

plot(df)
show()
ion()
plot(df)

df.iplot(x='A', y='B', mode='markers', size=25)
