"""
Module containing code to
1. calculate the maximum elevation
2. calculate the minimum elevation
3. calculate the surface area
of the specified planet and its ocean.
4. calculate the Volume of the ocean 
By: Caroline Gorham 6 March 2013
"""

import numpy as np
import math

radius = 6378.1  #km
degree_to_radius = math.pi/180


def maxEl(grid):
    """return the elevation array location of the
    maximum elevation"""
    return (np.where(grid == np.max(grid)))


def minEl(grid):
    """return the elevation array location of the
    minimum elevation"""
    return (np.where(grid == np.min(grid)))

def ocean_SurfaceArea( lon, lat, grid):
    """return the surface_area of the specified 
    planet and its ocean"""
    
    planet_surfaceArea=np.zeros(grid.shape)
    ocean_surfaceArea=0

    #calculate the surface area  of the planet as an array and sum over each element
    planet_surfaceArea=[[radius**2*np.cos(row*(degree_to_radius))*\
                 (math.pi/len(lat))*(2*math.pi/len(lon)) for col in lon] for row in lat]   # km^2
    
    planet_surfaceArea=np.sum(planet_surfaceArea)

    #calculate the surface area of the ocean as running sum for each element where the
    #elevation is <0
    for row in xrange(len(grid[:][:])):
        for col in xrange(len(grid[1][:])):
            if grid[row,col] < 0:
                ocean_surfaceArea= ocean_surfaceArea + radius**2*\
                    np.cos(lat[row]*(degree_to_radius))*(math.pi/len(lat))*\
                    (2*math.pi/len(lon))                                                    # km^2

    return planet_surfaceArea, ocean_surfaceArea 


def ocean_Volume( lon, lat, grid):
    """return the volume of the ocean"""

    ocean_Volume=0

    #calculate the volume of the ocean as running sum for each element where the
    #elevation is <0
    for row in xrange(len(lat)):
        for col in xrange(len(lon)):
            if grid[row,col] < 0:
                ocean_Volume=ocean_Volume + (1./3)*math.pi*radius**2*\
                                             np.cos(lat[row]*(degree_to_radius))*(math.pi/len(lat))*\
                                             (2*math.pi/len(lon)) * abs(grid[row,col]) * (10**3)**2   #m^3

    return ocean_Volume 



