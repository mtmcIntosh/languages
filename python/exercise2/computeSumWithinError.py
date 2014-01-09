from fractions import Fraction
import numpy as np

infsum=[0]
row=0
n=1

arraySteps=np.zeros(shape=(100,2))
arrayStepsClipped=np.zeros(shape=(100,2))
infoArray={"n      ", "  Sum"}

denom = 2.**n

"""or 1./denom """
infsum.append( infsum[row] + float(Fraction("1/%d" %denom)) )

arraySteps[row][0]=n

arraySteps[row][1]=float(infsum[row])

row=row+1
n=n+1


while infsum[row] > (infsum[row-1]+float(1e-12)) or infsum[row] < (infsum[row-1]-float(1e-12)):
    
    denom = 2**n

    infsum.append( infsum[row] + float(Fraction("1/%d" %denom)) )

    arraySteps[row][0]=n

    arraySteps[row][1]=float(infsum[row])

    if infsum[row] < (infsum[row-1]+float(1e-12)) and infsum[row] > (infsum[row-1]-float(1e-12)):
        break;
    n=n+1
    row=row+1

print  infoArray
print  arraySteps[0:row][0:row]
