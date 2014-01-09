""" Sum successive integers to exceed
a user specified value.
ImpVariables:
value= user defined
Sum= running sum (start 0)
n= iterations (start 1)
Author: C. Gorham, 30 Jan 2013"""

import sys

yes = {"y", "Y"}
x = {'x', 'X'}
continuation = 1

""" Run while user has not asked to leave. Initialize Sum, terms, and n for successive runs """
while continuation is 1:
        n = 1
        Sum = 0
        terms = 0
        
        """Ask user for input, or if they wish to exit the program """
        value = raw_input("What value do you want the computer to reach? (x to exit) ")
        if value in x:
                sys.exit()
        
        value = float(value.replace(",",""))


        
        """Check that value is >=0, repeat until condition met,
        also ask if they wish to exit the program"""
        while value < 0:
        
                value = raw_input("Please enter number greater than or equal to zero. (x to exit) ")
                if value in x:
                        sys.exit()
                
                value = float(value.replace(",",""))
                continue


        """1.(loop) If value is >= 0, add successive integers to sum until value is exceeded;
        2. (condition) If sum exceeds value print user value, computer sum, and iterations required;
        3. (condition) Ask if the user wishes to run the program for another number, if not exit. """
        while Sum <= value:

            Sum = Sum + n

            if Sum > value:


                print ("The user entered %.1f" % value + ". The computer summation reached %.1f"
                    % Sum + " with %d" % n + " iterations." )
                
                yon = raw_input("\n do you want to run another number? ")

                if yon[:1] not in yes:
                    continuation=0
                    break;
        

            terms = terms+1
            n = n+1

        
    
    
