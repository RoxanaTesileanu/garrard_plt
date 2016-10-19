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
>>> # ok, bn is binnumber - the bin in which an observation falls.
>>> import rpy

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    import rpy
ImportError: No module named rpy
>>> import rpy

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    import rpy
ImportError: No module named rpy
>>> import rpy

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    import rpy
ImportError: No module named rpy
>>> import rpy2

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    import rpy2
ImportError: No module named rpy2
>>> import rpy2
>>> print (r-y2._version_)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print (r-y2._version_)
NameError: name 'r' is not defined
>>> print (rpy2._version_)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print (rpy2._version_)
AttributeError: 'module' object has no attribute '_version_'
>>> import rpy2.robjects as robjects
>>> from rpy2.robjects import r
>>> x= np.range(1,30)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    x= np.range(1,30)
AttributeError: 'module' object has no attribute 'range'
>>> x= np.arange(1,30)
>>> y=np.arange(3,33)
>>> len(x)
29
>>> len(y)
30
>>> y=np.arange(3,32)
>>> r.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    r.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> pplot=r.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    pplot=r.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> plot=r.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    plot=r.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> rprint(r.plot(x,y))

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    rprint(r.plot(x,y))
NameError: name 'rprint' is not defined
>>> from rpy2.robjects.packages import importr
>>> base = importr('base')

>>> utils = importr('utils')
>>> plot=r.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    plot=r.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> plot(x,y)

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    plot(x,y)
NameError: name 'plot' is not defined
>>> stats    = importr('stats')
>>> graphics = importr('graphics')
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> stats.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    stats.plot(x,y)
AttributeError: 'InstalledSTPackage' object has no attribute 'plot'
>>> grdevices = importr('grDevices')
>>> grdevices.png(file="rpyplot.png", width=512, height=512)
rpy2.rinterface.NULL
>>> stats.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    stats.plot(x,y)
AttributeError: 'InstalledSTPackage' object has no attribute 'plot'
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> plot(x,y)

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    plot(x,y)
NameError: name 'plot' is not defined
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf18e1cb0 / R:0x60f7758>
[       1]
>>> grdevices.png(file="rpyplot.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf190f518 / R:0x60f9198>
[       1]
>>> graphics = importr('graphics')
>>> r.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    r.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> graphics.plot('x','y')

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: Error in plot.window(...) : need finite 'xlim' values


Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: In addition: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: Warning messages:


Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 1: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: In xy.coords(x, y, xlabel, ylabel, log) :

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning:  NAs introduced by coercion


Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 2: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 3: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: In min(x) :

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning:  no non-missing arguments to min; returning Inf


Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 4: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: In max(x) :

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning:  no non-missing arguments to max; returning -Inf


Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 5: 

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: 6: 

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    graphics.plot('x','y')
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 106, in __call__
    res = super(Function, self).__call__(*new_args, **new_kwargs)
RRuntimeError: Error in plot.window(...) : need finite 'xlim' values

>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> graphics.plot('x'=x,'y'=y)
SyntaxError: keyword can't be an expression
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf18e1bd8 / R:0x646e968>
[       1]
>>> grdevices.png(file="rpyplot.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> graphics.plot('x,y')

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: Error in plot.window(...) : need finite 'ylim' values


Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    graphics.plot('x,y')
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 106, in __call__
    res = super(Function, self).__call__(*new_args, **new_kwargs)
RRuntimeError: Error in plot.window(...) : need finite 'ylim' values

>>> graphics.plot([0,1,2,3], [0,1,2,3])
rpy2.rinterface.NULL
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf1907098 / R:0x65e2588>
[       1]
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> x= np.arange(1,30)
>>> y=np.arange(3,32)
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf195f1b8 / R:0x65e89b8>
[       1]
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(np.arange(1,30), np.arange(3,32))

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    graphics.plot(np.arange(1,30), np.arange(3,32))
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> x
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
>>> # so I guess it doesn't work with ndarrays...isn't that weird?
>>> import rpy2.rinterface
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(np.arange(1,30), np.arange(3,32))

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    graphics.plot(np.arange(1,30), np.arange(3,32))
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> import rpy2.robjects.numpt2ri

Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    import rpy2.robjects.numpt2ri
ImportError: No module named numpt2ri
>>> import rpy2.robjects.numpy2ri
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(np.arange(1,30), np.arange(3,32))

Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    graphics.plot(np.arange(1,30), np.arange(3,32))
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf1950908 / R:0x68a6998>
[       2]
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(x,y)

Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    graphics.plot(x,y)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'numpy.ndarray'>'
>>> from rpy2.robjects import numpy2ri
>>> numpy2ri.activate()
>>> grdevices.png(file="rpyplot2.png", width=512, height=512)
rpy2.rinterface.NULL
>>> graphics.plot(x,y)
rpy2.rinterface.NULL
>>> grdevices.dev_off()
R object with classes: ('integer',) mapped to:
<IntVector - Python:0x7f1bf1907fc8 / R:0x6a02ed8>
[       2]
>>> # yes! I've made it!!! The conversion worked!
>>> # similarly you can use pandas2ri and pandas2ri.activate() to use pandas data frames!!
>>> # from rpy2.robjects import pandas2ri
>>> # pandas2ri.activate()
>>> 
