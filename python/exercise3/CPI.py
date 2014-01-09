import csv
import sys
import numpy as np
import matplotlib.pylab as plt

header=[]
col0=[]
col0string=[]
col1=[]
I=[]
outputfilename= "inflation.csv"
trys=0

while True and trys<=3:
    try:
        filename=raw_input("Which file are we opening?\n")
        with open(filename,'r') as fin:
            fin=open(filename,'r')
            trys=0
            break
    except IOError as e:
        print "file does not exist. try again."
        if trys is 3:
            sys.exit("Three strikes you're out")
        trys=trys+1
        
while True and trys<=3:
    try:
        birthyear=int(raw_input("Kindly supply your birth year.\n"))
        break
    except ValueError:
        print "You did not enter an integer year. Try again."
        if trys is 3:
            sys.exit("Three strikes you're out")
        trys=trys+1


header.extend(fin.readline().rstrip('\n').split(','))

for line in fin:
    cols=line.strip('\n').split(',')
    if cols is ['','']:
        print "%d" %line
        break
    """year """
    col0.append(float(cols[0]))

    """CPI """
    col1.append(float(cols[1]))
    


"""collect data for certain years and,
compute the derivative """
for year in xrange(len(col0)):
    if col0[year] == birthyear:
        cpibirthyear = col1[year]
    if col0[year] == 2012:
        cpi2012 = col1[year]
    if col0[year] == 1954:
        cpi1954 = col1[year]
    if year > 0:
        I.append((col1[year]-col1[year-1])/12)



"""print some info to screen """

print "The change in cost of living from %d" %birthyear + " to 2012 is a whoping" \
      " $%.2f" %(cpi2012-cpibirthyear) + ".\n"

print "Following the same logic, if a color TV cost $1295 in 1954, it would cost "\
      "a whoping $%.2f" %(1295+(cpi2012-cpi1954)) +" in 2012. \n"



""" create and write output file """

outputfile=open(outputfilename,"wb")
data_file=csv.writer(outputfile, delimiter=",")

data_file.writerow([ "from year","to year", "inflation"])

for year in xrange(1,len(col0)):
    data_file.writerow([ col0[year-1], col0[year],I[year-1]])

outputfile.close()


f1=plt.figure()
plt.plot(col0, col1)
plt.xlabel(header[0] )
plt.ylabel(header[1] )
plt.draw()

f2= plt.figure()

plt.plot(col0[1:], I )
plt.hold(True)
plt.xlabel(header[0] )
plt.ylabel("inflation" )


plt.show()



   
