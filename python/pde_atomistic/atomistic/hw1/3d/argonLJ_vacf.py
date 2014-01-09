"""simple MD code - Argon in LJ potential
Using newton's force of motion and the
verlet algorhitm to calculate position
and velocity through time steps, arrive at
energies as function of time due to all
neighbor interactions
By: Caroline S. Gorham 17 April 2013"""

import sys
import numpy as np
import csv

np.seterr(all='ignore')

#outputfile names--------------------------------------------------------------------
outputfilename = "./Ar_LJ_data5_10.csv"
outputPOSfilename = "./Ar_LJ_positions.csv"
saveas = "Ar_LJ_data5_10"

#conversions-----------------------------------------------------------------------
eV_to_Joules = 1.67e-19         #J
A_to_metres = 1e-10             #m
ps_to_s = 1e-12                 #s
amu_to_kg = 1.66e-27            #kg

#parameters of LJ potential --------------------------------------------------------
epsilon = 0.0103*eV_to_Joules   #J
sigma = 3.405*A_to_metres       #meters

#lattice parameters --------------------------------------------------------------
Natoms= 1000
atoms_in_X = 10
atoms_in_Y= 10
atoms_in_Z= 10
mass = 40*amu_to_kg             #kg
R_min_energy=2.**(1./6)*sigma   #meters

#time details ----------------------------------------------------------------------
timestep = 0.01*ps_to_s         #s
total_time = 50*ps_to_s         #s
time = 0.0*ps_to_s              #s
time_in_step = np.arange(time,total_time,timestep,dtype=float)
    
def calcForces_and_potentialE(F_x, F_y,F_z, old_or_new, x_positions, y_positions, z_positions, V_atoms):
    """calculates x and y forces and potential energy per atom as summed over
    all contributions due to all neighbors, as functions of position and the
    parameters of the LJ potential"""

    for atom in xrange(Natoms):
        for i in xrange(Natoms):
            if i != atom:                    
                    delx = x_positions[atom,old_or_new]-x_positions[i,old_or_new]
                    dely = y_positions[atom,old_or_new]-y_positions[i,old_or_new]
                    delz = z_positions[atom,old_or_new]-z_positions[i,old_or_new]
                    r_ij = np.sqrt( (x_positions[atom,old_or_new]-x_positions[i,old_or_new])**2\
                                    + (y_positions[atom,old_or_new]-y_positions[i,old_or_new])**2\
                                    + (z_positions[atom,old_or_new]-z_positions[i,old_or_new])**2 )
                    F_x[atom,old_or_new] =  F_x[atom,old_or_new] - 24.0 *epsilon * sigma**6 \
                                           * delx * ( 1 - 2.0*(sigma/r_ij)**6 ) / r_ij**8
                    F_y[atom,old_or_new] =  F_y[atom,old_or_new] - 24.0 *epsilon * sigma**6 * \
                                           dely * ( 1 - 2.0*(sigma/r_ij)**6 ) / r_ij**8
                    F_z[atom,old_or_new] =  F_z[atom,old_or_new] - 24.0 *epsilon * sigma**6 * \
                                           delz * ( 1 - 2.0*(sigma/r_ij)**6 ) / r_ij**8  
                    V_atoms[atom] = V_atoms[atom] + 4.0 * epsilon \
                                    * ( (sigma/r_ij)**12-(sigma/r_ij)**6 )
                    if np.isnan(F_x[atom,old_or_new]) or np.isinf(F_x[atom,old_or_new]):
                        F_x[atom,old_or_new]=0
                    if np.isnan(F_y[atom,old_or_new]) or np.isinf(F_y[atom,old_or_new]):
                        F_y[atom,0]=0
                    if np.isnan(F_z[atom,old_or_new]) or np.isinf(F_z[atom,old_or_new]):
                        F_z[atom,0]=0
                    if np.isnan(V_atoms[atom]) or np.isinf(V_atoms[atom]):
                        V_atoms[atom]=0                   
    return F_x, F_y,F_z, V_atoms

#create position,velocity, force, and energy arrays ----------------------------------
x_velocities=np.zeros((Natoms, (round(total_time/timestep-time))), dtype=np.float)
x_positions=np.zeros((Natoms, 2), dtype=np.float)
F_atoms_x = np.zeros((Natoms, 2), dtype=np.float)

