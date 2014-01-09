numbers = [3, 4, 5]

i=0
for number in numbers: 
   if i == 0:
      max=number
   elif number>max:
      max=number
   i=1+i

print "The max value is",max

sum=0
i=0
for number in numbers:
   sum=sum+number
   i=i+1

sum=float(sum)
average=sum/i

print "The average is", average
