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
>>> # only need the Frank Church zone:
>>> wild_lyr.SetAttributeFilter( "WILD_NM = 'Frank Church - RONR'")
0
>>> # compute the extents of the selected geometry:
>>> envelops = [row.geometry().GetEnvelope() for row in wild_lyr]
>>> # gets the extents of the polygon.
>>> envelops
[(2397139.8132186467, 2461433.5767854652, 1577172.971495474, 1615295.5238143115), (2347778.078370039, 2443344.7754654535, 1519630.383184676, 1597151.110483063), (2437533.98645334, 2464980.173631916, 1575106.06222953, 1596072.194762523), (2381073.641918202, 2397558.4486929863, 1578025.9399057825, 1593479.5624097723), (2351397.998499874, 2354248.753683472, 1582697.1764466006, 1584277.8879005252), (2356491.437157528, 2357803.122735783, 1583590.0150078959, 1584131.190518769), (2433410.258469377, 2452258.7278520227, 1544028.0057485392, 1576605.2702438005), (2442848.5763856065, 2470558.146773548, 1520392.0195712307, 1569429.3777826636), (2377067.3776336857, 2470231.852124332, 1467254.3027636106, 1522534.8561032086), (2422967.859623324, 2441750.7492637374, 1467976.0686204894, 1488684.6377511998)]
>>> # the above variable is a list of tuples.
>>> # zip those tuples together:
>>> coords = list(zip(*envelopes))

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    coords = list(zip(*envelopes))
NameError: name 'envelopes' is not defined
>>> coords = list(zip(*envelops))
>>> coords
[(2397139.8132186467, 2347778.078370039, 2437533.98645334, 2381073.641918202, 2351397.998499874, 2356491.437157528, 2433410.258469377, 2442848.5763856065, 2377067.3776336857, 2422967.859623324), (2461433.5767854652, 2443344.7754654535, 2464980.173631916, 2397558.4486929863, 2354248.753683472, 2357803.122735783, 2452258.7278520227, 2470558.146773548, 2470231.852124332, 2441750.7492637374), (1577172.971495474, 1519630.383184676, 1575106.06222953, 1578025.9399057825, 1582697.1764466006, 1583590.0150078959, 1544028.0057485392, 1520392.0195712307, 1467254.3027636106, 1467976.0686204894), (1615295.5238143115, 1597151.110483063, 1596072.194762523, 1593479.5624097723, 1584277.8879005252, 1584131.190518769, 1576605.2702438005, 1569429.3777826636, 1522534.8561032086, 1488684.6377511998)]
>>> # is is a sort od dstack on the third dimension..
>>> # now get the min and max for each tuple:
>>> minx, maxx = min(coords[0]), max(coords[1])
>>> miny, maxy = min(coords[2]), max(coords[3])
>>> 
>>> # now that I have the extent of the zone, I need to select the roads in that extent
>>> road_lyr = shp_ds.GetLayerByName(roads_ln)
>>> road_lyr.SetSpatialFilterRect(minx, miny, maxx, maxy)
>>> 
>>> # now that the roads are selected, I turn them into a raster band for the proximity analysis.
>>> 
>>> os.chdir(folder)
>>> tiff_driver = gdal.GetDriverByName('GTiff')
>>> cols = int((maxx-minx)/cellsize)
>>> rows = int((maxy-miny)/cellsize)
>>> # I've just figured out how large the raster needs to be
>>> # smaller cell sizes result in more precise distances.
>>> # but they increase processing time.
>>> 
>>> roads_ds= tiff_driver.Create(road_raster_fn, cols, rows)
>>> roads_ds.SetProjection(
	road_lyr.GetSpatialRef().ExportToWkt())
0
>>> roads_ds.SetGeoTransform(
	(minx, cellsize, 0, maxy, 0, -cellsize))
0
>>> gdal.RasterizeLayer(road_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    gdal.RasterizeLayer(road_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
NameError: name 'road_ds' is not defined
>>> gdal.RasterizeLayer(roads_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
0
>>> roads_ds.FlushCache()
>>> roads_ds.FlushCache()
>>> roads_ds.FlushCache()
>>> gdal.RasterizeLayer(roads_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
0
>>> gdal.RasterizeLayer(roads_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
0
>>> roads_ds.FlushCache()
>>> 
roads_ds= tiff_driver.Create(road_raster_fn, cols, rows)
>>> roads_ds.SetProjection(
	road_lyr.GetSpatialRef().ExportToWkt())
0
>>> roads_ds.SetGeoTransform(
	(minx, cellsize, 0, maxy, 0, -cellsize))
0
>>> gdal.RasterizeLayer(roads_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
0
>>> roads_ds.FlushCache()
>>> roads_ds.FlushCache()
>>> roads_ds= tiff_driver.Create(road_raster_fn, bands=1, cols, rows)
SyntaxError: non-keyword arg after keyword arg
>>> roads_ds= tiff_driver.Create(road_raster_fn, cols, rows, bands=1)
>>> roads_ds.SetProjection(
	road_lyr.GetSpatialRef().ExportToWkt())
0
>>> roads_ds.SetGeoTransform(
	(minx, cellsize, 0, maxy, 0, -cellsize))
0
>>> gdal.RasterizeLayer(roads_ds, [1], road_lyr, burn_values=[1], callback=gdal.TermProgress)
0
>>> roads_ds.FlushCache()
>>> # I don't know why I get a black picture.
>>> 
>>> # lte's see what happens next
>>> prox_ds= tiff_driver.Create(proximity_fn, cols, rows, 1, gdal.GDT_Int32)
>>> prox_ds.SetProjection(roads_ds.GetProjection())
0
>>> prox_ds.SetGeoTransform(road_ds.GetGeoTransform())

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    prox_ds.SetGeoTransform(road_ds.GetGeoTransform())
NameError: name 'road_ds' is not defined
>>> prox_ds.SetGeoTransform(roads_ds.GetGeoTransform())
0
>>> gdal.ComputeProximity(roads_ds.GetRasterBand(1), prox_ds.GetRasterBand(1), ['DISTUNITS=GEO'], gdal.TermProgress)
0
>>> # I've got a black picture..
>>> # maybe at the end when I del ds it.
>>> 
