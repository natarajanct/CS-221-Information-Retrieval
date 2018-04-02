# CS 221 - Assignment 1 - Part A: Word Frequencies
# FileName: word_frequencies.py
#
# Student Name: Natarajan Chidhambharam
# 
# Functions Implemented:
# 		List<Token> tokenize(TextFilePath)
# 		Map<Token,Count> computeWordFrequencies(List<Token>)
# 		void print(Frequencies<Token,Count>)
#
# Execution: python word_frequencies.py <Input-file name>
#
# References: 
# https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
# https://stackoverflow.com/questions/5733419/how-to-iterate-over-the-file-in-python
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string/23853882
# https://stackoverflow.com/questions/4546879/which-one-to-prefer-line-lower-vs-word-lower	
# https://stackoverflow.com/questions/34156822/python-sort-dictionary-items-by-value-and-then-key

import sys 
import re
import timeit

def tokenize(TextFilePath):
    
	#Declaring 'Token' as a list
    Token = []

    #Open input file for reading
    with open(TextFilePath,"r") as file:
        for x in file:
        	#Replacing special characters with a space for tokenization
            x = re.sub('\W',' ',x)
            #Splitting the line and putting all the words in Token list as lowercase
            for word in x.lower().split():
                Token.append(word)

    #Returning the Token list            
    return Token

def computeWordFrequencies(Token):

	#Declaring 'Frequencies' as a dictionary (key, value) to compute count
    Frequencies = {}

    #Iterate through the Token list
    for word in Token:
        if word in Frequencies:
            Frequencies[word] += 1
        else:
            Frequencies[word] = 1
    
    #Return the word frequencies as a key value pair
    return Frequencies

def printWordFreqCount(Frequencies):

	#To sort the key-value pairs in the 'Frequencies' dictionary from highest to lowest:
    for key,value in sorted(Frequencies.items(),key=lambda x:x[1],reverse = True):
        print("%s - %s" %(key,value))

def main():
	# Checking the execution of the script - if the number of arguments is right
	if (len(sys.argv) != 2):
		print("Check the number of arguments. Execute as python 75003249_partA.py <Input-file name>")
		sys.exit()
	else:
		#Getting the input file name
		TextFilePath = sys.argv[1]

    		#Tokenize the input file
		Token = tokenize(TextFilePath)

		#Compute the word frequncies from the Token list
		Frequencies = computeWordFrequencies(Token)

		#Print the word frequency counts
    	printWordFreqCount(Frequencies)

#Calculating the start time
start = timeit.default_timer()

#Executing the main fucntion
main()

#Calculating the end time
stop = timeit.default_timer()

#Printing the total time taken by the program
print 'Total time - ',stop - start,'sec'
