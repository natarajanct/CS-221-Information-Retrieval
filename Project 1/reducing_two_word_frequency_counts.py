# CS 221 - Assignment 1 - Part C: Reducing two word-frequency counts
# FileName: reducing_two_word_frequency_counts.py
#
# Student Name: Natarajan Chidhambharam
# 
# The program takes two word-frequency maps and creates an output word-frequency count file where the counts are added
#
# Execution: python reducing_two_word_frequency_counts.py <Input-file 1> <Input-file 2>
#
# References: 
# https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
# https://stackoverflow.com/questions/34156822/python-sort-dictionary-items-by-value-and-then-key

import sys 
import re
import timeit

def printWordFreqCount(Frequencies,FileToWriteOutput):
    #Write to output file
    with open(FileToWriteOutput,'w') as file:
        #To sort the key-value pairs in the 'Frequencies' dictionary in alphabetical order:
        for key,value in sorted(Frequencies.items()):
            file.write("%s , %d\n" %(key,value))
        

def main():
	# Checking the execution of the script - if the number of arguments is right
	if (len(sys.argv) != 3):
		print('Check the number of arguments. Execute as python 75003249_partC.py <Input-file 1> <Input-file 2>')
		sys.exit()
	else:
		#Getting the input file names
		TextFilePath_1 = sys.argv[1]
        	TextFilePath_2 = sys.argv[2]

        	#Output File name with path
        	OutputFileName = "partC_output.txt"

        	#Initializing a dictionary to store the token-frequency pairs from the input file
        	Dict_1 = {}

        	#Reading the input file 1
        	with open(TextFilePath_1,"r") as file:
            		for x in file:
                		#Splitting the line and converting all the words into lowercase
                		x = x.lower().split(',')
                		#Storing the values to the corresponding keys in the dictionary - converting the word-frequency counts as integer values
                		Dict_1[x[0]] = int(x[1])

        	#Reading the input file 2
        	with open(TextFilePath_2,"r") as file:
            		for x in file:
                		#Splitting the line and converting all the words into lowercase
                		x = x.lower().split(',')
                		#Storing the values to the corresponding keys in the dictionary - converting the word-frequency counts as integer values
                		#If the new key is already in the first input file, then add the new value to the corresponding value or append the new key-value pair to the dictionary
                		if x[0] in Dict_1:
                    			Dict_1[x[0]] += int(x[1])
                		else:
                    			Dict_1[x[0]] = int(x[1])

        	#Printing the updated dictionary to the output file partC_output.txt
        	printWordFreqCount(Dict_1,OutputFileName)

#Calculating the start time
start = timeit.default_timer()

#Executing the main fucntion
main()

#Calculating the end time
stop = timeit.default_timer()

#Printing the total time taken by the program
print 'Total time - ',stop - start,'sec'
