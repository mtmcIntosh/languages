import sys
import numpy as np 

def mean(numbers):
   length=len(numbers)
   summ=np.sum(numbers)
   average=float(summ)/length
   return average
     
numbers = []
for line in sys.stdin:
   numbers.append(int(line))
  
print "The average is", mean(numbers)


