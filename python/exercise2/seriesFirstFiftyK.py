from fractions import Fraction
import numpy as np


infsum=[0]
row=0
m=0
K=0
denom=0
Krange=range(1,50,5)

arraySteps=np.zeros(shape=(len(Krange),2))
infoArray={"K      ", "  Sum"}


for K in Krange:
    
    m=K
    
    for m in range(m,m+5):
    
        denom = 2**m

        infsum.append( infsum[m-1] + float(Fraction("1/%d" %denom)) )

    arraySteps[row][0]=K

    arraySteps[row][1]=float(infsum[K])
    row=row+1

print infoArray
print arraySteps
