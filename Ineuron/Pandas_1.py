# pandas package #########
import pandas as pd
from pathlib import Path
import os

cwd = os.getcwd()  # get current working directory
print(cwd)

my_path = Path('C:\\Users\\proy\\OneDrive - Tractor Supply Co\\PRAT_TSC\\MISC\\PYTHON\\Krish_Naik\\materials\\files\\')
# my_path = Path('C:/Users/proy/OneDrive - Tractor Supply Co/PRAT_TSC/MISC/PYTHON/Krish_Naik/materials/files')
my_file = open(my_path/'ex3.txt')
# print(my_file.read())

a = pd.read_csv(my_path/'ex1.csv')
print(a)  # will show columns and row indexes
print(type(a))  # a is a type as dataframe with table structure

a.head()
a.tail()
a.dtypes  # show the data types of individual columns in the dataframe

a['d']  # access column d from dataframe and show the series
a[['c', 'a', 'd']]  # accessing multiple columns/ series by using double sqr brackets

type(a['d'])  # series  (In pandas, we encounter 2 type of objects: dataframe and series)

x = [2, 3, 4]
print(x)  # will not show any index but series does

list(a['d'])  # series to list conversion

a = pd.read_csv(my_path/'ex1.csv', header=None)
print(a)  # will show row and column indexes including 1st row as data

# we can read tsv file also from read_csv

a = pd.read_csv(my_path/'test.tsv', sep='\t')
print(a)

df = pd.read_table(my_path/'test.tsv')  # reading tsv file
print(df)

df1 = pd.read_csv(my_path/'ex1.csv', header=None, names=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df1)

# hierarchical index or index columns

print(pd.read_csv(my_path/'csv_mindex.csv', index_col=['key1', 'key2']))  # replacing default indexes with column indexes

# skipping junk data from reading files

print(pd.read_csv(my_path/'ex4.csv', skiprows=[0, 2, 3]))

print(pd.read_csv(my_path/'ex5.csv', na_values=['8']))  # blank or NULL treating as NaN not a number
# replacing 8 with NaN

# spread sheet
print(pd.read_excel(my_path/'test.xlsx', sheet_name='abc'))

# read data from html file where data is residing in a table.
# if there are multiple tables in a page, then pandas will put them in individual indexes in a list.
# though there are other elements in the web page, only data within </table>  tag will be considered here.
h = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
print(h)
print(type(h))  # type is list istead of dataframe
len(h)  # 1 as entire table is saved in 0th index in the list.
type(h[0])  # dataframe
h[0].columns  # will show all the columns

titanic = pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw"
                      "/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv", sep='\t')

print(titanic)
titanic[['Embarked', 'Cabin', 'Survived']]

titanic.to_csv(my_path/'titanic.csv')  # to save data file permanently:

print(pd.read_csv(my_path/'ex6.csv', nrows=5))

# Beautiful Soup package to pull everything from html file






