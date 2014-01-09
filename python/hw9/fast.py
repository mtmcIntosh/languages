import sys
import math
import time

import numpy as np
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# HPC Bootcamp lab1 Homework
# Mon Jun 13 21:18:22 EDT 2011
# Optimized to use numpy arrays by Mitch Smith (mms7r@virginia.edu)
# Note: the I9 first line count of records in the input file is ignored
# in this version. The count is determined dynamically from the shape
# of the data array.
#
# From original bad code example:
# Original Fortran version shamefully written by Ross Walker (SDSC, 2006)
#
# This code reads a series of coordinates and charges from the file
# specified as argument $1 on the command line.
#
# This file should have the format:
#  I9
# 4F10.4   (repeated I9 times representing x,y,z,q)
#
# It then calculates the following fictional function:
#
#			 exp(rij*qi)*exp(rij*qj)   1
#	E = Sum( ----------------------- - - )  (rij <= cut)
#		j<i		   r(ij)			a
#
# where cut is a cut off value specified on the command line ($2), 
# r(ij) is a function of the coordinates read in for each atom and 
# a is a constant.
#
# The code prints out the number of atoms, the cut off, total number of
# atom pairs which were less than or equal to the distance cutoff, the
# value of E, the time take to generate the coordinates and the time
# taken to perform the calculation of E.
#
# All calculations are done in double precision.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = 3.2

time0=time.clock()
print 'Value of system clock at start = %14.4f'%time0

# Step 1 - obtain the filename of the coord file and the value of
# cut from the command line.
#		 Argument 1 should be the filename of the coord file (char).
#		 Argument 2 should be the cut off (float).
argv=sys.argv
if len(argv) < 3:
   print "Too few arguments"
else:
   try:
	  filename=argv[1]
	  print "Coordinates will be read from file: %s"%filename
	  cut=float(argv[2])
   except(TypeError,ValueError):
	  print "Input error"

# Step 2 - read the coordinates and charges.
data = np.loadtxt(argv[1], skiprows=1)
natom = data.shape[0]
x = (data[:,0])
y = (data[:,1])
z = (data[:,2])
q = (data[:,3])

print 'Natom = %d'% natom
print '  cut = %10.3e'% cut

time1=time.clock()
print 'Value of system clock after coord read = %14.4f'%time1

# Step 3 - calculate the number of pairs and E. - this is the
# majority of the work.
total_e = 0.0
cut_count = 0

cut2 = cut * cut
pera = 1.0/a

for i in range(1, len(x)):
   deltax = x[i:natom] - x[0:-i]
   deltay = y[i:natom] - y[0:-i]
   deltaz = z[i:natom] - z[0:-i]
   qi = q[i:natom]
   qj = q[0:-1]
   vec2 = deltax*deltax + deltay*deltay + deltaz*deltaz
   idx = (vec2 <= cut2).nonzero()
   vec = np.sqrt(vec2[idx])
   cut_count += len(vec)
   current_e = sum(np.exp(vec * (qi[idx] + qj[idx]))/vec)
   total_e += current_e

total_e = total_e - (pera * cut_count)

#time after reading of file and calculation
time2=time.clock()
print 'Value of system clock after coord read and E calc = %14.4f'%time2

# Step 4 - write out the results
print '                         Final Results' 
print '                         -------------'
print '                   Num Pairs = %14.4f ' %cut_count
print '                     Total E = %14.4f' %total_e
print '     Time to read coord file = %14.4f Seconds'% (time1-time0)
print '     Time to calculate E = %14.4f Seconds'% (time2-time1)
print '     Total Execution Time = %14.4f Seconds'% (time2-time0)
