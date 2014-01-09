"""KMCS to model the co-adsorption
of A, irreversible reaction of A to B,
and desorption of B on a square lattice.
By: Caroline S Gorham, 30April2013 """

import sys
import numpy as np
import matplotlib.pylab as plt
import random
import decimal
import math
import csv

k_indicator = '_allsamek_A5_EA5E3_3'
KMCSdescription = 'AtoBirreversible'

# scientific values --------------
Kb = 1.38e-23      # JK^-1
Na = 6.022e23       #mol^-1
#conversions-----------------------------------------------------------------------
eV_to_Joules = 1.67e-19         #J
A_to_metres = 1e-10             #m
ps_to_s = 1e-12                 #s
amu_to_kg = 1.66e-27            #kg
#lattice parameters --------------------------------------------------------------
Natoms= 50
atoms_in_X = 5
atoms_in_Y= 10
R_min_energy = 2
#time details ----------------------------------------------------------------------
total_time = 10         #s
#environment ----------------------
T_array = np.linspace(101,401, 4)
# Arrhenius parameters --------------------------
A_A, E_A = 5, 5e3 / Na
A_Ax, E_Ax = 5, 5e3/ Na 
A_AB, E_AB = 5, 5e3/ Na
A_Bx, E_Bx = 5, 5e3/ Na 


class particle(object):
    """class to track probabilities and consequences of  events for particles
    which have given positions, activation energies, temperatures"""

    def __init__(self, x, y, T):

        self.T = T

        self.k_A_init =  A_A * math.exp(-E_A/Kb/ self.T)
        self.k_AB_init = A_AB * math.exp(-E_AB/Kb/ self.T)
        self.k_Ax_init = A_Ax * math.exp(-E_Ax/Kb/ self.T)
        self.k_Bx_init = A_Bx * math.exp(-E_Bx/Kb/ self.T)
        self.x_position = x*R_min_energy
        self.y_position = y*R_min_energy
        self.occupation = 0
        self.k_A = self.k_A_init
        self.k_AB = 0
        self.k_Bx = 0
        self.k_Ax = 0

    def adsorb (self):

        self.occupation = 1
        self.k_A = 0
        self.k_AB = self.k_AB_init
        self.k_Ax = self.k_Ax_init

    def irreversible (self):

        self.k_Ax = 0
        self.k_AB = 0
        self.k_Bx = self.k_Bx_init

    def desorb (self, *args):

        self.occupation = 0
        for x in args:
            if x is 'A':
                self.k_Ax = 0
                self.k_A = self.k_A_init
                self.k_AB = 0
            elif x is 'B':
                self.k_Bx = 0
                self.k_A = self.k_A_init

    def events (self, events_total):
        self.S_kA = self.k_A / events_total * 100
        self.S_kAx = self.k_Ax / events_total * 100
        self.S_kAB = self.k_AB / events_total * 100
        self.S_kBx = self.k_Bx / events_total * 100

