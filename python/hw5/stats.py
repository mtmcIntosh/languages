'''
This module contains functions for
cleaning data.

functions:
missing_check(A)
    will get rid of 'missing' data which has
    the value of the variable 'missing'
    ...return the number of missing datapoints
reject_outliers(A)
    decides if each data point is valid data by
    conducting a simple Normal distribution analysis
    to determine if the data lies the probable range
    ...return bool matrix [True if valid, False if not valid]
    
By: Caroline Gorham, 25 Feb 2013
'''

import numpy as np 
from scipy.special import erf 
from scipy.special import erfc

"""variable indicating the value given to missing from the
data acquisition system"""
missing=-99

"""determines if each element of the array (A) is valid
returns the bool Valid array"""
def reject_outliers(A):
    length=len(A)
    meanvalue=A.mean()
    stdvalue=A.std()
    criterion=1/(2.*length)
    devs=np.abs((A-meanvalue)/stdvalue)
    reduced_devs=devs/np.sqrt(2.)
    probs=erfc(reduced_devs)
    
    valid=np.array([True]*length)
    
    valid = (probs >=criterion)
    
    return valid


"""replaces 'missing' elements of the array (A) with
adjacent data, returns the number of elements that have
been replaced"""
def missing_check(A):
    missing_index=0
    for cell in xrange(len(A)):
        if A[cell] == missing:
            if cell==0:
                A[cell]=A[cell+1]
            else:
                A[cell]=A[cell-1]
                
            missing_index=missing_index+1
                
    return missing_index

