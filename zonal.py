Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # zonal analyses work on cells that share the same value, or belong to the same zone.
>>> import nunpy as np

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import nunpy as np
ImportError: No module named nunpy
>>> import numpy as np
>>> import random
>>> arr= np.arange(0,21)
>>> arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20])
>>> arr2=np.random.sample(arr, 100)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    arr2=np.random.sample(arr, 100)
  File "mtrand.pyx", line 1101, in mtrand.RandomState.random_sample (numpy/random/mtrand/mtrand.c:13875)
TypeError: random_sample() takes at most 1 positional argument (2 given)
>>> arr2=np.random.sample(arr, 100, replace=True)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    arr2=np.random.sample(arr, 100, replace=True)
  File "mtrand.pyx", line 1101, in mtrand.RandomState.random_sample (numpy/random/mtrand/mtrand.c:13875)
TypeError: random_sample() takes at most 1 positional argument (2 given)
>>> arr2=np.random.choice(arr, 100)
>>> arr2
array([15, 19, 19, 11, 19, 15, 17, 18,  2, 15,  2,  1,  2,  6, 14,  3,  6,
        7, 10,  8, 20,  0,  4, 13, 11, 20, 17,  4, 17,  1, 16,  4,  1,  3,
        1, 18, 19, 10,  2, 13,  7,  8, 10, 13, 20, 13,  4,  5, 12,  1, 11,
        1,  7, 13,  4, 18, 15, 10,  4, 18, 15, 20, 15, 20,  0, 11,  4,  0,
        8,  1, 10,  9,  6,  6, 10,  4,  6,  7, 11, 10, 20, 18, 13,  2,  6,
        1, 11,  5, 13,  5,  7,  2,  4, 13, 13,  3, 19,  5,  3,  2])
>>> arr2.reshape(20,5)
array([[15, 19, 19, 11, 19],
       [15, 17, 18,  2, 15],
       [ 2,  1,  2,  6, 14],
       [ 3,  6,  7, 10,  8],
       [20,  0,  4, 13, 11],
       [20, 17,  4, 17,  1],
       [16,  4,  1,  3,  1],
       [18, 19, 10,  2, 13],
       [ 7,  8, 10, 13, 20],
       [13,  4,  5, 12,  1],
       [11,  1,  7, 13,  4],
       [18, 15, 10,  4, 18],
       [15, 20, 15, 20,  0],
       [11,  4,  0,  8,  1],
       [10,  9,  6,  6, 10],
       [ 4,  6,  7, 11, 10],
       [20, 18, 13,  2,  6],
       [ 1, 11,  5, 13,  5],
       [ 7,  2,  4, 13, 13],
       [ 3, 19,  5,  3,  2]])
>>> arr3=arr2.reshape(20,5)
>>> arr3
array([[15, 19, 19, 11, 19],
       [15, 17, 18,  2, 15],
       [ 2,  1,  2,  6, 14],
       [ 3,  6,  7, 10,  8],
       [20,  0,  4, 13, 11],
       [20, 17,  4, 17,  1],
       [16,  4,  1,  3,  1],
       [18, 19, 10,  2, 13],
       [ 7,  8, 10, 13, 20],
       [13,  4,  5, 12,  1],
       [11,  1,  7, 13,  4],
       [18, 15, 10,  4, 18],
       [15, 20, 15, 20,  0],
       [11,  4,  0,  8,  1],
       [10,  9,  6,  6, 10],
       [ 4,  6,  7, 11, 10],
       [20, 18, 13,  2,  6],
       [ 1, 11,  5, 13,  5],
       [ 7,  2,  4, 13, 13],
       [ 3, 19,  5,  3,  2]])
>>> # define bins:
>>> def get_bins(data) :
	""" Return bin edges for all unique values in data. """
	bins=np.unique(data)
	return np.append(bins[~np.isnan(bins)], max(bins) +1)

