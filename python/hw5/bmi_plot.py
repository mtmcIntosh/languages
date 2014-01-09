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
import units
import stats



def main():

    header=[]
    body_fat_percent=[]
    age=[]
    weight_lbs=[]
    height_inches=[]

    """ file names"""
    filename="./bodyfat.csv"

    
    """ open and read csv file into header and appropriate arrays"""
    fin=open(filename,'r')

    """reads and records the header """
    header.extend(fin.readline().rstrip('\n').split(','))

    """ reads and records appropriate arrays"""
    for line in fin:
        cols=line.strip('\n').split(',')

        body_fat_percent.append(float(cols[0]))

        age.append(float(cols[1]))

        weight_lbs.append(float(cols[2]))

        height_inches.append(float(cols[3]))

        
    """convert lists to a numpy arrays for further processing """
    body_fat_percent=np.array(body_fat_percent)
    weight_lbs=np.array(weight_lbs)
    height_inches=np.array(height_inches)


    """convert the imperial units of height and weight to
    SI units using the lb_to_kg and cm_to_m( inch_to_cm() ) functions from the
    units module """
    weight_kg=units.lb_to_kg(weight_lbs)
    height_m=units.cm_to_m(units.inch_to_cm(height_inches))

    """calculate BMI for each element of the array from according kg and m data"""
    BMIdata = weight_kg/height_m**2


    """plot the BMI vs body_fat_percent data - before clean _ save """
    f1=plt.figure()

    plt.plot(body_fat_percent, BMIdata, '^')
    
    plt.xlabel(header[0] )
    plt.ylabel('BMI' )
    plt.xticks(np.arange(0,(50),(10)))
    plt.yticks(np.arange(0,100,10))
    f1.savefig('BMIdata_before_clean.png')


    """find and replace missing data using the missing_check
    function from stats module - print the number of replaced elements"""
    print "There are %d" %stats.missing_check(BMIdata) + " missing data points."

    """find and reject outlier data using the reject_outliers
    function from stats module"""
    valid=stats.reject_outliers(BMIdata)


    """Plot the compressed BMIdata array vs compressed
    body_fat_percent array - after clean _ save """
    f1=plt.figure()

    plt.scatter(body_fat_percent[valid], BMIdata[valid])
    
    plt.xlabel(header[0])
    plt.ylabel('BMI' )
    plt.xticks(np.arange(0,(50),(10)))
    plt.yticks(np.arange(0,60,10))
    f1.savefig('BMIdata_after_clean.png')
    plt.show()


if __name__=="__main__":
    
    sys.exit(main())