# run simulation for each temperature
for T in T_array:
    
    key_exp_label = '%d' %atoms_in_X +'x%d'%atoms_in_Y+ '_' +str(int(T)) + k_indicator

    #initialize event array information
    time = 0.0              #s
    processes = ['start']
    processID = [-1]
    A=[0]
    B=[0]
    Ax=[0]
    Bx=[0]
    x_position=[0]
    y_position=[0]
    timerecord = [time]
    coverage_A=[0]
    coverage_B=[0]
    empty_sites=[Natoms]
    
    atoms=np.empty((Natoms), dtype=particle)
    #initialize positions -------------------
    x=0
    y=0
    for atom_count in xrange(Natoms):
        atoms[atom_count]=particle(x,y, T)
        if x < atoms_in_X-1:
             x=x+1
        else:
            x=0
            y=y+1

    #run simulation in event-dependent time steps until the sim. time is reached ----
    i=1
    while time <= total_time:

        # generate random number - event probability 
        a = float(decimal.Decimal((random.random())))*100

        # calculate the total transition coefficients of all the events
        events_total=0
        for atom in atoms:
            events_total = events_total + atom.k_A + atom.k_Ax + atom.k_AB + atom.k_Bx
        if events_total==0:
            break;

        # calculate the probability of each event for each atom in the lattice
        for atom in atoms:
            atom.events(events_total)

        # caculate the time-step of the event
        dt = - np.log(a/100) / events_total

        # determine which event occurs and which lattice site --------------
        step=0
        for atom in atoms:
            if ((step) < a <= (step + atom.S_kA)) and atom.S_kA != 0:
                processes.append( 'k_A')
                processID.append(0)
                atom.adsorb()
                x_position.append(atom.x_position)
                y_position.append(atom.y_position)
            elif (step + atom.S_kA) < a <= (step + atom.S_kA + atom.S_kAx) and atom.S_kAx != 0:
                processes.append ( 'k_Ax')
                processID.append(1)
                atom.desorb('A')
                x_position.append(atom.x_position)
                y_position.append(atom.y_position)
            elif (step + atom.S_kA + atom.S_kAx)  < a <= (step + atom.S_kA + atom.S_kAx + atom.S_kAB) and atom.S_kAB != 0:
                processes.append('k_AB')
                processID.append(2)
                atom.irreversible()
                x_position.append(atom.x_position)
                y_position.append(atom.y_position)
            elif (step + atom.S_kA + atom.S_kAx + atom.S_kAB)  < a <= \
                 (step + atom.S_kA + atom.S_kAx + atom.S_kAB + atom.S_kBx) and atom.S_kBx != 0:
                processes.append('k_Bx')
                processID.append(3)
                atom.desorb('B')
                x_position.append(atom.x_position)
                y_position.append(atom.y_position)
            step = (step + atom.S_kA + atom.S_kAx + atom.S_kAB + atom.S_kBx)

        # maintain running list of event occurances
        A.append(A[i-1])
        Ax.append(Ax[i-1])
        B.append(B[i-1])
        Bx.append(Bx[i-1])
        coverage_A.append(coverage_A[i-1])
        coverage_B.append(coverage_B[i-1])
    
        if processID[i]==0:
            A[i]=(A[i]+1)
            coverage_A[i]=(coverage_A[i]+1)
        elif processID[i]==1:
            Ax[i]=(Ax[i]+1)
            coverage_A[i]=(coverage_A[i]-1)
        elif processID[i]==2:
            B[i]=(B[i]+1)
            coverage_A[i]=(coverage_A[i]-1)
            coverage_B[i]=(coverage_B[i]+1)
        elif processID[i]==3:
            Bx[i]=(Bx[i]+1)
            coverage_B[i]=(coverage_B[i]-1)
            
        empty_sites.append(Natoms-(coverage_A[i])-(coverage_B[i]))

        # advance the time-step of the event, keep track of the next start time and
        # index for lists        
        time = time + dt
        timerecord.append(time)
        i=i+1
        
    #write data to disk-------------------------------------------------------------------
    outputfilename = './' + KMCSdescription + key_exp_label + '.csv'
    saveas = KMCSdescription + key_exp_label
    
    outputfile=open(outputfilename,"wb")
    data_file=csv.writer(outputfile, delimiter=",")
    data_file.writerow(['Time (ps)','Event','x position','y position', 'Running Coverage - A', \
                        'Running Coverage - B', 'empty sites', '% coverage'])
    for row in xrange(len(timerecord)):
        data_file.writerow([timerecord[row], processes[row], x_position[row], \
                            y_position[row], coverage_A[row],coverage_B[row], \
                            empty_sites[row], \
                            empty_sites[row]/float(Natoms)*100])
    outputfile.close()

    # make plots
    f1=plt.figure()
    ax1 = f1.add_subplot(311)
    ax1.scatter(timerecord, coverage_A, facecolors='none', edgecolors='r', label='A')
    ax1.scatter(timerecord, coverage_B, facecolors='none', edgecolors='b', label='B')
    ax1.scatter(timerecord, empty_sites, facecolors='none', edgecolors='g', label='empty sites')
    plt.title('A and B coverage ',fontsize=12)
    plt.ylabel('number',fontsize=12)
    ax1.legend(loc='upper right',prop={'size':7})
    ax1.set_xticklabels([])
    plt.xlim([0, total_time])
    plt.ylim([0, np.max([np.max(coverage_A),np.max(coverage_B),np.max(empty_sites)])])
    
    ax2 = f1.add_subplot(312)
    for i in xrange(len(timerecord)):
        if A[i]>A[i-1]:
            ax2.scatter(timerecord[i], A[i], facecolors='none', edgecolors='r')
        if B[i]>B[i-1]:
            ax2.scatter(timerecord[i], B[i], facecolors='none', edgecolors='b')
    plt.title('A adsorption, B converted ',fontsize=12)
    plt.ylabel('number',fontsize=12)
    ax2.set_xticklabels([])
    plt.xlim([0, total_time])
    plt.ylim([0, np.max([np.max(A),np.max(B)])])

    ax3 = f1.add_subplot(313)
    for i in xrange(1, len(timerecord)):
        if Ax[i]>Ax[i-1]:
             ax3.scatter(timerecord[i], Ax[i], facecolors='none', edgecolors='r')
        if Bx[i]>Bx[i-1]:
            ax3.scatter(timerecord[i], Bx[i], facecolors='none', edgecolors='b')
    plt.title('A and B desorbtion',fontsize=12)
    plt.xlabel('Time',fontsize=12)
    plt.ylabel('number',fontsize=12)
    plt.xlim([0, total_time])
    plt.ylim([0, np.max([np.max(Ax),np.max(Bx)])])

    f1.savefig(saveas +'.png')

plt.show()
    
