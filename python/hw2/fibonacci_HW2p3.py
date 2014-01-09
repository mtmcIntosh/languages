"""Calculate the nth Fibonacci number
as desired by the user, and also from
the Fibonnaci formula - disclose the difference
ImpVariables:
iterations, user defined nth Fibonacci number to calculate
it, computer iterations counter
fibnum, array holding the calculated fibonnaci numbers up to the nth
formula, calculation for fibonacci number from fibonacci formula 
Author: C. Gorham 30 Jan 2013"""

from fractions import Fraction
import math

yes = {"y", "Y"}
x = {'x', 'X'}
continuation = 1


"""1. (loop-while) Run while user has not asked to stop running
2. (loop - while) ensure the user asks to compute at least one iteration
3.(loop - while) calculate the nth Fib Number, running the it_counter
to user defined iterations, store in fibnum[]
4. calculate Fibonnaci formula and print both computer calculation,
formula calculation, and the difference
5. ask if the user wants to continue with calculating fibonnaci numbers"""
while continuation is 1:
    it = 1
    fibnum = [1]
    
    iteration = raw_input("\nWhich order fibonacci number do you want to compute? (x to exit) ")
    if iteration in x:
        sys.exit()
        
    iteration = int(iteration)


    while iteration < 1:
        iteration = raw_input("Please enter an iteration 1 or above. (x to exit)  ")
        if iteration in x:
            sys.exit()
            
            iteration = int(iteration)


    while it <= iteration:
        if it is 1:
            fibnum.append(fibnum[it - 1] + 0)
        else:
            fibnum.append(math.ceil((fibnum[it - 1] + fibnum[it - 2])))
        
        it=it+1

    print "The %d" %iteration + "th Fibonacci number is, %d"  % fibnum[iteration-1] + "."

    sqrtfive=math.sqrt(5)

    formula = (1 / sqrtfive * (((1 + sqrtfive) / 2) ** iteration
                               - ((1 - sqrtfive) / 2) ** iteration))

    print "The Nth Fibonacci formula yields, %d" % formula + "."

    if fibnum[iteration - 1] != formula:
        print ("This is interesting. The difference between"
                " theory and calculation is %d" % (formula - fibnum[iteration - 1]))


    yon = raw_input("\n do you want to run another number? ")

    if yon[:1] not in yes:
        continuation = 0

