"""User input the radius
code calculates the Area 
and Volume, 
By: C. Gorham 25 Jan 2012"""


import math
import sys

string = raw_input("Enter the radius of a circle:"+ " ")
radius = float(string)

if radius>0:
   area = 4.*math.pi*radius**2
   volume = 4. / 3.* math.pi* radius **3

   print "Area is %4.3f"  % area + "\nVolume is %4.3f"  % volume

else: 

   print "Radius value is invalid"
