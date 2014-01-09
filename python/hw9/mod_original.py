import sys
import math
import time

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Bad coding example 1
#
# Original Fortran version shamefully written by Ross Walker (SDSC, 2006)
# Python version by Katherine Holcomb, 2011-2013
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
#             exp(rij*qi)*exp(rij*qj)   1
#    E = Sum( ----------------------- - - )  (rij <= cut)
#        j<i           r(ij)            a
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

def read_data(filename):
   fp=open(filename)
   natom=int(fp.readline().strip())

   coords=[[0.0 for j in range(3)] for i in range(natom)]
   q=[0]*natom

   # read the coordinates and charges.
   count=0
   for line in fp:
     linelist=[]
     coords[count]=[]
     linelist=map(float,line.strip().split())
     coords[count].extend(linelist[0:3])
     q[count]=linelist[3]
     count+=1

   return (natom,coords,q)

def calc_pairs(natom,cut,a,coords,q):
   from numpy import sqrt
   
   total_e = 0.0
   cut_count = 0
   vec2=[]
   rij=float
   count=0
   vec2=[[0.0] for j in range(natom**2)]
   vec2[count]=[]
   for i in range(natom):
      for j in range(natom):
          if ( j < i ):   #Avoid double counting.
               vec2[count]=((coords[i][0]-coords[j][0])**2   \
                    + (coords[i][1]-coords[j][1])**2   \
                    + (coords[i][2]-coords[j][2])**2)
               count+=1

   ########reduce the amount of times that math.sqrt is called           
   #X^2 + Y^2 + Z^2
   rij = sqrt(vec2)
   #Check if this is below the cut off
   for cell in xrange(len(rij)):
      if ( rij[cell] <= cut ):
         #Increment the counter of pairs below cutoff

         ####### 1  make 2 exponents into one
         current_e = (math.exp(rij[cell]*(q[i]+q[j])))/rij[cell]
         total_e = total_e + current_e - 1.0/a

   return (cut_count,current_e,total_e)

def write_data(cut_count,total_e,time0,time1,time2):
   print 'Value of system clock after coord read and E calc = %14.4f'%time2

   print '                         Final Results' 
   print '                         -------------'
   print '                   Num Pairs = %14.4f ' %cut_count
   print '                     Total E = %14.4f' %total_e
   print '     Time to read coord file = %14.4f Seconds'% (time1-time0)
   print '     Time to calculate E = %14.4f Seconds'% (time2-time1)
   print '     Total Execution Time = %14.4f Seconds'% (time2-time0)
 
   return None


a = 3.2

time0=time.clock()
print 'Value of system clock at start = %14.4f'%time0

# Step 1 - obtain the filename of the coord file and the value of
# cut from the command line.
#         Argument 1 should be the filename of the coord file (char).
#         Argument 2 should be the cut off (float).
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

# Step 2 - Open the coordinate file and read the first line to
# obtain the number of atoms

(natom,coords,q)=read_data(filename)

time1=time.clock()
print 'Value of system clock after coord read = %14.4f'%time1

# Step 3 - calculate the number of pairs and E. - this is the
# majority of the work.
(cut_count,current_e,total_e)=calc_pairs(natom,cut,a,coords,q)

#time after reading of file and calculation
time2=time.clock()

# Step 6 - write out the results
write_data(cut_count,total_e,time0,time1,time2)
