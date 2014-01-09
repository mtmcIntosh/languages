"""Categorize town size by user input
population values.
 By: C. Gorham 27 Jan 2013 
important variable: population is the user input"""

"""Allow exit option at each text input """
exittext = {'x', 'X'} 

population=raw_input("What is the population of the city? (x to quit)\n")

while population not in exittext:

    population=float(population.replace(",",""))
    
    if population<10000:
        print "This is a small town.\n"
    elif population >= 10000 and population <100000:
        print "This is a small city.\n"
    elif population >= 100000 and population <1000000:
        print "This is a medium city.\n"
    elif population > 1000000:
        print "This is a large city.\n"

    population=raw_input("What is the population of the city? (x to quit)\n")

