Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
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
>>> base.mean(x)
R object with classes: ('numeric',) mapped to:
<FloatVector - Python:0x7f1bf19614d0 / R:0x68c1ec8>
[15.000000]
>>> print(base.mean(x))
[1] 15

>>> np.mean(x)
15.0
>>> R=robjects.r
>>> x
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
>>> y
array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
       20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
>>> M=R.lm(y~x)
SyntaxError: invalid syntax
>>> M=R.lm('y~x')

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/rpy2/rinterface/__init__.py", line 185
    warnings.warn(x, RRuntimeWarning)
RRuntimeWarning: Error in eval(expr, envir, enclos) : object 'y' not found


Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    M=R.lm('y~x')
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 106, in __call__
    res = super(Function, self).__call__(*new_args, **new_kwargs)
RRuntimeError: Error in eval(expr, envir, enclos) : object 'y' not found

>>> M=stats.lm(y~x)
SyntaxError: invalid syntax
>>> M=stats.lm('y~x')

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    M=stats.lm('y~x')
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 106, in __call__
    res = super(Function, self).__call__(*new_args, **new_kwargs)
RRuntimeError: Error in eval(expr, envir, enclos) : object 'y' not found

>>> M=stats.lm('y~x', data=(y,x))

Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    M=stats.lm('y~x', data=(y,x))
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 105, in __call__
    new_kwargs[k] = conversion.py2ri(v)
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'tuple'>'
>>> numpy2ri.activate()
>>> M=stats.lm('y~x', data=(y,x))

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    M=stats.lm('y~x', data=(y,x))
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 105, in __call__
    new_kwargs[k] = conversion.py2ri(v)
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'tuple'>'
>>> M=stats.lm(y ~ x)
SyntaxError: invalid syntax
>>> data=x,y
>>> data
(array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
       20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]))
