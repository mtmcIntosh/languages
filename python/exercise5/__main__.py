import numpy as np
import numpy.ma as ma
import matplotlib.pylab as plt
import BMI
import sys


def main():

    """header and column array initializations """
    header=[]
    body_fat_percent=[]
    age=[]
    
    filename = raw_input("What is the filename you wish to open from ./")

    """ open and read csv file into header and appropriate arrays"""

    fin=open('./%s' %filename,'r')

    weight_lbs_height_inches_array=np.zeros(shape=(1000,2))
    
    header.extend(fin.readline().rstrip('\n').split(','))

    i=0
    for line in fin:
        cols=line.strip('\r\n').split(',')

        body_fat_percent.append(float(cols[0]))
    
        age.append(float(cols[1]))

        weight_lbs_height_inches_array[i,:]=[float(cols[2]),float(cols[3])]
        i=i+1

    weight_lbs_height_inches_array=weight_lbs_height_inches_array[:i,:]
        
    print ('\nWelcome to the BMI calculator')

    body_fat_percent=np.array(body_fat_percent)
    weight_lbs_height_inches_array=np.array(weight_lbs_height_inches_array)

    metricUser = BMI.conversion (weight_lbs_height_inches_array,i)
    BMIvalue = BMI.BMI (metricUser,i)

    buckets=BMI.weightClass(BMIvalue)

    f1=plt.figure()
    for datapoint in xrange(len(BMIvalue)):
        plt.plot(body_fat_percent[datapoint], BMIvalue[datapoint], '-o')
    
    plt.xlabel(header[0])
    plt.ylabel('BMI' )
    plt.xticks(np.arange(0,(50),(10)))
    plt.yticks(np.arange(0,100,10))
    f1.savefig('BMIdata.pdf')

    widths=[2.5, 6.5, 5, 5, 5, 10]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar([16, 18.5, 25, 30, 35, 40, 50], buckets)
    plt.xlabel(header[0])
    plt.ylabel('Entries' )
    plt.show()      


    
if __name__=="__main__":
    sys.exit(main())
