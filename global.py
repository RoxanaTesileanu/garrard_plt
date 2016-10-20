Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # global analyses
>>> # e.g. proximity analysis: determines the Euclidean distance of each cell to the nearest cell that's marked as a source
>>> # cost distance: determines the least cost of travelling between each cell and the nearest source, as determined by a cost surface
>>> #(the easiest, and therefore least costly path may not be the shortest)
>>> 
>>> # 1) Proximity analysis : determine the distance to the nearest road
>>> 
>>> folder = '//home//roxana//private//osgeopy//osgeopy-data'
>>> folder = '//home//roxana//private//osgeopy//osgeopy-data/osgeopy-data/Idaho'
>>> roads_ln= 'wilderness'
>>> roads_ln= 'allroads'
>>> wilderness_ln='wilderness'
>>> road_raster_fn='church_roads.tif'
>>> proximity_fn='proximity.tif'
>>> cellsize=10
>>> 
>>> shp_ds=ogr.Open(folder)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    shp_ds=ogr.Open(folder)
NameError: name 'ogr' is not defined
>>> import os
>>> import sys
>>> from osgeo import gdal, ogr
>>> shp_ds=ogr.Open(folder)
>>> wild_lyr = shp_ds.GetLayerByName(wilderness_ln)
>>> 
