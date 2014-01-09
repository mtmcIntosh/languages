""" Read .CSV file of bird sightings,
parse into array structures according to headers
Determine the min, mean and average of the total
sightings - print determinations to screen. Then,
plot the total sightings vs. the year sighted and
provide this information in an output .CSV file.
By: Caroline Gorham 08 Feb 2013
"""


import numpy as np
import matplotlib.pylab as plt
import csv

"""header and column array initializations """
header=[]
speciesId=[]
speciesCommonName=[]
year=[]
number=[]
numberPerHour=[]
numberPerHourMean=[]
hours=[]
reportingCounts=[]
reportingObservers=[]
totalCounts=[]
totalObservers=[]


""" file names"""
filename="./rebnut_US-VA_1-110.csv"
outputfilename="./numberVyear.csv"



""" open and read csv file into header and appropriate arrays"""

fin=open(filename,'r')

header.extend(fin.readline().rstrip('\n').split(','))

 
for line in fin:
    cols=line.strip('\n').split(',')

    speciesId.append(cols[0])

    speciesCommonName.append(cols[1])

    year.append(int(cols[2]))

    number.append(int(cols[3]))

    numberPerHour.append(float(cols[4]))

    numberPerHourMean.append(float(cols[5]))

    hours.append(float(cols[6]))

    reportingCounts.append(int(cols[7]))

    reportingObservers.append(int(cols[8]))

    totalCounts.append(int(cols[9]))

    totalObservers.append(int(cols[10]))



"""Determine min, max, and mean sightings/year -- print to screen  """

minyears = [year[0]]
minimum = number[0]
maxyears = [year[0]]
maximum = number[0]
runningcount = 0

for row in xrange(1, len(year)):
    
    minimum=np.minimum(number[row], minimum)
    if number[row] == minimum: 
        minyears.append(year[row])

    maximum=np.maximum(number[row], maximum)
    if number[row] == maximum and number[row] == number[row-1]: 
        maxyears.append(year[row])
    elif number[row] == maximum:
        maxyears=[year[row]]
        
    runningcount=runningcount+1

mean=np.mean(number)    
        

print "The minimum observed red-breasted nuthatches is %d" %minimum + ", these were "\
      "observed in years:%s" %minyears + ".\n"

print "The maximum observed red-breasted nuthatches is %d" %maximum + ", these were "\
      "observed in year %s" %maxyears+ ".\n"

print "The mean red-breasted nuthatches observed is %d" %mean + ", over %d" %runningcount+\
      " data points.\n" 

    

"""plot """

f1=plt.figure()
plt.plot(year, number, '-o')
plt.xlabel(header[2] )
plt.ylabel(header[3] )
plt.xticks(np.arange(5,120,10))
plt.yticks(np.arange(0,1700,100))
f1.savefig('numberVyear.pdf')
plt.show()



""" create and write output file """

outputfile=open(outputfilename,"wb")
data_file=csv.writer(outputfile, delimiter=",")

data_file.writerow([ header[2],header[3]])

for row in xrange(len(number)):
    data_file.writerow([ year[row],number[row]])

outputfile.close()



    
    
    
    

    