y_velocities=np.zeros((Natoms, (round(total_time/timestep-time))), dtype=np.float)
y_positions=np.zeros((Natoms, 2), dtype=np.float)
F_atoms_y = np.zeros((Natoms, 2), dtype=np.float)

z_velocities=np.zeros((Natoms, (round(total_time/timestep-time))), dtype=np.float)
z_positions=np.zeros((Natoms, 2), dtype=np.float)
F_atoms_z = np.zeros((Natoms, 2), dtype=np.float)

V_atoms = np.zeros((Natoms), dtype=np.float)
T_atoms = np.zeros((Natoms), dtype=np.float)
V_total = np.zeros((round(total_time/timestep-time)), dtype=np.float)
T_total = np.zeros((round(total_time/timestep-time)), dtype=np.float)
E_total = np.zeros((round(total_time/timestep-time)), dtype=np.float)

x_positions_t0 = np.zeros((Natoms), dtype=np.float)
y_positions_t0 = np.zeros((Natoms), dtype=np.float)
z_positions_t0 = np.zeros((Natoms), dtype=np.float)

x_velocities_t0 = np.zeros((Natoms), dtype=np.float)
y_velocities_t0 = np.zeros((Natoms), dtype=np.float)
z_velocities_t0 = np.zeros((Natoms), dtype=np.float)

VAF_atoms = np.zeros((Natoms), dtype=np.float)
VAF_total = np.zeros((round(total_time/timestep-time)), dtype=np.float)

#initialize positions -----------------------------------------------------------------
x=0
y=0
z=0
for atom in xrange(Natoms):
    x_positions[atom,0]=x*R_min_energy
    y_positions[atom,0]=y*R_min_energy
    z_positions[atom,0]=z*R_min_energy
    if x < atoms_in_X-1:
        x=x+1
    elif y >= atoms_in_Y-1:
        x=0
        y=0
        z=z+1
    elif x >= atoms_in_X-1 :
        x=0
        y=y+1
        

    x_velocities[atom,0] = 1
    y_velocities[atom,0] = 1
    z_velocities[atom,0] = 1

    x_positions_t0[atom] = x_positions[atom,0]
    y_positions_t0[atom] = y_positions[atom,0]
    z_positions_t0[atom] = z_positions[atom,0]
    
    x_velocities_t0[atom] = x_velocities[atom,0]
    y_velocities_t0[atom] = y_velocities[atom,0]
    z_velocities_t0[atom] = z_velocities[atom,0] 
    
    VAF_atoms[atom] = x_velocities_t0[atom]**2+y_velocities_t0[atom]**2+z_velocities_t0[atom]**2
    
VAF_total[0]=(1./Natoms) *np.sum(VAF_atoms[:])
VAF_total[0]=VAF_total[0]/VAF_total[0]
VAF_atoms[:] = 0

#initialize forces on each atom  at time_0  --------------------------------------------
(F_atoms_x, F_atoms_y, F_atoms_z, V_atoms) = \
                calcForces_and_potentialE(F_atoms_x, F_atoms_y, F_atoms_z,0, x_positions, y_positions, z_positions, V_atoms)
     
V_total[0] = np.sum(V_atoms[:]/2)*eV_to_Joules**-1
E_total[0] = (V_total[0]+T_total[0])
V_atoms[:]=0


