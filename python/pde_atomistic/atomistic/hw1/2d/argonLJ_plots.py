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
inputfile = "./Ar_LJ_data5_10.csv"
positioninputfile = "./Ar_LJ_positions.csv"
vacfinputfile = "./Ar_LJ_VACF.csv"
saveas = 'Ar_LJ'

#conversions---------------------------------------------------------------
eV_to_Joules = 1.67e-19         #J
A_to_metres = 1e-10             #m
ps_to_s = 1e-12                 #s
amu_to_kg = 1.66e-27            #kg

header=[]
time=[]
x_positions_t0=[]
y_positions_t0=[]
x_positions=[]
y_positions=[]
E_total=[]
T_total=[]
V_total=[]
tau=[]
VACF=[]

fin=open(inputfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))


for line in fin:
    cols =line.strip('\n').split(',')

    time.append(float(cols[0]))

    E_total.append(float(cols[1]))

    T_total.append(float(cols[2]))

    V_total.append(float(cols[3]))


fin=open(positioninputfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))

for line in fin:
    cols =line.strip('\n').split(',')

    x_positions_t0.append(float(cols[0]))

    y_positions_t0.append(float(cols[1]))

    x_positions.append(float(cols[2]))

    y_positions.append(float(cols[3]))

fin=open(vacfinputfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))

for line in fin:
    cols =line.strip('\n').split(',')

    tau.append(float(cols[0]))

    VACF.append(float(cols[1]))


    

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

f3=plt.figure()
for i in xrange(len(V_total)):
    plt.scatter(time[i]*ps_to_s**-1, V_total[i])
plt.title('Potential Energy')
plt.xlabel('Time (ps)')
plt.ylabel('Energy (eV)')

f4=plt.figure()
for i in xrange(len(T_total)):
    plt.scatter(time[i]*ps_to_s**-1, T_total[i])
plt.title('Kinetic Energy')
plt.xlabel('Time (ps)')
plt.ylabel('Energy (eV)')

f5=plt.figure()
for i in xrange(len(E_total)):
    plt.scatter(time[i]*ps_to_s**-1, E_total[i])
#plt.ylim([-1.5, -1])
plt.title('Total Energy')
plt.xlabel('Time (ps)')
plt.ylabel('Energy (eV)')

f6=plt.figure()
for i in xrange(len(tau)):
    plt.scatter(tau[i]*ps_to_s**-1, VACF[i])
#plt.ylim([49.995, 50.1])
plt.title('VACF')
plt.xlabel('Time (ps)')
plt.ylabel('m^2s^-2')

f1.savefig(saveas +'Initial_pos.png')
f2.savefig(saveas + 'Final_pos.png')
f3.savefig(saveas +'Energy_potential.png')
f4.savefig(saveas +'Energy_kinetic.png')
f5.savefig(saveas +'Energy_total.png')
f6.savefig(saveas +'VACF.png')

plt.show()


    
