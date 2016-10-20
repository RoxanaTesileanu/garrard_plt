Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # Map Algebra RECAP:
>>> # - local map algebra computations work on pixel-by-pixel basis
>>> # - focal map algebra involves a moving window that uses surrounding pixels to calculate the output value
>>> # - zonal calculations work on pixels that are all in the same zone (e.g. histo of landcover types based on land ownership)
>>> # - global calculations work on entire raster datasets
>>> 
>>> 
>>> # Resampling data
>>> # - resize cell sizes (ch. 9)
>>> # - more advanced resampling methods
>>> 
>>> # provide a step value when specifying your slice
>>> import numpy as np
>>> data = np.reshape(np.arange(24), (4,6))
>>> data
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
>>> data[::2, ::2]
array([[ 0,  2,  4],
       [12, 14, 16]])
>>> # a step value of 2 tells np to keep every second value
>>> # or you can slice like this:
>>> data[0:4:2, 0:6:2]
array([[ 0,  2,  4],
       [12, 14, 16]])
>>> data[0:4:2, 0:6:3]
array([[ 0,  3],
       [12, 15]])
>>> # the 3rd no. in the indexing is the step index, so not providing anythin to the start and end leaves only ::2
>>> 
>>> # if you want to start at the 2nd row and column:
>>> data[1::2, 1::2]
array([[ 7,  9, 11],
       [19, 21, 23]])
>>> # the results are similar to the automatic resampling when you read data from a file into a differently sized array
>>> 
>>> # you can also increase the size of an array => decrease pixel sizes
>>> np.repeat(data, 2, 1) # you provide the axis which will be repeated, 1 is cols, 0 is rows.
array([[ 0,  0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5],
       [ 6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],
       [12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],
       [18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23]])
>>> # the cols got repeated two times
>>> # if you want to do it symmetrically , call repeat once on rows and once on cols:
>>> np.repeat(np.repeat(data, 2, 0), 2,1)
array([[ 0,  0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5],
       [ 0,  0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5],
       [ 6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],
       [ 6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],
       [12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],
       [12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17],
       [18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23],
       [18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23]])
>>> 
