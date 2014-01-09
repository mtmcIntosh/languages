"""simple MD code - Argon in LJ potential
Using newton's force of motion and the
verlet algorhitm to calculate position
and velocity through time steps, arrive at
energies as function of time due to all
neighbor interactions
By: Caroline S. Gorham 17 April 2013"""

import sys
import numpy as np
import matplotlib.pylab as plt
import csv

#outputfile----------------------------------------------------------------
initialpositionfile = "./dump.0.xyz"
finalpositionfile = "./dump.5000.xyz"
saveas = '10nm_heat'

#conversions---------------------------------------------------------------
eV_to_Joules = 1.67e-19         #J
A_to_metres = 1e-10             #m
ps_to_s = 1e-12                 #s
amu_to_kg = 1.66e-27            #kg

atoms=[]
header=[]
x_positions_t0=[]
y_positions_t0=[]
z_positions_t0=[]
x_positions=[]
y_positions=[]
z_positions=[]


fin=open(inputpositionfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))

atoms=fin.readline()
header=fin.readline()

for line in fin:
    cols =line.strip('\n').split(',')
    

    x_positions_t0.append(float(cols[1]))

    y_positions_t0.append(float(cols[2]))

    z_positions_t0.append(float(cols[3]))

    
fin=open(finalpositionfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))

atoms=fin.readline()
header=fin.readline()

for line in fin:
    cols =line.strip('\n').split(',')

    x_positions.append(float(cols[1]))

    y_positions.append(float(cols[2]))

    z_positions.append(float(cols[3]))

    

#plot initial configuration-----------------------------------    
f1=plt.figure()
for i in xrange(len(x_positions_t0)):
    plt.scatter(x_positions_t0[i]*A_to_metres**-1, y_positions_t0[i]*A_to_metres**-1)
plt.title('Initial')
plt.xlabel('Distance (Ang)')
plt.ylabel('Distance (Ang)')
plt.ylim([-1,40])
plt.xlim([-1,40])

#plot data ---------------------------------------------------------------------------
f2=plt.figure()
for i in xrange(len(x_positions)):
    plt.scatter(x_positions[i]*A_to_metres**-1, y_positions[i]*A_to_metres**-1)
plt.title('Final')
plt.xlabel('Distance (Ang)')
plt.ylabel('Distance (Ang)')


f1.savefig(saveas +'Initial_pos.png')
f2.savefig(saveas + 'Final_pos.png')
plt.show()


    
