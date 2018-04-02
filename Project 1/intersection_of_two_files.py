# CS 221 - Assignment 1 - Part B: Intersection of two files
# FileName: intersection_of_two_files.py
#
# Student Name: Natarajan Chidhambharam
# 
# The program takes two text files as arguments and outputs the number of tokens they have in common
#
# Execution: python 75003249_partB.py <Input-file 1> <Input-file 2>
#
# References: 
# https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
# https://stackoverflow.com/questions/5733419/how-to-iterate-over-the-file-in-python
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string/23853882
# https://stackoverflow.com/questions/4546879/which-one-to-prefer-line-lower-vs-word-lower	
# https://www.geeksforgeeks.org/python-intersection-two-lists/

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

def intersection(Token_1, Token_2):
    #Using the set method to achieve intersection
    return list(set(Token_1) & set(Token_2))

def main():
	# Checking the execution of the script - if the number of arguments is right
	if (len(sys.argv) != 3):
		print('Check the number of arguments. Execute as python 75003249_partB.py <Input-file 1> <Input-file 2>')
		sys.exit()
	else:
		#Getting the input file names
		TextFilePath_1 = sys.argv[1]
        	TextFilePath_2 = sys.argv[2]

        	#Tokenize the 2 input files
        	Token_1 = tokenize(TextFilePath_1)
        	Token_2 = tokenize(TextFilePath_2)

        	#Printing the number of common tokens 
        	print 'Number of common tokens: ',len(intersection(Token_1, Token_2))

#Calculating the start time
start = timeit.default_timer()

#Executing the main fucntion
main()

#Calculating the end time
stop = timeit.default_timer()

#Printing the total time taken by the program
print 'Total time - ',stop - start,'sec'
