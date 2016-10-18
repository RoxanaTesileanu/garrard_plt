Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # focal analyses
>>> # create an 6x6 array and then use a smoothing filter that computes the mean of a 3x3 moving window:
>>> import numpy as np
>>> indata = np.arange(1, 37)
>>> indata.reshape(6,6)
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18],
       [19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36]])
>>> outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3])/9

Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    indata[3,1] + indata[3,2] + indata[3,3])/9
IndexError: too many indices for array
>>> outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3]) / 9

Traceback (most recent call last):
  File "<pyshell#8>", line 3, in <module>
    indata[3,1] + indata[3,2] + indata[3,3]) / 9
IndexError: too many indices for array
>>> outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3])

Traceback (most recent call last):
  File "<pyshell#9>", line 3, in <module>
    indata[3,1] + indata[3,2] + indata[3,3])
IndexError: too many indices for array
>>> outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] +indata[3,1] + indata[3,2] + indata[3,3])

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] +indata[3,1] + indata[3,2] + indata[3,3])
IndexError: too many indices for array
>>> indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] +indata[3,1] + indata[3,2] + indata[3,3]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] +indata[3,1] + indata[3,2] + indata[3,3]
IndexError: too many indices for array
>>> indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] + indata[3,1] + indata[3,2] + indata[3,3]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    indata[1,1] + indata[1,2] + indata[1,3] + indata[2,1] + indata[2,2] + indata[2,3] + indata[3,1] + indata[3,2] + indata[3,3]
IndexError: too many indices for array
>>> sum(indata[1,1],indata[1,2] , indata[1,3], indata[2,1], indata[2,2] , indata[2,3], indata[3,1], indata[3,2] , indata[3,3])

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sum(indata[1,1],indata[1,2] , indata[1,3], indata[2,1], indata[2,2] , indata[2,3], indata[3,1], indata[3,2] , indata[3,3])
IndexError: too many indices for array
>>> indata[1,1]

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    indata[1,1]
IndexError: too many indices for array
>>> indata[1;1]
SyntaxError: invalid syntax
>>> indata
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36])
>>> indata=indata.reshape(6,6)
>>> indata
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18],
       [19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36]])
>>> sum(indata[1,1],indata[1,2] , indata[1,3], indata[2,1], indata[2,2] , indata[2,3], indata[3,1], indata[3,2] , indata[3,3])

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sum(indata[1,1],indata[1,2] , indata[1,3], indata[2,1], indata[2,2] , indata[2,3], indata[3,1], indata[3,2] , indata[3,3])
TypeError: sum expected at most 2 arguments, got 9
>>> outdata[2,2] = (indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3])

Traceback (most recent call last):
  File "<pyshell#20>", line 3, in <module>
    indata[3,1] + indata[3,2] + indata[3,3])
NameError: name 'outdata' is not defined
>>> mymean=(indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3])
>>> mysum=(indata[1,1] + indata[1,2] + indata[1,3] +
		indata[2,1] + indata[2,2] + indata[2,3] +
		indata[3,1] + indata[3,2] + indata[3,3])
>>> mymean=mysum/9
>>> mymean
15
>>> # wow!! I've got a revelation!!!
>>> outdata=np.zeros(indata.shape)
>>> outdata[2,2] = mymean
>>> outdata[2,2] = np.mean(indata[1:4, 1:4])
>>> # using looping:
>>> outdata2=np.zeros(indata.shape)
>>> for i in range (1, rows-1) :
	for j in range (1, cols-1) :
		outdata[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for i in range (1, rows-1) :
NameError: name 'rows' is not defined
>>> for i in range (1, rows-1) :
	for j in range (1, cols-1) :
		outdata2[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for i in range (1, rows-1) :
NameError: name 'rows' is not defined
>>> for i in range (1, 6) :
	for j in range (1, 6) :
		outdata2[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata2
array([[  0. ,   0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   8. ,   9. ,  10. ,  11. ,  11.5],
       [  0. ,  14. ,  15. ,  16. ,  17. ,  17.5],
       [  0. ,  20. ,  21. ,  22. ,  23. ,  23.5],
       [  0. ,  26. ,  27. ,  28. ,  29. ,  29.5],
       [  0. ,  29. ,  30. ,  31. ,  32. ,  32.5]])
>>> for i in range (1, 5) :
	for j in range (1, 5) :
		outdata2[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata2
array([[  0. ,   0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   8. ,   9. ,  10. ,  11. ,  11.5],
       [  0. ,  14. ,  15. ,  16. ,  17. ,  17.5],
       [  0. ,  20. ,  21. ,  22. ,  23. ,  23.5],
       [  0. ,  26. ,  27. ,  28. ,  29. ,  29.5],
       [  0. ,  29. ,  30. ,  31. ,  32. ,  32.5]])
>>> # ok, I have an edge problem!
>>> 
for i in range (1, 4) :
	for j in range (1, 4) :
		outdata2[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata2
array([[  0. ,   0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   8. ,   9. ,  10. ,  11. ,  11.5],
       [  0. ,  14. ,  15. ,  16. ,  17. ,  17.5],
       [  0. ,  20. ,  21. ,  22. ,  23. ,  23.5],
       [  0. ,  26. ,  27. ,  28. ,  29. ,  29.5],
       [  0. ,  29. ,  30. ,  31. ,  32. ,  32.5]])
>>> outdata3=np.zeros(indata.shape)
>>> for i in range (1, 4) :
	for j in range (1, 4) :
		outdata3[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata3
array([[  0.,   0.,   0.,   0.,   0.,   0.],
       [  0.,   8.,   9.,  10.,   0.,   0.],
       [  0.,  14.,  15.,  16.,   0.,   0.],
       [  0.,  20.,  21.,  22.,   0.,   0.],
       [  0.,   0.,   0.,   0.,   0.,   0.],
       [  0.,   0.,   0.,   0.,   0.,   0.]])
>>> for i in range (1, 5) :
	for j in range (1, 5) :
		outdata3[i,j] = np.mean(indata[i-1:i+2, j-1:j+2])

		
>>> outdata3
array([[  0.,   0.,   0.,   0.,   0.,   0.],
       [  0.,   8.,   9.,  10.,  11.,   0.],
       [  0.,  14.,  15.,  16.,  17.,   0.],
       [  0.,  20.,  21.,  22.,  23.,   0.],
       [  0.,  26.,  27.,  28.,  29.,   0.],
       [  0.,   0.,   0.,   0.,   0.,   0.]])
>>> # ok, it works, but leaves out the edges!
>>> # now, do the same thing using numpy!
>>> outdata4=np.zeros(indata.shape)
>>> 
