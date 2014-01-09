'''
- reads and plots  the temperature [F] data from ./VARICHMO.txt
- rejects data that has a value of -99
- rejects data that is outside the reasonable centere of data
- compreses the array of data, converts to [C]
- plots the temperature [C]

By: Caroline Gorham, 25 Feb 2013
'''

import numpy as np
import matplotlib.pylab as plt
import sys
import stats
import units


def main():

    temperature=[]


    """ file names"""
    filename="./VARICHMO.txt"


    """ open and read csv file into header and appropriate list"""
    fin=open(filename,'r')
    

    for line in fin:
        cols=line.strip('\n').split()
    
        temperature.append(float(cols[3]))

    """convert list to a numpy array for further processing """
    temperature=np.array(temperature)

        
    """plot temp[F] as function of time -  before clean _ save"""
    f1=plt.figure()

    for temp in xrange(len(temperature)):
        plt.plot(temp+1, temperature[temp], '-o')
    
    plt.xlabel('arb.' )
    plt.ylabel('temperature [F]' )
    plt.xticks(np.arange(0,(16*360),(360)))
    plt.yticks(np.arange(0,100,5))
    f1.savefig('temperature_before_clean.png')


    """find and replace missing data using the missing_check
    function from stats module - print the number of replaced elements"""
    print "There are %d" %stats.missing_check(temperature) + " missing data points."


    """find and reject outlier data using the reject_outliers
    function from stats module"""
    valid=stats.reject_outliers(temperature)


    """compress the array to only valid data points """
    temperature_masked=temperature[valid]


    """convert the data to Celsius using the F_to_C function
    from units module"""        
    temperature_celsius=units.F_to_C(temperature_masked)
    
    """Plot the compressed data array [C] -  after clean _ save """
    f1=plt.figure()

    for temp in xrange(len(temperature_celsius)):
        plt.plot(temp+1, temperature_celsius[temp], '-o')

    plt.xlabel('arb.' )
    plt.ylabel('temperature [C]' )
    plt.xticks(np.arange(0,(16*360),(360)))
    plt.yticks(np.arange(0,15,5))
    f1.savefig('temperature_after_clean.png')
    
    plt.show()


if __name__=="__main__":
    
    sys.exit(main())
