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
>>> # stack the slices into a 3D array using the function dstack (which stacks the slices on top of each other).
>>> 
>>> slices []
SyntaxError: invalid syntax
>>> slices =[]
>>> for i in range (3) :
	for i in range (3) :
		slices.append(indata [i:6-2+i, j:6-2+j])

		
>>> slices
[array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]]), array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]]), array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]])]
>>> stacked=np.dstack(slices)
>>> outdata2[1:-1, 1:-1]=np.mean(stacked,2)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    outdata2[1:-1, 1:-1]=np.mean(stacked,2)
ValueError: could not broadcast input array from shape (4,2) into shape (4,4)
>>> for i in range (3) :
	for j in range (3) :
		slices.append(indata [i:6-2+i, j:6-2+j])

		
>>> slices
[array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]]), array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]]), array([[ 5,  6],
       [11, 12],
       [17, 18],
       [23, 24]]), array([[11, 12],
       [17, 18],
       [23, 24],
       [29, 30]]), array([[17, 18],
       [23, 24],
       [29, 30],
       [35, 36]]), array([[ 1,  2,  3,  4],
       [ 7,  8,  9, 10],
       [13, 14, 15, 16],
       [19, 20, 21, 22]]), array([[ 2,  3,  4,  5],
       [ 8,  9, 10, 11],
       [14, 15, 16, 17],
       [20, 21, 22, 23]]), array([[ 3,  4,  5,  6],
       [ 9, 10, 11, 12],
       [15, 16, 17, 18],
       [21, 22, 23, 24]]), array([[ 7,  8,  9, 10],
       [13, 14, 15, 16],
       [19, 20, 21, 22],
       [25, 26, 27, 28]]), array([[ 8,  9, 10, 11],
       [14, 15, 16, 17],
       [20, 21, 22, 23],
       [26, 27, 28, 29]]), array([[ 9, 10, 11, 12],
       [15, 16, 17, 18],
       [21, 22, 23, 24],
       [27, 28, 29, 30]]), array([[13, 14, 15, 16],
       [19, 20, 21, 22],
       [25, 26, 27, 28],
       [31, 32, 33, 34]]), array([[14, 15, 16, 17],
       [20, 21, 22, 23],
       [26, 27, 28, 29],
       [32, 33, 34, 35]]), array([[15, 16, 17, 18],
       [21, 22, 23, 24],
       [27, 28, 29, 30],
       [33, 34, 35, 36]])]
>>> slices2=[]
>>> for i in range (3) :
	for j in range (3) :
		slices2.append(indata [i:6-2+i, j:6-2+j])

		
>>> slices2
[array([[ 1,  2,  3,  4],
       [ 7,  8,  9, 10],
       [13, 14, 15, 16],
       [19, 20, 21, 22]]), array([[ 2,  3,  4,  5],
       [ 8,  9, 10, 11],
       [14, 15, 16, 17],
       [20, 21, 22, 23]]), array([[ 3,  4,  5,  6],
       [ 9, 10, 11, 12],
       [15, 16, 17, 18],
       [21, 22, 23, 24]]), array([[ 7,  8,  9, 10],
       [13, 14, 15, 16],
       [19, 20, 21, 22],
       [25, 26, 27, 28]]), array([[ 8,  9, 10, 11],
       [14, 15, 16, 17],
       [20, 21, 22, 23],
       [26, 27, 28, 29]]), array([[ 9, 10, 11, 12],
       [15, 16, 17, 18],
       [21, 22, 23, 24],
       [27, 28, 29, 30]]), array([[13, 14, 15, 16],
       [19, 20, 21, 22],
       [25, 26, 27, 28],
       [31, 32, 33, 34]]), array([[14, 15, 16, 17],
       [20, 21, 22, 23],
       [26, 27, 28, 29],
       [32, 33, 34, 35]]), array([[15, 16, 17, 18],
       [21, 22, 23, 24],
       [27, 28, 29, 30],
       [33, 34, 35, 36]])]
>>> stacked2=np.dstack(slices2)
>>> stacked2
array([[[ 1,  2,  3,  7,  8,  9, 13, 14, 15],
        [ 2,  3,  4,  8,  9, 10, 14, 15, 16],
        [ 3,  4,  5,  9, 10, 11, 15, 16, 17],
        [ 4,  5,  6, 10, 11, 12, 16, 17, 18]],

       [[ 7,  8,  9, 13, 14, 15, 19, 20, 21],
        [ 8,  9, 10, 14, 15, 16, 20, 21, 22],
        [ 9, 10, 11, 15, 16, 17, 21, 22, 23],
        [10, 11, 12, 16, 17, 18, 22, 23, 24]],

       [[13, 14, 15, 19, 20, 21, 25, 26, 27],
        [14, 15, 16, 20, 21, 22, 26, 27, 28],
        [15, 16, 17, 21, 22, 23, 27, 28, 29],
        [16, 17, 18, 22, 23, 24, 28, 29, 30]],

       [[19, 20, 21, 25, 26, 27, 31, 32, 33],
        [20, 21, 22, 26, 27, 28, 32, 33, 34],
        [21, 22, 23, 27, 28, 29, 33, 34, 35],
        [22, 23, 24, 28, 29, 30, 34, 35, 36]]])
>>> outdata3=np.zeros(indata.shape)
>>> outdata3[1:-1, 1:-1]=np.mean(stacked2,2)
>>> outdata3
array([[  0.,   0.,   0.,   0.,   0.,   0.],
       [  0.,   8.,   9.,  10.,  11.,   0.],
       [  0.,  14.,  15.,  16.,  17.,   0.],
       [  0.,  20.,  21.,  22.,  23.,   0.],
       [  0.,  26.,  27.,  28.,  29.,   0.],
       [  0.,   0.,   0.,   0.,   0.,   0.]])
>>> # ok, it worked but I have to try to understand what just happned!
>>> # ;)
>>> 
