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
import scipy
import scipy.fftpack
from scipy import pi
import random

#outputfile----------------------------------------------------------------
inputfile = "./Ar_LJ_data5_10.csv"
positioninputfile = "./Ar_LJ_positions.csv"
saveas = 'Ar_LJ'

#conversions---------------------------------------------------------------
eV_to_Joules = 1.67e-19         #J
A_to_metres = 1e-10             #m
ps_to_s = 1e-12                 #s
amu_to_kg = 1.66e-27            #kg

Kb=1.3806488e-23
T=297
mass = 40*amu_to_kg           #kg
MM = 40              #gmol^-1
density = 1.4e6/1000            #gm^-3      
Na = 6.022e23        #mol^-1

atomicdensity=Na*density/MM;

header=[]
time=[]
x_positions_t0=[]
y_positions_t0=[]
x_positions=[]
y_positions=[]
E_total=[]
T_total=[]
V_total=[]
VAF_total=[]

fin=open(inputfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))


for line in fin:
    cols =line.strip('\n').split(',')

    time.append(float(cols[0]))

    E_total.append(float(cols[1]))

    T_total.append(float(cols[2]))

    V_total.append(float(cols[3]))

    VAF_total.append(float(cols[4]))
    

fin=open(positioninputfile,'r')
header.extend(fin.readline().rstrip('\n').split(','))

for line in fin:
    cols =line.strip('\n').split(',')

    x_positions_t0.append(float(cols[0]))

    y_positions_t0.append(float(cols[1]))

    x_positions.append(float(cols[2]))

    y_positions.append(float(cols[3]))
    


N = len(VAF_total)
fs = 1e13
df1 = 2*pi * (2.0/fs)
df2 = 2*pi * (5.0/fs)
t = scipy.linspace(time[0], time[len(time)-1], N)
x = [10*np.sin(n*df1) + 5*np.sin(n*df2) + 2*random.random() for n in range(N)]
acc = lambda t: 10*scipy.sin(2*pi*2.0*t) + 5*scipy.sin(2*pi*8.0*t) + 2*scipy.random.random(len(t))

signal=acc(t)
     
freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
xdft=abs(scipy.fft(VAF_total))
DOS = .5 * mass * xdft * atomicdensity / Kb / T

f7=plt.figure()
plt.subplot(311)
plt.plot(t, x)
plt.subplot(312)
plt.plot(freqs,20*scipy.log10(xdft),'x')
plt.subplot(313)
plt.plot(freqs*2*scipy.pi,DOS,'x')
plt.xlim([-50, 50])

#plot initial configuration-----------------------------------    
"""f1=plt.figure()
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
plt.ylim([-1.5, -1])
plt.title('Total Energy')
plt.xlabel('Time (ps)')
plt.ylabel('Energy (eV)')

f6=plt.figure()
for i in xrange(len(VAF_total)):
    plt.scatter(time[i]*ps_to_s**-1, VAF_total[i])
#plt.ylim([49.995, 50.1])
plt.title('VACF')
plt.xlabel('Time (ps)')
plt.ylabel('m^2s^-2')

f1.savefig(saveas +'Initial_pos.png')
f2.savefig(saveas + 'Final_pos.png')
f3.savefig(saveas +'Energy_potential.png')
f4.savefig(saveas +'Energy_kinetic.png')
f5.savefig(saveas +'Energy_total.png')
f6.savefig(saveas +'VACF.png')"""

f7.savefig(saveas +'FFT_DOS.png')

plt.show()


    
