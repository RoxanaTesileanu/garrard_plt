Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> indata = np.arange(1,37)
>>> indata= indata.reshape(6,6)
>>> indate

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    indate
NameError: name 'indate' is not defined
>>> indata
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18],
       [19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36]])
>>> outdata = np.zeros(indata.shape)
>>> outdata
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
>>> for i in range (1,5) :
	for j in range (1,5) :
		outdata[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata
array([[  0.,   0.,   0.,   0.,   0.,   0.],
       [  0.,   8.,   9.,  10.,  11.,   0.],
       [  0.,  14.,  15.,  16.,  17.,   0.],
       [  0.,  20.,  21.,  22.,  23.,   0.],
       [  0.,  26.,  27.,  28.,  29.,   0.],
       [  0.,   0.,   0.,   0.,   0.,   0.]])
>>> # it works but leaves out the edges.
>>> # now, the same thing using numpy:
>>> 
>>> outdata2=np.zeros(indata.shape)
>>> outdata2
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
>>> 
