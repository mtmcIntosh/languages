"""
Code to make 3d plots.
Options Min and Max are accepted which
find min and max using geo.minEl and maxEl,
and indicate their positions on the figure
By: Caroline Gorham 6 March 2013
"""

import numpy as np
import pylab as plt
from matplotlib import cm


import geo
import gridSize


def figure(X, Y, Z, Xrange, Yrange, title, Xaxis, Yaxis, saveas, *args):
   """constructs the colored contour figure based on either one or more
   sclices required due to any crossing accross that may occur across
   boundaries of the graphic - however, these additional splices shouldn't
   be required"""

   fig, ax = plt.subplots()
   p = ax.pcolor(X, Y, Z)
   ax.contour(X, Y, Z, colors='black', linewidth=.5)

   i=0
   if args:
      p = ax.pcolor(args[i+0], args[i+1],args[i+2])
      ax.contour(args[i+0], args[i+1],args[i+2], colors='black', linewidth=.5)
      i=i+3
      
   b = fig.colorbar(p, orientation='vertical')
   plt.title(title, fontsize=14, fontweight='bold')
   plt.xlabel(Xaxis)
   plt.ylabel(Yaxis)

   return fig, ax


def plotsContour(x, y, grid, Xrange, lonres,  Yrange, latres, title, Xaxis, Yaxis, saveas, **options):
   """x y and grid are dimensions of the 3d plot - Min and Max are
   accepted as options"""
      
   X,Y = np.meshgrid(x, y)    
   Z = grid
   plot=figure(X, Y, Z, Xrange, Yrange, title, Xaxis, Yaxis, saveas)
   
   
   # if min and/or max is indicated as an option, find them using the geo.minEl
   # function and indicate on the 3d plot with a star and label
   if options.get("Min") == "y":
       (xmin,ymin)=geo.minEl(grid)
       plot[1].plot(x[ymin], y[xmin], 'w*', markersize=12)
       plot[1].text(x[ymin], y[xmin], "MIN",fontsize=15, weight='bold',color="w" )
       print "The min elevation is %d" %grid[xmin,ymin] +" m."

   if options.get("Max") == "y":
       (xmax,ymax)=geo.maxEl(grid)
       plot[1].plot(x[ymax], y[xmax],  'w*', markersize=12)
       plot[1].text(x[ymax], y[xmax], "MAX",fontsize=15, weight='bold',color="w" )
       print "The max elevation is %d" %grid[xmax,ymax]+" m."

   plot[0].savefig(saveas +'_elevation.png')
