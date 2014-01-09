"""This module contains class Wordstats
which initilizes the words in a document
into a dictioanry keeping the value of the keys as
the frequency of the word. Other members of the class include
number_unique (returns the number of unique words used),
frequencies (returns the self.dictionary as a new dictionary
sorted by frequency and alphabet), match_words (returns a
dictionary of words occuring in multiple documents), and
histogram (sets up a histogram of N most used words)
Author: Caroline S. Gorham, March 29, 2013"""

class Wordstats(object):

    # of the most common words, these should not be added to the dictionary
    ignore_words={'the', 'of', 'and', 'to', 'a', 'in', 'be','been', 'it', 'by', 'if', \
                  'that', 'or', 'for', 'which', 'this', 'an', 'all', 'its', 'not', 'with',\
                  'their','they','them','me','my', 'is', 'as', 'from', 'may', 'i', 'on', \
                  'but', 'can', 'only', 'his','her','our','there','here','what','when',\
                  'where','by','be','is','are','have','has','had','he','she','no','we','us',\
                  'you','your','these','those','was','were','above','below','behind','beneath',\
                  'before','after','upon','under','between','through','at','any','all','so','than'}
    
    def __init__(self, filename):
        """initialize instances with a name, a running total of words in the
        dictionary and the dictionary"""
        self.name_of_doc=filename
        self.total_words=0
        self.dictionary={}
        
        fin=open(filename,'r')

        # for each word in each line of the speech, lower case, strip punctuation, delete if it
        # should be ignored, rejoin on '' and add to dictionary
        for line in fin:

            line=line.lower().split(' ')

            for word in line:
                word=word.replace(";", '').replace(":", '').replace("!", '').replace("?", '').replace(",", '').\
                replace(".", '').replace("'", '').replace('"', '').replace("--", ' ').replace('\n', '')
                
                if word in set(Wordstats.ignore_words):
                    word=word.replace(word, '')

                
                if word is not '':
                    "".join(word)
                    if word not in self.dictionary:
                        self.dictionary[word]=1
                    else:
                        self.dictionary[word]+=1
                    self.total_words+=1


    def number_unique(self):
        """return the number of unique words in the file"""
                
        return len(self.dictionary)
                

    def frequencies(self, unique_dict, *args):
        """optionally take a number N and return the Nth most frequently-used words in
        the file, in descending order of frequency.
        If N is not provided it will return a list of all the words. """

        self.sorted_by_freq_n={}
        unique_key = sorted(unique_dict.items(), key=lambda item:item[0] )
        self.sorted_by_freq = sorted(unique_key, key=lambda item:item[1], reverse = True)
        
        if args:
            for arg in args:
               for n in range(arg):
                    self.sorted_by_freq_n= self.sorted_by_freq[:n]

        else:
            for key in self.sorted_by_freq:
                self.sorted_by_freq_n = self.sorted_by_freq

        return self.sorted_by_freq_n

    def match_words(self, filedictionary_to_match):
        """ takes a list of words and returns a list of the words in the dictionary
        that match the input list, along with the number of matches. """
        
        shared_words={}
        words_index=1
        
        for key in self.dictionary:
            if key in filedictionary_to_match.keys():
                if key not in shared_words.values():
                    shared_words[words_index]=key
                    words_index+=1
            else:
                continue
            
        for key in filedictionary_to_match:
            if key in self.dictionary.keys():
                if key not in shared_words.values():
                    shared_words[words_index]=key
                    words_index+=1
            else:
                continue
            
        return shared_words, len(shared_words)
    
    def histogram(self, frequencies_dict, filename, N):
        """takes a number N and plots the histogram of the Nth most frequent words.
        plot all if  N=-1"""
                
        import numpy as np
        import matplotlib.pyplot as plt

        fig = plt.figure()
        
        width = 1
        histo_values={}
        xlabels = {}

        if N==-1:
            ind = np.arange(len(frequencies_dict))
            for n in ind:
                histo_values[n] = frequencies_dict[n][1]
                xlabels[n]=frequencies_dict[n][0]
                   
            rects = plt.bar(ind, histo_values.values(), width)

        else:
            ind = np.arange(N)
            for n in ind:
                histo_values[n] = frequencies_dict[n][1]
                xlabels[n]=frequencies_dict[n][0]
                   
            rects = plt.bar(ind, histo_values.values(), width)

            if N <= 25:
                plt.xticks(ind+.5*width, xlabels.values() )

                   
            rects = plt.bar(ind, histo_values.values(), width)

        plt.title(filename + " : Word usage frequency")
        plt.ylabel('Frequency')

        plt.setp(plt.xticks()[1], rotation=90)

        fig.savefig(self.name_of_doc +'_histogram.png')
        
        return fig

