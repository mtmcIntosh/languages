"""Calculate the volume of a prolate spheroid
from user input axes values.
By: C. Gorham 27 Jan 2013 
important variables: 
Axes[long short] array holds user input of axes
Volume: of prolate spheroid"""

import math
import sys

"""Allow exit option at each text input"""
exittext = {'x', 'X'}

"""Allow continuation option after a volume is found"""
yes={"Y", "y"}

Volume=0.
longAxis=0.
shortAxis=0.

"""Ask for axes values until appropriate values are given
Calculate the volume and provide the information to user. """
while Volume==0:

    if longAxis<=0:
        longAxis=raw_input("\n What is the major-axis (in.) of the prolate spheroid? (x to quit)\n")
        longAxis=float(longAxis)
    
        if longAxis in exittext:
            sys.exit()

        
    if shortAxis<=0:
        shortAxis=raw_input("\nWhat is the minor-axis (in.) of the prolate spheroid? (x to quit)\n")
        shortAxis=float(shortAxis) 
    
        if shortAxis in exittext:
            sys.exit()


        semiAxes=(longAxis/2, shortAxis/2)

    if semiAxes[0]<=0 or semiAxes[1]<=0:
        print ("Exiting program because one or more axis is less than or equal to zero. Please" +
               " check parameters and run again.")
        sys.exit()

    else:
        print ("\nFor a prolate spheroid of long axis %.1f" % (2*semiAxes[0]) +
        " in. and short axis of %.1f" %  (2.*semiAxes[1]) + " in., ")

        Volume= 4. / 3. * math.pi * semiAxes[1]**2 * semiAxes[0]

        print "the volume is %.3f" % Volume + "\n"

        runAgain=raw_input("Find another volume?")
        
        if runAgain[:1] not in yes:
            break

        longAxis=0
        shortAxis=0
        Volume=0
        continue