#simulation interate over time-------------------------------------------------------------
for step in xrange(1, len(time_in_step)):  

    #calc position at current time---------------------------------------------------------
    for atom in xrange(Natoms):
        x_positions[atom,1] = x_positions[atom,0] + (timestep * x_velocities[atom,step-1]) \
                                  + (timestep**2 * F_atoms_x[atom,0] / (2.0*mass)) 
        y_positions[atom,1] = y_positions[atom,0] + (timestep * y_velocities[atom,step-1]) \
                                  + (timestep**2 * F_atoms_y[atom,0] / (2.0*mass))
        z_positions[atom,1] = z_positions[atom,0] + (timestep * z_velocities[atom,step-1]) \
                                  + (timestep**2 * F_atoms_z[atom,0] / (2.0*mass)) 
        x_positions[atom,0] = x_positions[atom,1] 
        y_positions[atom,0] = y_positions[atom,1]
        z_positions[atom,0] = z_positions[atom,1]
            
    #calc new forces and potential energies with new positions-----------------------------
    (F_atoms_x, F_atoms_y, F_atoms_z, V_atoms) = \
                calcForces_and_potentialE(F_atoms_x, F_atoms_y, F_atoms_z,1, x_positions, y_positions, z_positions, V_atoms)
    
    #calc new velocities and kinetic energy at current time----------------------------------
    for atom in xrange(Natoms):    
            x_velocities[atom,step] = x_velocities[atom,step-1] + \
                        ( timestep * (F_atoms_x[atom,1] + F_atoms_x[atom,0])/ (2.0*mass) )
            
            y_velocities[atom,step] = y_velocities[atom,step-1] + \
                        ( timestep * (F_atoms_y[atom,1]+F_atoms_y[atom,0]) / (2.0*mass) )
            z_velocities[atom,step] = z_velocities[atom,step-1] + \
                        ( timestep * (F_atoms_z[atom,1]+F_atoms_z[atom,0]) / (2.0*mass) )
            T_atoms[atom] = \
                        mass *( x_velocities[atom,step]**2 + y_velocities[atom,step]**2 + z_velocities[atom,step]**2)  / 2.0
            if np.isnan(T_atoms[atom]) or np.isinf(T_atoms[atom]):
                        T_atoms[atom]=0

            t0=time
            t0index=0
            while t0 < time_in_step[step]:

                t0index=t0index+1
                
                VAF_atoms[atom] = VAF_atoms[atom] + (x_velocities[atom,t0index-1]*x_velocities[atom,step]\
                              + y_velocities[atom,t0index-1]*y_velocities[atom,step]+ \
                              z_velocities[atom,t0index-1]*z_velocities[atom,step])\
                              / (x_velocities[atom,t0index-1]**2 +y_velocities[atom,t0index-1]**2+z_velocities[atom,t0index-1]**2)
                t0=t0+timestep

            VAF_atoms[atom] = VAF_atoms[atom]/t0index

            x_velocities[atom,step-1]= x_velocities[atom,step]
            y_velocities[atom,step-1]= y_velocities[atom,step]
            z_velocities[atom,step-1]= z_velocities[atom,step]
            F_atoms_x[atom, 0] = F_atoms_x[atom, 1]
            F_atoms_y[atom, 0] = F_atoms_y[atom, 1]
            F_atoms_z[atom, 0] = F_atoms_z[atom, 1]

    VAF_total[step]= (np.sum(VAF_atoms[:]/Natoms))
    V_total[step] = np.sum(V_atoms[:]/2)*eV_to_Joules**-1
    T_total[step] = np.sum(T_atoms[:])*eV_to_Joules**-1
    E_total[step] = (V_total[step]+T_total[step])
    F_atoms_x[:, 1] = 0
    F_atoms_y[:, 1] = 0
    F_atoms_z[:, 1] = 0
    VAF_atoms[:] = 0
    V_atoms[:] = 0
    T_atoms[:] = 0

#write data to disk-------------------------------------------------------------------
outputfile=open(outputfilename,"wb")
data_file=csv.writer(outputfile, delimiter=",")
data_file.writerow(['Time (ps)','Total Energy (eV)','Kinetic Energy (eV)','Potential Energy (eV)', 'VACF'])
for row in xrange(len(time_in_step)):
    data_file.writerow([time_in_step[row]*ps_to_s**-1, E_total[row], T_total[row], V_total[row], VAF_total[row]])
outputfile.close()

posoutputfile=open(outputPOSfilename,"wb")
data_file=csv.writer(posoutputfile, delimiter=",")   
data_file.writerow(['initialpos, x', 'initialpos, y', 'initialpos, z', 'finalpos, x', 'finalpos, y','finalpos, z'])
for atom in xrange(Natoms):
    data_file.writerow([x_positions_t0[atom], y_positions_t0[atom],z_positions_t0[atom],\
                        x_positions[atom,1], y_positions[atom,1], z_positions[atom,1]])
posoutputfile.close()
