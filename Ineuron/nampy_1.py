import numpy as np  # numerical python manuly dealing with arrays and matrixes

a = [3, 4, 5, 6.0]
print(np.array(a))  # convert this list to array
print(type(np.array(a)))  # n dimensional array

v = np.array([[1, 2, 3], [4, 5, 6]])
v
v.ndim  # no. of dimensions
v[0][0]
v[1][2]

v.shape  # no. of rows and columns
np.array([1, 2, 3], ndmin=10).ndim  # no. of dimensions
np.array([1, 2, 3], dtype=complex)  # changed data type
# complex data type: 1 + 2j where 1 is the real number and 2 is imaginary factor and j is the notation
n = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i2')])
# tuples in a list and changed data type
n
n[0][0]
type(n[1][1])  # numpy.int32 for i4 amd numpy.int16 for i2
#

m = np.mat([1, 2, 3])
m  # matrix is subclass of array
type(m)  # matrix is an instance of array or object of array

np.asanyarray([1, 2, 3])  # converting list to array
np.asanyarray(m)  # if my data set is available in some form of array, it will not convert to array

a = np.array([1, 2, 3, 4])
b = a  # this is swallow copy
b[0] = 123
b
a  # as a and b both referring to same location in memory, the change will reflect in 'a' also.
c = np.copy(a)  # deep copy: this will reserve a new location
c
c[0] = 345
c
a  # here the value of c and a are different as both pointing to different location.

np.fromfunction(lambda x, y: x == y, (3, 4))  # np treats everything as array or matrix.
# create an array with x as row num and y as column and perform operation as per the function
np.fromfunction(lambda x, y: x + y, (3, 4))

np.fromstring('1 3 5', sep=' ')  # create an array from string
m = np.array([1, 2, 3])
m.size
m.shape
m.ndim
n = np.arange(2.5, 9.87, .5)  # range function cant accept floating number where arange can
list(n)

np.linspace(3, 7, 20)  # generate an array with data starting from 3 to 7 total 20 numbers
np.linspace(3, 7, endpoint=False, retstep=True)  # remove 7 as end value
np.zeros((2, 3))  # create an aarray with zeroes
np.zeros((2, 5, 3))  # create an aarray with 3 dimension
np.ones((2, 3))
np.ones((2, 3)) + 2  # data manipulation in an array
np.empty((2, 4))  # create array with random numbers close to 0

np.eye(4)  # create identity matrix

np.logspace(5.6, 7.8, 6, base=2)  # logerithmic

m = np.random.rand(4, 5)  # generate random number
m = np.random.randn(4, 5)  # generate random number
m = np.random.randint(4, 5)  # generate random number
m.reshape(10, 2)  # changing row-column values
m.reshape(5, 4)

a = np.random.randint(3, 8, (5, 6))  # in between 3 to 8, generate 5*6 30 numbers
# where 5 is the row num and 6 is the column num
a
a[0:2, 0:2]  # slicing first 2 rows and respective first 2 columns

a > 5
a[a > 5]  # putting all fltered records in an array

a[0][0] = 90  # assigning a value
a

m = np.array([[1, 2, 3], [5, 6, 7]])
n = np.array([[10, 20, 30], [50, 60, 70]])
m + n

