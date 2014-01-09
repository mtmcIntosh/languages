import sys
import math
from fractions import Fraction

sumPi=0
evalPi=0
tol=10e-8
n=0
print "The computer value of pi is = %.8f" % math.pi



"""Evalutae pi to agree within with computer value """

while sumPi < (math.pi-float(tol/2)) or sumPi > (math.pi+float(tol/2)):

    numer = ((-1)**n)
    denom = ((2*n +1))
    sumPi=  sumPi + float(Fraction(("%d" %numer + "/%d" %denom)))
    Pi=4*sumPi

    if Pi > (math.pi-float(tol/2)) and Pi< (math.pi+float(tol/2)):
        break;
    
    n = n+1

print "The evaluated value of pi is = %.8f" % Pi + "/"
print "%d iterations were required to arrive at this value." % n


