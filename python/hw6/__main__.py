"""
Code to read in a degree based elevation file
of a spherical body -  plot the elevation -  determine the min
and max el. - determine the surface area of the sphere and the
surface area and volume of mass below 'sealevel'.
Code is also provided to parse out a section of the array and plot
the individual section.
By: Caroline Gorham 6 March 2013
"""

import sys
from optparse import OptionParser
import numpy as np
import pylab as plt

import geo
import gridSize
import gridPlotter

############ tilt the figures for ease of viewing
############ plots in 2d contour
############ no hard coding of number of points, able to work with any input resolutions

def main():
   """main function, in two sections - command line option parser - program objective  """

   # command line parser to populate lat, latres, lon, lonres, and filename
   usage = "usage: %prog [options]  --planet=opt1 --lat=opt2 --latres=opt3" \
   "--lon=opt4 --lonres=opt5 filename"

   parser = OptionParser(usage=usage, version="%prog 1.0")

   parser.add_option("--planet", type="string", dest="option1", default="Earth",
                     help="which planet are these calculations for")
 

   parser.add_option("--lat", type="float", dest="option2", default="0",
                  help="at which degree latitude does the file start (in N)")


   parser.add_option("--latres", type="float", dest="option3", default="1",  
                  help="what is the resolution of degree latitude in the file (in N from tropic)")


   parser.add_option("--lon",type="float", dest="option4", default="0",  
                  help="at which degree longitude does the file start (in E from meridian)")


   parser.add_option("--lonres", type="float", dest="option5", default="1",
                  help="what is the resolution of degree longitude in the file")

   (options, args) = parser.parse_args()

   planet=(options.option1)
   lat=(options.option2)
   latres=(options.option3)
   lon=(options.option4)
   lonres=(options.option5)


   #try to open file specified, if none specified exit
   if len(args) < 1:
      print "No file specified"
      sys.exit()
   else:
      infile=args[0]

   try:
       grid=np.loadtxt(infile, unpack=False,skiprows=0, dtype=float)
   except IOError:
      print "Cannot read file"
      sys.exit()

   
   latcell=len(grid[:][:])
   loncell=len(grid[1][:])

   # x in longitude (cols in grid)
   x_easter=np.c_[np.linspace(lon, 180+(lon-lonres), ((180)/lonres))]
   x_wester=np.c_[np.linspace(-180+(lon-lonres), (lon-lonres), ((180)/lonres))]
   
   x=np.concatenate((x_easter, x_wester), axis=0)

   # y in latitude (rows in grid)                  
   y=np.c_[np.linspace(lat, -(lat-latres), ((180)/latres))]


   #plot elevation over the entire grid, indicate the max and min on the plot 
   ax1=gridPlotter.plotsContour(x, y, grid,'EARTH', '(-180)W (+180)E', '(-90)S (+90)N','world_elevation', Min = "y", Max = "y")

   #compute  the Earth and ocean surface areas, ocean volume, and print to screen 
   surface_Areas=geo.ocean_SurfaceArea(x , y,  grid)
   ocean_volume=geo.ocean_Volume(x , y,  grid)

   print "The surface area of %s" %planet +" is %d" %surface_Areas[0] + " km^2."
   print "The ocean surface area is %d" %surface_Areas[1] + " km^2."
   print "The ocean volume is %d" %ocean_volume + " m^3."

   #gridSize.special_contour used to isolate elevation extract
   #from (lonmin, lonmax), (latmin,latmax)
   gridInfo1=gridSize.special_contour(x , y,  grid, (-130, -60), (12, 66.5))

   #plot elevation over the special_contour
   ax2=gridPlotter.plotsContour(gridInfo1[0], gridInfo1[1], gridInfo1[2],'NORTH AMERICA', '(-180)W (+180)E',\
                          '(-90)S (+90)N','north_america')

   plt.show()

if __name__=="__main__":
    
    sys.exit(main())
    