>>> # use the numpy histogram2d function to get the counts
>>> # I need 2 arrays to make a histo, so I have to create the second one. I will use colors.
>>> col_arr=np.zeros((20,5), int)
>>> col_arr
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
>>> col_arr[0:6,0:3]='Red'

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    col_arr[0:6,0:3]='Red'
ValueError: invalid literal for int() with base 10: 'Red'
>>> col_arr[0:6,0:3].dtype=string

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    col_arr[0:6,0:3].dtype=string
NameError: name 'string' is not defined
>>> col_arr[0:6,0:3]=dtype(string)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    col_arr[0:6,0:3]=dtype(string)
NameError: name 'dtype' is not defined
>>> col_arr[0:6,0:3]=string('Red')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    col_arr[0:6,0:3]=string('Red')
NameError: name 'string' is not defined
>>> col_arr=np.zeros((20,5), bool)
>>> col_arr
array([[False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False]], dtype=bool)
>>> col_arr[0:6,0:3]=True
>>> col_arr
array([[ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False]], dtype=bool)
>>> # I can't use strings...so I use false and true
>>> col_arr[7:16, 2:]=True
>>> col_arr
array([[ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [ True,  True,  True, False, False],
       [False, False, False, False, False],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False,  True,  True,  True],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False]], dtype=bool)
>>> # I have to flatten the 2d arrays:
>>> hist, col_bins, arr3_bins = np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    hist, col_bins, arr3_bins = np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])
NameError: name 'col_bins' is not defined
>>> hist, col_arr_bins, arr3_bins = np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    hist, col_arr_bins, arr3_bins = np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])
NameError: name 'col_bins' is not defined
>>> np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    np.histogram2d(col_bins.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])
NameError: name 'col_bins' is not defined
>>> hist, col_bins, arr3_bins = np.histogram2d(col_arr.flatten(), arr3.flatten(), [get_bins(col_arr), get_bins(arr3)])
>>> hist
array([[ 0.,  5.,  4.,  3.,  5.,  3.,  3.,  2.,  2.,  1.,  2.,  5.,  0.,
         6.,  1.,  3.,  1.,  1.,  3.,  3.,  2.],
       [ 3.,  3.,  3.,  1.,  4.,  1.,  3.,  3.,  1.,  0.,  5.,  1.,  1.,
         3.,  0.,  3.,  0.,  2.,  2.,  2.,  4.]])
>>> # two lists: one for the false values and one for the true values
>>> # each list contains the counts for each value from 0 to 20
>>> col_bins
array([ 0.,  1.,  2.])
>>> arr3_bins
array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.,
        11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.,  20.,  21.])
>>> # the histogram rows correspond to the bins from the first array that was passed in (two rows:false and true), and the columns correspond to the second array (arr3).
>>> 
>>> #########
>>> # using SciPy, you can get a histogram with the function called stats.binned_statistic_2d:
>>> import scipy.stats
>>> hist2, col_bins2, arr3_bins2, bn = scipy.stats.binned_statistic_2d(
	col_arr.flatten(), arr3.flatten(),col_arr.flatten(), 'count', [get_bins(col_arr), get_bins(arr3)])
>>> hits2

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    hits2
NameError: name 'hits2' is not defined
>>> hist2
array([[ 0.,  5.,  4.,  3.,  5.,  3.,  3.,  2.,  2.,  1.,  2.,  5.,  0.,
         6.,  1.,  3.,  1.,  1.,  3.,  3.,  2.],
       [ 3.,  3.,  3.,  1.,  4.,  1.,  3.,  3.,  1.,  0.,  5.,  1.,  1.,
         3.,  0.,  3.,  0.,  2.,  2.,  2.,  4.]])
>>> bn
array([62, 66, 66, 35, 43, 62, 64, 65, 26, 39, 49, 48, 49, 30, 38, 50, 53,
       54, 34, 32, 67, 47, 51, 37, 35, 67, 64, 51, 41, 25, 40, 28, 25, 27,
       25, 42, 43, 57, 49, 60, 31, 32, 57, 60, 67, 37, 28, 52, 59, 48, 35,
       25, 54, 60, 51, 42, 39, 57, 51, 65, 39, 44, 62, 67, 47, 35, 28, 47,
       55, 48, 34, 33, 53, 53, 57, 28, 30, 54, 58, 57, 44, 42, 37, 26, 30,
       25, 35, 29, 37, 29, 31, 26, 28, 37, 37, 27, 43, 29, 27, 26])
>>> # I don't know what bn is...
>>> 