>>> M=stats.lm('y ~ x', data)

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    M=stats.lm('y ~ x', data)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 178, in __call__
    return super(SignatureTranslatedFunction, self).__call__(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/functions.py", line 102, in __call__
    new_args = [conversion.py2ri(a) for a in args]
  File "/usr/local/lib/python2.7/dist-packages/singledispatch.py", line 210, in wrapper
    return dispatch(args[0].__class__)(*args, **kw)
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/conversion.py", line 60, in _py2ri
    raise NotImplementedError("Conversion 'py2ri' not defined for objects of type '%s'" % str(type(obj)))
NotImplementedError: Conversion 'py2ri' not defined for objects of type '<type 'tuple'>'
>>> from rpy2.robjects import tuple2ri

Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    from rpy2.robjects import tuple2ri
ImportError: cannot import name tuple2ri
>>> from rpy2.robjects import tuples2ri

Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    from rpy2.robjects import tuples2ri
ImportError: cannot import name tuples2ri
>>> from rpy2.robjects import pandas2ri

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    from rpy2.robjects import pandas2ri
  File "/usr/local/lib/python2.7/dist-packages/rpy2/robjects/pandas2ri.py", line 9, in <module>
    from pandas.core.frame import DataFrame as PandasDataFrame
ImportError: No module named pandas.core.frame
>>> import pandas as pd

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    import pandas as pd
ImportError: No module named pandas
>>> import pandas as pd
>>> from rpy2.robjects import pandas2ri
>>> pandas2ri.activate()
>>> R = robjects.r
>>> df= pd.DataFrame({'x':x, 'y':y})
>>> df
     x   y
0    1   3
1    2   4
2    3   5
3    4   6
4    5   7
5    6   8
6    7   9
7    8  10
8    9  11
9   10  12
10  11  13
11  12  14
12  13  15
13  14  16
14  15  17
15  16  18
16  17  19
17  18  20
18  19  21
19  20  22
20  21  23
21  22  24
22  23  25
23  24  26
24  25  27
25  26  28
26  27  29
27  28  30
28  29  31
>>> M=R.lm('y~x', data=df)
>>> print(R.summary(M))

Call:
(function (formula, data, subset, weights, na.action, method = "qr", 
    model = TRUE, x = FALSE, y = FALSE, qr = TRUE, singular.ok = TRUE, 
    contrasts = NULL, offset, ...) 
{
    ret.x <- x
    ret.y <- y
    cl <- match.call()
    mf <- match.call(expand.dots = FALSE)
    m <- match(c("formula", "data", "subset", "weights", "na.action", 
        "offset"), names(mf), 0L)
    mf <- mf[c(1L, m)]
    mf$drop.unused.levels <- TRUE
    mf[[1L]] <- quote(stats::model.frame)
    mf <- eval(mf, parent.frame())
    if (method == "model.frame") 
        return(mf)
    else if (method != "qr") 
        warning(gettextf("method = '%s' is not supported. Using 'qr'", 
            method), domain = NA)
    mt <- attr(mf, "terms")
    y <- model.response(mf, "numeric")
    w <- as.vector(model.weights(mf))
    if (!is.null(w) && !is.numeric(w)) 
        stop("'weights' must be a numeric vector")
    offset <- as.vector(model.offset(mf))
    if (!is.null(offset)) {
        if (length(offset) != NROW(y)) 
            stop(gettextf("number of offsets is %d, should equal %d (number of observations)", 
                length(offset), NROW(y)), domain = NA)
    }
    if (is.empty.model(mt)) {
        x <- NULL
        z <- list(coefficients = if (is.matrix(y)) matrix(, 0, 
            3) else numeric(), residuals = y, fitted.values = 0 * 
            y, weights = w, rank = 0L, df.residual = if (!is.null(w)) sum(w != 
            0) else if (is.matrix(y)) nrow(y) else length(y))
        if (!is.null(offset)) {
            z$fitted.values <- offset
            z$residuals <- y - offset
        }
    }
    else {
        x <- model.matrix(mt, mf, contrasts)
        z <- if (is.null(w)) 
            lm.fit(x, y, offset = offset, singular.ok = singular.ok, 
                ...)
        else lm.wfit(x, y, w, offset = offset, singular.ok = singular.ok, 
            ...)
    }
    class(z) <- c(if (is.matrix(y)) "mlm", "lm")
    z$na.action <- attr(mf, "na.action")
    z$offset <- offset
    z$contrasts <- attr(x, "contrasts")
    z$xlevels <- .getXlevels(mt, mf)
    z$call <- cl
    z$terms <- mt
    if (model) 
        z$model <- mf
    if (ret.x) 
        z$x <- x
    if (ret.y) 
        z$y <- y
    if (!qr) 
        z$qr <- NULL
    z
})(formula = "y~x", data = structure(list(x = 1:29, y = 3:31), .Names = c("x", 
"y"), row.names = c("0", "1", "2", "3", "4", "5", "6", "7", "8", 
"9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
"20", "21", "22", "23", "24", "25", "26", "27", "28"), class = "data.frame"))

Residuals:
       Min         1Q     Median         3Q        Max 
-1.098e-14 -3.518e-16 -3.400e-17  2.167e-16  1.114e-14 

Coefficients:
             Estimate Std. Error   t value Pr(>|t|)    
(Intercept) 2.000e+00  1.171e-15 1.709e+15   <2e-16 ***
x           1.000e+00  6.815e-17 1.467e+16   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 3.071e-15 on 27 degrees of freedom
Multiple R-squared:      1,	Adjusted R-squared:      1 
F-statistic: 2.153e+32 on 1 and 27 DF,  p-value: < 2.2e-16


>>> print(R.summary(M).rx2('coefficients'))
            Estimate   Std. Error      t value Pr(>|t|)
(Intercept)        2 1.170510e-15 1.708657e+15        0
x                  1 6.814971e-17 1.467358e+16        0

>>> 
>>> 
>>> 

