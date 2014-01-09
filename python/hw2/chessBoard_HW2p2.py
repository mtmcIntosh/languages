""" Create a (colored) chess board
of a user defined size n (i.e., [n x n])
ImpVariables: chessBoard [nxn] to fill by
row and column
Author: C. Gorham 30 Jan 2013"""

import sys
import numpy as np

yes = {"y", "Y"}
x = {'x', 'X'}
continuation = 1

"""1. (while-loop) Run while user has not asked to leave, ask for size of chessboard
2. (while-loop) ensure the chessboard is at least 1x1
3. (for-for--if loop) color the board based on conditions, if both colxrow are even or
both colxrow are odd the sqare is Red, otherwise the square is Black
4. (variable yon) 'Do you want to make another chessboard?' if not exit loop1 """
while continuation is 1:

        
    n = raw_input("What size 'n' should the [n x n] chessboard be? (x to exit) ")
    if n in x:
        sys.exit()
        
    n = int(n)


    while n <= 0:
        n= raw_input("\nAn imaginary chessboard is only available in your brainspace,\n"+
        "please enter a real number for 'n' (x to exit) ")
        if n in x:
            sys.exit()
        n = int(n)

    chessBoard = [[[]*n]*n]*n


    iteration = 1
    for row in range(n):
    
        for col in range(n):
        
            if (((row % 2 ==0) and ( col % 2 ==0 )) or
                ((row % 2 !=0) and (col % 2 !=0))):
            
                chessBoard[row][col]="R"
            
            else:
                chessBoard[row][col]="B"

            sys.stdout.write("%s" % chessBoard[row][col] + " ")
            if (iteration) % n is 0:
                sys.stdout.write("\n")
        
            iteration=iteration+1

    yon = raw_input("\n do you want to make another chessboard? ")

    if yon[:1] not in yes:
        continuation=0



    
