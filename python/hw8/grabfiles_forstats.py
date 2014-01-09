"""
This script asks the user for a file/files to
collect stats on. The Wordstats class from filestats
module is called to create a dictionary of the words
in the document and their frequency of use, and an attribute
for the total words in the document. members of
the Wordstats class provide other
statistical information such as the number of
unique words and a sorted dictionary by the
frequency of use; Wordstats.histogram is called
to generate a figure indicating the frequency of the use of
words in the documents. If statistics on two documents are
desired, the match_words attribute of Wordstats will
provide the list of shared words and the count thereof.
Author: Caroline S. Gorham, March 29, 2013
"""

import sys
from filestats import Wordstats
import matplotlib.pylab as plt
import numpy as np
from optparse import OptionParser

def print_stats(wordstats_instance):
    print "\n"
    print "There are %d" %wordstats_instance.number_unique() + " unique words in %s" %wordstats_instance.name_of_doc + "."
    print "Therefore the ratio of unique to all words is: %d" %wordstats_instance.number_unique() + "/%d" %wordstats_instance.total_words
    print "\n"
    

def main():
    
    # command line parser 
    usage = "usage: %prog [options] --histo filename1 filename2"

    parser = OptionParser(usage=usage, version="%prog 1.0")

    parser.add_option("--histo", type="int", dest="option1", default="25",
                    help="Do you want a histogram? enter # of how many on histo plot, -1 all, 0 no histo  - Default=25")

    (options, args) = parser.parse_args()
    
    # make sure the user has entered their desired number of files (up to two only), and that they exist
    if len(args)<2:
        continue_w_one=raw_input("You did not provide two files. Do you wish to continue with one file?")
        continue_w_one=continue_w_one.lower()
        
        if continue_w_one[0] is 'y':
            if len(args)<1:
                
                filename_1=raw_input("Please enter the filename.")
                try:
                    open(filename_1)
                except IOError:
                        sys.exit("Error opening file. File may not exist")
                num_of_files=1
            elif len(args)==1:
                
                filename_1=args[0]
                try:
                    open(filename_1)
                except IOError:
                        sys.exit("Error opening file. File may not exist")

                #variable indicating the number of files the user has decided to work with for future use in logic
                num_of_files=1   
        else:
            sys.exit("Ok.")
            
    else:
        num_of_files=2
        filename_1=args[0]
        filename_2=args[1]
        try:
            open(filename_1)
        except IOError:
            sys.exit("Error opening files. Either/both of the files may not exist")
        try:
            open(filename_2)
        except IOError:
            sys.exit("Error opening s. Either/both of the files may not exist")

    # the user has entered 0 if they do not want to see histograms, default is 25 indicating 'show me the 25 most
    # used words in a histo'
    histograms_desired=options.option1

    # initialize instance
    file1_dict=Wordstats(filename_1)
    
    #create a sorted dictionary by frequency and alphabet
    file1_dict.frequencies(file1_dict.dictionary)    
    print_stats(file1_dict)


    if num_of_files == 2:
        file2_dict=Wordstats(filename_2)
        file2_dict.frequencies(file2_dict.dictionary)
        print_stats(file2_dict)

        # compare the files and print the number of shared words
        (shared_words, shared_words_count)=file1_dict.match_words(file2_dict.dictionary)
        print "%d" %shared_words_count + " words overlap between the two documents."


    # if the user desires to see histograms, print histograms to the index indicated by variable histograms_desired
    if histograms_desired!=0:
        fig1 = file1_dict.histogram(file1_dict.frequencies(file1_dict.dictionary), filename_1, histograms_desired)
        if num_of_files==2:
            fig2 = file2_dict.histogram(file2_dict.frequencies(file2_dict.dictionary), filename_2, histograms_desired)
        
        plt.show()


if __name__=="__main__":
    sys.exit(main())
    

    
        
