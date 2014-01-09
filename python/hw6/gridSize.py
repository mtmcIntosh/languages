"""
Code to isolate an extract from the
elevation array between prescribed
longitude and latitude points
By: Caroline Gorham 6 March 2013
"""

import numpy as np

def special_contour(lon, lat, grid, (lower_lon, upper_lon),(lower_lat, upper_lat)):
   """accept original lat,lon,grid arrays and bounds as isolation parameters"""

   # save original arrays for safekeeping
   latorig=lat
   lonorig=lon

   # determine which cells meet lie within the prescribed bounds, mask others
   nzcond_lat=np.nonzero((lower_lat <= lat) & (lat <= upper_lat))
   nzcond_lon=np.nonzero((lower_lon <= lon) & (lon <= upper_lon))

   lat=lat[nzcond_lat]
   lon=lon[nzcond_lon]

   # initialize new grid to be shape of new lat and lon arrays
   contourgrid= np.zeros(shape=(len(lat), len(lon)))
   
   for row in xrange(len(lat)):
        for col in xrange(len(lon)):

               cellInLat= np.where(latorig==lat[row])   
               cellInLon= np.where(lonorig==lon[col])
               
               # amend the new grid cells consecutively with the elevation 
               # data corresponding to the latitude and longitude 
               contourgrid[row,col] = grid[cellInLat[0],cellInLon[0]]
                
   
   return lon, lat, contourgrid
