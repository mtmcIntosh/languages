#!/bin/bash
#user and process info, with fun fortune BASH HW1
#by Caroline Gorham, 14 Feb 2013 - user cg6ww

#script variables 
asteriks='***********************************'


#print block indicating who the user is
#this moment's long date and the host 
#they are logged in to, surrounded by asteriks
echo "$asteriks"
echo 'Hello' `whoami`'! Today is ' `date`'.'
echo 'You are logged in as' `whoami`'.'
echo 'The machine you are using is' `hostname -s`'.'
echo -e "$asteriks\n"

#print user processes /process ids / running time / 
echo 'Your processes are'
echo "$(ps -u $USER)"


# print a lovely random fortune to the screen
echo -e "\nHere is a fortune for you:"
echo `fortune`
