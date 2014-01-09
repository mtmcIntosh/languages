""" Read .CSV output file of bird sightings
created by importList_makeList.py,
parse into array structures according to headers
Determine the first time derivative  - and plot .
By: Caroline Gorham 08 Feb 2013
IMP variables: year[], number[], derivative[]
"""

import numpy as np
import matplotlib.pylab as plt
import csv

"""header and column array initializations """
header=[]

year=[]

number=[]


"""file name"""
filename="numberVyear.csv"



""" open and read csv file into appropriate arrays """

fin=open(filename,'r')

header.extend(fin.readline().rstrip('\r\n').split(','))

 
for line in fin:
    cols=line.rstrip('\r\n').split(',')

    year.append(int(cols[0]))

    number.append(int(cols[1]))



"""compute the derivative """
derivative=[]

for row in xrange(len(year)):
    
    if row > 0:
        derivative.append((number[row]-number[row-1])/(year[row]-year[row-1]))



"""plot """

f1=plt.figure()
plt.plot(year[1:], derivative, '-o')
plt.xlabel(header[0] )
plt.xticks(np.arange(5,120,10))
plt.yticks(np.arange(-1500,1700,200))
plt.ylabel("derivative")
plt.savefig('derivative.pdf')
plt.show()
