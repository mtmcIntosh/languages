"""Collect strings for which the first set of  two characters
are 'de' OR the second set of two characters are 'no'.
Make sure the string is at least four characters long.
By: C. Gorham 27 Jan 2013 
important variable: acceptedWords[] includes the user input 
words that pass the test. """

import sys


acceptedWords=[]
rejectedWords=[]

"""Allow exit option at each text input """
exitword={'x', 'X'} 

word= raw_input("Please supply a word (x to quit): \n")

"""run program while user has not entered the key to exit"""    
while word[:1] not in exitword:

    if len(word)>=4:
        if bool(word[:2]=='de')!= bool(word[2:4]=='no'):
            acceptedWords.append(word)
            print "Word is accepted.\n"
        else:
            rejectedWords.append(word)
            print "Word is rejected.\n"

    else:
        print "Word is not long enough, enter another.\n"

    word= raw_input("Please supply a word (x to quit): \n")

