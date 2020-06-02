import pandas as pd
import numpy as np
from pathlib import Path
import csv
import json

print(pd.date_range('05/20/2020', periods=7, freq='M'))
d = pd.date_range('05/20/2020', periods=7, freq='Y')

np.arange(7)  # it can take floating value also where range cant.
pd.Series(np.arange(2, 9))

#  create/assign ur own index using date_range. index should be equal to number of data.
pd.Series(np.arange(2, 9), index=d)
pd.Series(np.arange(2, 9), index=[3, 4, 5, 6, 'a', 'b', 3.0])  # pass list as index

s = pd.Series([1, 2, 3, 'a'], index=[3, 4, 5, 6])
print(s[4])  # pass list as index

my_path = Path('C:\\Users\\proy\\OneDrive - Tractor Supply Co\\PRAT_TSC\\MISC\\PYTHON\\Krish_Naik\\materials\\files\\')
my_file = open(my_path/'ex7.csv', 'r')
my_open_file = csv.reader(my_file)

with open(my_path/'ex7.csv') as f:
    lines = list(csv.reader(f))

lines

for i in my_open_file:
    print(i)

#  need to check zip method

#  json data

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"],"key1" :[1,2,34]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
j = json.loads(obj)
print(type(j))
j['siblings']
# converting json subset data to dataframe using pandas
pd.DataFrame(j['siblings'])
pd.DataFrame(j['siblings'], columns=['name', 'pets'])

# now there is a list in pets field. how you can separate using apply function

# create a json from dataframe
d = pd.DataFrame(j['siblings'], columns=['name', 'pets'])
d.to_json(my_path/"ss.json")  # will be created with column indexes

d.to_json(my_path/"ss.json", orient='records')  # will remove column indexes

# read data from APIs

import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
r = requests.get(url)
u = r.json()

titanic_train = pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/ff414a1bcfcba32481e4d"
                            "4e8db578e55872a2ca1/titanic.csv", sep='\t')

titanic_train.dtypes
list(titanic_train.index)
type(titanic_train.Name)  # selecting a column and type
type(titanic_train['Name'])  # selecting a column other way

titanic_train.describe()  # by default will show only integer columns

#  to get the describe of object data types

titanic_train.dtypes == 'object'

type(titanic_train.dtypes)  # series type so to filter out the object types only, do below:
titanic_train.dtypes[titanic_train.dtypes == 'object']  # accessing dtype as object from the series

i = titanic_train.dtypes[titanic_train.dtypes == 'object'].index
titanic_train[i].describe()  # here we are getting describe of object columns only

# accessing rows from
l = ['a', 'b', 'c']
l1 = [1, 2, 3, 4]
d = {'a': 1, 'b': 2, 'c': 5}

pd.DataFrame(d, columns=['a', 'b', 'c'])

titanic_train.loc[0]
titanic_train.iloc[0]
titanic_train.ix[0]


